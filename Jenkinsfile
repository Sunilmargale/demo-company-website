pipeline {
    agent any
    stages {
        stage("code"){
            steps {
            echo "cloning the code" 
            git url:"https://github.com/Sunilmargale/django-notes-app.git", branch: "master"
            }
        }
        stage("build"){
            steps {
                echo "building the image"
                sh "docker build -t demo-website ."
            }
        }
        stage("push to dockerhub"){
            steps {
                echo "pushing the image to dockerhub"
                withCredentials([usernamePassword(credentialsId:"docker-hub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"  
                sh "docker tag notes-app ${env.dockerHubUser}/demo-website:latest"
                sh "docker push ${env.dockerHubUser}/demo-website:latest"
                }
            } 
        }
        stage("deploy"){
            steps {
                echo "deploying the container"
                sh "docker run -d -p 8081:8081 sunilmargale/demo-website:latest"
            }
        }
    }
}
