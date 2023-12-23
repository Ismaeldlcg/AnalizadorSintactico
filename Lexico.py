import ply.lex as lex

reservadas = {
    'int': 'INT',
    'float': 'FLOAT',
    'while': 'WHILE',
    'do': 'DO',
    'if': 'IF',
    'break': 'BREAK',
    'true': 'TRUE',
    'false': 'FALSE',
    'else': 'ELSE'
}

tokens = [
    'ID', 'NUMERO', 'REAL', 'PUNTOYCOMA', 'LLLAVE', 'RLLAVE',
    'LPAREN', 'RPAREN', 'LCORCHETE', 'RCORCHETE', 'COMA', 'IGUAL', 'MAS',
    'MENOS', 'MULTIPLICACION', 'DIVISION', 'LT', 'LE', 'GT', 'GE', 'IGUALES', 'NE',
    'NOT', 'AND', 'OR',
] 
tokens = tokens + list(reservadas.values())

t_PUNTOYCOMA = r';'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORCHETE = r'\['
t_RCORCHETE = r'\]'
t_COMA = r','
t_IGUAL = r'='
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_IGUALES = r'=='
t_NE = r'!='
t_ignore = ' \t\n'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t    

def t_error(t):
    print(f"Carácter no reconocido: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Lee el código desde el archivo
archivo_codigo = 'codigo6.txt'
with open(archivo_codigo, 'r') as file:
    codigo = file.read()

lexer.input(codigo)

for token in lexer:
    print(f"{token.type}: {token.value}")
    
