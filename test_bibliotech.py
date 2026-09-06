from src.bibliotech import pode_emprestar, calcular_multa, classificar_atraso

# ==========================================
# Testes de Caixa Preta: pode_emprestar (RF01)
# ==========================================

def test_usuario_valido_pode_emprestar():
    # CT-02: Usuário ativo, sem pendências e com 0 empréstimos
    resultado = pode_emprestar(True, False, 0)
    assert resultado is True

def test_usuario_inativo_nao_pode_emprestar():
    # CT-03: Usuário inativo
    resultado = pode_emprestar(False, False, 0)
    assert resultado is False

def test_usuario_com_pendencia_nao_pode_emprestar():
    # CT-04: Usuário com pendência
    resultado = pode_emprestar(True, True, 0)
    assert resultado is False

def test_usuario_no_limite_nao_pode_emprestar():
    # CT-01: Usuário no limite de 3 empréstimos
    resultado = pode_emprestar(True, False, 3)
    assert resultado is False


# ==========================================
# Testes de Caixa Preta: calcular_multa (RF02)
# ==========================================

def test_calcular_multa_zero_dias():
    # CT-05: 0 dias de atraso
    assert calcular_multa(0) == 0.0

def test_calcular_multa_sete_dias():
    # CT-06: 7 dias de atraso (limite faixa leve)
    assert calcular_multa(7) == 14.0

def test_calcular_multa_oito_dias():
    # CT-07: 8 dias de atraso (início excedente)
    assert calcular_multa(8) == 17.0

def test_calcular_multa_dez_dias():
    # CT-08: 10 dias de atraso
    assert calcular_multa(10) == 23.0


# ==========================================
# Testes de Caixa Preta: classificar_atraso (RF03)
# ==========================================

def test_classificar_atraso_sem_atraso():
    # CT-09: 0 dias
    assert classificar_atraso(0) == "sem atraso"

def test_classificar_atraso_leve():
    # CT-10: 7 dias
    assert classificar_atraso(7) == "atraso leve"

def test_classificar_atraso_moderado():
    # CT-11: 8 dias
    assert classificar_atraso(8) == "atraso moderado"

def test_classificar_atraso_grave():
    # CT-12: 31 dias
    assert classificar_atraso(31) == "atraso grave"
