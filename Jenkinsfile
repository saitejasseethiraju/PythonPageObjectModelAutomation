def envTestPath = params.env_test_path ?: "./tests"
def branchName =  params.branch_name ?: ""


pipeline{
    agent {
            node{
                label 'my-agent'
            }

    }
    stages{
            stage("Install Requirements"){
            steps{
            echo "Branch name is ${branchName}"
//             virtualenv venv --distribute
//             . venv/bin/activate
//             pip install -r requirements.txt
//             sudo apt-get install python-pip
//             sh 'pip install -r requirements.txt'
             sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt'
                }
                            }
           }
        }
