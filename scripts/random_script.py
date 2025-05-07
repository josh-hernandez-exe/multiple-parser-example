import logging

from main_module.submodule1 import __main__ as submodule1

logger = logging.getLogger(__name__)

def main():
    logger.info('random script main')
    submodule1.main(
        submodule1.make_parser().parse_args([
            '--arg11', 'value1',
            '--arg12', 'value2',
            '--vector', '1', '2', '3',
            '--vector', '4', '5', '6',
            '--count',
            '--count',
        ])
    )

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        # https://docs.python.org/3/library/logging.html#logrecord-attributes
        format=' '.join([
            '%(asctime)s',
            '[%(levelname)s]',
            '[%(filename)s:%(name)s:%(lineno)d]',
            # '%(process)d-%(thread)d-%(taskName)s',
            '%(message)s',
        ])
    )
    main()
