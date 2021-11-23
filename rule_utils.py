from antlr4 import CommonTokenStream, ParserRuleContext

from gen.CPP14_v2Lexer import CPP14_v2Lexer


def extract_exact_text(token_stream: CommonTokenStream, rule: ParserRuleContext) -> str:
    return token_stream.getText(rule.start.tokenIndex, rule.stop.tokenIndex)


def is_break(rule: ParserRuleContext) -> bool:
    return rule.start.type == CPP14_v2Lexer.Break
