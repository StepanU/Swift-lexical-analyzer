import sys

sys.path.insert(0, sys.path[0] + '/Swift-lexical-analyzer')

from src.swift_tokens import *
from src.LexicalAnalyzer import *


def analyze_boolean_expression(b_expr: str):
    pass


def analyze_code_block(code_block: str):
    pass


def analyze_if(s: str):
    if_index = s.index(keywords['if'])
    if if_index != -1:
        if_index += len(keywords['if'])
        LCP_index = s.index(delimiters['{'])
        else_index = s.index(keywords['else'])
        if else_index != -1:
            if_else_block = s[if_index: else_index]
            boolean_expression = if_else_block[:LCP_index]
            if_code_block = if_else_block[LCP_index:]
            else_index += len(keywords['else'])
            else_code_block = s[else_index:]
            next_if, next_if_index = analyze_if(else_code_block)
            if not next_if:
                return analyze_code_block(else_code_block)
        else:
            boolean_expression, if_code_block = s[if_index:]
    return False, 0


if_code = \
    """
    if y == 1 {
        let x = 13
    } else {
        let x = 12
    }
    """
if_code = str(process(if_code))

print(analyze_if(if_code))