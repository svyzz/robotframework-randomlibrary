from distutils.core import setup

DESCRIPTION = """
This repository details a collection of random utilities that can be used within tests written using RobotFramework
"""[1:-1]

setup(
    name = 'robotframework-random',
    version = '0.1.4',
    author = 'Arun Venkatram',
    author_email = 'stuxnetting@gmail.com',
    packages = ['src', 'tests'],
    url = 'https://github.com/svyzz/robotframework-random',
    license = 'LICENSE.txt',
    keywords = 'robotframework testing test automation random arun',
    description = DESCRIPTION,
    long_description = open('README.txt').read(),
    install_requires = [
        "requests >= 2.0.0",
        "yolk >= 0.4.3",
    ],
)