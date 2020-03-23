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
            values '30', '31'
          }
        }
        stages {
          stage('Build Packages') {
            container('fedora') {
              steps {
                sh 'Hello!'
              }
            }
          }
        }
      }
    }
  }
}
