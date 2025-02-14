#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:54:52 2021

@author: anirban
"""

import argparse
from simulator import Simulator
from collections import OrderedDict
import configparser 
import random

def parse_cli_args():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--cache-size',
        type=int,
        required=True,
        help='the size of the cache in words')

    parser.add_argument(
        '--num-blocks-per-set',
        type=int,
        default=1,
        help='the number of blocks per set')

    parser.add_argument(
        '--num-words-per-block',
        type=int,
        default=2,
        help='the number of words per block')
    
    parser.add_argument(
        '--num-partitions',
        type=int,
        default=1,
        help='the number of partitions')

    parser.add_argument(
        '--word-addrs',
        nargs='+',
        type=int,
        required=True,
        help='one or more base-10 word addresses')

    parser.add_argument(
        '--num-addr-bits',
        type=int,
        default=32,
        help='the number of bits in each given word address')

    parser.add_argument(
        '--replacement-policy',
        choices=('lru', 'rand'),
        default='rand',
        # Ignore argument case (e.g. "lru" and "LRU" are equivalent)
        type=str.lower,
        help='the cache replacement policy (LRU or RAND)')

    return parser.parse_args()

class Configs(dict):
   
    def __init__(self, configs):
       for params in configs:
           if params == 'cache-size':
               self.cache_size = int(configs[params])
           if params ==  'num-blocks-per-set':
               self.num_blocks_per_set = int(configs[params])
           if params == 'num-words-per-block':
               self.num_words_per_block = int(configs[params])
           if params == 'num-partitions':
               self.num_partitions = int(configs[params])
           if params == 'num-addr-bits':
               self.num_addr_bits = int(configs[params])
           if params == 'replacement-policy':
               self.replacement_policy = configs[params]

            

def main(address, num_of_victim_access):
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    
    sections = parser.sections()
    cli_args = Configs(parser[sections[0]])
    vars(cli_args)['word_addrs'] = address    
    
    sim = Simulator()
    timing_vals = OrderedDict()
    timing_vals = sim.run_simulation(**vars(cli_args), num_of_victim_access = num_of_victim_access)

    timing_list = []
    for word, timing in timing_vals.items():
        timing_list.append(timing)
    
    address_misses = 0
    for index, item in enumerate(timing_list):
        if (item == 600):
            address_misses += 1
    print(address_misses)
    return(address_misses)
    


if __name__ == '__main__':
	base_address = 10000000

	num_for_0 = []; num_for_1 = []


	file_0 = f"outfile_v100_for_0.txt"
	file_1 = f"outfile_v100_for_1.txt"
	num_of_receiver_access = [1000, 2000, 3000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]

	sender_access_for_0 = 1000
	sender_access_for_1 = 2000

    for i in range(sender_access_for_0):
        num_for_0.append(base_address + (1000 * i))

    with open(file_0, "w") as f:
        for i in range(len(num_of_receiver_access)):
            print(num_of_receiver_access[i])
            for j in range(100):
                no_of_misses = main(num_for_0, num_of_receiver_access[i])
                write_list = [num_of_receiver_access[i], no_of_misses]
                f.write(str(write_list))
                f.write("\n")
                f.flush()
    print("")

    for i in range(sender_access_for_1):
        num_for_1.append(base_address + (1000 * i))

    with open(file_1, "w") as f:
        for i in range(len(num_of_receiver_access)):
            print(num_of_receiver_access[i])
            for j in range(100):
                no_of_misses = main(num_for_1, num_of_receiver_access[i])
                write_list = [num_of_receiver_access[i], no_of_misses]
                f.write(str(write_list))
                f.write("\n")
                f.flush()
    print("")

	print("Ceaser-S simulation Done!!!")
    