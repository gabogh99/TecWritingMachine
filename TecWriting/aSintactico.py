from aLexico import tokens,analizador
from sys import stdin


precedence = (

    ('right', 'IGUAL', 'DIFERENTE'),
    ('right', 'ASSIGN'),
    ('left', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTI', 'DIV'),
    ('left', 'LPAREN', 'RPAREN','LPARENC','RPARENC' )
    )


nombres = {}

def p_init(p):
    'init : instrucciones'
    p[0] = p[1]

def p_instrucciones_lista(p):
    'instrucciones : instrucciones instruccion'
    p[1].append(p[2])
    p[0] = p[1]

def p_instrucciones_instruccion(p):
    'instrucciones :  instruccion'
    p[0] = [p[1]]
###Linea 30###
    
def p_instruccion(p):
    '''
    instruccion : asignacion_instr
                | if_instr
                | while_instr
    '''
    p[0] = p[1]


def p_if(p):
    '''if_instr : IF expresion_logica RPAREN statement RPAREN'''

    print(p[3])
    if(p[3]):
        p[0] = p[6]

def p_statement(p):
    '''statement : if_instr
                    | expresion
                    | while_instr'''
    p[0] = p[1]
    print(p[0])

def p_while(p):
    ''' while_instr : WHILE LPARENC expresion_logica RPARENC LPARENC statement RPARENC'''
    while(p[3]): ###Linea 60###
        p[0] = p[6]

def p_put(p):
        ''' asignacion_instr :  PUT ID ASSIGN expresion PUNTOCOMA'''
        nombres[p[1]] = p[4]

def p_put_tipo(p):
        '''expresion : ENTERO
                    | DECIMAL
                    | CADENA    '''
        p[0] = p[1]

def p_expresion_id(p):
        ''' expresion : ID'''
        p[0] = nombres[p[1]]

def p_expresion_group(p):
        ''' expresion : LPAREN expresion RPAREN'''
        p[0] = p[2]

def p_expresion_logica(p):
        '''expresion_logica : expresion MENOR expresion
                            | expresion MAYOR expresion
                            | expresion IGUAL expresion
                            | expresion DIFERENTE expresion
                            | expresion MAYORIGUAL expresion
                            | expresion MENORIGUAL expresion '''

        if p[2] == '<' : p[0] = p[1] < p[3]
        elif p[2] == '>' : p[0] = p[1] > p[3]
        elif p[2] == '==' : p[0] = p[1] == p[3]
        elif p[2] == '!=' : p[0] = p[1] != p[3]
        elif p[2] == '>=' : p[0] = p[1] >= p[3]
        elif p[2] == '<=' : p[0] = p[1] <= p[3]


def p_expresion_logica_group(p):
        ''' expresion_logica : LPAREN expresion_logica RPAREN MENOR LPAREN expresion_logica RPAREN
                            | LPAREN expresion_logica RPAREN MAYOR LPAREN expresion_logica RPAREN
                            | LPAREN expresion_logica RPAREN IGUAL LPAREN expresion_logica RPAREN
                            | LPAREN expresion_logica RPAREN DIFERENTE LPAREN expresion_logica RPAREN
                            | LPAREN expresion_logica RPAREN MAYORIGUAL LPAREN expresion_logica RPAREN
                            | LPAREN expresion_logica RPAREN MENORIGUAL LPAREN expresion_logica RPAREN'''

        if p[4] == '<' : p[0] = p[2] < p[5]
        elif p[4] == '>' : p[0] = p[2] > p[5]
        elif p[4] == '==' : p[0] = p[2] == p[5]
        elif p[4] == '!=' : p[0] = p[2] != p[5]
        elif p[4] == '>=' : p[0] = p[2] >= p[5]
        elif p[4] == '<=' : p[0] = p[2] <= p[5]

def p_expresion_operaciones(p):
    
        ''' expresion : expresion SUMA expresion
                        | expresion RESTA expresion
                        | expresion MULTI expresion
                        | expresion DIV expresion
        '''

        if p[2] == '+' : p[0] = p[1] + p[3]
        elif p[2] == '-' : p[0] = p[1] - p[3]
        elif p[2] == '*' : p[0] = p[1] * p[3]
        elif p[2] == '/' : p[0] = p[1] / p[3]


def p_error(p):
    global resultado_gramatica

    if p:
        resultado = "Error  sint??ctico de tipo [] en el valor {}".format(str(p.type), str(p.value))
    else:
        resultado = "Error sint??ctico {}".format(p)

    resultado_gramatica.append(resultado)
                                

import ply.yacc as yacc
parser = yacc.yacc()

resultado_gramatica = []

def prueba(data):
    resultado_gramatica.clear()
    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
    return resultado_gramatica 
    

        



                    
        






    
