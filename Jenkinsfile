pipeline {
    agent none

    stages {
        stage('Checkout') {
            agent any
            steps {
                git branch: 'main',
                    credentialsId: 'github-ssh-key',   // 【修改】替换为你 Jenkins 中真实的 SSH 凭证 ID
                    url: 'git@github.com:chenpeiyong/tools.git'
            }
        }

        stage('Run tests in Docker') {
            agent {
                docker {
                    image 'python:3.11-slim'
                    args '-u root'                     // 以 root 运行，避免 pip 权限问题
                }
            }
            steps {
                sh '''
                    pip install pytest pytest-cov
                    # 确保 src 包能被找到（如果你的项目缺少 __init__.py，这行可以临时解决）
                    export PYTHONPATH="${WORKSPACE}:${PYTHONPATH}"
                    pytest tests/ --junit-xml=test-results.xml \
                           --cov=src --cov-report=html:htmlcov
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                    publishHTML([
                        reportDir: 'htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report',
                        allowMissing: false,          // 报告缺失时不使构建失败
                        alwaysLinkToLastBuild: true,  // 在构建页面始终显示链接
                        keepAll: false                // 不保留所有历史报告（仅当前构建）
                    ])
                    // 删除由 root 产生的临时文件，避免下次 git checkout 权限问题
                    sh 'rm -rf .pytest_cache htmlcov'
                }
            }
        }
    }
}