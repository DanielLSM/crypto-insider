from setuptools import setup, find_packages
import sys

if sys.version_info.major != 3:
    print('This Python is only compatible with Python 3, but you are running '
          'Python {}. The installation will likely fail.'.format(sys.version_info.major))

setup(name='baselines',
      packages=[package for package in find_packages()
                if package.startswith('crypto-insider')],
      install_requires=[
          'lxml',
          'requests',
      ],
      description='A library to scrap popular crypto currencies websites ',
      author='Marta. Daniel Luis',
      url='https://github.com/DanielLSM/crypto-insider',
      author_email='daniellsmarta@gmail.com',
      version='0.0.1')