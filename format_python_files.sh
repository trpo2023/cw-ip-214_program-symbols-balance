#!/bin/bash

git ls-files '*.py' | xargs autopep8 --in-place