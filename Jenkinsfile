def envTestPath = params.env_test_path ?: "./tests"
def branchName =  params.branch_name ?: ""

export TEST_PATH=${envTestPath}

pipeline{
    agent any
    stages{
            stage("checkout"){
            checkout([$class: 'GitSCM', branches: [[name: ${branchName}]], extensions: [],
            userRemoteConfigs: [[url: 'https://github.com/saitejasseethiraju/PythonPageObjectModelAutomation.git']]])
            }
            }
        }
