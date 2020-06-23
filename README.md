# TailHunter

# [page finder]

Tailhunter is a tool for finding hidden pages 
using url endpoints, based on dictionary attacks (wordlist).

Tailhunter is a asynchronous project.
So you can send a bunch of requests to the server
at a same time. you'll get kind of 'Hydra' like feeling, 
while using it. 

# [installation]

```
$ apt-get install git python

$ git clone https://github.com/mosheur15/tailhunter.git

$ cd tailhunter

$ pip install --editable .

```
Do not forget to put the (.) dot in the
last command.
After installing,  you can run tailhunter from
anywhere in the terminal.

# [Run]

```
$ tailhunter -u [example.com] -w [example_wordlist.txt]
```

# [Uninstall]

```
$ pip uninstall tailhunter
````
