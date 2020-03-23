Name:       byond-dreammaker
Version:    %{_byondmajor}.%{_byondminor}
Release:    %{_releaseversion}%{?dist}
Summary:    BYOND Language Compiler
URL:        http://www.byond.com/
License:    BYOND
Group:      BYOND
Requires:   libgcc, glibc, libstdc++, byond-common >= %{_byondmajor}.%{_byondminor}-%{_releaseversion}
Source0:    http://www.byond.com/download/build/%{_byondmajor}/%{_byondmajor}.%{_byondminor}_byond_linux.zip

%description
Provides the BYOND language compiler, known as DreamMaker.

%prep
cd %{_builddir}
rm -rf *
/usr/bin/unzip -qq %{_sourcedir}/%{_byondmajor}.%{_byondminor}_byond_linux.zip
cp byond/legal.txt LICENSE
/usr/bin/gzip byond/man/man6/DreamMaker.6

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man6
install -m 0755 %{_builddir}/byond/bin/DreamMaker %{buildroot}%{_bindir}/DreamMaker
install -m 0644 %{_builddir}/byond/man/man6/DreamMaker.6.gz %{buildroot}%{_mandir}/man6/DreamMaker.6.gz

%files
%license LICENSE
%{_bindir}/DreamMaker
%{_mandir}/man6/DreamMaker.6.gz

%changelog
* Mon Mar 23 2020 Stephen001 <stephen001@byondlabs.io> - %{_byondmajor}.%{_byondminor}-%{_releaseversion}
- Built automatically from BYOND upstream
