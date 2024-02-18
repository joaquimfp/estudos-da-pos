#pos_graduacao = "seja oficialmente bem vindo"

#print (pos_graduacao)


#constantes = o python n trabalha com constantes, usamos a regra da boa vizinhanca; Colocamos a constante em letra MAIUSCULAS.
#ex: MAIORIDADE= 18
#REGRAS: 1- Sem espacos; 2- sem comecar numero; 3- sem caracter especial;
# python e a tipagem dinamica e interpretada


#nome= input("digite seu nome:") introducao aos dados, insercao de daos msempre atraves do input
#nascimento= input(f"bem vindo ao mundo {nome} ") 

#OUTPUT;apresentamos o conceito de concatenar o codigo, que e nada mais que vc colocar/otimizar as linhas de codigo, juntando varios codigos em uma unica linha

#nome= input("digite seu nome: ")
#nascimento =input("qual seu ano de nascimento? ")
#email=input("digite seu e-mail: ")

#print("nome: ",nome, ". e-mail: ",email , ". nascimento: " ,nascimento)


#conversor de input; quando falamos de input estamos sempre nos referindo ao strrng, ou seja, TEXTO. para que haja conversao, para que ele leia numeros, dentro de um input, e necessario que se coloque o INT(abreviacao de inteiro) antes do codigo input.


#vamos la, estou escrevendo de uma forma mais solta sobre os assuntos estudados ontem... apos muito estresse finalmente consegui arrumar a mesa que esta prestes a ir de arrasta para cima.
#ontem, vimos os operadores do python; primeiro vamos falar sobre os operadores relacionais(uma coisa relacionado a outro, em matematica,um numero relacionado ao outro)
#== igual; =! diferente;> maior;>= maior igual,;<menor;=< menor igual. 


#operadores lógicos: LEMBRAR DAS AULAS DO GUANABARA; SAO ELES: AND(E) OR(OU)  NOT/IS NOT(NÃO É)




#em seguida vimos as condicionais:
#if else elif: basicamente é mas, se, e se. a estrutura é mais ou menos assim:


#carro = " fiat "
#moto= "piloto moto"
#outras_marcas_de_carro= "volvo"; "mercedes" ; "lefan"

#modelo= input(" qual o modelo do seu  carro ?")
#if modelo.lower()is not carro:
 #   print("parabens pelo carro")
#elif modelo.lower is outras_marcas_de_carro:
#    print ( "esse carro n presta")
#else:
 #   print("eu não tenho carro")    

#CARRO = "fiat"
#MOTO_OU_BIKE =["bike","moto"]
#MODELOS_DE_CARROS = ["renalt","pegout","chevrolert"]

#seu_carro= input("qual o modelo do seu carro ?")
#if seu_carro.lower() == CARRO:
 #   print("parabens pelo seu carro")
#elif seu_carro.lower() in MODELOS_DE_CARROS:
 #   print("ta na hora de melhorar seu carro. ")
#else:
 #   print ("acho que vc n anda de carro")



#vale mais uma vez ressaltar que o python é uma linguagem de programacao que se basei em indentacao ou seja, os espacos. E como que se fosse uma questao de pertencimento; ela se inicia com os dois pontos. 

#outro modo de condicional em si e o TERNARIO. o ternario basicamente e uma forma de concatenar, de resumir varias linhas de codigo em uma unica visando deixar o codigo mais clean e eficiente.
#ex:

#maior_de_idade= 18
#idade = int(input("digite uma idade"))
#print("é maior"if idade >= maior_de_idade else "é menor") repare bem nessa linha, bem clean e, atente-se a juncao de varios codigos na mesma linha.


#amanha switch case



#exercicio 1
# adivnha= int(input("digite um numero inteiro positivo:"))
# n= adivnha + 1
# print((f"somando 1 ao seu numero escolhido teremos {n} como resposta" )) obs para comentar mais rapido ctrl k e depois ctrl c 

# exercicio 2
# n=int(input("digite um numero de 0 a 9 que em sequencia lhe direi sua tabuada :"))

# for fator in range(0,11):
    # print(f"{n} x {fator} = {n * fator}")

# exercico 3 verificador de numeros primos

# n_primo = int(input("me fale um numero e direi se ele é primo ou nao "))
# if n_primo >1:
    # for n in range (2,n_primo):
        # if n_primo % n == 0:
            # print("n e primo")
            # break
    # else:
        # print("primo")
# else:
    # print("primo")

#vale ressaltar que esse problema a parte mais dificl foi a logica de programacao
#explicando um pouco mais sobre o que foi feito nesse exercicio:
#n primo sao aqueles que so se dividem por 1 e por ele mesmo. dito isto, usando as ferramentas de looping e de condicionais nos tivemos a seguinte disposicao:
#se o n primo(input) for maior que 1, ou seja, aqui estamos apenas chamando o input para que em seguida criarmos o looping for.
#o for compreende 2 e a classe n_primo. pq dois? pq se ele for divido por 2 e o seu resto da divisao for 0 significa que ele foi divido por mais numeros alem do 1 e ele mesmo.
#em seguida dizemos que se a divisao do n_primo pela minha class criada para o looping for 0, logo ele n é primo, pela logica acima explicada. E a parte principal do desse codigo o BREAK, pois n se esqueca que estamos trabalhando com loopins. Se n der o break ele continuara "trabalhando"

#já, else, caso contrario, else, ele primo pois a divisao n der zero, significa que ele so pode ser divido por 1 e por ele mesmo. E por fim fechar o ultimo else com o nao e primo pois anteriormente demos break no looping e caso queira que ele retorne a resposta sera necessario escrever fora do looping


# exercio da pos - lista de nomes 

# a=[]
# b= 1
# while b <=3:
    #  a.append (input("digite o nome do aluno "))
    #  b=b+1   #isso é um exemplo simples de encremento para cessar o while
    
# print(a)


#exercicio proposto

# Aluno = []
# Matricola = []
# Nota = []

# nome_do_aluno= input(" Insira o nome do aluno: ")

# matricula_do_aluno = input(" insira a maticola do aluno ")

# nota_do_aluno = float(input("insira a nota do aluno "))

# Aluno.append(nome_do_aluno)
# Matricola.append(matricula_do_aluno)
# Nota.append(nota_do_aluno)

# for nome_do_aluno in Aluno:
    # print(nome_do_aluno)

# for matricula_do_aluno in Matricola:
    # print(matricula_do_aluno)

# for nota_do_aluno in Nota:
    # print(nota_do_aluno)

# if nota_do_aluno >= 6:
    # Email= input(" Insira o e-mail do aluno: ")
    # Cpf = input(" insira o cpf do aluno: ")
    # print (f"parabens! voce recebera o diploma com seus seguintes dados,{nome_do_aluno},{Email} , {Cpf} . Em caso de divergencia de dados, favor entrar em contato com a coordenação do seu curso ")
# elif nota_do_aluno <= 6:
    # print(" infelizmente voce não atingiu o resultado necessario, sera preciso a realização de uma nova prova")
# else:
    # ()
  
# def soma ():
    # Txt = "primeira função def"
    # return Txt
# print (soma())

#primeiros passos no def

 # Codigo_dos_Produtos = ["AbC123", "bca123","CAb123 "," BaC123 "]


# def reforma (correcao):
   #  correcao_maiuscula = correcao.upper()
   #  correcao_espacos = correcao.strip()
   #  return correcao_maiuscula,correcao_espacos

# codigo_aleatorio = "abc123 "
# pos_reforma = reforma(codigo_aleatorio)

# print(pos_reforma)
 
#  for
# def calculo(a,b):
    #soma = a + b
    #multiplicacao = a * b
    #return soma, multiplicacao

#resultado_soma, resultado_multiplicacao = calculo(5,6)
#print("soma:", resultado_soma)
#print("multiplicação:", resultado_multiplicacao)

# def calcular_media (a,b,c,):
    # média = (a + b + c)/3
    # return média
    
# resultado_media =calcular_media(4,6,8)
# print("o resultado foi", resultado_media)


# Kmaioridade = 18 

# maior_de_idade = 18
# pergunta= int(input(f"qual a sua idade ? "))

# def verificador(stop): # o stop me remeteu ha uma parada de tipo = "parado, identidade"
#    if stop >= 18:
    #   print("maior, entra!") 
    #   return stop
#    elif menor <= 18: #primeira tentativa foi fazendo um else, fica aqui de resguardo que nem sempre if tem elif, tente usar o else direto
    #   print("menor, rala!") SEMPRE TEM QUE RETORNAR, SEMPRE USAR O RETURN
    #   return maior,menor
#    else:
    #   return "menor,não entra!" , stop
   
# pergunta= int(input(f"qual a sua idade ? ")) tinha ficado na duvida se 
# verdade = verificador(pergunta)
# print (verdade)


#FATOR RECURSIVO "NORMAL"
# def FATOR (N):
    # if N == 1:
        # return 1
    # return N * FATOR(N-1)
# print (FATOR(9))
#FATOR RECURSIVO INVERSO    
#def FATORI(N):
 #   if N == 10:
  #      return 10
   # return N * FATORI(N+1)
#print (FATORI(7))

#carnaval foi estudando