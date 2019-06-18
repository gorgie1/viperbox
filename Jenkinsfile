pipeline {

  agent any

    stages {

      stage('Build and Upload') {

        steps('build, upload to PyPi and install locally from cloud') {
          sh 'python3 setup.py sdist'
          sh 'python3 -m twine upload dist/* -u vipervit'
          sh 'pip install --upgrade tesqos'
          //sh 'rm -r dist'
       }
      }
    }

}
