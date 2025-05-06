import argparse


def make_shared_parser(parser: argparse.ArgumentParser = None) -> argparse.ArgumentParser:
    if parser is None:
        parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument(
        '--log-level',
        type=lambda x: x.upper(),
        choices=[
            'ERROR',
            'WARNING',
            'INFO',
            'DEBUG',
        ],
        default='INFO',
        help=' '.join([
            'Specify the log level of the program.'
        ]),
    )

    return parser
