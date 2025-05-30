def classificador_de_idade():
    print("Classificador de idade.")

    idade = int(input("Digite a idade: "))

    if idade < 13:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"
 
print(classificador_de_idade())