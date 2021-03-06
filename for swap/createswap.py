#!/usr/bin/env python3
# encoding: utf-8
'''
create_swap.py
A Python 3 script for creating and removing Linux swap files.
Made by VIDISH 1PE15IS118


NOTE:
    THIS SCRIPT WORKS ONLY WITH PYTHON VERSION 3.
    
'''

import sys
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='the file full name on which the swap space is going to be built (must be used with --size option)')
    parser.add_argument('-s', '--size', help='size of the swap space in megabytes (must be used with --file option)', type=int)
    parser.add_argument('-o', '--off', help='removes the swap file and disables its swap space', metavar='FILE')
    parser.add_argument('--verbose', help='executes in the verbose mode (useful for tracking errors)', action='store_true')
    args = parser.parse_args()
        
    try:
        if not args.file and not args.size and not args.off:
            if not args.verbose:
                parser.print_help()
                raise Exception()
            else:
                raise Exception("--verbose option cannot be used alone")

        if(args.file and not args.size) or (not args.file and args.size):
            raise Exception("--file and --size options must be used together")
        
        if args.off and (args.file or args.size):
            raise Exception("--off option cannot be used with other options")
 
    except Exception as ex:
        show_error(ex, 3)
        
    return args

def is_verbose():
    return args.verbose

def print_header():
    os.system('clear')
    print('-'*50)
    print('createswap.py v 2.0 (Python 3)\n')
    print('use to create swap file')
    print('made by VIDISH | kaos@kaosbox')
    print('-'*50)
    
def print_step(message):
    if is_verbose():
        end_char = '\n'
        print ()
    else:
        end_char = ''        
    print ('{:40.40}'.format(message), end=end_char, flush=True)
        
def print_status(is_failed=False):
    status = ('Failed' if is_failed else 'OK')
    print('[{}]'.format(status))

def show_error(exception, exit_code):
    print('\n{}'.format(exception))
    sys.exit(exit_code)

def sudo():
    os.system('sudo id > /dev/null')
    
def exec_step(message, command, arg_tuple=None):
    print_step(message)
    
    command = 'sudo ' + command
    if not is_verbose(): command += ' > /dev/null 2>&1'
        
    if arg_tuple != None:
        exit_code = os.system(command.format(*arg_tuple))
    else:
        exit_code = os.system(command)
    
    if exit_code == 0:
        print_status()
    else:
        print_status(True)        
       
def create_swap(filename, size):
    try:
        tuple1 = (filename, size)
        tuple2 = (filename,)
        
        exec_step('Creating the file', 'dd if=/dev/zero of={} bs=1M count={}', tuple1)
        exec_step('Setting the file access mode', 'chmod 600 {}', tuple2)
        exec_step('Setting up the swap space', 'mkswap {}', tuple2)
        exec_step('Enabling the swap space', 'swapon {}', tuple2)
    except Exception as ex:
        show_error(ex, 2)  

def drop_swap(filename):
    try:
        tuple1 = (filename,)        
        exec_step('Disabling the swap space', 'swapoff {}', tuple1)
        exec_step('Removing the file', 'rm {}', tuple1)
    except Exception as ex:
        show_error(ex, 2)
        
# program entry point
print_header()
args = parse_args()
sudo()

if args.file:
    create_swap(args.file, args.size)
elif args.off:
    drop_swap(args.off)  
    
print()
