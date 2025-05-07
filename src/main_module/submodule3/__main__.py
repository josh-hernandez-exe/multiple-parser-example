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

    parser.add_argument('--arg31', help="Command line argument 3-1")
    parser.add_argument('--arg32', help="Command line argument 3-2")

    _mutex_group = parser.add_argument_group(
        title='Mutually Exclusive Arguments',
        description='Arguments that are mutually exclusive.',
    )
    mutex_group = _mutex_group.add_mutually_exclusive_group(required=False)

    mutex_group.add_argument(
        '--int-option',
        type=int,
        help=' '.join([
            'Specify an integer parameter.',
            'This argument is mutually exclusive with --int-option and --choice-option.',
        ]),
    )
    mutex_group.add_argument(
        '--choice-option',
        choices=[
            'option1',
            'option2',
            'option3',
        ],
        help=' '.join([
            'Specify a choice parameter.',
            'This argument is mutually exclusive with --int-option and --choice-option.',
        ]),
    )



    return parser


def main(args: argparse.Namespace) -> None:
    logger.info('main 3')
    helper1.helper_function1(
        args.arg31, args.arg32,
    )

    if args.int_option is not None:
        logger.info('Integer option is set to %d', args.int_option)

    if args.choice_option is not None:
        logger.info('Choice option is set to %s', args.choice_option)


if __name__ == '__main__':
    parser = make_parser()
    args = parser.parse_args()
    logging.basicConfig(
        level=logging.getLevelName(args.log_level),
        # https://docs.python.org/3/library/logging.html#logrecord-attributes
        format=' '.join([
            '%(asctime)s',
            '[%(levelname)s]',
            '[%(module)s:%(lineno)d]',
            # '%(process)d-%(thread)d-%(taskName)s',
            '%(message)s',
        ])
    )
    main(args)
