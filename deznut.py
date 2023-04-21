import os
import time
import sys
import random

global running
running = True

def main():
    try:
        while running:
            a = "deez nuts "
            print(a+a+a+a+a+a+a)
    except KeyboardInterrupt:
        sys.exit()

main()