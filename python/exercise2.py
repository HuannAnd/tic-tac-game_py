candidates_id = []
candidates_names = []
counter_of_votes = 0
counter_of_invalid_votes = 0

def will_be_second_round(votes):
  for p in range(len(votes)):
    if p >= 0.5: 
      return False
  
  return True
  
def get_candidate_index_by_id(id):
  for i in range(len(candidates_id)):
    if candidates_id[i] == id:
      return i

  # n achou o candidato
  return -1

with open("candidatos.txt", mode="r", encoding="utf-8") as candidates_file:
  document = candidates_file.readlines()

  for candidate_line in document:
    [id, name] = candidate_line.split("-")

    candidates_id.append(int(id))
    candidates_names.append(name)
  
aux_votes = [0] * len(candidates_names)
with open("votos.txt", mode="r", encoding="utf-8") as votos_file:
  document = candidates_file.readlines()  

  for vote in document:
    id_of_candidate = int(vote) 

    candidate_index = get_candidate_index_by_id(id_of_candidate)

    if candidate_index == -1:
      counter_of_invalid_votes += 1
    else:
      aux_votes[candidate_index] += 1
      counter_of_votes += 1

valid_votes = counter_of_votes - counter_of_invalid_votes

print("Votos registrados: %d" % counter_of_votes)
print("Votos validos: %d" % valid_votes)

# contabilizando os votos 
aux_percentage_votes = [0] * len(aux_votes)

for v in range(len(aux_votes)):
  percentage_vote = v / valid_votes
  aux_percentage_votes.append(percentage_vote)


print("")