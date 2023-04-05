import subprocess

# Clone the TensorFlow models repository
subprocess.run(['rm', '-rf', './models'])
subprocess.run(['git', 'clone', 'https://github.com/tensorflow/models.git'])

# Install the object_detection library
subprocess.run(['cd', 'models/research'])
subprocess.run(['protoc', 'object_detection/protos/*.proto', '--python_out=.'])
subprocess.run(['cp', 'object_detection/packages/tf2/setup.py', '.'])
subprocess.run(['python3', '-m', 'pip', 'install', '--use-feature=2020-resolver', '.'])