import numpy as np

authors = []
all_files = []
author_flag = 1

for line in open("./author.txt").readlines():

  if not line:
    break

  if line == '\n':
    author_flag = 1
    continue

  line = line.rstrip('\n')

  if author_flag == 1:
    author_flag = 0     
    if line not in authors:
      authors.append(line)
      
  else:
    if line not in all_files:
      all_files.append(line)

authorship = np.zeros((len(authors), len(all_files)))
print(authorship)

author_index = 0
file_index = 0
created_files = []

for line in open("./author.txt").readlines():

  if not line:
    break

  if line == '\n':
    author_flag = 1
    author_index = 0
    continue

  line = line.rstrip('\n')

  if author_flag == 1:
    author_flag = 0    
    author_index = authors.index(line)
      
  else:
    file_index = all_files.index(line)
    if line in created_files:
      created_files.append(line)
      authorship[author_index][file_index] += 0.5
      for i in len(authors):
        if i == author_index or authorship[i][file_index] == 0:
          continue
        else:
          authorship[i][file_index] -= 0.1
    else:
      authorship[author_index][file_index] += 1

author_points = []
author_points = authorship.sum(axis=1)

most_important_authors_index = author_points.argsort()[-10:][::-1]

for i in most_important_authors_index:
  print("Autor: " + authors[i] + "\nPontos: " + str(author_points[i]))
