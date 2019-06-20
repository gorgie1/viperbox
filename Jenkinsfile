pipeline {

  agent any

    stages {

      stage('TEST') {
        steps('Run pytest tests - viperlib') {
          sh 'pytest viperbox/viperlib/tests'
        }

      }

      stage('BUILD') {

        steps('build, upload to PyPi and install locally from cloud') {
          sh 'rm -r -f dist'
          sh 'python3 setup.py sdist'
          sh 'python3 -m twine upload dist/* -u vipervit'
          sh 'pip install --upgrade viperbox'
       }

      }

    }

}
