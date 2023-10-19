from conexaoBD import conectar
from tkinter import messagebox
import mysql.connector

def consultar():
    conexao, cursor = conectar()
    try:
        sqlConsulta = "SELECT * FROM tb_dados_viagens"
        cursor.execute(sqlConsulta)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha",
        "Falha ao consultar"+str(falha))
        return None
    finally:
        cursor.close()
        conexao.close()