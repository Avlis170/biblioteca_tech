LIMITE_EMPRESTIMOS = 3

def pode_emprestar(usuario_ativo, possui_pendencia, emprestimos_ativos):
    if not usuario_ativo:
        return False
    if possui_pendencia:
        return False
    if emprestimos_ativos >= LIMITE_EMPRESTIMOS:
        return False
    return True

def calcular_multa(dias_atraso):
    if dias_atraso <= 0:
        return 0.0
    elif dias_atraso <= 7:
        return dias_atraso * 2.0
    else:
        return 14.0 + (dias_atraso - 7) * 3.0

def classificar_atraso(dias_atraso):
    if dias_atraso <= 0:
        return "sem atraso"
    elif dias_atraso <= 7:
        return "atraso leve"
    elif dias_atraso <= 30:
        return "atraso moderado"
    else:
        return "atraso grave"
