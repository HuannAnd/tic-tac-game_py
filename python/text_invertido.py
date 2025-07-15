nome_do_arquivo = "text_invertido.txt"
texto_input = open("text_invertido_out.txt", "r+")

with open(nome_do_arquivo, "r") as arquivo_bufferizado:
    documento = arquivo_bufferizado.readlines()

    for linha in range(len(documento) - 1, -1, -1):
      linha_str = documento[linha]
      texto_input.write(documento[linha])

print(texto_input.read())
