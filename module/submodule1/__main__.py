import argparse


def make_parser(parser: argparse.ArgumentParser = None) -> argparse.ArgumentParser:
    if parser is None:
        parser = argparse.ArgumentParser()

    parser.add_argument('--arg11')
    parser.add_argument('--arg12')

    return parser


def main(args: argparse.Namespace) -> None:
    print('main 1')
    print(args.arg11)
    print(args.arg12)

if __name__ == '__main__':
    parser = make_parser()
    main(parser.parse_args())
