node {
    def app

    stage('Clone repository') {
      

        checkout scm
    }

    stage('Build image') {
  
       // Use your docker hub repo name
       app = docker.build("anbuselvi/demo")
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        // replace docker with the jenkins credential for docker hub
        docker.withRegistry('https://registry.hub.docker.com', 'docker') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}
