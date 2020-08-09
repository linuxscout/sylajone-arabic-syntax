#!/usr/bin/python
# -*- coding=utf-8 -*-
from setuptools import setup

# to install type:
# python setup.py install --root=/
from io import open
def readme():
    with open('README.rst', encoding="utf8") as f:
        return f.read()

setup (name='sylajone', version='0.2',
      description="Sylajone: Arabic syntax Analyzer library",
      long_description = readme(),      

      author='Taha Zerrouki',
      author_email='taha.zerrouki@gmail.com',
      url='http://sylajone.sourceforge.net/',
      license='GPL',
      package_dir={'sylajone': 'sylajone'},
      packages=['sylajone'],
      install_requires=[ 'pyarabic>=0.6.2',
      ],         
      include_package_data=True,
      package_data = {
        'aranasyn': ['doc/*.*','doc/html/*', 'data/*.sqlite', 'data/*.sql'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
    );

