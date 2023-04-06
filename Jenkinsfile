pipeline{
    agent any
    stages{
            stage("build"){
                steps{
                    echo "this is first jenkins file"
                    echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                            }
                    }
            stage('Install Requirements') {
                steps {
                    sh """
                        source /etc/profile
                        source /Users/jenkins/PycharmProjects/voltron/venv/bin/activate
                        pip install -r requirements.txt
                        """
                                            }
                        }
            }
        }
