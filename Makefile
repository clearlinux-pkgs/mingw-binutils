PKG_NAME := mingw-binutils
URL := https://mirrors.kernel.org/gnu/binutils/binutils-2.34.tar.xz
include ../common/Makefile.common

update:
	pushd ~/git/binutils-gdb ; git remote update -p ; git diff binutils-2_34..origin/binutils-2_34-branch  > ~/clear/packages/mingw-binutils/binutils-stable-branch.patch.in ; filterdiff  ~/clear/packages/mingw-binutils/binutils-stable-branch.patch.in > ~/clear/packages/mingw-binutils/binutils-stable-branch.patch  ; rm ~/clear/packages/mingw-binutils/binutils-stable-branch.patch.in ; popd
	git diff --exit-code  binutils-stable-branch.patch || bash ./update.sh
