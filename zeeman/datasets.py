#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:26:48 2026

@author: nclotta
"""

# Time-stamp: </Users/nclotta/Documents/__UBA/__LABO_5_CINCO/git_repo/zeeman/datasets.py, 2026-05-26 Tuesday 15:17:27 nclotta>

import importlib.util as ilu
import pathlib
import sys

d = pathlib.Path("./zeedat")

def load_ext(fp):
    spec = ilu.spec_from_file_location(fp.stem, fp)
    if spec and spec.loader:
        md = ilu.module_from_spec(spec)
        sys.modules[fp.stem] = md
        spec.loader.exec_module(md)
        return md
    else:
        return None


all = []
[all.append([load_ext(p), q.stem, p.stem]) for q in d.glob("*/")
                              if q.is_dir() for p in q.glob("data*.py")]



# eof
