# -*- coding: utf-8 -*-

import sys

file = sys.argv[1]

searchfile = open(file, "r")

skiparray = ['To: ', 'From: ', 'Subject: ', 'Date: ', '(mobiel verstuurd)', 'Vriendelijke groeten, Maarten Scherpenisse', 'Vriendelijker groeten, Maarten Scherpenisse', 'Met vriendelijke groet, Maarten Scherpenisse', 'Groeten, Maarten', '2014', '2015', '2016']

prevskip = 0
prevempty = 0

def skipfunction():
    pass

for line in searchfile:
    skip = 0
    for string in skiparray: #kijk of de regel qua waarde moet worden overgeslagen
        if str(string) in line:
            skip = 1
            prevskip = 1
    if prevskip == 1 and line == '\n': #indien vorige regel overgeslagen en nieuwe regel leeg, negeer
        skipfunction()
    elif prevempty == 1 and line == '\n': #indien vorige regel leeg en nieuwe regel ook leeg, negeer
        skipfunction()
    elif skip != 1: #indien de regel geen waardes heeft die reden geven om over te slaan, toon
        print line,
        prevskip = 0;
        prevempty = 0;
    else: #indien de regel wel een waarde heeft die reden is om deze over de slaan, negeer
        skipfunction()
    if line == '\n': #onthoud of de huidige regel leeg was
        prevempty = 1

searchfile.close()