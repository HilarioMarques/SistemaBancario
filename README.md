# Sistema Bancário (Python)

Projeto didático em Python (somente biblioteca padrão) usado para praticar
o fluxo de colaboração no GitHub: fork, branch, commit e pull request.

## Como executar

```bash
python main.py
```

Requer Python 3.8 ou superior.

## Estrutura

| Arquivo      | Conteúdo                                              |
|--------------|-------------------------------------------------------|
| `conta.py`   | `Conta`, `ContaCorrente`, `ContaPoupanca` e exceção   |
| `cliente.py` | `Cliente`                                             |
| `banco.py`   | `Banco` (cadastro de clientes e contas)               |
| `main.py`    | Menu interativo no terminal                           |

## Tarefas em aberto (sugestões de pull request)

- [ ] Extrato: registrar o histórico de operações em cada conta e exibi-lo no menu.
- [ ] Listar todas as contas de um cliente.
- [ ] Opção de menu para aplicar rendimento na `ContaPoupanca`.
- [ ] Taxa de manutenção mensal na `ContaCorrente`.

## Como contribuir

1. Faça um fork do repositório.
2. Crie uma branch: `git checkout -b feature/nome-da-tarefa`.
3. Faça commits pequenos e com mensagens claras.
4. Envie a branch para o seu fork e abra um pull request.
