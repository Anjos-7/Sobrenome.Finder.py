print('Olá, vamos descobrir se o seu nome possui um dos sobrenomes mais usados no Brasil!')
name = input('Digite o seu nome completo: ')
names = 'Silva, Santos, Oliveira, Souza, Pereira, Lima, Carvalho, Almeida, Ferreira, Rodrigues'
sobrenomes = names.split(', ')

# Verifica se o nome possui um dos sobrenomes comuns
possui_sobrenome_comum = any(sobrenome in name for sobrenome in sobrenomes)

print('O nome {} tem um dos 10 sobrenomes mais comuns no Brasil? {}'
.format(name, possui_sobrenome_comum))
