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
            values '30', '31', '32', 'rawhide'
          }
        }
        stages {
          stage('Build Common Package') {
            steps {
              container('rpmdev-fedora') {
                sh 'gpg --batch --import /secret/stephen001-byondlabs.io.asc || true'
                sh 'echo \'%_gpg_name "Stephen001 @ BYONDLabs <stephen001@byondlabs.io>"\' > ~/.rpmmacros'
                sh 'rpmdev-setuptree'
                sh 'cp /data/upstream/stable/512.1488/512.1488_byond_linux.zip ~/rpmbuild/SOURCES/'
                sh 'rpmbuild -bb --define \'_byondmajor 512\' --define \'_byondminor 1488\' --define \'_releaseversion 1\' --target i386 specs/byond-common.spec'
                sh "mkdir -p /data/fedora/${RELEASE}/base/i386/Packages"
                sh "cp ~/rpmbuild/RPMS/i386/byond-common-512.1488-1.i386.rpm /data/fedora/${RELEASE}/base/i386/Packages/"
                sh "createrepo /data/fedora/${RELEASE}/base/i386"
                sh "gpg --detach-sign --armor /data/fedora/${RELEASE}/base/i386/repodata/repomd.xml"
              }
            }
          }

          stage('Build DreamMaker Package') {
            steps {
              container('rpmdev-fedora') {
                sh 'gpg --batch --import /secret/stephen001-byondlabs.io.asc || true'
                sh 'echo \'%_gpg_name "Stephen001 @ BYONDLabs <stephen001@byondlabs.io>"\' > ~/.rpmmacros'
                sh 'rpmdev-setuptree'
                sh 'cp /data/upstream/stable/512.1488/512.1488_byond_linux.zip ~/rpmbuild/SOURCES/'
                sh 'rpmbuild -bb --define \'_byondmajor 512\' --define \'_byondminor 1488\' --define \'_releaseversion 1\' --target i386 specs/byond-dreammaker.spec'
                sh "mkdir -p /data/fedora/${RELEASE}/base/i386/Packages"
                sh "cp ~/rpmbuild/RPMS/i386/byond-dreammaker-512.1488-1.i386.rpm /data/fedora/${RELEASE}/base/i386/Packages/"
                sh "createrepo /data/fedora/${RELEASE}/base/i386"
                sh "gpg --detach-sign --armor /data/fedora/${RELEASE}/base/i386/repodata/repomd.xml"
              }
            }
          }

          stage('Build DreamDaemon Package') {
            steps {
              container('rpmdev-fedora') {
                sh 'gpg --batch --import /secret/stephen001-byondlabs.io.asc || true'
                sh 'echo \'%_gpg_name "Stephen001 @ BYONDLabs <stephen001@byondlabs.io>"\' > ~/.rpmmacros'
                sh 'rpmdev-setuptree'
                sh 'cp /data/upstream/stable/512.1488/512.1488_byond_linux.zip ~/rpmbuild/SOURCES/'
                sh 'rpmbuild -bb --define \'_byondmajor 512\' --define \'_byondminor 1488\' --define \'_releaseversion 1\' --target i386 specs/byond-dreamdaemon.spec'
                sh "mkdir -p /data/fedora/${RELEASE}/base/i386/Packages"
                sh "cp ~/rpmbuild/RPMS/i386/byond-dreamdaemon-512.1488-1.i386.rpm /data/fedora/${RELEASE}/base/i386/Packages/"
                sh "createrepo /data/fedora/${RELEASE}/base/i386"
                sh "gpg --detach-sign --armor /data/fedora/${RELEASE}/base/i386/repodata/repomd.xml"
              }
            }
          }
        }
      }
    }
  }
}
