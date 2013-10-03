from distutils.core import setup

setup(
    name='RobotFramework-Random',
    version='0.1.1',
    author='Arun Venkatram',
    author_email='stuxnetting@gmail.com',
    packages=['robotframework-random', 'robotframework-random.test'],
    url='http://pypi.python.org/pypi/RobotFramework-Random/',
    license='LICENSE.txt',
    description='This repository details a collection of random utilities that can be used within tests written using RobotFramework',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 2.0.0",
        "yolk >= 0.4.3",
    ],
)