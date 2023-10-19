from conexaoBD import conectar
from tkinter import messagebox
import mysql.connector

def deletar(id):
    conexao, cursor = conectar()
    try:
        sqlDeletar = f"""DELETE FROM tb_dados_viagens
              WHERE forma_pagamento='{id}'
               """
        cursor.execute(sqlDeletar)
        conexao.commit()
        messagebox.showinfo("Deletado",
            "Apagado com sucesso!")
        return True
    
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha",
            "Falha ao deletar"+str(falha))
        return None
    
    finally:
        cursor.close()
        conexao.close()