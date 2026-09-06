# Roteiro de Testes — BiblioTech

## CT-01
**Requisito:** RF01  
**Título:** Usuário com três empréstimos não pode realizar outro empréstimo  
**Tipo:** Caixa preta  
**Prioridade:** Alta  
**Pré-condição:** Sistema disponível e usuário ativo  
**Dados de teste:** `usuario_ativo = True`, `possui_pendencia = False`, `emprestimos_ativos = 3`  
**Passos:** 1. Executar `pode_emprestar(True, False, 3)`  
**Resultado esperado:** `False`  
**Resultado obtido:**  
**Status:** [ ] Passou [ ] Falhou  

---

## CT-02
**Requisito:** RF01  
**Título:** Permissão concedida para usuário ativo, sem pendência e com 0 empréstimos  
**Tipo:** Caixa preta  
**Prioridade:** Alta  
**Pré-condição:** Sistema disponível  
**Dados de teste:** `usuario_ativo = True`, `possui_pendencia = False`, `emprestimos_ativos = 0`  
**Passos:** 1. Executar `pode_emprestar(True, False, 0)`  
**Resultado esperado:** `True`  
**Resultado obtido:**  
**Status:** [ ] Passou [ ] Falhou  

---

## CT-03
**Requisito:** RF01  
**Título:** Empréstimo recusado para usuário inativo  
**Tipo:** Caixa preta  
**Prioridade:** Média  
**Pré-condição:** Sistema disponível  
**Dados de teste:** `usuario_ativo = False`, `possui_pendencia = False`, `emprestimos_ativos = 0`  
**Passos:** 1. Executar `pode_emprestar(False, False, 0)`  
**Resultado esperado:** `False`  
**Resultado obtido:**  
**Status:** [ ] Passou [ ] Falhou  

---

## CT-04
**Requisito:** RF01  
**Título:** Empréstimo recusado para usuário com pendência  
**Tipo:** Caixa preta  
**Prioridade:** Alta  
**Pré-condição:** Sistema disponível  
**Dados de teste:** `usuario_ativo = True`, `possui_pendencia = True`, `emprestimos_ativos = 0`  
**Passos:** 1. Executar `pode_emprestar(True, True, 0)`  
**Resultado esperado:** `False`  
**Resultado obtido:**  
**Status:** [ ] Passou [ ] Falhou  

---

## CT-05
**Requisito:** RF02  
**Título:** Cálculo de multa para 0 dias de atraso  
**Tipo:** Caixa preta  
**Prioridade:** Média  
**Pré-condição:** Sistema disponível  
**Dados de teste:** `dias = 0`  
**Passos:** 1. Executar `calcular_multa(0)`  
**Resultado esperado:** `0.0`  
**Resultado obtido:**  
**Status:** [ ] Passou [ ] Falhou  

---

## CT-06
**Requisito:** RF02  
**Título:** Cálculo de multa para 7 dias de atraso (limite da faixa leve)  
**Tipo:** Caixa preta  
**Prioridade:** Alta  
**Pré-condição:** Sistema disponível  
**Dados de teste:** `dias = 7`  
**Passos:** 1. Executar `calcular_multa(7)`  
**Resultado esperado:** `14.0`  
**Resultado obtido:**  
**Status:** [ ] Passou [ ] Falhou  

---

## CT-07
**Requisito:** RF02  
**Título:** Cálculo de multa para 8 dias de atraso (início do excedente)  
**Tipo:** Caixa preta  
**Prioridade:** Alta  
**Pré-condição:** Sistema disponível  
**Dados de teste:** `dias = 8`  
**Passos:** 1. Executar `calcular_multa(8)`  
**Resultado esperado:** `17.0`  
**Resultado obtido:**  
**Status:** [ ] Passou [ ] Falhou  

---

## CT-08
**Requisito:** RF02  
**Título:** Cálculo de multa para 10 dias de atraso  
**Tipo:** Caixa preta  
**Prioridade:** Média  
**Pré-condição:** Sistema disponível  
**Dados de teste:** `dias = 10`  
**Passos:** 1. Executar `calcular_multa(10)`  
**Resultado esperado:** `23.0`  
**Resultado obtido:**  
**Status:** [ ] Passou [ ] Falhou  

---

## CT-09
**Requisito:** RF03  
**Título:** Classificação para 0 dias de atraso  
**Tipo:** Caixa preta  
**Prioridade:** Baixa  
**Pré-condição:** Sistema disponível  
**Dados de teste:** `dias = 0`  
**Passos:** 1. Executar `classificar_atraso(0)`  
**Resultado esperado:** `"sem atraso"`  
**Resultado obtido:**  
**Status:** [ ] Passou [ ] Falhou  

---

## CT-10
**Requisito:** RF03  
**Título:** Classificação para 7 dias de atraso  
**Tipo:** Caixa preta  
**Prioridade:** Média  
**Pré-condição:** Sistema disponível  
**Dados de teste:** `dias = 7`  
**Passos:** 1. Executar `classificar_atraso(7)`  
**Resultado esperado:** `"atraso leve"`  
**Resultado obtido:**  
**Status:** [ ] Passou [ ] Falhou  

---

## CT-11
**Requisito:** RF03  
**Título:** Classificação para 8 dias de atraso  
**Tipo:** Caixa preta  
**Prioridade:** Média  
**Pré-condição:** Sistema disponível  
**Dados de teste:** `dias = 8`  
**Passos:** 1. Executar `classificar_atraso(8)`  
**Resultado esperado:** `"atraso moderado"`  
**Resultado obtido:**  
**Status:** [ ] Passou [ ] Falhou  

---

## CT-12
**Requisito:** RF03  
**Título:** Classificação para 31 dias de atraso  
**Tipo:** Caixa preta  
**Prioridade:** Média  
**Pré-condição:** Sistema disponível  
**Dados de teste:** `dias = 31`  
**Passos:** 1. Executar `classificar_atraso(31)`  
**Resultado esperado:** `"atraso grave"`  
**Resultado obtido:**  
**Status:** [ ] Passou [ ] Falhou

## 2. Testes de Caixa Branca

## CB-01
**Requisito:** RF01  
**Título:** Validação de limite exato no código (`emprestimos_ativos == 3`)  
**Tipo:** Caixa branca  
**Prioridade:** Alta  
**Pré-condição:** Leitura do código-fonte `bibliotech.py`  
**Dados de teste:** `usuario_ativo = True`, `possui_pendencia = False`, `emprestimos_ativos = 3`  
**Passos:** 1. Executar `pode_emprestar(True, False, 3)`  
**Resultado esperado:** `False`  
**Resultado obtido:** `True` (Bug detectado: a condição `>` permitiu o empréstimo)  
**Status:** [ ] Passou [x] Falhou  

---

## CB-02
**Requisito:** RF02 / RF03  
**Título:** Cobertura do ramo condicional para dias de atraso negativos  
**Tipo:** Caixa branca  
**Prioridade:** Média  
**Pré-condição:** Leitura do código-fonte `bibliotech.py`  
**Dados de teste:** `dias = -5`  
**Passos:** 1. Executar `calcular_multa(-5)` e `classificar_atraso(-5)`  
**Resultado esperado:** `0.0` e `"sem atraso"`  
**Resultado obtido:**  
**Status:** [ ] Passou [ ] Falhou
