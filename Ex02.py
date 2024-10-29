def converter_minutos_para_horas(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

def converter_horas_para_minutos(horas, minutos):
    return horas * 60 + minutos

minutos = int(input("Digite a quantidade de minutos: "))

horas, minutos_restantes = converter_minutos_para_horas(minutos)
print(f"{minutos} minutos equivalem a {horas} horas e {minutos_restantes} minutos.")

horas_input = int(input("Digite a quantidade de horas: "))
minutos_input = int(input("Digite a quantidade de minutos: "))

minutos_totais = converter_horas_para_minutos(horas_input, minutos_input)
print(f"{horas_input} horas e {minutos_input} minutos equivalem a {minutos_totais} minutos.")
