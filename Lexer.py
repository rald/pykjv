from Token import TokenType, Token
from enum import Enum

class LexerState(Enum):
    DEFAULT = 1
    STRING  = 2
    NUMBER  = 3
    COLON   = 4
    DASH    = 5
    COMMA   = 6

class Lexer:
    @staticmethod
    def lex(code):
        n = len(code)
        text = ""
        tokens = []
        state = LexerState.DEFAULT
        i = 0

        while i < n:
            c = code[i]

            if state == LexerState.DEFAULT:
                if c.isalpha() or c == " ":
                    i-=1
                    state = LexerState.STRING
                elif c.isdecimal():
                    i-=1
                    state = LexerState.NUMBER
                elif c == ':':
                    tokens.append(Token(TokenType.COLON, c))
                elif c == '-':
                    tokens.append(Token(TokenType.DASH, c))
                elif c == ',':
                    tokens.append(Token(TokenType.COMMA, c))

            elif state == LexerState.STRING:
                if c.isalpha() or c == " ":
                    text += c
                else:
                    if text.strip():
                        tokens.append(Token(TokenType.STRING, text.strip()))
                    text = ""
                    i-=1
                    state = LexerState.DEFAULT

            elif state == LexerState.NUMBER:
                if c.isdecimal():
                    text += c
                else:
                    tokens.append(Token(TokenType.NUMBER, text))
                    text = ""
                    i-=1
                    state = LexerState.DEFAULT

            i += 1

        if state == LexerState.STRING and text.strip():
            tokens.append(Token(TokenType.STRING, text.strip()))
        elif state == LexerState.NUMBER and text:
            tokens.append(Token(TokenType.NUMBER, text))

        tokens.append(Token(TokenType.EOF, None))

        return tokens
