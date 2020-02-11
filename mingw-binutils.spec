
%define binutils_target %{_arch}-generic-linux

Name:           mingw-binutils
Version:        2.34
Release:        325
License:        GPL-3.0
Summary:        GNU binary utilities
Url:            http://www.gnu.org/software/binutils/
Group:          devel
Source0:        https://mirrors.kernel.org/gnu/binutils/binutils-2.34.tar.xz
BuildRequires:  flex
BuildRequires:  libstdc++-dev
BuildRequires:  dejagnu
BuildRequires:  expect
BuildRequires:  tcl
BuildRequires:  glibc-staticdev
BuildRequires:  zlib-dev
BuildRequires:  texinfo
BuildRequires:  bison
BuildRequires:  mingw-gcc mingw-binutils
BuildRequires:  mingw-crt mingw-crt-dev
Requires:       binutils-info

Patch1:         binutils-stable-branch.patch
Patch2:         binutils-add-LD_AS_NEEDED-global-env.patch

# CVEs

Patch100: binutils-2.20.51.0.2-libtool-lib64.patch


%description
GNU binary utilities.

%package dev
License:        GPL-3.0
Summary:        GNU binary utilities
Group:          devel
Provides: binutils-devel

%description dev
GNU binary utilities.

%package doc
License:        GPL-3.0
Summary:        GNU binary utilities
Group:          doc

%description doc
GNU binary utilities.

%package locale
License:        GPL-3.0
Summary:        GNU binary utilities
Group:          libs

%description locale
GNU binary utilities.


%package extras
License:        GPL-3.0
Summary:        GNU binary utilities
Group:          libs

%description extras
GNU binary utilities.



%prep
%setup -q -n binutils-2.34

%patch1 -p1
%patch2 -p1

# CVEs

%patch100 -p1

rm -rf gdb libdecnumber readline sim

%build
export SOURCE_DATE_EPOCH=1549215809 
sed -i -e "s/#define BFD_VERSION_DATE.*/#define BFD_VERSION_DATE 20190203/g" bfd/version.h
# Do not use a macro - breaks toolchain
./configure --prefix=/usr \
    --enable-shared --disable-static \
    --target=x86_64-w64-mingw32	 \
    --build=%{binutils_target} \
    --libdir=/usr/mingw/lib \
    --includedir=/usr/include \
    --enable-deterministic-archives \
    --enable-lto \
    --enable-plugins \
    --enable-gold \
    --enable-secureplt \
    --with-sysroot=/usr/x86_64-w64-mingw32/sys-root \
    --with-lib-path=/usr/mingw/lib:/usr/lib64/mingw32:/usr/lib64:/usr/lib32:/usr/lib \
    --enable-targets=x86_64-w64-mingw32,i686-w64-mingw32	 \
    --disable-werror
make %{?_smp_flags} tooldir=/usr

%check
#make %{?_smp_flags} check tooldir=/usr || :

%install
export SOURCE_DATE_EPOCH=1549215809 
make %{?_smp_flags} tooldir=/usr DESTDIR=%{buildroot} install
install -d %{buildroot}%{_prefix}/include
ln -s mingw %{buildroot}/usr/x86_64-w64-mingw32
ln -s x86_64-w64-mingw32-windres %{buildroot}/usr/bin/windres


%find_lang binutils bin.lang
%find_lang bfd bfd.lang
%find_lang gas gas.lang
%find_lang gprof gprof.lang
%find_lang ld ld.lang
%find_lang opcodes opcodes.lang
cat *.lang > %{name}.lang

%files
/usr/x86_64-w64-mingw32
/usr/bin/x86_64-w64-mingw32-addr2line
/usr/bin/x86_64-w64-mingw32-ar
/usr/bin/x86_64-w64-mingw32-as
/usr/bin/x86_64-w64-mingw32-c++filt
/usr/bin/x86_64-w64-mingw32-dlltool
/usr/bin/x86_64-w64-mingw32-dllwrap
/usr/bin/x86_64-w64-mingw32-elfedit
/usr/bin/x86_64-w64-mingw32-gprof
/usr/bin/x86_64-w64-mingw32-ld
/usr/bin/x86_64-w64-mingw32-ld.bfd
/usr/bin/x86_64-w64-mingw32-nm
/usr/bin/x86_64-w64-mingw32-objcopy
/usr/bin/x86_64-w64-mingw32-objdump
/usr/bin/x86_64-w64-mingw32-ranlib
/usr/bin/x86_64-w64-mingw32-readelf
/usr/bin/x86_64-w64-mingw32-size
/usr/bin/x86_64-w64-mingw32-strings
/usr/bin/x86_64-w64-mingw32-strip
/usr/bin/x86_64-w64-mingw32-windmc
/usr/bin/x86_64-w64-mingw32-windres
/usr/bin/windres
/usr/lib/ldscripts/i386pe.x
/usr/lib/ldscripts/i386pe.xa
/usr/lib/ldscripts/i386pe.xbn
/usr/lib/ldscripts/i386pe.xe
/usr/lib/ldscripts/i386pe.xn
/usr/lib/ldscripts/i386pe.xr
/usr/lib/ldscripts/i386pe.xu
/usr/lib/ldscripts/i386pep.x
/usr/lib/ldscripts/i386pep.xa
/usr/lib/ldscripts/i386pep.xbn
/usr/lib/ldscripts/i386pep.xe
/usr/lib/ldscripts/i386pep.xn
/usr/lib/ldscripts/i386pep.xr
/usr/lib/ldscripts/i386pep.xu


%exclude   /usr/include/ctf-api.h
%exclude    /usr/include/ctf.h
   /usr/mingw/lib/libctf-nobfd.la
   /usr/mingw/lib/libctf-nobfd.so
   /usr/mingw/lib/libctf-nobfd.so.0
   /usr/mingw/lib/libctf-nobfd.so.0.0.0
   /usr/mingw/lib/libctf.la
   /usr/mingw/lib/libctf.so
   /usr/mingw/lib/libctf.so.0
   /usr/mingw/lib/libctf.so.0.0.0

/usr/x86_64-generic-linux/x86_64-w64-mingw32/

%exclude /usr/bin/ar
%exclude    /usr/bin/as
/usr/bin/dlltool
%exclude    /usr/bin/nm
%exclude    /usr/bin/objcopy
%exclude    /usr/bin/objdump
%exclude    /usr/bin/ranlib
%exclude    /usr/bin/readelf
%exclude    /usr/bin/strip


%files extras

%files dev

%files doc
/usr/share/man/
%exclude /usr/share/info/as.info
%exclude /usr/share/info/bfd.info
%exclude /usr/share/info/binutils.info
%exclude /usr/share/info/gprof.info
%exclude /usr/share/info/ld.info


%files locale
%exclude /usr/share/locale/
