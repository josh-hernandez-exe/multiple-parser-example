import argparse
import logging

from .submodule1 import __main__ as _submodule1_main
from .submodule2 import __main__ as _submodule2_main
from .submodule3 import __main__ as _submodule3_main
from .sharedparser import make_shared_parser

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command', required=True)

sharedparser = make_shared_parser()
subparser1 = subparsers.add_parser("main1", parents=[sharedparser])
subparser2 = subparsers.add_parser("main2", parents=[sharedparser])
subparser3 = subparsers.add_parser("main3", parents=[sharedparser])

subparser_all = subparsers.add_parser("all", parents=[sharedparser])

# In-place create the fields for each subparser,
#   using the parser generators for each module
_submodule1_main.make_parser(subparser1)
_submodule2_main.make_parser(subparser2)
_submodule3_main.make_parser(subparser3)

# add all argunments from each parser to subparser_all
_submodule1_main.make_parser(subparser_all)
_submodule2_main.make_parser(subparser_all)
_submodule3_main.make_parser(subparser_all)

# Define a variable for the main function to run based off which subparser is used.
subparser1.set_defaults(main=_submodule1_main.main)
subparser2.set_defaults(main=_submodule2_main.main)
subparser3.set_defaults(main=_submodule3_main.main)


if __name__ == '__main__':
    args = parser.parse_args()

    # Configure basic logging first
    logging.basicConfig(
        level=logging.getLevelName(args.log_level),
        # https://docs.python.org/3/library/logging.html#logrecord-attributes
        format=' '.join([
            '%(asctime)s',
            '[%(levelname)s]',
            '[%(name)s:%(lineno)d]',
            # '[%(pathname)s:%(lineno)d]',
            # '[%(filename)s:%(lineno)d]',
            # '[%(module)s:%(lineno)d]',
            # '%(process)d-%(thread)d-%(taskName)s',
            '',
            '%(message)s',
        ]),
        # Remove the filters argument from here
    )

    # Create filter objects
    filters = [
        # logging.Filter('main_module'),
        # logging.Filter('main_module.submodule1'),
        # logging.Filter('main_module.submodule2'),
        # logging.Filter('main_module.submodule3'),
        # logging.Filter('aux_module1'),
    ]

    # Add filters to the handlers created by basicConfig
    root_logger = logging.getLogger()
    if root_logger.handlers:
        for handler in root_logger.handlers:
            for f in filters:
                handler.addFilter(f)
    else:
        # Handle the case where basicConfig might not have added a handler (unlikely but possible)
        # Or configure handlers manually if more control is needed.
        logger.warning("No handlers found on root logger after basicConfig. Filters not applied.")


    match args.command:
        case "main1" | "main2" | "main3":
            logger.info(args)
            logger.info('Running {}'.format(args.command))
            args.main(args)
        case "all":
            _submodule1_main.main(args),
            _submodule2_main.main(args),
            _submodule3_main.main(args)
