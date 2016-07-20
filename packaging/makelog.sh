#!/bin/bash

mainlog="CHANGELOG"
pypilog="../library/CHANGELOG.txt"

# generate pypi changelog

sed -e "/--/d" -e "s/  \*/\*/" \
    -e "s/.*\([0-9].[0-9].[0-9]\).*/\1/" \
    -e '/[0-9].[0-9].[0-9]/ a\
    -----' $mainlog | cat -s > $pypilog

exit 0
