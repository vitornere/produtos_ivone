#!/bin/bash
pip install autopep8
find . -name '**.py' -exec autopep8 --in-place '{}' \;