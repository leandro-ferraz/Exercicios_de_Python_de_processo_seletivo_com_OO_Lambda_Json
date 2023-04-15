# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

class PercentualEstados():
    def __init__(self):
        self.faturamentoMensalPorEstado = {
                                        'sp': 67836.43,
                                        'rj': 36678.66,
                                        'mg': 29229.88,
                                        'es': 27165.48,
                                        'outros':19849.53
        }
        self.calcularEArmazenarPercentuaisFaturamentoEstados()
    
    def exibirPercentualMensalEstado(self, siglaEstado):
        perEstado = self.faturamentoMensalPorEstado[siglaEstado.lower()][1]
        print(f'=> Percentual para o estado [{siglaEstado.upper()}]: {perEstado:.2f}%')
        
    def exibirPercentuaisMensaisDeTodosEstados(self):
        print('========= Percentual de faturamento mensal =================')
        for key, value in self.faturamentoMensalPorEstado.items():
            print(f"=> [{key.upper()}]: {value[1]:.2f}%")
        print('============================================================')

    def exibirEstadosArmazenados(self):
        print('======== Estados armazenados ============ ')
        for key in self.faturamentoMensalPorEstado.keys():
            print(str(key).upper())
        print('========================================= ')

    def armazenarEstado(self, siglaEstado, faturamentoMensalEstado):
        #se for sigla de 2 palavras e possuir faturamento
        if (len(siglaEstado) == 2) & (isinstance(faturamentoMensalEstado, (int, float))):
            self.faturamentoMensalPorEstado[siglaEstado.lower()] = faturamentoMensalEstado
            self.calcularEArmazenarPercentuaisFaturamentoEstados()
            print(f'=> Armazenado com sucesso! [{siglaEstado.upper()}]')
            
        elif isinstance(faturamentoMensalEstado, (int, float)):
            print('Sigla inválida!')
        else:
            print('Parâmetros inválidos! Digite uma sigla de estado válida e seu faturamento mensal em um formáto valido!')

    def removerEstado(self, siglaEstado):
        siglaEstado = siglaEstado.lower()
        if siglaEstado in self.faturamentoMensalPorEstado:
            self.faturamentoMensalPorEstado.pop(siglaEstado)
            print(f'Estado [{siglaEstado.upper()}] removido com sucesso')
        else:
            print(f'Estado [{siglaEstado.upper()}] nao encontrado ou informado incorretamente!')
    
    def calcularEArmazenarPercentuaisFaturamentoEstados(self):
        def obterFaturamentoTotalMensalEstados():
            vetorFaturamentos = []
            #preenche um array com os valores dos faturamentos dos estados
            for value in self.faturamentoMensalPorEstado.values():
                try:
                    vetorFaturamentos.append(value[0])
                except:
                    vetorFaturamentos.append(value)        

            faturamentoTotalMensalEstados = sum(vetorFaturamentos)
            return faturamentoTotalMensalEstados

        def atualizarPercentuaisFaturamentosEstados(faturamentoTotalMensalEstados):
            for key, value in self.faturamentoMensalPorEstado.items():
                #se o valor do dicionário for um array, usa a posiçao que contem o faturamento
                try:
                    self.faturamentoMensalPorEstado[key] = [value[0], ((value[0]/faturamentoTotalMensalEstados)*100)]
                except:
                #do contrario, realiza o cálculo com a chave do dicionário não sendo um vetor
                    self.faturamentoMensalPorEstado[key] = [value, ((value/faturamentoTotalMensalEstados)*100)]

        faturamentoTotalMensalEstados = obterFaturamentoTotalMensalEstados()
        atualizarPercentuaisFaturamentosEstados(faturamentoTotalMensalEstados)

consultaPercentual1 = PercentualEstados()
consultaPercentual1.exibirPercentualMensalEstado('sp')
consultaPercentual1.armazenarEstado('df', 15000)
consultaPercentual1.exibirPercentualMensalEstado('df')
consultaPercentual1.exibirPercentualMensalEstado('sp')
consultaPercentual1.exibirPercentuaisMensaisDeTodosEstados()