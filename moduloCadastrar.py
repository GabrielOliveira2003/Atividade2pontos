from conexaoBD import conectar
from tkinter import messagebox
import mysql.connector

def inserir(clnt, data, origm, dstn, formpgm):
    conexao, cursor = conectar()
    try:
        sql = f"""
                INSERT INTO tb_dados_viagens
                (nome_cliente, data_viagem, local_origem, local_destino, forma_pagamento)
                VALUES
                ('{clnt}','{data}','{origm}', '{dstn}', '{formpgm}')        
               """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Cadastrado",
            "Funcionário cadastrado")
    except mysql.connector.Error as erro:
        messagebox.showerror("Falha",
            "Falha ao cadastrar"+str(erro))
    finally:
        cursor.close()
        conexao.close()
