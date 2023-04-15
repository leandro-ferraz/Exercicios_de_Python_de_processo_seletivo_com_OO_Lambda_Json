# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

from functools import reduce
import locale, json

class MetricasFaturamento():
    def __init__(self):
        locale.setlocale(locale.LC_ALL, "pt_BR")
        self.maiorValor = None
        self.menorValor = None
        self.diaMaiorValor = None
        self.diaMenorValor = None
        self.qtdDiasFaturamentoAcimaDaMedia = None


    def exibirMetricasFaturamento(self, diretorioArquivoJson):
        arrayDadosFaturamentosNaoNulos = self.criarArrayDadosFaturamentosNaoNulos(diretorioArquivoJson)
        self.calcularMetricasFaturamento(arrayDadosFaturamentosNaoNulos)

        print('=================================== Resultado ===============================================')
        # print("Dia maior valor: "+ metricas['diaMaiorValor'])
        print('No dia ['+self.diaMaiorValor+'] houve o maior faturamento do mês: R$ '+ self.maiorValor)
        print('No dia ['+self.diaMenorValor+'] houve o menor faturamento do mês: R$ '+ self.menorValor)
        print('Total de dias com faturamento acima da média mensal: '+ self.qtdDiasFaturamentoAcimaDaMedia)
        print('====================================== Fim ==================================================')                

    def criarArrayDadosFaturamentosNaoNulos(self, diretorioArquivoJson):
        with open(diretorioArquivoJson) as arquivoDados:
            dados_json = json.load(arquivoDados)
            arrayDados = []
            for dado in dados_json:
                arrayDados.append([dado['dia'], dado['valor']])

        arrayDadosFaturamentoNaoNulo = list(filter(lambda x: x[1] != 0, arrayDados))
        return arrayDadosFaturamentoNaoNulo
        
    def calcularMetricasFaturamento(self, arrayDadosFaturamentoNaoNulo):                
        def calcularMaiorValor(arrayDadosFaturamentoNaoNulo):
            #o arrayMaiorValor armazena a posição na memória devido ao resultado ser também um array
            arrayMaiorValorDiaUnico = reduce(lambda x, y: x if x[1] > y[1] else y, arrayDadosFaturamentoNaoNulo[:])
            
            #atribuindo os valores à uma variável para formatar
            dataMaiorValor = arrayMaiorValorDiaUnico[0]            
            maiorValor = arrayMaiorValorDiaUnico[1]
            
            #formatando para exibição
            dataMaiorValor = str(dataMaiorValor)
            maiorValor = locale.format_string('%.2f', maiorValor, grouping=True)

            return [dataMaiorValor, maiorValor]
            
        def calcularMenorValor(arrayDadosFaturamentoNaoNulo):
            #o arrayMenorValor armazena a posição na memória devido ao resultado ser também um array
            arrayMenorValorDiaUnico = reduce(lambda x, y: x if x[1] < y[1] else y, arrayDadosFaturamentoNaoNulo[:])
            
            #atribuindo os valores à uma variável para formatar
            dataMenorValor = arrayMenorValorDiaUnico[0]
            menorValor = arrayMenorValorDiaUnico[1]

            #formatando para exibição
            dataMenorValor = str(dataMenorValor)
            menorValor = locale.format_string('%.2f', menorValor, grouping=True)

            return [dataMenorValor, menorValor]

        def calcularQtdDiasFaturamentoAcimaDaMedia(arrayDadosFaturamentoNaoNulo):
            #retorna como uma lista um array com apenas a posicao x[1] de x
            arrayFaturamentoNaoNulo = list(map(lambda x: x[1], arrayDadosFaturamentoNaoNulo))
            mediaFaturamento = sum(arrayFaturamentoNaoNulo) / len(arrayFaturamentoNaoNulo)
            #reduz o arrayfaturamento até um único valor - o acumulador x que conta os dias acima da média de faturamento
            qtdDiasFaturamentoAcimaDaMedia = reduce(lambda x, y: x + 1 if y > mediaFaturamento else x, arrayFaturamentoNaoNulo, 0)
            return str(qtdDiasFaturamentoAcimaDaMedia)
                
        dadosMaiorValorDiaUnico = calcularMaiorValor(arrayDadosFaturamentoNaoNulo)
        dadosMenorValorDiaUnico = calcularMenorValor(arrayDadosFaturamentoNaoNulo)
        qtdDiasFaturamentoAcimaDaMedia = calcularQtdDiasFaturamentoAcimaDaMedia(arrayDadosFaturamentoNaoNulo)

        self.diaMaiorValor = dadosMaiorValorDiaUnico[0]
        self.maiorValor     = dadosMaiorValorDiaUnico[1]
        self.diaMenorValor = dadosMenorValorDiaUnico[0]
        self.menorValor     = dadosMenorValorDiaUnico[1]
        self.qtdDiasFaturamentoAcimaDaMedia = qtdDiasFaturamentoAcimaDaMedia

MetricasFaturamento().exibirMetricasFaturamento(diretorioArquivoJson='Arquivo/dados.json')