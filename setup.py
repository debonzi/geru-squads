#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup

requires = [
    'pyramid',
    'gunicorn',
    ]

extras_require = {
    'test': [
        'pytest',
        'pytest-cov'
    ]
}


setup(name='GeruSquads',
      version='0.0.1',
      description='',
      author='Time QA',
      author_email='timeqa@geru.com.br',
      install_requires=requires,
      extras_require=extras_require,
      url='',
      packages=['squads'],
      entry_points="""\
          [paste.app_factory]
          main = squads:main
      """,
      )
