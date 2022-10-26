import pandas as pd
import numpy as np
import csv
from datetime import date

COLUNAS = ["Nome", "E-mail", "Curso", "Etapas Concluídas", "Total de Etapas", "Concluído", "Data de Conclusão", "Data de Início"]

def comparativo(nome_grupo_economico, nome_csv_curso_antigo, nome_csv_curso_novo, destino = None):

    Nestodou = []
    df = pd.read_csv(f"{nome_csv_curso_antigo}", sep=',')
    linhas = df.shape[0]
    DB = np.zeros((linhas+1,8), dtype=object)

    with open(f'{nome_csv_curso_antigo}', encoding='utf-8') as Antigo:
        Linhas = csv.reader(Antigo, delimiter=',')
        aux = 0
        for linha in Linhas:
            DB[aux][0] = linha[1]
            DB[aux][1] = linha[2]
            DB[aux][2] = linha[4]
            DB[aux][3] = linha[5]
            DB[aux][4] = linha[6]
            DB[aux][5] = linha[7]
            DB[aux][6] = linha[8]
            DB[aux][7] = linha[9]
            aux += 1

    df = pd.read_csv(f"{nome_csv_curso_novo}",sep=',')
    linhas = df.shape[0]
    DB2 = np.zeros((linhas+1,8), dtype=object)

    with open(f'{nome_csv_curso_novo}',encoding='utf-8') as Antigo:
        Linhas = csv.reader(Antigo, delimiter=',')
        aux = 0
        for linha in Linhas:
            DB2[aux][0] = linha[1] # 0 nome 
            DB2[aux][1] = linha[2] # 1 E-mail
            DB2[aux][2] = linha[4] # 2 Curso
            DB2[aux][3] = linha[5] # 3 Etapas Concluídas
            DB2[aux][4] = linha[6] # 4 Total de Etapas
            DB2[aux][5] = linha[7] # 5 Concluído
            DB2[aux][6] = linha[8] # 6 Data de Conclusão
            DB2[aux][7] = linha[9] # 7 Data de início
            aux += 1

    for aux in range(len(DB)):

        if DB[aux][5]=='NÃO' and DB2[aux][5]=='NÃO':
            if int(DB[aux][3]) > 0:
                Nestodou.append(DB[aux])
            elif int(DB2[aux][3]) > 0:
                Nestodou.append(DB2[aux])
            else:
                Nestodou.append(DB[aux])

        elif DB[aux][5]=='SIM':
            Nestodou.append(DB[aux])
        
        elif DB2[aux][5]=='SIM':
            Nestodou.append(DB2[aux])

    if destino:
        df = pd.DataFrame(Nestodou, columns=COLUNAS)
        df.to_excel(f'{destino}/{nome_grupo_economico}_{date.today().strftime("%d_%m_%Y")}.xlsx', index=False)
    else:
        df = pd.DataFrame(Nestodou, columns=COLUNAS)
        df.to_excel(f'{nome_grupo_economico}_{date.today().strftime("%d_%m_%Y")}.xlsx', index=False)
