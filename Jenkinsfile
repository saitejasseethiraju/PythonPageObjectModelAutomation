def envTestPath = params.env_test_path ?: "./tests"
def branchName =  params.branch_name ?: ""


pipeline{
    agent any
    stages{
            stage("Install Requirements"){
            steps{
            echo "Branch name is ${branchName}"
            pip install -r requirements.txt
                }
                            }
           }
        }
