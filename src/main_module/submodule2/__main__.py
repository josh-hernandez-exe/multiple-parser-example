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

    parser.add_argument('--arg21', help="Command line argument 2-1")
    parser.add_argument('--arg22', help="Command line argument 2-2")

    flag_group = parser.add_argument_group(
        title='Flag Arguments',
        description='Arguments that are flags.',
    )

    flag_group.add_argument(
        '--flag',
        default=False,
        action='store_true',
    )
    flag_group.add_argument(
        '--dry-run',
        dest='should_save',
        default=True,
        action='store_false',
    )

    return parser


def main(args: argparse.Namespace) -> None:
    logger.info('main 2')
    helper1.helper_function1(
        args.arg21, args.arg22,
    )

    if args.flag:
        logger.info('Flag is set')

    if args.should_save:
        logger.info('should save')
    else:
        logger.info('should not save (dry run)')


if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.getLevelName(args.log_level),
        # https://docs.python.org/3/library/logging.html#logrecord-attributes
        format=' '.join([
            '%(asctime)s',
            '[%(levelname)s]',
            '[%(filename)s:%(lineno)d]',
            # '%(process)d-%(thread)d-%(taskName)s',
            '%(message)s',
        ])
    )
    main(args)
