# Calculadora Simples em Python

Este é um projeto simples de uma calculadora em Python, que permite realizar as quatro operações básicas: adição, subtração, multiplicação e divisão.

## Funcionalidades
- Adição de dois números.
- Subtração de dois números.
- Multiplicação de dois números.
- Divisão de dois números (com validação para evitar divisão por zero).
- Menu interativo que permite múltiplas operações sem fechar o programa.

## Como Executar
1. Certifique-se de ter o Python instalado em sua máquina (versão 3.6 ou superior).
2. Baixe ou clone este repositório:
   ```bash
   git clone https://github.com/SeuUsuario/NomeDoRepositorio.git

## Testes Unitários

Este projeto inclui testes unitários desenvolvidos com a biblioteca pytest, para garantir a confiabilidade e a funcionalidade correta da calculadora. Esses testes foram projetados para cobrir os principais casos de uso e situações específicas que poderiam levar a erros.

## Cobertura dos Testes
Os testes unitários desenvolvidos verificam:

## Operações básicas: 
- Confirmação de que adição, subtração, multiplicação e divisão retornam os resultados esperados.
- Divisão por zero: Garantia de que a calculadora lida corretamente com tentativas de divisão por zero, retornando mensagens apropriadas.
Entradas inválidas: Validação de entradas não numéricas ou fora do esperado.

## Como Executar os Testes
Para rodar os testes, siga estas instruções:

- Certifique-se de que o pytest está instalado. Caso não esteja, instale-o com o comando:
   pip install pytest
   No diretório do projeto, execute os testes com:
   pytest
   Os resultados dos testes serão exibidos no terminal, indicando quais casos passaram ou falharam, além de fornecer detalhes sobre possíveis erros.

## Benefícios dos Testes
A inclusão de testes unitários com pytest neste projeto traz diversas vantagens:

- Confiabilidade: Garante que todas as operações funcionem como esperado.
- Manutenção facilitada: Novas alterações no código podem ser testadas rapidamente para verificar se não introduzem erros.
- Prevenção de erros comuns: Situações como divisões por zero e entradas inválidas são tratadas antes de se tornarem problemas no uso real da calculadora.
