def envTestPath = params.env_test_path ?: "./tests"
def branchName =  params.branch_name ?: ""


pipeline{
    agent {
            node{
                label 'my-agent'
            }

    }
    stages
    {
            stage("Install Requirements")
            {
                steps
                {
                    echo "Branch name is ${branchName}"
                    bat 'python -m venv venv'
                    bat 'venv/Scripts/activate.bat'
                    bat 'cd venv/Lib/site-packages'
                    bat 'pip install -r requirements.txt'
                }
            }

            stage("Run Testcase")
            {
                steps
                {
                    echo "Test path is ${envTestPath}"
                    bat 'pytest ${envTestPath}'
                }
                            }
           }

    }
