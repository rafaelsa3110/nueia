import unicodedata
import re


def limpar_string_lower(texto_entrada):
    """
    Higieniza a string para criação de nomes de arquivos ou identificadores.
    Remove acentos, caracteres especiais e padroniza o formato.
    """
    if not isinstance(texto_entrada, str):
        return texto_entrada

    # 1. Remove acentos (Normaliza para decompor caracteres acentuados)
    forma_nfkd = unicodedata.normalize('NFKD', texto_entrada)
    texto = "".join([c for c in forma_nfkd if not unicodedata.combining(c)])

    # 2. Converte para minúsculas (Recomendado para sistemas de arquivos no Fabric/Lakehouse)
    texto = texto.lower()

    # 3. Substitui espaços e hifens por sublinhados (undercore)
    texto = re.sub(r'[\s\-]+', '_', texto)

    # 4. Remove caracteres especiais restantes (mantém apenas a-z, 0-9 e _)
    texto = re.sub(r'[^a-z0-9_]', '', texto)

    # Retorna o texto removendo sublinhados extras no início ou fim
    return texto.strip('_')

    # Crie uma função para limpar sinais gráficos e caracteres especiais
# deixando em maiúsculo somente a primeira letra de cada palavra

def limpar_string_title(texto_entrada):
    """
    Higieniza a string mantendo a primeira letra de cada palavra em maiúscula
    e preserva o hífen (ex: DECRETO-LEI -> Decreto-Lei).
    """
    if not isinstance(texto_entrada, str):
        return texto_entrada

    # 1. Remove acentos (Normalização NFKD)
    forma_nfkd = unicodedata.normalize('NFKD', texto_entrada)
    texto = "".join([c for c in forma_nfkd if not unicodedata.combining(c)])

    # 2. Converte para Title Case
    # O Python tratará letras após o hífen como início de nova palavra
    texto = texto.title()

    # 3. Limpeza de caracteres especiais
    # Mantemos letras (a-z, A-Z), números (0-9), hifens (-) e espaços ( )
    # Removemos o restante (como º, ª, parênteses, etc.)
    texto = re.sub(r'[^a-zA-Z0-9\-\s]', '', texto)

    # 4. Ajuste de espaços (opcional)
    # Se quiser transformar espaços em underline mas MANTER o hífen:
    texto = texto.replace(' ', '_')
    
    return texto.strip()

# Crie uma função para limpar sinais gráficos e caracteres especiais
# deixando todas as palavras em maiúsculo

def limpar_string_upper(texto_entrada):
    """
    Higieniza a string e converte todos os caracteres para MAIÚSCULAS.
    Ideal para padronização rigorosa de nomes de arquivos e IDs.
    """
    if not isinstance(texto_entrada, str):
        return texto_entrada

    # 1. Remove acentos (Normalização NFKD)
    forma_nfkd = unicodedata.normalize('NFKD', texto_entrada)
    texto = "".join([c for c in forma_nfkd if not unicodedata.combining(c)])

    # 2. Converte todo o texto para MAIÚSCULAS
    texto = texto.upper()

    # 3. Substitui espaços e hifens por sublinhados
    texto = re.sub(r'[\s\-]+', '_', texto)

    # 4. Remove caracteres especiais (mantém A-Z, 0-9 e _)
    # Note que aqui não precisamos de 'a-z' pois tudo já é maiúsculo
    texto = re.sub(r'[^A-Z0-9_]', '', texto)

    # Remove sublinhados extras nas extremidades
    return texto.strip('_')