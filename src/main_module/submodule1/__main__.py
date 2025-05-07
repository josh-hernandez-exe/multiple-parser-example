import argparse
import logging

from aux_module1 import helper1

from ..sharedparser import make_shared_parser

logger = logging.getLogger(__name__)


def make_parser(parser: argparse.ArgumentParser = None) -> argparse.ArgumentParser:
    if parser is None:
        parser = argparse.ArgumentParser(
            parents=[make_shared_parser()],
        )

    parser.add_argument('--arg11')
    parser.add_argument('--arg12')

    parser.add_argument(
        '--vector',
        type=int,
        nargs='*',
        default=[],
        action='append',
    )

    parser.add_argument(
        '-c',
        '--count',
        default=0,
        action='count',
    )

    return parser


def main(args: argparse.Namespace) -> None:
    logger.info('main 1')

    helper1.helper_function1(
        args.arg11, args.arg12,
        vectors=args.vector,
        count=args.count,
    )


if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.getLevelName(args.log_level),
        # https://docs.python.org/3/library/logging.html#logrecord-attributes
        format=' '.join([
            '%(asctime)s',
            '[%(levelname)s]',
            '[%(pathname)s:%(lineno)d]',
            # '%(process)d-%(thread)d-%(taskName)s',
            '%(message)s',
        ])
    )
    main(args)
