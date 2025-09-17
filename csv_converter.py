import csv

# Arquivo CSV de entrada
entrada = "servidores_prefeitura.csv"

# Nome da tabela
tabela = "servidores"

# Arquivo SQL de saída
saida = "servidores_prefeitura.sql"

with open(entrada, "r", encoding="utf-8") as infile, open(saida, "w", encoding="utf-8") as outfile:
    reader = csv.reader(infile)
    colunas = next(reader)  # primeira linha do CSV são os nomes das colunas
    
    valores_linhas = []
    for linha in reader:
        valores = []
        for v in linha:
            # tenta converter para número, senão mantém como texto
            if v.replace(".", "", 1).isdigit():
                valores.append(v)
            else:
                valores.append(f"'{v}'")
        valores_linhas.append(f"({', '.join(valores)})")
    
    sql = f"INSERT INTO {tabela} ({', '.join(colunas)}) VALUES\n" + ",\n".join(valores_linhas) + ";"
    outfile.write(sql + "\n")
