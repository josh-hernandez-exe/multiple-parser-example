# multiple-parser-example
Multiple Parser as Subcommands Examp[le

Example usage of making a python module with subcommands.
With each subcommand comming from it's own submodule having their own respective `__main__`.

Using top level module
```bash
python -m module --help
python -m module main1 --help
python -m module main2 --help
python -m module main3 --help
```

Using the submodules directly
```bash
python -m module.submodule1 --help
python -m module.submodule2 --help
python -m module.submodule3 --help
```
