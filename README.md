# Feature1: Ajustes para Testes Unitários Automatizados

#### Descrição

A branch feature1 foi criada com o objetivo de ajustar o código para que os testes unitários sejam executados corretamente usando o framework pytest. No código principal (main), a função entra em um menu interativo, o que causava problemas durante a execução dos testes unitários, pois o menu era acionado, interrompendo o fluxo automatizado de testes.

Nesta branch, foram feitas as seguintes modificações:

- Separação da lógica principal do menu da funcionalidade que será testada.
- Adaptação do código para garantir que os testes sejam executados automaticamente, sem necessidade de interação humana.
- Garantia de que os testes possam ser executados em qualquer ambiente suportado pelo código sem interrupções.

#### Mudanças Principais

- Isolamento do Menu Interativo:
A lógica que aciona o menu foi isolada, permitindo que a funcionalidade principal seja chamada sem depender do menu.

- Adaptação para Testes Unitários:
O código foi refatorado para suportar chamadas diretas às funções que serão testadas.
Foi adicionada uma condição para impedir que o menu seja acionado durante a execução dos testes.

- Automatização com pytest:
Os testes unitários agora podem ser executados com o comando pytest sem bloqueios ou interações inesperadas.

#### Como Testar: 

- Certifique-se de estar na branch feature1:
git checkout feature1

- Execute os testes unitários usando o pytest:
pytest

- Verifique se todos os testes passam sem problemas.

##### Notas Adicionais

Certifique-se de revisar as alterações no código principal antes de realizar o merge para a branch main.
Documentação adicional sobre a refatoração está disponível nos comentários do código.

