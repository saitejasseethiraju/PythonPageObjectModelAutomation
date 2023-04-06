def envTestPath = params.env_test_path ?: "./tests"

export TEST_PATH=${envTestPath}

pipeline{
    agent any
    stages{
            stage("checkout"){
            checkout([$class: 'GitSCM', branches: [[name: ${env_test_path}]], extensions: [],
            userRemoteConfigs: [[url: 'https://github.com/saitejasseethiraju/PythonPageObjectModelAutomation.git']]])
            }
            stage("build"){
                steps{
                    echo "this is first jenkins file"

                            }
                    }
//             stage('Install Requirements') {
//                 steps {
//                     sh """
//                         source D:/ProjectPythonSelenium/PythonPageObjectModelAutomation/venv/bin/activate
//                         pip install -r requirements.txt
//                         """
//                                             }
//                         }

            stage('Run Tests') {
            steps {
                sh 'pytest tests/test_one_open_browser.py'
                                }
                   }
            }
        }
