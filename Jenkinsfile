def envTestPath = params.env_test_path ?: "./tests"
def branchName =  params.branch_name ?: ""


pipeline{
    agent any
    stages{
            stage("checkout"){
            steps{
            checkout([$class: 'GitSCM', branches: [[name: "${branchName}"]], extensions: [],
            userRemoteConfigs: [[url: 'https://github.com/saitejasseethiraju/PythonPageObjectModelAutomation.git']]])
            }

            }
            }
        }
