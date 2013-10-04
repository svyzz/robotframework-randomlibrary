from setuptools import setup

setup(
    name='robotframework-randomlibrary',
    version='0.0.2',
    author=u'Arun Venkatram',
    author_email='stuxnetting@gmail.com',
    package_dir={'' : 'src'},
    packages=['RandomLibrary'],
    url='https://github.com/svyzz/robotframework-random',
    license='Apache 2.0, see LICENSE.txt',
    keywords='robotframework automation arun',
    platforms='any',
    description='A collection of random utilities that can be used within tests written using RobotFramework',
    long_description=open('README.txt').read(),
    zip_safe=False,
    install_requires = ['robotframework'],
)