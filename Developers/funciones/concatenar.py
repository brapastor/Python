__author__ = 'brapastor'

def concatenar(*arg, sep="/"):
    return sep.join(arg)

print(concatenar('tierra','jupiter', 'sape',sep="."))
