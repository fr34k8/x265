Summary:	Open Source H265/HEVC video encoder
Name:		x265
Version:	1.4
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	https://bitbucket.org/multicoreware/x265/get/%{version}.tar.gz
# Source0-md5:	c27bee78929b7acb9fc09890f59ad191
BuildRequires:	cmake
BuildRequires:	yasm
Requires:	libx265 = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%package -n libx265
Summary:	x265 library
Group:		Libraries

%description -n libx265
x265 library.

%package -n libx265-devel
Summary:	Header files for x265 library
Group:		Development/Libraries
Requires:	libx265 = %{version}-%{release}

%description -n libx265-devel
This is the package containing the header files for x265 library.

%prep
%setup -qn multicoreware-x265-5e604833c5aa

%build
cd build/linux
%cmake ../../source
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/linux install \
	DESTDIR=$RPM_BUILD_ROOT

# workaround
%{__mv} $RPM_BUILD_ROOT{%{_prefix}/%{_pkgconfigdir},%{_pkgconfigdir}}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libx265 -p /usr/sbin/ldconfig
%postun	-n libx265 -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/x265

%files -n libx265
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libx265.so.*

%files -n libx265-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libx265.so
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

