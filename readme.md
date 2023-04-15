# Exercícios de Python de processo seletivo com OO, Lambda, Json, List functions e List Methods

Este projeto contém uma série de exercícios para treino de lógica de programação em Python, abrangendo conceitos como orientação a objeto, funções lambda, manipulação de listas e arquivos Json.

## Introdução
Os exercícios foram elaborados para servir como material de treino para candidatos a processos seletivos ou para quem deseja aprimorar seus conhecimentos em Python. Além de abordar temas relevantes da linguagem, os exercícios têm como objetivo estimular o pensamento lógico e a criatividade dos usuários.

## Instalação

### Pré-requisitos
- Versão do python: 3.10.7

### Bibliotecas utilizada no projeto
- functools (função reduce)
- locale 
- json

### Módulos 
Os exercícios estão organizados em módulos independentes, cada um abordando uma questão específica. Abaixo está uma breve descrição de cada um dos módulos disponíveis:

2. <u>Fibonnaci</u> - procedimento que verifica se um número informado pertence à sequência de Fibonacci.
3. <u>Obter métricas Distribuidora</u> [OO] - método que obtém dados da distribuidora (arquivo Json) e calcula as métricas (quantidade de dias com faturamento acima da média, o maior e menor faturamento do mês).
4. <u>Percentual de faturamento de estados</u> [OO] - possui vários métodos úteis para obter o percentual de faturamento dos estados em relação ao total. Já existe uma base de dados na classe, então é possível instanciar a classe e consultar os dados de forma simples.
5. <u>Inverter textos</u> - função que retorna seu parâmetro em ordem inversa (sem usar a função .reverse())

## Uso
Cada arquivo pode ser executado de forma independente, e contém a lógica necessária para resolver a questão proposta. Para entender melhor como os módulos funcionam, recomenda-se ocultar a lógica dos métodos das classes e executá-las apenas através de seus métodos.

### Exemplos de uso
Cada arquivo pode ser executado de forma independente, e contém a lógica necessária para resolver a questão proposta. Para entender melhor como os módulos funcionam, recomenda-se ocultar a lógica dos métodos das classes e executá-las apenas através de seus métodos.

- Módulo 2: 
    - "calcularFibonnaci()"
- Módulo 3: MetricasFaturamento()
    1. "metricas1 = MetricasFaturamento()"
    2. "metricas1.exibirMetricasFaturamento(diretorioArquivoJson='Arquivo/dados.json')"
- Módulo 4: 
    1. "consultaPercentual1 = PercentualEstados()"
    2. "consultaPercentual1.exibirPercentuaisMensaisDeTodosEstados()"
- Módulo 5:
    - "inverterTextoFornecidoPeloUsuario()"

## Contribuições

Se você tiver alguma contribuição, correção de bugs ou feedback, sinta-se à vontade para compartilhar. Agradeço qualquer ajuda para melhorar este projeto.

## Autor

- Leandro de Sousa Ferraz
