import re

def EsCodigoDeArticuloValido(textoParaValidar):
    pattern = re.compile("^([a-zA-Z]{1})([0-9]{3})$")  
    return re.search(pattern, textoParaValidar)

def EsEnteroValido(textoParaValidar):
    pattern = re.compile("^\d+$")  
    return re.search(pattern, textoParaValidar)


def EsSucursalValida(textoParaValidar):
    pattern = re.compile("^([a-zA-Z]{3})([0-9]{3})$")
    return re.search(pattern,textoParaValidar)