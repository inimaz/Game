import helpers as h
import numpy as np

n_players=3
world = np.array([[0,1,0],
                  [0,0,2],
                  [0,2,0]])
#world[1] = (0,0,1)
#
#print(world)
A=h.ranking (world,3)
N=h.count_countries(world)
print(N)
print(A)
count_sort_ind = np.argsort(-N[1])
Players=N[0][count_sort_ind]
Countries =N[1][count_sort_ind]
print('Players',Players)
print('Countries',Countries)

n=N[0].size

Ranking=np.zeros((n_players,3))
for i in range(0,n):
    player = Players[i]
    countries = Countries[i]
#Note that in python we start to count from 0. If we want to print Position 1, we have to do i+1
    Ranking[i]=([i+1,player,countries])
    
print ("Ranking 1",Ranking)

for i in range(0,n_players):
    if i not in Players:
        #The last loop ended up in n. This one starts in n+1
        Ranking[n][:]=([n+1,i,0])
        n+=1
Ranking=Ranking.astype(int)

print ("Ranking 2",Ranking)