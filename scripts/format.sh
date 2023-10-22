#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place sqlmodel docs_src tests --exclude=__init__.py
black sqlmodel_v2_beta tests docs_src
isort sqlmodel_v2_beta tests docs_src
