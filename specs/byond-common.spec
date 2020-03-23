Name:       byond-common
Version:    %{_byondmajor}.%{_byondminor}
Release:    %{_releaseversion}
Summary:    Common BYOND libraries
URL:        http://www.byond.com/
License:    FIXME
Requires:   libgcc
Source0:    http://www.byond.com/download/build/%{_byondmajor}/%{_byondmajor}.%{_byondminor}_byond_linux.zip

%description
Provides common BYOND libraries needed by BYOND tools.

%prep
cd %{_builddir}
rm -rf byond
/usr/bin/unzip -qq %{_sourcedir}/%{_byondmajor}.%{_byondminor}_byond_linux.zip

%build

%install
mkdir -p %{buildroot}%{_libdir}
install -m 0644 %{_builddir}/byond/bin/libbyond.so %{buildroot}%{_libdir}/libbyond.so
install -m 0644 %{_builddir}/byond/bin/libext.so %{buildroot}%{_libdir}/libext.so

%files
%{_libdir}/libbyond.so
%{_libdir}/libext.so

%changelog
# let's skip this for now
