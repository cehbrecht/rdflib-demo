from setuptools import setup, find_packages

setup(
    name='provdemo',
    version='0.1',
    description='Graph Demo for Provenance',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    install_requires=[
        'rdflib',
        'prov',
        'sqlalchemy',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'provdemo=provdemo.cli:cli',
        ]
    },
)
