#include <stdint.h>
#include <random>
#include <time.h>
#include <ctime>
#include <cstdint>
#include <cstdlib>
#include <stdio.h>
#include "AES-KeyExp.h"
#include "AES-Encryption.h"
#define attacker_arr_size 8388608 

int cache_miss = 0;
uint64_t extra_data[16777216 + 512];
uint64_t attacker_arr[attacker_arr_size + 512];
uint8_t victim_arr_1[1000];
uint8_t victim_arr_2[4000];

unsigned cycles_low, cycles_high, cycles_low1, cycles_high1;

static __inline__ unsigned long long rdtsc(void)
{
    __asm__ __volatile__ ("RDTSC\n\t"
            "mov %%edx, %0\n\t"
            "mov %%eax, %1\n\t": "=r" (cycles_high), "=r" (cycles_low)::
            "%rax", "rbx", "rcx", "rdx");
}

static __inline__ unsigned long long rdtsc1(void)
{
    __asm__ __volatile__ ("RDTSC\n\t"
            "mov %%edx, %0\n\t"
            "mov %%eax, %1\n\t": "=r" (cycles_high1), "=r" (cycles_low1)::
            "%rax", "rbx", "rcx", "rdx");
}

__attribute__((noinline))
void attacker_access(int should_measure_time){
    uint64_t start, end;
    uint64_t data;
    if(should_measure_time)
	rdtsc();
    for(int i = 0; i < attacker_arr_size + 512; i++){
	data = attacker_arr[i] + 10;	
    }

    if(should_measure_time){
	rdtsc1();
	start = ( ((uint64_t)cycles_high << 32) | cycles_low );
	end = ( ((uint64_t)cycles_high1 << 32) | cycles_low1 );	
	printf("Attacker access time(2f): %lu, ", end-start);
   }
}

__attribute__((noinline))
void victim_1_access(){
    uint8_t data;
    for(int i = 0; i < 1000; i++)
       data = victim_arr_1[i] + 10;
}

__attribute__((noinline))
void victim_2_access(){
    uint8_t data;
    for(int i = 0; i < 4000; i++)
        data = victim_arr_2[i] + 10;
}

int main(){
    uint8_t data;
    //BYTE bKey[16] = { 0xff, 0xee, 0xdd, 0xcc, 0xbb, 0xaa, 0x99, 0x88, 0x77, 0x66, 0x55, 0x44, 0x33, 0x22, 0x11, 0x00 };
    BYTE bKey[16] = { 0x77, 0x66, 0x55, 0x44, 0x33, 0x22, 0x11, 0x00, 0xff, 0xee, 0xdd, 0xcc, 0xbb, 0xaa, 0x99, 0x88 };

    BYTE bInput[16];
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(0, 255);
    for (int i = 0; i < 16; i++)
	    bInput[i] = dist(gen);
    BYTE bExpKey[176];
    KeyExpansion(bKey, bExpKey);
    ComputeTBoxes();   
  
    for(int i = 0; i < 16777216 + 512; i++){	
	data = extra_data[i] + 10;
    }

    attacker_access(0);
    AesEncyption(bInput, bExpKey);
    attacker_access(1); 

    printf(" for ciphertext: ");
    for (int i = 0; i < 16; i++)
    	printf("%02x ", bInput[i]);

    printf(" and round 10 key: ");
    for(int i = 10*16; i < 10*16 + 16; i++){
    	printf("%02x ", bExpKey[i]);
    }
    printf("\n");
}
