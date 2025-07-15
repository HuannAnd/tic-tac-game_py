texto_1 = open("text_1.txt", "r")
texto_2 = open("text_2.txt", "r")


def verficar_simetricidade_do_conteudo():
  texto_2_pos = texto_2.tell()
  texto_2.seek(0)
  print(texto_2_pos)

  # for linha1 in texto_1:
  #     print(texto_2.readline(texto_2_pos - 1).strip())
  #     print(linha1.strip())

  #     if texto_2.readline(texto_2_pos).strip() != linha1.strip():
  #       return False
  #     texto_2_pos -= 1
  return False


print( "Texto simetrico" if verficar_simetricidade_do_conteudo() else "Nao sao simetricos")