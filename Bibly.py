#!/usr/bin/env python3

import sys
import textwrap

from Lexer import Lexer
from Parser import Parser
from Passage import Passage

def chunkstring(string, length):
    """Generate fixed-length chunks from a string."""
    return (string[0+i:length+i] for i in range(0, len(string), length))

def bibly(code):

    tokens=Lexer.lex(code)

    cites=Parser(tokens).parse()

    passages=[]
    for cite in cites:
        passages.extend(Passage.find(cite))

    for passage in passages[:5]:
        for chunk in textwrap.wrap(str(passage),256):
            print(chunk)



if __name__ == "__main__":

    if len(sys.argv)==2:
        bibly(sys.argv[1])

