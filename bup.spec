Summary:	Efficient backup system based on the git packfile format
Name:		bup
Version:	0.26
Release:	1
License:	GPLv2+
Group:		Archiving/Backup
Url:		https://github.com/bup/bup
Source0:	https://github.com/bup/bup/archive/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
Requires:	python-fuse
Requires:	python-pylibacl
Requires:	python-xattr

%description
Bup is a very efficient backup system based on the git packfile format,
providing fast incremental saves and global deduplication (among and
within files, including virtual machine images).

%files
%{_bindir}/%{name}
# this path seems to be hardcoded so using _libdir requires testing,
# just leave it like that for now
%{_prefix}/lib/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
./configure
%make

%install
%makeinstall_std

%check
# Tests are quite long, don't enable them for ABF
# make check
