import argparse
import logging
import sys
import os

from utils.logger import setup_logger,set_log_level
from fit import FIT

def parse_args():
    parser = argparse.ArgumentParser(
        description='Sport Stats',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('fit',
                        metavar='FIT',
                        nargs=1,
                        help='Path to fit file')
    
    # Add debug flag
    parser.add_argument('-d', '--debug',
                        action='store_true',
                        help='Enable debug logging')

    return parser.parse_args()


def signal_handler(sig, frame):
    print("Signal received - exitting")
    sys.exit(0)


def main():
    setup_logger()

    args = parse_args()
    set_log_level('DEBUG' if args.debug else 'INFO')

    fit_path = args.fit[0]

    fit = FIT(fit_path)


if __name__ == "__main__":
    main()
