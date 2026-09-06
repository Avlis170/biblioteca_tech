from src.bibliotech import pode_emprestar, calcular_multa, classificar_atraso

# RF01 - Testes de Caixa Preta
def test_usuario_ativo_sem_pendencia_poucos_emprestimos():
    assert pode_emprestar(True, False, 1) is True

def test_usuario_inativo():
    assert pode_emprestar(False, False, 1) is False

def test_usuario_com_pendencia():
    assert pode_emprestar(True, True, 1) is False

def test_usuario_no_limite_nao_pode_emprestar():
    assert pode_emprestar(True, False, 3) is False

# RF02 - Testes de Caixa Preta (Multa)
def test_multa_sem_atraso():
    assert calcular_multa(0) == 0.0

def test_multa_atraso_levedia_7():
    assert calcular_multa(7) == 14.0

def test_multa_atraso_grave_dia_8():
    assert calcular_multa(8) == 17.0

def test_multa_dias_negativos():
    assert calcular_multa(-5) == 0.0

# RF03 - Testes de Caixa Preta (Classificação)
def test_classificacao_sem_atraso():
    assert classificar_atraso(0) == "sem atraso"

def test_classificacao_atraso_leve():
    assert classificar_atraso(7) == "atraso leve"

def test_classificacao_atraso_moderado():
    assert classificar_atraso(30) == "atraso moderado"

def test_classificacao_atraso_grave():
    assert classificar_atraso(31) == "atraso grave"

# Testes de Caixa Branca
def test_caixa_branca_bug_limite_exato_3_emprestimos():
    assert pode_emprestar(True, False, 3) is False

def test_caixa_branca_cobertura_branches_multa():
    assert calcular_multa(5) == 10.0
    assert calcular_multa(10) == 23.0
