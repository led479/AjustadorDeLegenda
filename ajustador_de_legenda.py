import re
import datetime

regex_tempo = re.compile(r'\d{2}:\d{2}:\d{2},\d{3}')

def atualiza_tempo(tempo, valor):
    tempo = datetime.datetime.strptime(tempo, '%H:%M:%S,%f')
    tempo_incrementado = tempo + datetime.timedelta(seconds=valor)
    return tempo_incrementado.strftime('%H:%M:%S,%f')[0:12]

def linha_com_tempo_atualizado(tempos_antigos, valor):
    tempos_novos = []
    for tempo in tempos_antigos:
        tempos_novos.append(atualiza_tempo(tempo, valor))
    return tempos_novos[0] + ' --> ' + tempos_novos[1] + '\n'

def cria_legenda_atualizada(arquivo_antigo, arquivo_novo, valor):
    for line in arquivo_antigo:
        tempos_antigos = regex_tempo.findall(line)

        if len(tempos_antigos) > 0:
            arquivo_novo.write(linha_com_tempo_atualizado(tempos_antigos, valor))
        else:
            arquivo_novo.write(line)

def main():
    print("ATUALIZADOR DE LEGENDA")
    print("Será criado um novo arquivo com a legenda atualizada\n")

    nome_arquivo_entrada = input("Digite o exato nome do arquivo da legenda (não é para incluir o .srt no fim):\n")
    nome_arquivo_saida = f"{nome_arquivo_entrada}_atualizado"
    valor = float(input("Entre em segundos a quantidade que quer atualizar (Valor positivo é para atrasar e valor negativo é para adiantar):\n"))

    with open(f"{nome_arquivo_entrada}.srt", 'rt', encoding="utf8") as fin:
        with open(f"{nome_arquivo_saida}.srt", 'wt', encoding="utf8") as fout:
            cria_legenda_atualizada(fin, fout, valor)

    print(f"Atualizou as legendas em {valor} segundos!")
    print(f"Gravou a legenda atualizada no arquivo: {nome_arquivo_saida}.srt")
    input("Aperte qualquer tecla para sair...")

main()



