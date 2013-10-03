from setuptools import setup
from setuptools import find_packages

setup(
    name='rf-random',
    version='0.0.2',
    author=u'Arun Venkatram',
    author_email='stuxnetting@gmail.com',
    packages=find_packages(),
    url='https://github.com/svyzz/robotframework-random',
    license='Apache 2.0, see LICENSE.txt',
    keywords='robotframework automation arun',
    platforms='any',
    description='A collection of random utilities that can be used within tests written using RobotFramework',
    long_description=open('README.txt').read(),
    zip_safe=False,
    install_requires = ['robotframework', 'requests'],
)