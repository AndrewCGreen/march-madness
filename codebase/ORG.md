`march-madness` - a reusable codebase for the March Madness Project 
---

## Getting Started

1. Export the `MMPATH` environment variable prior to getting started, so that the Python modules can find internal dependencies.
Example:

```shell
$ export MMPATH="$HOME/Workspace/march-madness/"
```
2. Run the setup script to create a virtualenv that includes the `march-madness` Python package
```shell
$ ./setup
```
3. Source the environment to begin developing
```shell
$ source mm_env/bin/activate
```
4. Launch notebooks, scripts etc.
```shell
$ (mm_env) jupyter notebook
```

See `deps.txt` for the list of third-party dependencies that are pre-installed. If you want a custom
third-party library, simply `pip3 install` while `(mm_env)` is active. To permanently add a 
third party library to the environment, add it to `deps.txt`.

### Type hints:
- It is strongly recommended to add [PEP484](https://www.python.org/dev/peps/pep-0484/) type hints to _all_ function/method signatures, and any variable declarations
where the underlying type is non-obvious. These are technically ignored by the interpreter, however it is extremely
helpful as a form of self-documentation.

e.g.

Trivial, but maybe not entirely clear just via naming convention:
```python
def adder(a, b, ok):
  res = [x for x in a if ok]
  res.append(a[0] + b)
  return res
```
Much better. We know the type signature instantly, which is especially useful when exploring via a Python notebook's `?` operator:
```python
from typing import List

def adder(a: List[int], b: int, ok: bool) -> List[int]:
  res = [x for x in a if ok]
  res.append(a[0] + b)
  return res
```
### Testing:
- Unit testing is run using the `pytest` package. New modules should be unit tested to ensure that as the coebase grows, as much correctness as possible is retained

### Vendored dependencies:
- Use of the system (MacOS/Linux/WSL) Python is discouraged, as this limits reproducability and may introduce unexpected behaviors. Virtual environments and Python versions should be managed using the builtin `venv` module and `pyenv` tool, respectively. Management of this process (and compilation of the `march-madness` module) may be automated with a shell script in the future.
