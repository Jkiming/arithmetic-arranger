import re

def separar_problemitas(problem):
  res = []
  for op in problem:
    res.append(op.split(' '))
  return res
    


def calcular_mayores(problem):
  
  c = separar_problemitas(problem)
  largo_c = len(c)
  kl = []
  
  for expresion in range(largo_c):
    op1 = c[expresion][0]
    op2 = c[expresion][2]

    mayor_valor = max(int(op1), int(op2))
    kl.append(str(mayor_valor))
  return kl

# función que calcula los operadores menores de cada expresion en la array
# y la almacena y devuelve como una array.
def calcular_menores(problem):

  c = separar_problemitas(problem)
  largo = len(c)
  men = []
  
  for expresion in range(largo):
    op1 = c[expresion][0]
    op2 = c[expresion][2]

    men_valor = min(int(op1),int(op2))
    men.append(str(men_valor))
  return men

def only_simbolos(problem):
    c = separar_problemitas(problem)
    largo = len(c)
    smb = []
    
    for expresion in range(largo):
        smb.append(c[expresion][1])
    return smb
    


def separar_problemitas(problem):
  res = []
  for op in problem:
    res.append(op.split(' '))
  return res


def indentif_op(problem,operador,index):
    c = separar_problemitas(problem)
    largo = len(c)
    op1 = c[index][0]
    op2 = c[index][2]
    if operador == op1:
        return True
    return False


def obtener_componentes(problema):
  return [calcular_mayores(problema),calcular_menores(problema),only_simbolos(problema)]
# Problema
c = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]


def formatear_operaciones(problema):
    
    largo = len(problema)
    text = ""
    text_m = ""
    text_l = ""
    may,men,smb = obtener_componentes(problema)

    for expresion in range(largo):
        if indentif_op(problema,may[expresion],expresion):
            esp = min(max(3, len(may[expresion]) + 2), 6)
            lg = esp - len(may[expresion])
            text += lg * " " + may[expresion] + 4 * " "
            lg_m = esp - (len(smb[expresion]) + len(men[expresion]))
            text_m += smb[expresion] + lg_m * " " + men[expresion] + 4 * " "
            text_l += "-" * esp + 4 * " "
        else:
            esp = min(max(3, len(may[expresion]) + 2), 6)
            lg = esp - len(men[expresion])
            text += lg * " " + men[expresion] + 4 * " "
            text_m += smb[expresion] + " " + may[expresion] + 4 * " "
            text_l += "-" * esp + 4 * " "
    return f'{text[:-4]}\n{text_m[:-4]}\n{text_l[:-4]}'


def arithmetic_arranger(problems, result=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        if '+' not in problem and '-' not in problem:
            return "Error: Operator must be '+' or '-'."
        if re.findall(r'[a-zA-Z]', problem):
            return 'Error: Numbers must only contain digits.'
        if re.findall(r'[0-9]{5}', problem):
            return 'Error: Numbers cannot be more than four digits.'
    arranged_problems = formatear_operaciones(problems)
    return arranged_problems
