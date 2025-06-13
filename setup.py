from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='lambertbattin',
    version='1.0',
    description='Lambertbattin module',
    license="MIT",
    author='Miguel',
    packages=['lambertbattin'],  #same as name
    install_requires=requirements
)