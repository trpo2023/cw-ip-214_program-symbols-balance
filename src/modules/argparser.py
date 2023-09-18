import argparse


def init_argparser():
    parser = argparse.ArgumentParser(
        description="Read and check for bracket balance in .c file")
    parser.add_argument(
        'input_file',
        metavar='file',
        type=str,
        help='Input .c file')

    return parser
