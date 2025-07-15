candidate_filename = input()
votes_filename = input()
counter_of_votes = 0
candidates = {-10: ["Jubileu", 0, 0.0]}
counter_of_invalid_votes = 0

def max_candidates_id():
  max_id = -10
  max_id_2  = max_id

  for candidate_id in candidates.keys():
  
    if candidates[candidate_id][2] > candidates[max_id][2]:
      max_id_2 = max_id
      max_id = candidate_id
  
  return [max_id, max_id_2]

with open(candidate_filename, mode="r", encoding="utf-8") as candidates_file:
  document = candidates_file.read().splitlines()

  print("Candidatos:\n")
  for candidate_line in document:
    print(candidate_line)
    [id, name] = candidate_line.split("-")

    candidates[int(id)] = [name, 0, 0.0]
  
  print("\n")
  
with open(votes_filename, mode="r", encoding="utf-8") as votos_file:
  document_votes = votos_file.read().splitlines()

  print("Votos:\n")
  for vote in document_votes:
    counter_of_votes += 1

    print(vote)
    id_of_candidate = -1 if vote == "" else int(vote)
    
    if not(id_of_candidate in candidates):
      counter_of_invalid_votes += 1
    else:
      current_candidate = candidates[id_of_candidate]
      candidates[id_of_candidate][1] += 1
  
  print("\n")

valid_votes = counter_of_votes - counter_of_invalid_votes

print("Votos registrados: %d" % counter_of_votes)
print("Votos validos: %d" % valid_votes)

for candidate in candidates.values():
  votes_of_candidate = candidate[1]

  candidate[2] = votes_of_candidate / valid_votes


[max_id_1, max_id_2] =  max_candidates_id()

if candidates[max_id_1][2] >= 0.5:
   print("Não haverá segundo turno. Candidato eleito: %s (%d)" % (candidates[max_id_1][0], max_id_1))
else:
  print("Haverá segundo turno entre os candidatos: %s (%d) e %s (%d)" % (candidates[max_id_1][0], max_id_1, candidates[max_id_2][0], max_id_2))