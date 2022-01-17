class Exp(object):
    def __init__(self, op, operands):
        self.operator = op
        self.operands = operands
    def __repr__(self):
        return f'Exp({repr(self.operator)},{repr(self.operands)})'
    def __str__(self):
        return f'{self.operator}({",".join(map(str,self.operands))})'

from operator import mul
from functools import reduce

def calc_apply(operator, args):
    if operator in ('add','+'):
        return sum(args)
    if operator in ('sub','-'):
        if len(args) == 0:
            raise TypeError(operator + ' required at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[0] + [-arg for arg in args[1:]])
    if operator in ("mul",'*'):
        return reduce(mul,args,1)
    if operator in ('dev', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        return args[0] / args[1]


def calc_eval(exp):
    if type(exp) in (int,float):
        return exp
    elif type(exp) == Exp:
        return calc_apply(exp.operator, list(map(calc_eval,exp.operands)))


def tokenize(line):
    return line.replace('(', ' ( ').replace(')' , ' ) ').replace(',', ' , ').split()


def assert_non_empty(tokens):
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')


def analyze_operands(tokens):
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected: ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)
    return operands


def analyze_token(token):
    try: return int(token)
    except (TypeError, ValueError):
        try: return float(token)
        except (TypeError, ValueError):
            return token



def analyze(tokens):
    ops = ['add','sub','mul','div','+','-','/','*']
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int,float):
        return token
    if token in ops:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token,analyze_operands(tokens))
    else:
        raise SyntaxError('unexpected token: ' + token)


def calc_parse(line):
    tokens = tokenize(line)
    exo_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return exo_tree



def read_eval_print_loop():
    while True:
        exp_tree = calc_parse(input('calc> '))
        print(calc_eval(exp_tree))


e = 'add(2,mul(4,6))'
print(repr(analyze(tokenize(e))))
print(str(analyze(tokenize(e))))
read_eval_print_loop()