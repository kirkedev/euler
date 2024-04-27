Project Euler
-------------

### Setup

Create a virtual environment and activate it

```bash
python -m venv .venv
source .venv/bin/activate
```

Verify the environment is activated by running `which python` and install dependencies:

```bash
which python
pip install -r requirements.txt
```

Verify installation by running tests

```bash
pytest
```

To deactivate, just run `deactivate` in the terminal. You should activate the environment when working on the project
and deactivate when finished.

Activate git hooks

```bash
git config core.hooksPath .githooks
```

### Commands

Run solutions

```bash
bin/solve           # Run all solutions
bin/solve 1         # Run the first solution
bin/solve 1 2 3     # Run the first 3 solutions 
```

Lint code, check types, and run tests

```bash
bin/check
```
