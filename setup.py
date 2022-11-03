import os
from setuptools import setup

JFROG_USERNAME = os.environ.get('JFROG_USERNAME')
JFROG_PASSWORD = os.environ.get('JFROG_PASSWORD')

setup(
  name = 'abbreviations',
  packages = ['abbreviations'], # this must be the same as the name above
  version = '0.2.6',
  description = 'Python3 implementation of the Schwartz-Hearst algorithm for extracting abbreviation-definition pairs',
  license = 'MIT',
  author = 'Phil Gooch and Vincent Van Asch and Ryan Christensen :D',
  author_email = 'ryan.christensen@tellic.com',
  url = 'https://github.com/ryanchristensen20/abbreviation-extraction',
  keywords = ['python3', 'nlp', 'keyword-extraction', 'abbreviations', 'information-extraction'],
  classifiers = [],
  install_requires=[
    'regex',
  ],
  zip_safe=False,
)
