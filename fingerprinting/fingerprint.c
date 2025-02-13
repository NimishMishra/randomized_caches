#include <stdint.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <x86intrin.h>

#define SPURIOUS_OCC 2777728
#define FINGERPRINT_OCC 157286

uint64_t extra_data[SPURIOUS_OCC];
uint64_t fingerprint_data[FINGERPRINT_OCC];

int main(){
 uint8_t data; 
 for(int i = 0; i <  SPURIOUS_OCC; i++)
 	data = extra_data[i] + 10; 
 

 for(int i = 0; i < FINGERPRINT_OCC; i++)
 	data = fingerprint_data + 10;


 uint64_t start = __rdtsc();
 while ((__rdtsc() - start) < 50000000)
	 __asm__ __volatile__("nop");

 for(int i = 0; i < FINGERPRINT_OCC; i++)
 	data = fingerprint_data + 10;
}
