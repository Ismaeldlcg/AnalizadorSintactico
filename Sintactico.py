import ply.yacc as yacc
from Lexico import tokens

errores = False

def p_programa(p):
    ' programa : bloque '
    if not errores:
        print("Analizado correctamente")

def p_bloque(p):
    ' bloque : LLLAVE decls instrs RLLAVE '

def p_decls(p):
    '''
    decls : decls decl
          | epsilon

    '''

def p_empty(p):
    '''epsilon : '''
    pass

def p_decl(p):
    '''
    decl : tipo ID PUNTOYCOMA

    '''

def p_tipo(p):
    '''
    tipo : tipo LCORCHETE NUMERO RCORCHETE
         | basico

    '''

def p_basico(p):
    '''
    basico : INT
           | FLOAT

    '''

def p_instrs(p):
    '''
    instrs : instrs instr
           | epsilon

    '''

def p_instr(p):
    '''
    instr : loc IGUAL bool PUNTOYCOMA
         | IF LPAREN bool RPAREN instr
         | IF LPAREN bool RPAREN instr ELSE instr
         | WHILE LPAREN bool RPAREN instr
         | DO instr WHILE LPAREN bool RPAREN PUNTOYCOMA
         | BREAK PUNTOYCOMA
         | bloque

    '''

def p_loc(p):
    '''
    loc : loc LCORCHETE bool RCORCHETE
        | ID

    '''

def p_bool(p):
    '''
    bool : bool OR comb
         | comb

    '''

def p_comb(p):
    '''
    comb : comb AND igualdad
         | igualdad

    '''

def p_igualdad(p):
    '''
    igualdad : igualdad IGUALES rel
             | igualdad NE rel
             | rel

    '''

def p_rel(p):
    '''
    rel : expr LT expr
        | expr LE expr
        | expr GE expr
        | expr GT expr
        | expr

    '''

def p_expr(p):
    '''
    expr : expr MAS term
         | expr MENOS term
         | term

    '''

def p_term(p):
    '''
    term : term MULTIPLICACION unario
         | term DIVISION unario
         | unario

    '''

def p_unario(p):
    '''
    unario : NOT unario
           | MENOS unario
           | factor
           
    '''

def p_factor(p):
    '''
    factor : LPAREN bool RPAREN
           | loc
           | NUMERO
           | REAL
           | TRUE
           | FALSE
    '''

def p_error(p):

    global errores
    errores = True

    if p:
        print(f"Error de sintaxis en '{p.value}', línea {p.lineno}")
    else:
        print("Error de sintaxis")

parser = yacc.yacc()

archivo_codigo = 'codigo.txt'
def cargar_codigo_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()
codigo_prueba = cargar_codigo_desde_archivo(archivo_codigo)

print("Código fuente original:")
print(codigo_prueba)

parser.parse(codigo_prueba)

