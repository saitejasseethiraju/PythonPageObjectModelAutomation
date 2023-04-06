def envTestPath = params.env_test_path ?: "./tests"
def branchName =  params.branch_name ?: ""


pipeline{
    agent any
    stages{
            stage("Install Requirements"){
            steps{
            echo "Branch name is ${branchName}"
            sh 'pip install -r requirements.txt'
                }
                            }
           }
        }
