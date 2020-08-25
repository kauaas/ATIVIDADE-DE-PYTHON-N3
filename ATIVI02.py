print('faça o seu cadrasto')
usuario = str(input('Informe o seu nome de usuário: '))
senha = str(input('Informe uma senha: '))
while usuario==senha:
    print('Tente Novamente!')
    usuario = str(input('Informe o nome de usuário: '))
    senha = str(input('Informe a senha: '))
else:
     print('Cadrasto efetuado!')
