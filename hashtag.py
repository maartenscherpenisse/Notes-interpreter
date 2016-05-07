# -*- coding: utf-8 -*-

import sys
import time

file = sys.argv[1]

if sys.argv[2] == ('qoute' or 'qoutes'):
    searchterm = '–'
elif sys.argv[2] == 'undefined':
    searchterm = '##'
elif sys.argv[2] == ('priority' or 'priorities'):
    searchterm = '!!'
else:
    searchterm = '#{}'.format(sys.argv[2])

searchfile = open(file, "r")

restartarray = [2014, 2015, 2016, '[']

record = '\n' #variable waarde geven zodat er iets aan toe te voegen valt
date = '\n' #variable waarde geven zodat als er geen waarde is het script geen foutmelding daarop geeft

def cleanrecord():
    global record
    record = '\n'

print searchterm
print

for line in searchfile:
        record += line
        for string in restartarray: #opname herstarten zodra er een nieuwe mail lijkt te beginnen, vanaf datumnotatie of mailhoofd
            if 'To: Maarten Scherpenisse <maartenscherpenisse@me.com>' in line:
                cleanrecord()
                continue
            elif str(string) in line:
                cleanrecord()
                date = line
                continue
        if searchterm in line:
            print record #toon opname!!
            time.sleep(3)
            print
            cleanrecord()
        elif '#' in line or '–' in line:
            cleanrecord()
searchfile.close()

#record = "{:>88s}".format(date) #opname resetten
