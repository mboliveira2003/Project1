"""
FUNDAMENTOS DE PROGRAMAÇÃO - PROJETO 1
Este projeto consiste num conjunto de rotinas que permitem criar, modificar e
manipular matrizes esparsas, respeitando diversas barreiras de abstração.
"""

__author__ = "ist1103514 Margarida Barros de Oliveira"
__version__ = "5.2"
__all__ = ['cria_posicao', 'eh_posicao', 'posicao_linha', 'posicao_coluna',
           'posicao_igual', 'posicao_str', 'cria_matriz', 'eh_matriz',
           'matriz_zero', 'matriz_copia', 'matriz_posicao', 'matriz_valor',
           'matriz_dimensao', 'matriz_densidade', 'matriz_nulo', 'matriz_str',
           'matriz_linha', 'matriz_coluna', 'matriz_diagonal']


# REPRESENTAÇÃO DA COORDENADA
'''
uma posição é definida como um tuplo cujo primeiro e segundo elemento 
correspondem respetivamente ao índice da linha e da coluna dessa posição
'''


def cria_posicao(num_linha: int, num_coluna: int):
    """a função devolve uma posição dados dois inteiros não negativos
        num_linha: representa o índice da linha do elemento
        num_coluna: representa o índice da coluna do elemento
        retorno: posição
    """
    # os índices linha e coluna são inteiros não negativos
    if type(num_linha) != int or type(num_coluna) != int \
            or num_linha < 0 or num_coluna < 0:
        raise ValueError("cria_posição: argumentos inválidos")
    posicao = (num_linha, num_coluna)
    return posicao


def eh_posicao(arg) -> bool:
    """a função verifica se o argumento introduzido é uma posição
        arg: any
    """
    # a posição é um tuplo de 2 inteiros não negativos
    if type(arg) == tuple and len(arg) == 2:
        if type(arg[0]) == int and type(arg[1]) == int:
            return arg[0] >= 0 and arg[1] >= 0
    return False


def posicao_linha(posicao) -> int:
    """a função devolve o índice da linha de uma posição
        posicao: posição
    """
    return posicao[0]


def posicao_coluna(posicao) -> int:
    """a função devolve o índice da coluna de uma posição
        posicao: posição
    """
    return posicao[1]


def posicao_igual(posicao1, posicao2) -> bool:
    """a função verifica se as posições introduzidas são iguais
        posicao1: posição
        posicao2: posição
    """
    return posicao1 == posicao2


def posicao_str(posicao) -> str:
    """a função devolve uma representação textual da posição
        posicao: posição
    """
    return str(posicao)


# REPRESENTAÇÃO DA MATRIZ
'''
a matriz é definida como um dicionário, cujas keys são tuplos correspondentes
a posições e cujos values são floats correspondentes aos valores que ocupam 
essas posições; existe ainda uma key "valor_nulo" que guarda o valor do zero da
matriz, que ocupa todas as posições não representadas
'''


def cria_matriz(zero=0.0):
    """a função cria uma matriz vazia, contendo apenas o valor nulo
        zero: float, valor nulo da matriz
        retorno: matriz
    """
    if type(zero) != float and type(zero) != int:
        raise ValueError("cria_matriz: argumentos inválidos")
    # a matriz vazia contém apenas o valor nulo
    matriz = {"valor_nulo": float(zero)}
    return matriz


def posicao_key(posicao) -> tuple:
    """a função converte uma posição numa key do dicionário matriz
        posicao: posição
        retorno: estrutura do tuplo: (índice linha, índice coluna)
    """
    return posicao_linha(posicao), posicao_coluna(posicao)


def eh_posicao_key(arg) -> bool:
    """a função verifica se o argumento é uma key válida do dicionário
        arg: any
    """
    # uma key do dicionário é um tuplo de dois inteiros não negativos
    if type(arg) == tuple and len(arg) == 2:
        if type(arg[0]) == int and type(arg[1]) == int:
            return arg[0] >= 0 and arg[1] >= 0
    return False


def eh_matriz(arg) -> bool:
    """a função verifica se o argumento introduzido é uma matriz esparsa
        arg: any
    """
    # uma matriz é um dicionário...
    if type(arg) != dict:
        return False
    # ...que tem obrigatoriamente uma key "valor_nulo"...
    if "valor_nulo" not in arg.keys():
        return False
    for i in arg:
        # ... em que as restantes keys são posições transformadas em keys...
        if eh_posicao_key(i) or i == "valor_nulo":
            # ... cujos values são floats...
            # ...e em que a todas as posições correspondem values não nulos
            if type(arg[i]) != float or (arg[i] == arg["valor_nulo"]
                                         and i != "valor_nulo"):
                return False
    return True


def matriz_zero(matriz) -> float:
    """a função devolve o valor correspondente ao zero da matriz
        matriz: matriz
    """
    return matriz["valor_nulo"]


def matriz_copia(matriz):
    """a função devolve uma cópia da matriz passada como argumento
        matriz: matriz
        retorno: matriz
    """
    return matriz.copy()


# MANIPULAÇÃO DA MATRIZ
def matriz_valor(matriz, posicao) -> float:
    """a função devolve o valor da posição da matriz passadas como argumentos
        matriz: matriz
        posicao: posição
    """
    posicao = posicao_key(posicao)
    # devolve-se o elemento que ocupa a posição especificada
    # caso a posição não esteja representada é devolvido o zero da matriz
    return matriz.get(posicao, matriz_zero(matriz))


def matriz_posicao(matriz, posicao, valor: float) -> float:
    """a função modifica o valor que ocupa a posição especificada
        matriz: matriz
        posicao: posição
        retorno: valor que anteriormente ocupava a posição especificada
    """
    valor_antigo = matriz_valor(matriz, posicao)
    posicao = posicao_key(posicao)
    # o valor a introduzir não é o valor nulo
    if valor != matriz_zero(matriz):
        # se a posição estiver representada o seu valor é modificado
        # caso contrário é criado um novo elemento da matriz
        matriz[posicao] = float(valor)
    # o valor a introduzir é o valor nulo
    # caso a posição introduzida esteja representada esta é apagada
    elif posicao in matriz.keys():
        del matriz[posicao]
    return valor_antigo


def matriz_dimensao(matriz) -> tuple:
    """a função devolve um tuplo com o par das posições extremas da matriz
        matriz: matriz
        retorno: estrutura do tuplo: (coordenada mínima, coordenada máxima)
    """
    # se a matriz estiver vazia devolve-se um tuplo vazio
    if len(matriz) == 1:
        return ()
    # criam-se listas com todos os índices linha e coluna representados
    posicoes_linha = [posicao_linha(i) for i in matriz if i != "valor_nulo"]
    posicoes_coluna = [posicao_coluna(i) for i in matriz if i != "valor_nulo"]
    # criam-se posições com as coordenadas extremas
    cord_min = cria_posicao(min(posicoes_linha), min(posicoes_coluna))
    cord_max = cria_posicao(max(posicoes_linha), max(posicoes_coluna))
    return cord_min, cord_max


def indices_linha(matriz) -> list:
    """a função devolve uma lista com todos os índices das linhas da matriz
        matriz: matriz
    """
    # obtém-se os índices linha extremos
    cord_extremas = matriz_dimensao(matriz)
    linha_min = posicao_linha(cord_extremas[0])
    linha_max = posicao_linha(cord_extremas[1])
    # cria-se uma lista com todos os índices entre eles, inclusive
    return [i for i in range(linha_min, linha_max + 1)]


def indices_coluna(matriz) -> list:
    """a função devolve uma lista com todos os índices colunas da matriz
        matriz: matriz
    """
    # obtém-se os índices coluna extremos
    cord_extremas = matriz_dimensao(matriz)
    coluna_min = posicao_coluna(cord_extremas[0])
    coluna_max = posicao_coluna(cord_extremas[1])
    # cria-se uma lista com todos os índices entre eles, inclusive
    return [i for i in range(coluna_min, coluna_max + 1)]


def matriz_densidade(matriz) -> float:
    """a função devolve a densidade da matriz introduzida
        matriz: matriz
    """
    # se a matriz estiver vazia a sua densidade é 0
    if len(matriz) == 1:
        return 0.0
    # a dimensão da matriz é o produto do número de linhas e colunas
    dim_total = len(indices_linha(matriz)) * len(indices_coluna(matriz))
    # num de elementos não nulos é o comprimento da matriz sem o valor nulo
    return (len(matriz) - 1) / dim_total


def matriz_nulo(matriz, novo_zero: float):
    """a função permite definir um novo zero para a matriz introduzida
        matriz: matriz
        retorno: None
    """
    for i in list(matriz):
        # se o elemento da matriz for igual ao novo zero o elemento é apagado
        if float(novo_zero) == matriz[i]:
            del matriz[i]
    matriz["valor_nulo"] = float(novo_zero)


# OPERAÇÕES SOBRE A MATRIZ ESPARSA
def matriz_str(matriz, formato: str) -> str:
    """a função devolve uma representação da matriz sobre a forma de uma string
        matriz: matriz
        formato: formato de representação dos elementos da matriz
    """
    if matriz_dimensao(matriz) == ():
        return ""
    string = ""
    # itera-se sobre os elementos da matriz entre as dimensões extremas
    for i in indices_linha(matriz):
        for j in indices_coluna(matriz):
            # adicionam-se os elementos formatados à string e um espaço
            string += formato % matriz_valor(matriz, cria_posicao(i, j)) \
                + " "
            # no fim de uma linha retira-se o espaço a mais e mudamos de linha
            if j == indices_coluna(matriz)[-1]:
                string = string[:-1]
                string += "\n"
        # no fim da matriz retiramos a linha a mais
        if i == indices_linha(matriz)[-1]:
            string = string[:-1]
    return string


def matriz_linha(matriz, indice_linha: int) -> tuple:
    """a função devolve uma linha da matriz como um tuplo
        matriz: matriz
        indice_linha: índice da linha a ser devolvida
    """
    if matriz_dimensao(matriz) == () \
            or indice_linha not in indices_linha(matriz):
        return ()
    linha = ()
    # itera-se sobre os elementos da linha indicada
    for i in indices_coluna(matriz):
        # adicionam-se os elementos ao tuplo
        linha += (matriz_valor(matriz, cria_posicao(indice_linha, i)),)
    return linha


def matriz_coluna(matriz, indice_coluna: int) -> tuple:
    """a função devolve uma coluna da matriz como um tuplo
        matriz: matriz
        indice_coluna: índice da coluna a ser devolvida
    """
    if matriz_dimensao(matriz) == () \
            or indice_coluna not in indices_coluna(matriz):
        return ()
    coluna = ()
    # itera-se sobre os elementos da coluna indicada
    for i in indices_linha(matriz):
        # adicionam-se os elementos ao tuplo
        coluna += (matriz_valor(matriz, cria_posicao(i, indice_coluna)),)
    return coluna


def matriz_diagonal(matriz) -> tuple:
    """a função devolve a diagonal da matriz, caso esta seja quadrada
        matriz: matriz
    """
    if matriz_dimensao(matriz) == ():
        return ()
    if len(indices_linha(matriz)) != len(indices_coluna(matriz)):
        raise ValueError("matriz_diagonal: matriz não quadrada")
    diagonal = ()
    # itera-se sobre as posições da diagonal
    for i, j in zip(indices_linha(matriz), indices_coluna(matriz)):
        # adicionam-se os elementos ao tuplo
        diagonal += (matriz_valor(matriz, cria_posicao(i, j)),)
    return diagonal
