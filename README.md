# multiple-parser-example
Multiple Parser as Subcommands Examp[le

Example usage of making a python module with subcommands.
With each subcommand comming from it's own submodule having their own respective `__main__`.

Using top level module
```bash
python -m main_module --help
python -m main_module main1 --help
python -m main_module main2 --help
python -m main_module main3 --help
```

Using the submodules directly
```bash
python -m main_module.submodule1 --help
python -m main_module.submodule2 --help
python -m main_module.submodule3 --help
```

# Example Comands

```bash
python -m main_module.submodule1 \
    --arg11 qwer --arg12 asdf
```

```bash
python -m main_module.submodule2 \
    --arg21 zxcv --arg22 uiop \
    --flag --dry-run
```


```bash
python -m main_module.submodule3 \
    --arg31 hjlk --arg32 vbnm
```

```bash
python -m main_module all \
    --arg11 qwer --arg12 asdf \
    --arg21 zxcv --arg22 uiop \
    --arg31 hjlk --arg32 vbnm
```

```bash
python scripts/random_script.py
```


# Logging

https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook
