pipeline {
  agent {
    kubernetes {
      yamlFile 'agent-pod.yaml'
    }
  }

  triggers {
    upstream(upstreamProjects: 'BYOND/byond-release-finder/master', threshold: hudson.model.Result.SUCCESS)
  }

  stages {
    stage('Fetch Releases') {
      sh 'TODO!'
    }
  }
}
