from setuptools import setup

setup(name='utilities',
    version='0.1',
    description='General purpose functions',
    author='Nathaniel Rodriguez',
    packages=['utilities'],
    url='https://github.com/Nathaniel-Rodriguez/utilities.git',
    install_requires = [
    	'numpy',
    	'matplotlib',
    	'networkx'],
    zip_safe=False)