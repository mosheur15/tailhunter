#!/data/data/com.termux/files/usr/bin/python
# -*- coding : utf-8 -*-

__author__ : "Mosheur Rahman"
__version__ : "1.0"
__github__ : "https://github.com/mosheur15"

# :::::::::WARNING:::::::::
#XXX: Do not use this program on multiple terminal window at once!
#XXX: If you do so,  it can act like DOS ATTACK!
#XXX: Be safe. Use it on your own risk.

from tailhunter_core import search
from os import path
import click

@click.command()
@click.option("--url", "-u", default=None, help="Target url.")
@click.option("--wordlist", "-w", default=None, help="Wordlist path. ")

def main(url, wordlist):

	if url != None and wordlist != None:
		if path.exists(wordlist) and (url[:7].lower() == "http://" or url[:8].lower() == "https://"):
			ob = search(wordlist, url)
			ob.run()
		else:
			print ("\n\033[31m error to load. url / file\033[0m\n")
	else:
		print ("\nUsage: runner.py [OPTIONS]\nTry 'runner.py --help' for help.\n")

if __name__ == "__main__":
	main()
