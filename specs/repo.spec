Name:       byondlabs-release
Version:    %{_releasever}
Release:    1
Summary:    BYONDLabs Repository Installer
URL:        https://fedora.byondlabs.io/
License:    GPLv3
BuildArch:  noarch
Source1:    byondlabs.repo
Source2:    byondlabs-testing.repo
Source3:    RPM-GPG-KEY-byondlabs

Requires:   system-release(%{version})
Provides:   byondlabs-repos(%{version})

%description
Provides the BYONDLabs repository configuration and keys.

%prep

%build

%install
install -d -m755 \
  %{buildroot}%{_sysconfdir}/pki/rpm-gpg  \
  %{buildroot}%{_sysconfdir}/yum.repos.d

%{__install} -Dp -m644 \
    %{SOURCE3} \
    %{buildroot}%{_sysconfdir}/pki/rpm-gpg

ln -s $(basename %{SOURCE3}) %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-byondlabs-fedora-30
ln -s $(basename %{SOURCE3}) %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-byondlabs-fedora-31
ln -s $(basename %{SOURCE3}) %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-byondlabs-fedora-32
ln -s $(basename %{SOURCE3}) %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-byondlabs-fedora-rawhide

%{__install} -p -m644 \
    %{SOURCE1} \
    %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/yum.repos.d

%files
%config %{_sysconfdir}/pki/rpm-gpg/*
%config(noreplace) %{_sysconfdir}/yum.repos.d/byondlabs.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/byondlabs-testing.repo

%changelog
* Mon Mar 23 2020 Stephen001 <stephen001@byondlabs.io> - %{_releasever}-1
- Built to deploy repositories