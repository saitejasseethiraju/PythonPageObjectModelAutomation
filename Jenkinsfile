def envTestPath = params.env_test_path ?: "./tests"

export TEST_PATH=${envTestPath}

pipeline{
    agent any
    stages{
            stage("checkout"){
            checkout([$class: 'GitSCM', branches: [[name: ${env_test_path}]], extensions: [],
            userRemoteConfigs: [[url: 'https://github.com/saitejasseethiraju/PythonPageObjectModelAutomation.git']]])
            }
            }
        }
