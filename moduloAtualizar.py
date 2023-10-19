from conexaoBD import conectar
from tkinter import messagebox
import mysql.connector

def atualizarCadastro(dest, clnt, data, origm, formpgm):
    conexao, cursor = conectar()
    try:
        sql = f"""UPDATE tb_dados_viagens
            SET nome_cliente='{clnt}', data_viagem= '{data}',
            local_origem='{origm}', local_destino='{dest}',
             WHERE forma_pagamento='{formpgm}'
              """ 
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Atualizar",
            "Cadastro atualizado!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha",
        "Falha ao atualizar"+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()