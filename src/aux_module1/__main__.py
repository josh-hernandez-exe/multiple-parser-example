import argparse
import logging

from . import helper1

logger = logging.getLogger(__name__)


def main() -> None:
    logger.info('aux_module1 main')

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        # https://docs.python.org/3/library/logging.html#logrecord-attributes
        format=' '.join([
            '%(asctime)s',
            '[%(levelname)s]',
            '[%(filename)s:%(lineno)d]',
            # '%(process)d-%(thread)d-%(taskName)s',
            '%(message)s',
        ])
    )
    main()
