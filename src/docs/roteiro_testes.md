# Roteiro de Testes — BiblioTech

## 1. Testes de Caixa Preta

### 1.1 Função: `pode_emprestar` (RF01)

| ID | Descrição / Cenário | Ativo | Pendência | Empréstimos Ativos | Resultado Esperado | Técnicas Aplicadas |
|---|---|---|---|---|---|---|
| **CP01** | Usuário ativo, sem pendências, 0 empréstimos (Cenário Válido) | `True` | `False` | 0 | `True` | Partição Equivalente / Válido |
| **CP02** | Usuário inativo, sem pendências, 0 empréstimos | `False` | `False` | 0 | `False` | Partição Equivalente / Inválido |
| **CP03** | Usuário ativo, com pendência, 0 empréstimos | `True` | `True` | 0 | `False` | Partição Equivalente / Inválido |
| **CP04** | Usuário ativo, sem pendência, limite de 3 empréstimos | `True` | `False` | 3 | `False` | Análise de Valor de Fronteira |
| **CP05** | Usuário ativo, sem pendência, limite inferior de 2 empréstimos | `True` | `False` | 2 | `True` | Análise de Valor de Fronteira |

---

### 1.2 Função: `calcular_multa` (RF02)

| ID | Descrição / Cenário | Dias de Atraso | Resultado Esperado (R$) | Técnicas Aplicadas |
|---|---|---|---|---|
| **CP06** | Sem atraso ou dias negativos (Fronteira 0) | 0 | `0.0` | Valor de Fronteira / Sem multa |
| **CP07** | Atraso curto - Limite superior da 1ª faixa (7 dias) | 7 | `14.0` | Valor de Fronteira / (7 * R$ 2) |
| **CP08** | Atraso intermediário - Início da 2ª faixa (8 dias) | 8 | `17.0` | Valor de Fronteira / (R$ 14 + 1 * R$ 3) |
| **CP09** | Atraso longo - 10 dias | 10 | `23.0` | Partição Equivalente / (R$ 14 + 3 * R$ 3) |

---

### 1.3 Função: `classificar_atraso` (RF03)

| ID | Descrição / Cenário | Dias de Atraso | Classificação Esperada | Técnicas Aplicadas |
|---|---|---|---|---|
| **CP10** | Sem atraso (0 dias) | 0 | `"sem atraso"` | Valor de Fronteira |
| **CP11** | Atraso leve - Limite superior (7 dias) | 7 | `"atraso leve"` | Valor de Fronteira |
| **CP12** | Atraso moderado - Limite inferior (8 dias) | 8 | `"atraso moderado"` | Valor de Fronteira |
| **CP13** | Atraso grave - Acima de 30 dias (31 dias) | 31 | `"atraso grave"` | Valor de Fronteira |
