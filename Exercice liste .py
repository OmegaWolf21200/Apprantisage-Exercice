
from random import shuffle

chain = input ("Donner une liste de mot sous cette forme mot1/mot2/mot3/mot4 ...")

chain_split = chain.split ("/")

shuffle(chain_split)

world_len = len(chain_split)

if world_len < 10 :
    print (chain_split[0], chain_split[1])
else :
    print (chain_split [world_len -1],chain_split [world_len -2],chain_split [world_len -3])

    
