#!usr/bin/env python3

import argparse

def main():

    desc = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')

    args = parser.parse_args()

    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()