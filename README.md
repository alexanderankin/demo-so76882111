# Importing modules from other directory

answer 76882111

to run this project, make sure python is python3 and, in this folder:

```bash
test -d .venv || python -m venv .venv # make sure all venv pkgs are available
pip install -e .
. .venv/bin/activate # or as appropriate for your os
python tests/test_app.py
```
