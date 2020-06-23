
#XXX: Do NOT EDIT THIS FILE!
#XXX: MESSING WITH THIS FILE CAN HARM YOUR SYSTEM.


from distutils.core import setup
from os import system

try:
	from Cython.Build import cythonize
except:
	print ("module 'cython' not found!")
	print ("\033[31minstalling cython")
	system("pip install cython")
	from Cython.Build import cythonize

setup(
name = "tailhunter",
author = "Mosheur Rahman",
description = "A Tool to hunt down tails of URL",
version = "1.0",
install_requires = [
	"click",
	"cython",
	"requests",
	"tqdm"
	],
py_modules=["tailhunter.tailhunter"],
entry_points="""
	[console_scripts]
	tailhunter=tailhunter.tailhunter:main
""",
ext_modules = cythonize("tailhunter/tailhunter_core.pyx")
)
