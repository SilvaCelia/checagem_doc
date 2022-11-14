#O programa possui três informações sobre cada aluna e verificar se ela foi selecionada ou não.

cpf = str(input())
rg = str(input())
comp = str(input())

if cpf != 0 and rg == 'ok' and comp == 'ok':
    print(str(cpf)+ " selecionada")
else: 
    print(str(cpf)+ " não selecionada")