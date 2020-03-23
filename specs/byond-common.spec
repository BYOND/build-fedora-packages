Name:       byond-common
Version:    %{_byondmajor}.%{_byondminor}
Release:    %{_releaseversion}%{?dist}
Summary:    Common BYOND libraries
URL:        http://www.byond.com/
License:    BYOND
Requires:   libgcc, glibc, libstdc++
Source0:    http://www.byond.com/download/build/%{_byondmajor}/%{_byondmajor}.%{_byondminor}_byond_linux.zip

%description
Provides common BYOND libraries needed by BYOND tools.

%prep
cd %{_builddir}
rm -rf *
/usr/bin/unzip -qq %{_sourcedir}/%{_byondmajor}.%{_byondminor}_byond_linux.zip
cp byond/legal.txt LICENSE

%build

%install
mkdir -p %{buildroot}%{_libdir}
install -m 0644 %{_builddir}/byond/bin/libbyond.so %{buildroot}%{_libdir}/libbyond.so
install -m 0644 %{_builddir}/byond/bin/libext.so %{buildroot}%{_libdir}/libext.so

%files
%license LICENSE
%{_libdir}/libbyond.so
%{_libdir}/libext.so

%changelog
* Mon Mar 23 2020 Stephen001 <stephen001@byondlabs.io> - %{_byondmajor}.%{_byondminor}-%{_releaseversion}
- Built automatically from BYOND upstream
