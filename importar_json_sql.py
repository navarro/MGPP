import json
import pymysql

json_data = open("data.json").read()
json_obj = json.loads(json_data)
con = pymysql.connect(host="127.0.0.1", user="root", password="root", db="testejson")

cursor = con.cursor()

for item in json_obj:
    DT_LANCAMENTO = item.get("DT_LANCAMENTO", "")
    CD_FONTE_RECURSO = item.get("CD_FONTE_RECURSO", "")
    CD_RUBRICA_RECEITA = item.get("CD_RUBRICA_RECEITA", "")
    CD_TP_RECEITA = item.get("CD_TP_RECEITA", "")
    DS_TP_RECEITA = item.get("DS_TP_RECEITA", "")
    VL_ARRECADADO = item.get("VL_ARRECADADO", "")
    ID_RECEITA_ARRECADADA = item.get("ID_RECEITA_ARRECADADA", "")
    CATEGORIA = item.get("CATEGORIA", "")
    ORIGEM = item.get("ORIGEM", "")
    ESPECIE = item.get("ESPECIE", "")
    RUBRICA = item.get("RUBRICA", "")
    ALINEA = item.get("ALINEA", "")
    SUBALINEA = item.get("SUBALINEA", "")
    DS_RUBRICA_RECEITA = item.get("DS_RUBRICA_RECEITA", "")
    cursor.execute("INSERT INTO json_files (DT_LANCAMENTO, CD_FONTE_RECURSO, CD_RUBRICA_RECEITA, CD_TP_RECEITA, DS_TP_RECEITA, VL_ARRECADADO, ID_RECEITA_ARRECADADA, CATEGORIA, ORIGEM, ESPECIE, RUBRICA, ALINEA, SUBALINEA, DS_RUBRICA_RECEITA) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (DT_LANCAMENTO, CD_FONTE_RECURSO, CD_RUBRICA_RECEITA, CD_TP_RECEITA, DS_TP_RECEITA, VL_ARRECADADO, ID_RECEITA_ARRECADADA, CATEGORIA, ORIGEM, ESPECIE, RUBRICA, ALINEA, SUBALINEA, DS_RUBRICA_RECEITA))

con.commit()
con.close()
