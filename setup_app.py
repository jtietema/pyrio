# -*- coding: utf-8 -*-
from setuptools import setup
from os.path import join
from glob import glob

setup(
    app = [{
        'script': 'main.py'
    }],
    setup_requires = ['py2app'],
    data_files = [
        ('assets', glob(join('assets', '**/*.*'))),
        ('maps', glob(join('maps', '**/*.*')))
    ],
    options = {
        'py2app': {
            'includes': ['pygame'],
            'packages': ['py2app-0.3.6-py2.5']
        }
    }
)

