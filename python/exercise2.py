candidates_id = []
candidates_names = []
counter_of_votes = 0
candidates = {}
counter_of_invalid_votes = 0

def get_index_of_max(vector):
  max_index = 0

  for i in range(len(vector)):
    if vector[max] < vector[i]:
      max_index = i
  
  return max_index

def get_candidate_index_by_votes(votes, vote):
  for i in range(len(votes)):
    if votes[i] == vote:
      return i

def will_be_second_round(votes):
  for p in range(len(votes)):
    if votes[p] >= 0.5: 
      return False
  
  return True

def swap(vector, from_index, to_index):
    temp = vector[from_index]
    vector[from_index] = vector[to_index]
    vector[to_index] = temp

def select_smallest(vector, start):
    smallest_index = start

    for i in range(start + 1, len(vector)):
        if vector[i] < vector[smallest_index]:
            smallest_index = i

    return smallest_index

def sort(vector):
    for j in range(len(vector) - 1):
        smallest_index = select_smallest(vector, j)
        swap(vector, smallest_index, j)

def handle_on_second_round(votes):
  votes_copy = votes.copy()
  sort(votes_copy)    
  print(votes_copy)

  if will_be_second_round(votes):
    first_candidate_votes = votes_copy[-1]
    second_candidate_votes = votes_copy[-2]
    print(candidates_names)
    first_candidate_index = get_candidate_index_by_votes(votes_copy, first_candidate_votes)
    print(first_candidate_index)
    second_candidate_index = get_candidate_index_by_votes(votes_copy, second_candidate_votes)
    print(second_candidate_index)
    first_candidate_name = candidates_names[first_candidate_index]
    second_candidate_name = candidates_names[second_candidate_index]
    first_candidate_id = candidates_id[first_candidate_index]
    second_candidate_id = candidates_id[second_candidate_index]

    print("Haverá segundo turno entre os candidatos: %d (%d) e %d (%d" % (first_candidate_name, first_candidate_id, second_candidate_name, second_candidate_id))

  else:
    winner_candidate_votes = votes_copy[-1]
    winner_candidate_index = get_candidate_index_by_votes(winner_candidate_votes)
    winner_candidate_name  = candidates_names[winner_candidate_index]
    winner_candidate_id = candidates_id[winner_candidate_index]

    print("Não haverá segundo turno. Candidato eleito: %d (%d)" % (winner_candidate_name, winner_candidate_id))

def get_candidate_index_by_id(id):
  for i in range(len(candidates_id)):
    if candidates_id[i] == id:
      return i

  # n achou o candidato
  return -1

with open("candidatos.txt", mode="r", encoding="utf-8") as candidates_file:
  document = candidates_file.read().splitlines()

  for candidate_line in document:
    [id, name] = candidate_line.split("-")

    candidates_id.append(int(id))
    candidates_names.append(name)
  
aux_votes = [0] * len(candidates_names)
with open("votos.txt", mode="r", encoding="utf-8") as votos_file:
  document_votes = votos_file.read().splitlines()

  for vote in document_votes:
    counter_of_votes += 1

    if vote == "":
      counter_of_invalid_votes += 1
      continue

    id_of_candidate = int(vote) 

    candidate_index = get_candidate_index_by_id(id_of_candidate)

    if candidate_index == -1:
      counter_of_invalid_votes += 1
    else:
      aux_votes[candidate_index] += 1

valid_votes = counter_of_votes - counter_of_invalid_votes

print("Votos registrados: %d" % counter_of_votes)
print("Votos validos: %d" % valid_votes)

# contabilizando os votos 
aux_percentage_votes = [0] * len(aux_votes)

for v in range(len(aux_votes)):
  percentage_vote = aux_votes[v] / valid_votes
  aux_percentage_votes.append(percentage_vote)

handle_on_second_round(aux_percentage_votes)