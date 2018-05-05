#!/usr/bin/python

import re

def main():
    fh = open('sarcozy.txt')
    for c, line in enumerate(fh):
        match = re.search('president', line, re.IGNORECASE)
        if match:
            print(c, match.group())


if __name__=="__main__":main()