# Overview

If this is your first time contributing to an open-source project, welcome!
Before you dive into the code, we recommend checking out the [contribution guide](../development/contribution.md) for an introduction to general development workflow, tools, and best practices.

This guide will walk you through the process of setting up a development environment for HyperBench, contributing to the codebase and documentation, and understanding our development policies.

## Prerequisites

- [uv](https://github.com/astral-sh/uv)
- [make](https://www.gnu.org/software/make/)
- [pre-commit](https://pre-commit.com)

## Creating a development environment

### Build

Clone the repository and navigate to the project directory:

```bash
git clone https://www.github.com/hypernetwork-research-group/hyperbench.git
cd hyperbench
```

To simplify development, we provide a Makefile with common targets for building, testing, linting, and more. You can see all available commands with:

```bash
make help
```

or check the [Makefile documentation](../development/makefile.md) for details on each command.

To build the project, run:
```bash
make
```
This will set up the environment, install dependencies, and prepare everything for development.

### Tensorboard support
To set up TensorBoard support, run:

```bash
make setup-tensorboard
```
This will install the optional dependencies required for TensorBoard integration and set up the necessary configuration.


### Linter and type checker

Use [Ruff](https://github.com/charliermarsh/ruff) for linting and formatting:

```bash
make lint
```

Use [Ty](https://docs.astral.sh/ty/) for type checking:

```bash
make typecheck
```

Use the `check` target to run both linter and type checker:

```bash
make check
```

## Contributing to the code base

### Pre-commit hooks

Run the following command to install the pre-commit hook:

```bash
make setup

pre-commit install --config .github/hooks/.pre-commit-config.yaml --hook-type pre-commit --install-hooks --overwrite
```

### Tests

Use [pytest](https://docs.pytest.org/en/latest/) to run the test suite:

```bash
make test

# Run tests with HTML report
uv run pytest --cov=hyperbench --cov-report=html
```

This will ensure that your code adheres to the project's coding standards before each commit.

## Contributing to the documentation



## Policies

See the [Policies](../development/policies.md) page for information on versioning, Python support, and security policies.
