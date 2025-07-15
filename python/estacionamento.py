N, K = map(int, input().split())
carros = dict()
ordem = []
estacionamento = []

def pegar_carro_tempo(tempo):
  for key in carros.keys():
    if tempo in carros[key]:
      return [key, carros[key]]

def verificar_se_ja_esta_no_estacionamento(carro_key_procurada):
  for i in range(len(estacionamento)):
    if estacionamento[i] == carro_key_procurada:
      return i 
  
  return -1


for i in range(1, N + 1):
  tempo_inicial, tempo_final = map(int, input().split())
  ordem.append(tempo_inicial, tempo_final)
  
  carros[i] = [tempo_inicial, tempo_final]

def verificar_se_e_possivel():
  ordem.sort()

  for tempo in ordem:
    [carro_key] = pegar_carro_tempo(tempo)

    posicao = verificar_se_ja_esta_no_estacionamento(carro_key)
    if posicao == -1:
      estacionamento.append(carro_key)
    else:
      carros_de_tras = estacionamento[posicao:-1]

      if len(carros_de_tras) == 0:
        estacionamento.pop()
      else:
        return False
  
  return True



    
    

