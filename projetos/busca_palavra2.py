#!/usr/bin/python

import re


def main():

    fh = open('sarcozy.txt')
    for c, line in enumerate(fh):
        match = re.search('Nicolas', line)
        if match:
            print(c, match.group())


if __name__ == "__main__":main()