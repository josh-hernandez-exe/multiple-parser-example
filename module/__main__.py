import argparse

from . import submodule1
from . import submodule2
from . import submodule3

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(required=True)


subparser1 = subparsers.add_parser("main1")
subparser2 = subparsers.add_parser("main2")
subparser3 = subparsers.add_parser("main3")


submodule1.make_parser(subparser1)
submodule2.make_parser(subparser2)
submodule3.make_parser(subparser3)

subparser1.set_defaults(main=submodule1.__main__.main)
subparser2.set_defaults(main=submodule2.__main__.main)
subparser3.set_defaults(main=submodule3.__main__.main)


if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    args.main(args)
