#! /usr/bin/env python
# -*- coding: utf-8 -*-

__title__ = 'upyun'
__version__ = '2.2.2'
__author__ = 'Monkey Zhang (timebug)'
__license__ = 'MIT License: http://www.opensource.org/licenses/mit-license.php'
__copyright__ = 'Copyright 2014 UPYUN'

from .upyun import UpYun, UpYunServiceException, UpYunClientException
from .upyun import ED_AUTO, ED_TELECOM, ED_CNC, ED_CTT

__all__ = [
    'UpYun', 'UpYunServiceException', 'UpYunClientException',
    'ED_AUTO', 'ED_TELECOM', 'ED_CNC', 'ED_CTT'
]
