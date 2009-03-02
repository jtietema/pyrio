# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe
from os.path import join
from glob import glob

setup(
    windows = [{"script":"main.py"}],
    data_files =[
        ("assets", glob(join("assets", "**/*.*"))),
        ("maps", glob(join("maps", "**/*.*")))],
    options = {"py2exe": {"bundle_files":1}}
    )