from cProfile import label
from textwrap import fill
import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import font
from io import open
import os
import re


res1 = 0
operator = ""


# Configuración de la raiz del editor
title = "Editor | Python - Cheke"
root = Tk()
root.title(title)

# URL del archivo
url_file = ""

# Diccionario de Lenguaje cheke++
operator_diccionario = {
	'=': 'Asignacion',
	'+': 'Suma',
	'-': 'Resta',
	'/': 'División',
	'*': 'Multiplicación',
	'<': 'menor que',
	'>': 'mayor que'
}

keywords_diccionario = {
	'chekInt': 'Número entero',
	'chekFloat': 'Número flotante',
	'chekString': 'Cadena de texto',
	'chekBool': 'Booleano',
}



# Se asume que la variable y ya tiene un valor asignado (en este caso, 5)
tabla_de_simbolos = {
	'y': 5
}


# Clases

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

# Funciones

def evaluar_expresion(expresion):
    try:
        expresion_postfija = obtener_expresion_postfija(expresion)
        resultado_evaluacion = evaluate_postfix(expresion_postfija, tabla_de_simbolos)
        if resultado_evaluacion is not None:
            print(f"Resultado de la expresión: {resultado_evaluacion}")
    except Exception as e:
        print(f"Error al evaluar la expresión: {expresion}, {str(e)}")

def dividir_expresion_en_tokens(expresion):
    tokens = re.findall(r'\d+|[\+\-\*/\(\)]', expresion)
    return tokens

    for variable, valor in tabla_de_simbolos.items():
        texto = texto.replace(variable, str(valor))
def obtener_expresiones_infijas(texto, tabla_de_simbolos, variables_asignadas):

    # for variable, valor in tabla_de_simbolos.items():
    #     texto = texto.replace(variable, str(valor))
    
    for variable, valor in tabla_de_simbolos.items():
        # Modificación: Solo reemplazar si la variable no está asignada en esta línea
        if variable not in variables_asignadas:
            texto = re.sub(rf'(?<!\w){re.escape(variable)}(?! *=[^=])', str(valor), texto)
            

    print(texto)    
    #expresiones_infijas = re.findall(r'\b(?:\s*\d+\s*[\+\-*/]\s*)*\d+\s*\b|\((?:\s*\d+\s*[\+\-*/]\s*)*\d+\s*\)\s*[\+\-*/]?\d*\s*\(\s*\d*[\+\-*/]?\s*\d*\)\s*[\+\-*/]\s*\d*', texto)
    expresiones_infijas = re.findall(r'\b(?:\s*\d+(?:\.\d+)?\s*[\+\-*/]\s*)*\d+(?:\.\d+)?\s*\b|\((?:\s*\d+(?:\.\d+)?\s*[\+\-*/]\s*)*\d+(?:\.\d+)?\s*\)\s*[\+\-*/]?\d*(?:\.\d+)?\s*\(\s*\d*(?:\.\d+)?[\+\-*/]?\s*\d*(?:\.\d+)?\)\s*[\+\-*/]\s*\d*(?:\.\d+)?', texto)
    
    

    
    #expresiones_infijas = re.findall(r'\b(?:\s*\d+(?:\.\d+)?\s*[\+\-*/]\s*)*\d+(?:\.\d+)?\s*\b|\((?:\s*\d+(?:\.\d+)?\s*[\+\-*/]\s*)*\d+(?:\.\d+)?\s*\)\s*[\+\-*/]?\d+(?:\.\d+)?\s*\(\s*\d+(?:\.\d+)?[\+\-*/]?\s*\d+(?:\.\d+)?\)\s*[\+\-*/]\s*\d+(?:\.\d+)?', texto)

    #expresiones_infijas = re.findall(r'\b(?:\s*\d+\s*[\+\-*/]\s*)*\d+\s*\b|\([\s\d\+\-*/]+\)\s*[\+\-*/]?\d*\s*', texto)
    #expresiones_infijas = re.findall(r'\b(?:\s*\d+(?:\.\d+)?\s*[\+\-*/]\s*)*\d+(?:\.\d+)?\s*\b|\([\s\d\+\-*/]+\)\s*[\+\-*/]?\d+(?:\.\d+)?\s*', texto)
    
    print(expresiones_infijas)  # Agregar esta línea para imprimir los tokens
    return expresiones_infijas




#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def obtener_expresion_postfija(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    salida = []
    pila = []

    # for token in tokens:
    #     token = token  # Eliminar espacios alrededor del token
    #     if not token:
    #         continue  # Saltar tokens vacíos después de eliminar espacios

    # Utilizar una expresión regular más general para dividir la expresión en tokens
    if(expresion.count('.')>0):
        tokens = re.findall(r'\b(?:\w+\.\w+|\w+|\S)\b', expresion)
    else:
        tokens = expresion
        
    for token in tokens:
        token = token.strip()  # Eliminar espacios alrededor del token
        if not token:
            continue  # Saltar tokens vacíos después de eliminar espacios
        
        print(token)
    # token = re.findall(r'\d+\.\d+|\d+|[\+\-\*/\(\)]', tokens)

        if(token.count('.')>0):
            token = float(token)            
    
    
        if isinstance(token, float) or re.match(r'^[a-zA-Z_]\w*$', token) or token.isdigit() or token in {'+', '-', '*', '/', '(', ')'}:
            # Es una variable, número o operador
            if token == '(':
                    # Es un paréntesis de apertura
                pila.append(token)
            elif token == ')':
                # Es un paréntesis de cierre, desapilamos hasta encontrar el paréntesis de apertura
                while pila and pila[-1] != '(':
                    salida.append(pila.pop())
                if pila:  # Verificar si la pila no está vacía antes de hacer pop
                    pila.pop()  # Quitamos el paréntesis de apertura de la pila
            elif token in precedencia:
                # Es un operador
                while pila and pila[-1] != '(' and precedencia[token] <= precedencia[pila[-1]]:
                    salida.append(pila.pop())
                pila.append(token)
            else:
                # Es una variable o número
                salida.append(token)

    # Desapilamos los operadores restantes
    while pila:
        salida.append(pila.pop())

    return salida


def evaluate_postfix(postfix_expression, tabla_de_simbolos, expresiones_infijas):
    operand_stack = Stack()
    global res1
    global operator       

    for i in range(len(postfix_expression)):
        if(isinstance(postfix_expression[i], float)):
             postfix_expression[i] = str(postfix_expression[i])
    # postfix_expression = str(postfix_expression)     
    # print(type(postfix_expression))

    # if(postfix_expression.count('.')>0):
    #     postfix_expression = re.findall(r'\b(?:\w+\.\w+|\w+|\S)\b', postfix_expression)
    # else:
    #     postfix_expression = postfix_expression        
    # Iterar sobre los elementos de la lista
    for i in range(len(postfix_expression)):
        if isinstance(postfix_expression[i], str) and '.' in postfix_expression[i]:
            # Si el elemento es una cadena y contiene un punto decimal, convertir a float
            postfix_expression[i] = float(postfix_expression[i])

    # postfix_expression = str(postfix_expression)
    for token in postfix_expression:
        token = str(token)
        if re.match(r'^[a-zA-Z_]\w*$', token):
                # Es una variable, consultamos la tabla de símbolos para obtener su valor
                    if token in tabla_de_simbolos:
                        operand_stack.push(tabla_de_simbolos[token])
                    else:
                    # La variable no está en la tabla de símbolos, manejar este caso según tu lógica
                        print(f"La variable {token} no tiene un valor asignado.")
                        operand_stack.push(None)
        elif isinstance(token, str) and token not in operator_diccionario  or token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            # Es un número
            operand_stack.push(float(token))
        elif token in operator_diccionario:
            # Es un operador
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

            if operand1 is not None and operand2 is not None:
                if token == '+':
                    operand_stack.push(operand1 + operand2)
                elif token == '-':
                    operand_stack.push(operand1 - operand2)
                elif token == '*':
                    operand_stack.push(operand1 * operand2)
                elif token == '/':
                    operand_stack.push(operand1 / operand2)
            else:
                # Uno o ambos operandos son None, manejar este caso según tu lógica
                if operand1 is not None:
                    res1 = operand1
                    operator = token
                else:
                    res1 = operand2
                    operator = token


    if operand_stack.is_empty():
        return None
    else:
        result = operand_stack.pop()
        return result



def new_file():
	global url_file
	text.delete(1.0, "end")
	url_file = ""
	root.title(url_file + " " + title)

def open_file():
	global url_file
	url_file = fd.askopenfilename(initialdir =  '.', filetype = (("Archivos de texto", "*.txt"),), title = "Abrir archivo")

	if( url_file != ""):
		file = open(url_file, 'r') # Se le dice que es de lectura con r
		content = file.read()
		text.delete(1.0, "end")
		text.insert('insert', content)
		file.close()
		root.title(url_file + " | " + title)

def save_file():
    global url_file
    if url_file != "":
        content = text.get(1.0, "end-1c")  # Para que no guarde el último salto de línea
        with open(url_file, "w", encoding="utf-8") as file:
            file.write(content)
        root.title("Archivo guardado | " + url_file + " " + title)
    else:
        file = fd.asksaveasfile(
            title="Guardar archivo",
	        mode="w",
	        defaultextension=".txt",
	        filetypes=[("Archivos de texto", "*.txt")]
        )
        if file is not None:
            content = text.get(1.0, "end-1c")
            url_file = file.name  # Obtener la ruta del archivo desde el objeto de archivo
            with open(url_file, "w", encoding="utf-8") as file:
                file.write(content)
            root.title("Archivo guardado | " + url_file + " " + title)
        else:
            url_file = ""
            root.title("Guardado cancelado | " + url_file + " " + title)

def save_file_as():
    global url_file
    file = fd.asksaveasfile(
        title="Guardar archivo como",
        mode="w",
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt")]
    )
    if file is not None:
        content = text.get(1.0, "end-1c")
        url_file = file.name  # Obtener la ruta del archivo desde el objeto de archivo
        with open(url_file, "w", encoding="utf-8") as file:
            file.write(content)
        root.title("Archivo guardado como | " + url_file + " " + title)

def search():
	search_term = simpledialog.askstring("Buscar", "Buscar texto:")
	if search_term:
		start_pos = "1.0"
		while True:
			# Buscar la siguiente ocurrencia del texto
			start_pos = text.search(search_term, start_pos, stopindex="end")
			if not start_pos:
				break
			end_pos = f"{start_pos}+{len(search_term)}c"
			text.tag_add("highlight", start_pos, end_pos)  # Resaltar la ocurrencia
			start_pos = end_pos
		text.tag_config("highlight", background="yellow")

def replace():
	search_term = simpledialog.askstring("Reemplazar", "Buscar texto:")
	if search_term:
		replace_term = simpledialog.askstring("Reemplazar", "Reemplazar con:")
		if replace_term:
			start_pos = "1.0"
			while True:
				# Buscar la siguiente ocurrencia del texto
				start_pos = text.search(search_term, start_pos, stopindex="end")
				if not start_pos:
					break
				end_pos = f"{start_pos}+{len(search_term)}c"
				text.delete(start_pos, end_pos)  # Eliminar la ocurrencia
				text.insert(start_pos, replace_term)  # Insertar el texto de reemplazo
				start_pos = end_pos

def cut():
	global clipboard
	clipboard = text.get("sel.first", "sel.last")  # Obtener el texto seleccionado
	text.delete("sel.first", "sel.last")  # Eliminar el texto seleccionado


def copy():
	global clipboard
	clipboard = text.get("sel.first", "sel.last")  # Obtener el texto seleccionado

def paste():
	global clipboard
	text.insert(INSERT, clipboard)  # Insertar el contenido del portapapeles en la posición actual

def table():
	mensaje = "Tabla de operadores:\n"
	for clave, valor in operator_diccionario.items():
		mensaje += f"{clave}: {valor}\n"

	mensaje += "\nTabla de keywords:\n"
	for clave, valor in keywords_diccionario.items():
		mensaje += f"{clave}: {valor}\n"


	messagebox.showinfo("Tabla de simbolos", mensaje)


def analizar():
    content = text.get(1.0, "end-1c")
    lines = content.split('\n')
    resultados = []
    global tabla_de_simbolos
    # Mantener un conjunto de variables que están siendo asignadas
    variables_asignadas = set()
        

    for line_number, line in enumerate(lines, start=1):
        tokens = re.findall(r'\b\w+\b|[-+*/=<>]', line)

        for token in tokens:
            if re.match(r'^[a-zA-Z_]\w*$', token):
                if token not in tabla_de_simbolos:
                    resultados.append(f"Línea {line_number}: Variable no definida: {token}")
                    tabla_de_simbolos[token] = None  # Asignar None a la variable no definida
                else:
                    resultados.append(f"Línea {line_number}: Variable: {token}")
            elif token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                resultados.append(f"Línea {line_number}: Valor numérico: {token}")
            elif token in {'+', '-', '*', '/'}:
                resultados.append(f"Línea {line_number}: Operador: {token}")

        resultados.append("")  # Agregar un salto de línea después de procesar una línea

     # Modificación: Analizar expresiones de asignación
        match_asignacion = re.match(r'^\s*(\w+)\s*=', line)
        if match_asignacion:
            variable_asignada = match_asignacion.group(1)
            variables_asignadas.add(variable_asignada)

    # Evaluar expresiones aritméticas en notación postfija
    expresiones_infijas = obtener_expresiones_infijas(content, tabla_de_simbolos, variables_asignadas)
    for expresion_infija in expresiones_infijas:
        expresion_postfija = obtener_expresion_postfija(expresion_infija)
        if expresion_postfija:
            resultado_evaluacion = evaluate_postfix(expresion_postfija, tabla_de_simbolos, expresiones_infijas)
            
            print(res1)
            print(resultado_evaluacion)
            if resultado_evaluacion is not None:
                # Extraer la variable de la expresión infija
                print(content)
                match = re.match(r'^\s*(\w+)\s*=', content)
                print(match)
                if match:
                    variable = match.group(1)
                    print(variable)
                    
                        # Actualizar la tabla de símbolos
                    tabla_de_simbolos[variable] = resultado_evaluacion
                    print(tabla_de_simbolos[variable])
                    resultados.append(f"Resultado de la expresión: {resultado_evaluacion}")

    resultados.append("")  # Agregar un salto de línea después de procesar una línea

    if resultados:
        mensaje = "\n".join(resultados)  # Concatenar resultados en un solo mensaje
        messagebox.showinfo("Resultados del Análisis Léxico", mensaje)

# Menu
bar = Menu(root)
file_menu = Menu(bar, tearoff= 0)
file_menu.add_command(label = "Nuevo archivo", command = new_file)
file_menu.add_separator()
file_menu.add_command(label = "Abrir archivo", command = open_file)
file_menu.add_separator()
file_menu.add_command(label = "Guardar archivo", command = save_file)
file_menu.add_separator()
file_menu.add_command(label = "Gardar como...", command = save_file_as)
file_menu.add_separator()
file_menu.add_command(label= "Salir", command = root.quit)

edit_menu = Menu(bar, tearoff= 0)
edit_menu.add_command(label = "Buscar", command = search)
edit_menu.add_separator()
edit_menu.add_command(label = "Reemplazar", command = replace)
edit_menu.add_separator()
edit_menu.add_command(label = "Copiar", command = copy)
edit_menu.add_separator()
edit_menu.add_command(label = "Cortar", command = cut)
edit_menu.add_separator()
edit_menu.add_command(label = "Pegar", command = paste)

analizador_lexico_menu = Menu(bar, tearoff= 0)
analizador_lexico_menu.add_command(label = "Tabla de simbolos", command = table)
analizador_lexico_menu.add_command(label = "Analizar léxico", command= analizar)



# Añadimos el desplegable a la barra
bar.add_cascade(menu = file_menu, label = "Archivo")
bar.add_cascade(menu = edit_menu, label = "Edición")
bar.add_cascade(menu = analizador_lexico_menu, label = "Analizador Léxico")

# Caja de texto
text = Text(root)
text.pack(fill = "both", expand = 1)
text.config(bd = 0, padx = 6, pady = 5, font = ("Arial", 14))

# Run
root.config(menu = bar)
root.mainloop()