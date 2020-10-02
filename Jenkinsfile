pipeline {
    environment { 
        registry = "jerdoss/timeoff-management-app" 
        registryCredential = '65b920c0-2ccd-4f53-a11a-1edeb91c69ee' 
        dockerImage = ''
    }
    agent { node {label 'centos'} }
    stages {
        stage('Clone Repository') { 
            steps {
                cleanWs()
                git url: "https://github.com/jerdoss/timeoff-management-application.git/"
            }
        }
        stage('Build Docker Image') { 
            steps {
                script { 
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                }
            }
        }
        stage('Installing & Starting Application') { 
            steps {
                script { 
                    sh "npm install"
                    sh "nohup npm start &"
                    //sh 'docker run --name timeoff -p 3000:3000 "${registry}"' + '":$BUILD_NUMBER"'
                }
            }
        }
        stage('Runnning Coverage Test') { 
            steps {
                sh "USE_CHROME=1 npm test"
            }
        }
        stage('Push Docker Image') { 
            steps {
                script { 
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() 
                    }
                }
            }
        }
        stage('Deleting Docker Image') { 
            steps {
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
    }    
}