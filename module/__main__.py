import argparse

from .submodule1 import __main__ as _submodule1_main
from .submodule2 import __main__ as _submodule2_main
from .submodule3 import __main__ as _submodule3_main

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(required=True)

subparser1 = subparsers.add_parser("main1")
subparser2 = subparsers.add_parser("main2")
subparser3 = subparsers.add_parser("main3")

_submodule1_main.make_parser(subparser1)
_submodule2_main.make_parser(subparser2)
_submodule3_main.make_parser(subparser3)

subparser1.set_defaults(main=_submodule1_main.main)
subparser2.set_defaults(main=_submodule2_main.main)
subparser3.set_defaults(main=_submodule3_main.main)


if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    args.main(args)
