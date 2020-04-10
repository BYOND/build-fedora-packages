pipeline {
  agent none

  triggers {
    upstream(upstreamProjects: 'BYOND/byond-release-finder/master', threshold: hudson.model.Result.SUCCESS)
  }

  stages {
    stage('Build Packages') {
      matrix {
        agent {
          kubernetes {
            yamlFile "agent-pod-${RELEASE}.yaml"
          }
        }
        axes {
          axis {
            name 'RELEASE'
            values '30', '31', '32'
          }
        }
        stages {
          stage('Build Common Package') {
            steps {
              container('rpmdev-fedora') {
                sh "./process-releases.sh stable ${RELEASE} common"
                sh "./process-releases.sh beta ${RELEASE} common"
              }
            }
          }

          stage('Build DreamMaker Package') {
            steps {
              container('rpmdev-fedora') {
                sh "./process-releases.sh stable ${RELEASE} dreammaker"
                sh "./process-releases.sh beta ${RELEASE} dreammaker"
              }
            }
          }

          stage('Build DreamDaemon Package') {
            steps {
              container('rpmdev-fedora') {
                sh "./process-releases.sh stable ${RELEASE} dreamdaemon"
                sh "./process-releases.sh beta ${RELEASE} dreamdaemon"
              }
            }
          }

          stage('Build Repo Config') {
            steps {
              container('rpmdev-fedora') {
                sh 'rpmdev-setuptree'
                sh 'cp repo-config/* ~/rpmbuild/SOURCES/'
                sh 'gpg --batch --import /secret/stephen001-byondlabs.io.asc || true'
                sh 'gpg --batch --yes --export -a \'Stephen001 @ BYONDLabs <stephen001@byondlabs.io>\' > ~/rpmbuild/SOURCES/RPM-GPG-KEY-byondlabs'
                sh "rpmbuild -bb --define '_releasever ${RELEASE}' specs/repo.spec"
                sh "mkdir -p /data/fedora/${RELEASE}/base/i686/Packages /data/fedora/${RELEASE}/base/x86_64/Packages"
                sh "cp ~/rpmbuild/RPMS/noarch/byondlabs-release-${RELEASE}-*.noarch.rpm /data/fedora/${RELEASE}/base/i686/Packages/"
                sh "cp ~/rpmbuild/RPMS/noarch/byondlabs-release-${RELEASE}-*.noarch.rpm /data/fedora/${RELEASE}/base/x86_64/Packages/"
              }
            }
          }

          stage('Sign') {
            steps {
              container('rpmdev-fedora') {
                sh 'gpg --batch --import /secret/stephen001-byondlabs.io.asc || true'
                sh 'echo \'%_gpg_name Stephen001 @ BYONDLabs\' > ~/.rpmmacros'
                sh 'echo \'%_signature gpg\' >> ~/.rpmmacros'
                sh 'echo \'%_gpgbin /usr/bin/gpg\' >> ~/.rpmmacros'
                sh "rpm --resign /data/fedora/${RELEASE}/base/i686/Packages/*.rpm"
                sh "rpm --resign /data/fedora/${RELEASE}/base/x86_64/Packages/*.rpm"
                sh "rpm --resign /data/fedora/${RELEASE}/updates/i686/Packages/*.rpm"
                sh "rpm --resign /data/fedora/${RELEASE}/updates/x86_64/Packages/*.rpm"
                sh "mkdir -p /data/fedora/${RELEASE}/base/i686/repodata /data/fedora/${RELEASE}/base/x86_64/repodata"
                sh "mkdir -p /data/fedora/${RELEASE}/updates/i686/repodata /data/fedora/${RELEASE}/updates/x86_64/repodata"
                sh "cp group.xml /data/fedora/${RELEASE}/base/i686/repodata/"
                sh "cp group.xml /data/fedora/${RELEASE}/base/x86_64/repodata/"
                sh "cp group.xml /data/fedora/${RELEASE}/updates/i686/repodata/"
                sh "cp group.xml /data/fedora/${RELEASE}/updates/x86_64/repodata/"
                sh "createrepo -g repodata/group.xml /data/fedora/${RELEASE}/base/i686"
                sh "gpg --batch --yes --detach-sign --armor /data/fedora/${RELEASE}/base/i686/repodata/repomd.xml"
                sh "createrepo -g repodata/group.xml /data/fedora/${RELEASE}/base/x86_64"
                sh "gpg --batch --yes --detach-sign --armor /data/fedora/${RELEASE}/base/x86_64/repodata/repomd.xml"
                sh "createrepo -g repodata/group.xml /data/fedora/${RELEASE}/updates/i686"
                sh "gpg --batch --yes --detach-sign --armor /data/fedora/${RELEASE}/updates/i686/repodata/repomd.xml"
                sh "createrepo -g repodata/group.xml /data/fedora/${RELEASE}/updates/x86_64"
                sh "gpg --batch --yes --detach-sign --armor /data/fedora/${RELEASE}/updates/x86_64/repodata/repomd.xml"
              }
            }
          }
        }
      }
    }

    stage("Copy Site Root") {
      agent {
        kubernetes {
          yamlFile "agent-pod.yaml"
        }
      }

      steps {
        container('busybox') {
          sh 'cp -rf site/* /data/fedora/'
        }
      }
    }
  }
}
