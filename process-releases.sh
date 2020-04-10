#!/usr/bin/env bash


UPSTREAM_TYPE=${1}
RELEASE=${2}
PACKAGE=${3}

if [ "${UPSTREAM_TYPE}" = "stable" ]; then
  DOWNSTREAM_TYPE="base"
else
  DOWNSTREAM_TYPE="updates"
fi

mkdir -p /data/fedora/${RELEASE}/${DOWNSTREAM_TYPE}/i686/Packages /data/fedora/${RELEASE}/${DOWNSTREAM_TYPE}/x86_64/Packages

VERSIONS=($(comm -2 -3 <(ls /data/upstream/${UPSTREAM_TYPE}) <(ls /data/fedora/${RELEASE}/${DOWNSTREAM_TYPE}/i686/Packages/ | grep ${PACKAGE} | cut -d '-' -f 3)))

if [ "${#VERSIONS[@]}" -gt "1" ]; then
  echo "Processing new versions"
  for VERSION in "${VERSIONS[@]}"; do
      echo "Processing ${i} for Fedora ${RELEASE} ${DOWNSTREAM_TYPE}"
      MAJOR_VERSION=$(cut -d '.' -f 1 <<< "${VERSION}")
      MINOR_VERSION=$(cut -d '.' -f 2 <<< "${VERSION}")
      rm -rf ~/rpmbuild
      rpmdev-setuptree
      cp /data/upstream/${UPSTREAM_TYPE}/${VERSION}/${VERSION}_byond_linux.zip ~/rpmbuild/SOURCES/
      rpmbuild -bb --define "_byondmajor ${MAJOR_VERSION}" --define "_byondminor ${MINOR_VERSION}" --define "_releaseversion 1" --target i686 specs/byond-${PACKAGE}.spec
      cp ~/rpmbuild/RPMS/i686/byond-${PACKAGE}-${MAJOR_VERSION}.${MINOR_VERSION}-1.fc${RELEASE}.i686.rpm /data/fedora/${RELEASE}/${DOWNSTREAM_TYPE}/i686/Packages/
      cp ~/rpmbuild/RPMS/i686/byond-${PACKAGE}-${MAJOR_VERSION}.${MINOR_VERSION}-1.fc${RELEASE}.i686.rpm /data/fedora/${RELEASE}/${DOWNSTREAM_TYPE}/x86_64/Packages/
  done
fi