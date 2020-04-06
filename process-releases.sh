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

echo "Versions to process:"
for i in "${VERSIONS[@]}"; do
    echo "    ${i}"
done
