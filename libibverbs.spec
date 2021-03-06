%define	major 1
%define libname	%mklibname ibverbs %{major}
%define develname %mklibname -d ibverbs

%define _disable_lto 1

Summary:	A library for direct userspace use of RDMA (InfiniBand/iWARP) hardware
Name:		libibverbs
Version:	1.2.1
Release:	2
Group:		System/Libraries
License:	GPLv2 or BSD
URL:		http://openfabrics.org/
Source0:	http://openfabrics.org/downloads/verbs/libibverbs-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:  pkgconfig(libnl-1)

%description
libibverbs is a library that allows userspace processes to use RDMA "verbs" as
described in the InfiniBand Architecture Specification and the RDMA Protocol
Verbs Specification. This includes direct hardware access from userspace to
InfiniBand/iWARP adapters (kernel bypass) for fast path operations. For this
library to be useful, a device-specific plug-in module should also be
installed.

%package -n	%{libname}
Summary:	A library for direct userspace use of RDMA (InfiniBand/iWARP) hardware
Group:          System/Libraries

%description -n	%{libname}
libibverbs is a library that allows userspace processes to use RDMA "verbs" as
described in the InfiniBand Architecture Specification and the RDMA Protocol
Verbs Specification. This includes direct hardware access from userspace to
InfiniBand/iWARP adapters (kernel bypass) for fast path operations. For this
library to be useful, a device-specific plug-in module should also be
installed.

This package contains the shared libibverbs library.

%package -n	%{develname}
Summary:	Static library and header files for the libibverbs library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{develname}
libibverbs is a library that allows userspace processes to use RDMA "verbs" as
described in the InfiniBand Architecture Specification and the RDMA Protocol
Verbs Specification. This includes direct hardware access from userspace to
InfiniBand/iWARP adapters (kernel bypass) for fast path operations. For this
library to be useful, a device-specific plug-in module should also be
installed.

This package contains the static libibverbs library and its header files.

%package	utils
Summary:	Examples for the libibverbs library
Group:		System/Libraries
Requires:	%{libname} = %{version}

%description	utils
Useful libibverbs example programs such as ibv_devinfo, which displays
information about RDMA devices.

%prep
%setup -q

%build
export CC=gcc
%configure
%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/libibverbs*.so.%{major}*

%files -n %{develname}
%{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man3/*

%files utils
%{_bindir}/*
%{_mandir}/man1/*
