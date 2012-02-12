#!/usr/bin/python
import sys, ConfigParser, argparse, time, serial, threading, subprocess, os
parser = argparse.ArgumentParser()

parser.add_argument('-i','--include', type=str,
                    default=".",
                    dest = "include",
                    help = "Include directories"
                    )
parser.add_argument("name", type=str,
                   help="source file to assemble")
parser.add_argument("-v", "--verbose", action="store_true",
                    dest = "verbose",
                    help = "Enable verbose output")


args = parser.parse_args()

print os.getcwd()
command = 'wine asemw.exe'

os.system(command)









