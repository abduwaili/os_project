#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 12:43:28 2017

@author: adu
"""


#获取当前用户名方法1
import os
import pwd

def get_username1():
	
    print pwd.getpwuid( os.getuid() )[ 0 ]

	
#获取当前用户名方法1
import getpass
def get_username2():
	print getpass.getuser()
	pwd = getpass.getpass('password: ');
	print pwd;
	
	
if __name__=="__main__":
	  get_username1();
	  get_username2();