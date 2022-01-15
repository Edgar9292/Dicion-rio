loginSenha={'Joao:', 'good',
            'Maria:', 'well',
            'Mario:', 'since'}
login = input("Qual seu login:")
senha = input("Qual sua senha:")

if loginSenha[login] == senha:
    print("Acesso autorizado..")
else:
    print("Senha errada")
