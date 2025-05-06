import argparse
import logging

from ..sharedparser import make_shared_parser

logger = logging.getLogger(__name__)


def make_parser(parser: argparse.ArgumentParser = None) -> argparse.ArgumentParser:
    if parser is None:
        parser = argparse.ArgumentParser(
            parents=[make_shared_parser()],
        )

    parser.add_argument('--arg11')
    parser.add_argument('--arg12')


    return parser


def main(args: argparse.Namespace) -> None:
    logger.info('main 1')
    logger.info(args.arg11)
    logger.info(args.arg12)
    # logger.info(args.groups)


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
