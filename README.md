#### Este projeto contém dois arquivos principais: agent.py e main.py. Eles formam um sistema que executa tarefas específicas e interagem entre si para alcançar objetivos definidos.

## Clonando o repositório

```bash
git clone https://github.com/vinicios-campera/webdev-python.git
```

## Estrutura de Arquivos

- **main.py:** Api na qual o agente irá buscar os dados conforme definido no desafio.

- **agent.py:** Agente que realiza algumas operações com base no resultado da api.

## Abrindo a pasta do projeto

```bash
cd webdev-python
```

## Dependências

Instalando as bibliotecas necessárias

```bash
pip install fastapi uvicorn faker python-Levenshtein pandas requests
```

## Executando a api

```bash
uvicorn main:app --reload
```

OBS: As credenciais da api estão definidas diretamente no código fonte. Em ambiente de produção, devem ser armazenadas nas váriaveis de ambiente

## Testando a api

```bash
curl -u meu_usuario:minha_senha http://127.0.0.1:8000/names
```

## Executando o agente

```bash
python agent.py
```
