import argparse
import logging

from aux_module1 import helper1

from ..sharedparser import make_shared_parser

logger = logging.getLogger(__name__)


def make_parser(parser: argparse.ArgumentParser = None) -> argparse.ArgumentParser:
    if parser is None:
        parser = argparse.ArgumentParser(
            description='Submodule 1 main function.',
            parents=[make_shared_parser()],
        )

    parser.add_argument('--arg11', help="Command line argument 1-1")
    parser.add_argument('--arg12', help="Command line argument 1-2")

    special_group = parser.add_argument_group(
        title='Special Arguments',
        description='Arguments for special features.',
    )

    special_group.add_argument(
        '--vector',
        type=int,
        nargs='*',
        default=[],
        action='append',
        help=' '.join([
            'Specify a vector of integers.',
            'This argument can be used multiple times.',
            'Example: --vector 1 2 3 --vector 4 5 6',
        ]),
    )

    special_group.add_argument(
        '-c',
        '--count',
        default=0,
        action='count',
        help=' '.join([
            'Count the number of times this argument is used.',
            'Example: -c -c -c will set count to 3.',
        ]),
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
