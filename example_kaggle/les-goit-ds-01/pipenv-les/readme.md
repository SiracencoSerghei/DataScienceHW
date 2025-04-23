# Pipenv

## Installation
```bash
pip install pipenv
```

## Basic Commands

### Create a New Environment
```bash
pipenv install
```

### Install a Package
```bash
pipenv install <package_name>
```

### Install a Dev Dependency
```bash
pipenv install <package_name> --dev
```

### Uninstall a Package
```bash
pipenv uninstall <package_name>
```

### Activate the Virtual Environment
```bash
pipenv shell
```

### Deactivate the Virtual Environment
```bash
exit
```

### Check Installed Packages
```bash
pipenv graph
```

### Check Security Vulnerabilities
```bash
pipenv check
```

### Lock Dependencies
```bash
pipenv lock
```

### Install from `Pipfile.lock`
```bash
pipenv sync
```

## Additional Commands

### Run a Script in the Virtual Environment
```bash
pipenv run <command>
```
< pipenv run python3 app.py >

### Install All Dev Dependencies
```bash
pipenv install --dev
```

### Remove the Virtual Environment
```bash
pipenv --rm
```

### Specify Python Version
```bash
pipenv --python <version>
```

## Useful Flags
- `--three`: Use Python 3.
- `--two`: Use Python 2.
- `--pre`: Allow pre-releases.

For more details, visit the [Pipenv Documentation](https://pipenv.pypa.io/en/latest/).