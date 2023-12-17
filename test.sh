#!/bin/sh

set -ex

pip3 install -r test_requirements.txt
MYPYPATH=src mypy src/*.py --namespace-packages --explicit-package-bases 
MYPYPATH=src mypy tests/*.py --namespace-packages --explicit-package-bases
pytest
