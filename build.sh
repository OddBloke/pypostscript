#!/bin/bash
function build {
    CODE_ROOT=$1

    # Remove .pyc files from codebase
    find ./${CODE_ROOT} -name "*.pyc" | xargs rm

    # Run tests
    nosetests

    # Sphinx docs
    ( cd docs; make clean html SPHINXOPTS="-a -n -w sphinx-output" )

    # PEP8
    pep8 --ignore=W293 --exclude=migrations,manage.py -r ${CODE_ROOT} > pep8.txt || echo "PEP-8 violations."
}

build pyformprint
