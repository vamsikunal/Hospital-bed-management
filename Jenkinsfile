pipeline {
    agent {
        label 'jenkins-slave'
    }

    environment {
        ECR_REGISTRY = credentials('ecr_registry')
        ECR_REGION = credentials('ecr_region')
        ECS_CLUSTER = credentials('ecs_cluster')
    }

    stages {
        stage('gitclone') {
            steps {
                git branch: 'main', credentialsId: 'github_credentials', url: 'https://github.com/vamsikunal/Hospital-bed-management.git'
            }
        }

        stage('Connect ECR'){
            steps {
                // Connect to ECR
                sh 'aws ecr get-login-password --region ${ECR_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t ecomm:latest .'
            }
        }

        stage('Run Python Tests') {
            steps {
                sh 'docker container run -e DB_NAME=ecomm.sqlite3 -e DB_ENGINE=django.db.backends.sqlite3 --name web -p 8000:8000 hbms:latest'
                sh 'docker container exec web python manage.py test'
                sh 'docker contianer stop web'
                sh 'docker container rm web'
            }
        }

        stage('Push') {
            steps {
                // Push the image to ECR
                sh 'docker tag ecomm:latest ${ECR_REGISTRY}/ecomm:latest'
                sh 'docker push ${ECR_REGISTRY}/ecomm:latest'
            }
        }

        stage('Deploy to EKS') {
        steps {
            script {
                // Define the ECS service name and task definition name
                
            }
        }
    }
    }
}