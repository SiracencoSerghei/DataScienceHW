### Set up the environment

```bash
conda create -n conda_env_example python=3.11
conda activate conda_env_example

pip install -r requirements.txt  # should include 'notebook' as a dependency

jupyter notebook
```

#### If you've already installed everything and want to generate a requirements.txt:

```
pip freeze > requirements.txt
```
