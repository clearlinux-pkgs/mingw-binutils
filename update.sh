#!/bin/bash

spec=mingw-binutils.spec
patch=binutils-stable-branch.patch
make bumpnogit
git commit -m "Stable branch update" $spec $patch release
make koji
