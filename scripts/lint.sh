#!/usr/bin/env bash

set -e
set -x

# mypy sqlmodel_v2_beta
flake8 sqlmodel_v2_beta tests docs_src
black sqlmodel_v2_beta tests docs_src --check
isort sqlmodel_v2_beta tests docs_src scripts --check-only
