import argparse

from ..sharedparser import make_shared_parser

def make_parser(parser: argparse.ArgumentParser = None) -> argparse.ArgumentParser:
    if parser is None:
        parser = argparse.ArgumentParser(
            parents=[make_shared_parser()],
        )

    parser.add_argument('--arg31')
    parser.add_argument('--arg32')

    return parser


def main(args: argparse.Namespace) -> None:
    print('main 3')
    print(args.arg31)
    print(args.arg32)

if __name__ == '__main__':
    parser = make_parser()
    main(parser.parse_args())
