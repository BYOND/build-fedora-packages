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
            values '31', 'rawhide'
          }
        }
        stages {
          stage('Build Common Package') {
            steps {
              container('rpmdev-fedora') {
                sh 'rpmdev-setuptree'
                sh 'cp /releases/stable/512.1488/512.1488_byond_linux.zip ~/rpmbuild/SOURCES/'
                sh 'rpmbuild -bb --define \'_byondmajor 512\' --define \'_byondminor 1488\' --define \'_releaseversion 1\' --target i386 specs/byond-common.spec'
                sh "mkdir -p /mnt/packages/${RELEASE}/arch/i386/Packages"
                sh "cp ~/rpmbuild/RPMS/i386/byond-common-512.1488-1.i386.rpm /mnt/packages/${RELEASE}/arch/i386/Packages/"
              }
            }
          }

          stage('Build DreamMaker Package') {
            steps {
              container('rpmdev-fedora') {
                sh 'rpmdev-setuptree'
                sh 'cp /releases/stable/512.1488/512.1488_byond_linux.zip ~/rpmbuild/SOURCES/'
                sh 'rpmbuild -bb --define \'_byondmajor 512\' --define \'_byondminor 1488\' --define \'_releaseversion 1\' --target i386 specs/byond-dreammaker.spec'
                sh "mkdir -p /mnt/packages/${RELEASE}/arch/i386/Packages"
                sh "cp ~/rpmbuild/RPMS/i386/byond-dreammaker-512.1488-1.i386.rpm /mnt/packages/${RELEASE}/arch/i386/Packages/"
              }
            }
          }
        }
      }
    }
  }
}
