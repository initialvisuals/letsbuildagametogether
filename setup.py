# -*- coding: utf-8 -*- 
# we can use this to build the package 
# Learn more: https://github.com/kennethreitz/setup.py
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='A Game',
    version='1.0.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Initial Visuals and Friends',
    author_email='',
    maintainer='Initial Visuals',
    maintainer_email='initialcreature@gmail.com',
    url='https://github.com/initialvisuals/letsbuildagametogether',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

