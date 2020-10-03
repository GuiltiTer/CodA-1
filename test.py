# in the name of allah

from gen.CFGListener import CFGListener
from gen.CPP14_v2Lexer import CPP14_v2Lexer
from gen.CPP14Parser import CPP14Parser

from antlr4 import *

<<<<<<< HEAD
input_path = 'test_source/4.cpp'
=======
# input_path=input("please write the source code path:\n")
input_path = 'test_source/1.cpp'
>>>>>>> 67ee24dbc8df336420fee590f788957040829f69
f = open(input_path, 'r')
source = f.read()

stream = InputStream(source)

lexer = CPP14_v2Lexer(stream)

token_stream = CommonTokenStream(lexer)

parser = CPP14Parser(token_stream)

pars_tree = parser.translationunit()
lexer.reset()
number_of_tokens = len(lexer.getAllTokens())
cfg_listener = CFGListener(token_stream , number_of_tokens)
walker = ParseTreeWalker()

walker.walk(cfg_listener, pars_tree)
