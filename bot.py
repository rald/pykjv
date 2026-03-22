#!/usr/bin/env python3

import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr

import sys
import time
import logging

from Lexer import Lexer
from Parser import Parser
from Passage import Passage

channel=None
COMMAND_PREFIX='.'

def chunkstring(string, length):
    """Generate fixed-length chunks from a string."""
    return (string[0+i:length+i] for i in range(0, len(string), length))

class TestBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_privmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        """
        a = e.arguments[0].split(":", 1)
        if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(
            self.connection.get_nickname()
        ):
            self.do_command(e, a[1].strip())
        return
        """

        a = e.arguments[0]
        if a[0]==COMMAND_PREFIX:
            self.do_command(e,a[1:])

    def do_command(self, e, cmd):
        nick = e.source.nick
        c = self.connection
        a=cmd.split(" ",1)

        if len(a)==2 and a[0]=="kjv":
            tokens=Lexer.lex(a[1])
            cites=Parser(tokens).parse()
            passages=[]
            for cite in cites:
                if cite:
                    passages.extend(Passage.find(cite))
            for passage in passages[:4]:
                for chunk in chunkstring(str(passage),256):
                    c.privmsg(self.channel, f"{nick}: {chunk}")
                    time.sleep(5)
            if len(passages)>4:
                c.privmsg(self.channel, f"{nick}: You can only display 4 passages at a time.")

def main():

    logging.basicConfig(level=logging.DEBUG)

    if len(sys.argv) != 4:
        print("Usage: testbot <server[:port]> <channel> <nickname>")
        sys.exit(1)

    s = sys.argv[1].split(":", 1)
    server = s[0]
    if len(s) == 2:
        try:
            port = int(s[1])
        except ValueError:
            print("Error: Erroneous port.")
            sys.exit(1)
    else:
        port = 6667
    channel = sys.argv[2]
    nickname = sys.argv[3]

    bot = TestBot(channel, nickname, server, port)
    bot.start()

if __name__ == "__main__":
    main()
