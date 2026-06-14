pipeline {
    agent none  // 不在任何固定 agent 上执行，后续动态分配
    
    stages {
        stage('Run tests in Docker') {
            agent {
                docker {
                    image 'python:3.11-slim'    // 使用的镜像
                    args '-v $WORKSPACE/test-results:/app/test-results'  // 挂载卷
                    reuseNode false
                }
            }
            steps {
                // 创建测试结果输出目录（宿主机）
                sh 'mkdir -p test-results'
                
                // 在容器内执行测试，并将结果输出到挂载的目录
                sh '''
                    pip install pytest pytest-cov
                    pytest tests/ --junit-xml=/app/test-results/test-results.xml \
                           --cov=src --cov-report=html:/app/test-results/htmlcov
                '''
            }
            post {
                always {
                    // 容器销毁后，结果仍在 test-results 目录中
                    junit 'test-results/*.xml'
                    publishHTML([
                        reportDir: 'test-results/htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                    // 可选：清理生成的临时文件（保留报告）
                    // cleanWs()
                }
            }
        }
    }
}