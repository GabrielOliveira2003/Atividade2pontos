from moduloCadastrar import inserir
from moduloConsultar import consultar
from moduloDeletar import deletar
from moduloAtualizar import atualizarCadastro

atualizarCadastro( "Joséfino", "20:10:2023","Brasil", "México", "Cartão de crédito")
atualizarCadastro(clnt= "Joséfino", data= "20:10:2023", origm= "Brasil", dest= "México", formpgm= "Cartão de crédito")




# for item in consultar():
#     print("CÓDIGO:" +str(item[0]))
#     print("DESCRIÇÃO:" + item[1])
#     print("SETOR: "+ item[2])
#     print("CATEGORIA: "+item[3])
#     print("------------------")


#inserir("Joséfino","20:10:2023","Brasil", "México", "Cartão de crédito")
 