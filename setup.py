from setuptools import setup
from os import path
from re import sub

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

# remove emojiis
long_description = sub(":[a-z_]+:", "- ", long_description)

setup(
  name = 'prune',
  packages = ['prune'],
  version = "0.0.1",
  description = 'Trim Entries from a Python Dictionary',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'Daniel J. Dufour',
  author_email = 'daniel.j.dufour@gmail.com',
  url = 'https://github.com/DanielJDufour/prune',
  download_url = 'https://github.com/DanielJDufour/prune/tarball/download',
  keywords = ['branch','dictionary','entry','prune','python','string','unpick'],
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3',
    'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    'Operating System :: OS Independent',
  ],
  install_requires=[]
)
