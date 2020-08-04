#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:34:46 2020

@author: ssj
"""

import argparse
import os
import shutil
import time

import torch

import resnet

res_version = 'resnet56'
from ptflops import get_model_complexity_info

model = resnet.__dict__[res_version]()
from ptflops import get_model_complexity_info
macs, params = get_model_complexity_info(model, (3, 32, 32), as_strings=True,
                                       print_per_layer_stat=True, verbose=True)
print('{:<30}  {:<8}'.format('Computational complexity: ', macs))
print('{:<30}  {:<8}'.format('Number of parameters: ', params))


res_version = 'resnet56_gst'
model = resnet.__dict__[res_version]()
from ptflops import get_model_complexity_info
macs, params = get_model_complexity_info(model, (3, 32, 32), as_strings=True,
                                       print_per_layer_stat=True, verbose=True)
print('{:<30}  {:<8}'.format('Computational complexity: ', macs))
print('{:<30}  {:<8}'.format('Number of parameters: ', params))