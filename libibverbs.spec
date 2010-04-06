%define	major 1
%define libname	%mklibname ibverbs %{major}
%define develname %mklibname -d ibverbs

Summary:	A library for direct userspace use of RDMA (InfiniBand/iWARP) hardware
Name:		libibverbs
Version:	1.1.3
Release:	%mkrel 1
Group:		System/Libraries
License:	GPLv2 or BSD
URL:		http://openfabrics.org/
Source0:	http://openfabrics.org/downloads/verbs/libibverbs-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/libibverbs*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_libdir}/lib*.*a
%{_includedir}/*
%{_mandir}/man3/*

%files utils
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*

