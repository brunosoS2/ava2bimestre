#Bruno Sousa--
def calculo_imc(imc):
    imc = altura * altura
    resultado = imc / peso

#Mariana Godoy--
def classificar(valor_imc):
    if valor_imc >= 25:
        return "Acima do peso"
    else:
        return "Normal "
#Ana Julia Campos Bazarin--
def gerar_aviso(status):
    if status == "Normmal":
        return "Excelente! Seu imc está na faixa ideal."
    else:
        return "Atenção! Seu imc indica que você está acima do peso ideal."

    #gabriela cristina.s firmiano
    #Entrada de dados-
resultado = calculo_imc(peso,altura)
status = classificar(resultado)
aviso=gerar_viso(status)

print(f"imc:{resultado:.2f}")
print(f"cassificação:{status}")



