#!usrbinenv python3
from setuptools import setup, find_packages

setup(
    name='DynamodbToCSV',
    version='1.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dynamotocsv=scripts.dynamodbJson_to_csv:clistart'
        ]
    }
)