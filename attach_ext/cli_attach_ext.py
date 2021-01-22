#!/bin/env python3
import argparse
import signal
import sys

from . import attach_ext


def get_opt() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Extract attachments from EML files')
    parser.add_argument("files", action="store", nargs="+")

    args = parser.parse_args()

    return args


def sig_handler(signum, frame) -> None:
    sys.stderr.write("Terminated.\n")
    sys.exit(15)


def main() -> int:
    signal.signal(signal.SIGTERM, sig_handler)

    args = get_opt()

    for filepath in args.files:
        attach_ext.parse_email_from_file(filepath)

    return 0


if __name__ == "__main__":
    sys.exit(main())
