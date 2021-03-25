import ply.lex as lex


reservdas = {

    'Def':'DEF','Put':'PUT','Add':'ADD','ContinueUp':'CONTINUEUP', 'ContinueDown':'CONTINUEDOWN'
    'ContinueRight':'CONTINUERIGHT', 'ContinueLeft':'CONTINUELEFT', 'Pos':'POS',
    'PosX':'POSX': 'PosY':'POSY', 'UseColor':'USECOLOR', 'Down':'DOWN', 'Begin':'BEGIN',
    'Speed':'SPEED', 'Run': 'RUN', 'Repeat': 'REPEAT', 'If':'IF', 'IfElse':'IFELSE',
    'Until':'UNTIL', 'While':'WHILE', 'Equal':'EQUAL', 'And':'AND', 'Or': 'OR',
    'Greater':'GREATER', 'Smaller':'SMALLER', 'Substr':'SUBSTR', 'Random':'RANDOM','Mult':'MULT',
    'Fin': 'FIN', 'Para': 'PARA'

    }


tokens = [
        'COMA', 'PUNTOCOMA','IGUAL', 'LPAREN', 'RPAREN','LPARENC','RPARENC', #Símbolos exclusivos
        'ID', 'NUMERO',
        'DIFERENTE', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL', 'SUMA','RESTA', 'MULTI', 'DIV', 'ASSIGN'
] + list(reservadas.values())

t_ignore = ' \t'  #Espacio en blanco

t_COMA = r','
t_PUNTOCOMA = r';'
t_IGUAL = r'='
t_ASSIGN = r'=='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LPARENC = r'\['
t_RPARENC = r'\]'
t_DIFERENTE = r'\!='
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTI = r'\*'
t_DIV = r'\/'

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\--.*'
    pass

def t_ID(t):

    r'[a-zA-Z][a-zA-Z0-9_&@]*'
    if t.value.upper() in reservadas.values():
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
        except ValueError:
            print("Integer value too large %d", t.value)
            t.value = 0
        return t

def t_DECIMAL(t):
        r'(\d*\.\d+)|(\d+\.\d*)'
        try:
            t.value = float(t.value)
            expect ValueError:
                print("Float value too large %d", t.value)
            return t

def t_error(t):
    print("Caracter ilegal: Error de sintaxis in line"+ str(t.lexer.lineno)+"'%s'" % t.value[0])       
    #t.lexer.skip(1)
    sys.exit(0)


def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t



analizador = lex.lex()

    








