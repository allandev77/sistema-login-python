tentativas = 3
usuario = "JojiDeveloper"
senha = "Docker"
login = False
while tentativas > 0 and login == False:
 print('''===== SISTEMA DE LOGIN =====
 ''') 
 usuariotentativa = str(input("Usuário: "))
 senhatentativa = str(input("Senha: "))

 if usuariotentativa != usuario and senhatentativa != senha:
  print("Credenciais incorretas")
  tentativas = tentativas - 1
  print("Tentativas restantes: {}".format (tentativas)) 
  
 elif usuariotentativa != usuario:
  print("Credenciais incorretas")
  tentativas = tentativas - 1
  print("Tentativas restantes: {}".format (tentativas)) 
 

 elif senhatentativa != senha:
  print("Credenciais incorretas")
  tentativas = tentativas - 1
  print("Tentativas restantes: {}".format (tentativas)) 

  
 elif usuariotentativa == usuario and senhatentativa == senha:
  print('''Login realizado com sucesso!
  Bem vindo ao sistema!''')
  login = True

