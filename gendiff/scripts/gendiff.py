import argparse
from gendiff.differ import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')
    parser.add_argument('-f', '--format', dest='format', help='set format of output')
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file)
    print(result)


if __name__ == '__main__':
    main()
