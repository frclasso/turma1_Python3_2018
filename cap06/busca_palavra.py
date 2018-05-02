#!/usr/bin/python

import re


def main():

    fh = open('sarcozy.txt')
    for line in fh:
        if re.search(' Sarkozy', line):
            print(line, end='')


if __name__ == "__main__":main()