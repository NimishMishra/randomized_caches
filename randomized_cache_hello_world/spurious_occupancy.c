#include <stdint.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define SPURIOUS_OCC 2777728

uint64_t extra_data[SPURIOUS_OCC];

int main(){
 uint8_t data; 
 for(int i = 0; i <  SPURIOUS_OCC; i++)
 	data = extra_data[i] + 10; 
 printf("Spurious Occupancy step finished.\n"); 
}
