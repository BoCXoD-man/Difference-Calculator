"""
This Cli-program return differents two files
"""

from gendiff.engine import generate_diff
from gendiff.cli import path1, path2


def main():
    print(generate_diff(path1, path2))


if __name__ == '__main__':
    main()