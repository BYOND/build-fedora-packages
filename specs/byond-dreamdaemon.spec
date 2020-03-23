Name:       byond-dreamdaemon
Version:    %{_byondmajor}.%{_byondminor}
Release:    %{_releaseversion}%{?dist}
Summary:    BYOND Hosting Process
URL:        http://www.byond.com/
License:    BYOND
Group:      BYOND
Requires:   libgcc(x86-32), glibc(x86-32), libstdc++(x86-32), byond-common(x86-32) >= %{_byondmajor}.%{_byondminor}-%{_releaseversion}
Source0:    http://www.byond.com/download/build/%{_byondmajor}/%{_byondmajor}.%{_byondminor}_byond_linux.zip

%description
DreamDaemon is BYOND's server hosting process.

%prep
cd %{_builddir}
rm -rf *
/usr/bin/unzip -qq %{_sourcedir}/%{_byondmajor}.%{_byondminor}_byond_linux.zip
cp byond/legal.txt LICENSE
/usr/bin/gzip byond/man/man6/DreamDaemon.6

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man6
install -m 0755 %{_builddir}/byond/bin/DreamDaemon %{buildroot}%{_bindir}/DreamDaemon
install -m 0644 %{_builddir}/byond/man/man6/DreamDaemon.6.gz %{buildroot}%{_mandir}/man6/DreamDaemon.6.gz

%files
%license LICENSE
%{_bindir}/DreamDaemon
%{_mandir}/man6/DreamDaemon.6.gz

%changelog
* Mon Mar 23 2020 Stephen001 <stephen001@byondlabs.io> - %{_byondmajor}.%{_byondminor}-%{_releaseversion}
- Built automatically from BYOND upstream
