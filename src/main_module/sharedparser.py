import argparse


def make_shared_parser(parser: argparse.ArgumentParser = None) -> argparse.ArgumentParser:
    if parser is None:
        parser = argparse.ArgumentParser(add_help=False)

    parser_group = parser.add_argument_group(
        title='Shared Arguments',
        description='Arguments shared by all submodules.',
    )

    parser_group.add_argument(
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
