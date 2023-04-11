from random import randint

def np(pseudo):
    return {'pseudo':pseudo,'des':[],'jetons':0} 

def ades(player):
    for i in range (3):
        n=randint(1,6)
        player['des'].append(n)

def rdes(player):
    while not player['des']==[]:
        for de in player['des']:
            player['des'].remove(de)

def vd(p,p2):
    if sorted(p['des']) > sorted(p2['des']):
        co(p,p2)
    elif sorted(p['des']) < sorted(p2['des']):
        co(p2,p)
    else:
        return False
    
def co(player,player2):
    if sorted(player['des']) == [1,2,4]:
        player2['jetons']+=10
    elif sorted(player['des']) == [1,1,1]:
        player2['jetons']+=7
    elif sorted(player['des']) == [1,1,6] or sorted(player['des']) == [6,6,6]:
        player2['jetons']+=6
    elif sorted(player['des']) == [1,1,5]or sorted(player['des']) == [5,5,5]:
        player2['jetons']+=5
    elif sorted(player['des']) == [1,1,4]or sorted(player['des']) == [4,4,4]:
        player2['jetons']+=4
    elif sorted(player['des']) == [1,1,3]or sorted(player['des']) == [3,3,3]:
        player2['jetons']+=3
    elif sorted(player['des']) == [1,1,2]or sorted(player['des']) == [2,2,2]:
        player2['jetons']+=2
    elif sorted(player['des']) == [1,2,3]or sorted(player['des']) == [2,3,4]or sorted(player['des']) == [3,4,5]or sorted(player['des']) == [4,5,6]:
        player2['jetons']+=2
    else:
        player2['jetons']+=1

def co2(player,player2):
    if sorted(player['des']) == [1,2,4]:
        player2['jetons']+=10
        player['jetons']-=10
    elif sorted(player['des']) == [1,1,1]:
        player2['jetons']+=7
        player['jetons']-=7
    elif sorted(player['des']) == [1,1,6] or sorted(player['des']) == [6,6,6]:
        player2['jetons']+=6
        player['jetons']-=6
    elif sorted(player['des']) == [1,1,5]or sorted(player['des']) == [5,5,5]:
        player2['jetons']+=5
        player['jetons']-=5
    elif sorted(player['des']) == [1,1,4]or sorted(player['des']) == [4,4,4]:
        player2['jetons']+=4
        player['jetons']-=4
    elif sorted(player['des']) == [1,1,3]or sorted(player['des']) == [3,3,3]:
        player2['jetons']+=3
        player['jetons']-=3
    elif sorted(player['des']) == [1,1,2]or sorted(player['des']) == [2,2,2]:
        player2['jetons']+=2
        player['jetons']-=2
    elif sorted(player['des']) == [1,2,3]or sorted(player['des']) == [2,3,4]or sorted(player['des']) == [3,4,5]or sorted(player['des']) == [4,5,6]:
        player2['jetons']+=2
        player['jetons']-=2
    else:
        player2['jetons']+=1
        player['jetons']-=1
    
def c(player):
    t=0
    if sorted(player['des']) == [1,2,4]:
        t+=1
    elif sorted(player['des']) == [1,1,1]:
        t+=2
    elif sorted(player['des']) == [1,1,6] or sorted(player['des']) == [6,6,6]:
        t+=3
    elif sorted(player['des']) == [1,1,5]or sorted(player['des']) == [5,5,5]:
        t+=4
    elif sorted(player['des']) == [1,1,4]or sorted(player['des']) == [4,4,4]:
        t+=5
    elif sorted(player['des']) == [1,1,3]or sorted(player['des']) == [3,3,3]:
        t+=6
    elif sorted(player['des']) == [1,1,2]or sorted(player['des']) == [2,2,2]:
        t+=7
    elif sorted(player['des']) == [1,2,3]or sorted(player['des']) == [2,3,4]or sorted(player['des']) == [3,4,5]or sorted(player['des']) == [4,5,6]:
        t+=8
    else:
        t+=9
    return t
    
def debut(player1,player2):
    ades(player1)
    
    if sorted (player1['des']) < sorted (player2['des']):
        rdes(player1)
        rdes(player2)
        return 'le joueur 2 commence'
    elif sorted (player1['des']) > sorted (player2['des']):
        rdes(player1)
        rdes(player2)
        return 'le joueur 1 commence'
    else:
        rdes(player1)
        rdes(player2)
        debut(player1,player2)

def ch(player1,player2):
    debut(player1,player2)
    ades(player1)
    ades(player2)
    print (player1['des'])
    print (player2['des'])
    if c(player1)>c(player2):
        co(player2,player1)
    elif c(player1)<c(player2):
        co(player1,player2)
    rdes(player2)
    rdes(player1)
    print (player1['jetons'] , player2['jetons'])
    
def dch(player1,player2):
    ades(player1)
    ades(player2)
    print (player1['des'])
    print (player2['des'])
    if c(player1)>c(player2):
        co2(player2,player1)
    elif c(player1)<c(player2):
        co2(player1,player2)
    rdes(player2)
    rdes(player1)
    print (player1['jetons'] , player2['jetons'])
    
def jeux(player1,player2):
    pot=21
    while not pot<=0:
        ch(player1,player2)
        pot=21-player1['jetons']-player2['jetons']
    while not player1['jetons']<=0 or player2['jetons']<=0:
        dch(player1,player2)
    if player1['jetons']< player2['jetons']:
        return ('le gagnant est',player2['pseudo'])
    else:
        return ('le gagnant est',player1['pseudo'])