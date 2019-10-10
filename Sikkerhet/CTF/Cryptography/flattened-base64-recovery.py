#!/usr/bin/env python2
# Author: Caleb Stewart
# Date: January 20th, 2019
# This code, given a lowercased Base64 string, will determine the correct and original Base64 encoding

from pwn import *
import sys
import argparse

def all_case_combos(inp):
    n = len(inp) 
   
    # Number of permutations is 2^n 
    mx = 1 << n 
   
    # Converting string to lower case 
    inp = inp.lower() 

     # Using all subsequences and permuting them
    i = long(0)
    while i < mx: 
        # If j-th bit is set, we convert it to upper case 
        combination = [k for k in inp] 
        for j in xrange(n): 
            if (((i >> j) & 1) == 1): 
                combination[j] = inp[j].upper() 
   
        temp = "" 
        # Printing current combination 
        for j in combination: 
            temp += j
        i += 1
        yield temp

def count_printable(s):
    n = len([c for c in s if ord(c) >= 32 and ord(c) <= 126])
    return n

def base64_pad(s):
    if (len(s)%4) == 0:
        return s
    return s.ljust(len(s)+3-(int((len(s)/4)*3)%3), '=')

def bruteforce_base64(flat):
    # The entire result in the correct case
    result = ''

    # Iterate through each 4 character (3 byte) chunkk
    for i in range(0, len(flat), 4):
        p = log.progress('bruteforcing chunk[{0}:{1}]'.format(i,i+4))

        # Indicates whether the next loop failed
        found = 0

        # Iterate all cases of this chunk
        for option in all_case_combos(flat[i:i+4]):
            # Make sure the padding is right
            option = base64_pad(option)
            
            p.status('trying case {0}'.format(option))

            # Decode the data
            data = option.decode('base64')

            # Count the printable characters
            nprint = count_printable(data)

            # We consider is success if it is all ascii printable
            if nprint == len(data):
                p.success("correct case is {0}".format(option))
                result += option.replace('=', '')
                found = 1
                break

        # Make sure the last loop succeeded. If not, we have completely failed
        if found == 0:
            p.failure('unable to find correct case')
            return None

    # We found it
    return result

# Parse arguments
parser = argparse.ArgumentParser(description='bruteforce base64 case')
parser.add_argument('base64', help='the base64 input you want to bruteforce')
args = parser.parse_args()

# Padding
args.base64 = base64_pad(args.base64)

# Loop condition
cont = 'y'

# Loop forever
while cont.upper() == 'Y':
    log.info('bruteforcing case of {0}'.format(args.base64))

    # Brute force it!
    result = base64_pad(bruteforce_base64(args.base64))

    # Check if we failed
    if result == None:
        log.error('failed to bruteforce {0}!'.format(args.base64))
        sys.exit(1)

    # Should we continue?
    log.info('the correct case is {0}'.format(result))
    log.info('the decoded output is: {0}'.format(result.decode('base64')))
    # loop till they listen
    cont = ''
    while cont.upper() != 'Y' and cont.upper() != 'N':
        cont = raw_input('should we continue? (y/n) ').rstrip()

    # If we continue, the result is now our target
    args.base64 = result.decode('base64')