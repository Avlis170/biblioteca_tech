# Matriz de Rastreabilidade — BiblioTech

| Requisito | Descrição Breve | Casos de Teste Associados |
| :--- | :--- | :--- |
| **RF01** | Elegibilidade de Empréstimo | CT-01, CT-02, CT-03, CT-04, CB-01 |
| **RF02** | Cálculo de Multa por Atraso | CT-05, CT-06, CT-07, CT-08, CB-02 |
| **RF03** | Classificação da Categoria de Atraso | CT-09, CT-10, CT-11, CT-12, CB-02 |

---

### Análise de Rastreabilidade
- **Existe requisito sem teste?** Não. Todos os requisitos funcionais (RF01, RF02 e RF03) possuem casos de teste de caixa preta e caixa branca associados.
- **Existe teste que não sabemos qual requisito verifica?** Não. Cada função de teste criada no `test_bibliotech.py` mapeia diretamente uma regra de negócio dos requisitos.
