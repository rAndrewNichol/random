from distutils.core import setup, Extension

module1 =  Extension('exmod',
	include_dirs = ['C:/Users/Andrew/Programs/Anaconda3/envs/python2/include'],
	libraries = [],
	sources = ['testmodule.c'])

setup(name = "exmod",
	version = "1.0",
	description = "This is a test",
	author = "Andrew J Nickels",
	ext_modules = [module1])