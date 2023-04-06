pipeline{
    agent any
    stages{
            stage("build"){
                steps{
                    echo "this is first jenkins file"
                    echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
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
