nota1 = float(input('Digite sua 1° nota: '))
nota2 = float(input('Digite sua 2° nota: '))
nota3 = float(input('Digite sua 3° nota: '))

media = (nota1 + nota2 + nota3) / 3
print('Sua Média foi: ',  media)

if media == 10:
    print('Aprovado com distinção !!')
elif media >= 7 and media < 10:
    print('Aprovado !!')
else:
    print('Reprovado !!')