from setuptools import setup, find_packages

setup(
    name='tfmodelserver',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'Flask',
        'flask-cors',
        'opencv-python',
        'numpy',
        'requests',
        'pytz',
        'absl-py'
    ],
    extras_require={
      'dev': [
          'tensorflow==1.11.0'
      ]
    },
    version='1.0.3.dev0',
    description='Libraries for easy bootstrapping TensorFlow server',
    author='Sanghoon Yoon',
    author_email='shygiants@gmail.com',
    url='https://github.com/shygiants/tfmodelserver',
    keywords=['tensorflow', 'libraries'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 2.7',
    ],
    python_requires='>=2.7'
)