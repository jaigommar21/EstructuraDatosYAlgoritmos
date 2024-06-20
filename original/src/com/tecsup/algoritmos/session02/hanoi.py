
'''
Created on Mar 11, 2024
@author: jgomezm
'''
# Hanoi Function 
def towersOfHanoi(_nro_disks, _from=1,  _to=3, _tmp=2):
    
    if _nro_disks == 1:
        #print(f"Move disk {nro_disks}, from tower {_from} to tower {_to}")
        print(f"Mover el disco {_nro_disks}, desde la torre {_from} a la torre {_to}")
        return
    
    towersOfHanoi(_nro_disks-1, _from = _from, _to = _tmp, _tmp = _to)
    #print(f"Move disk {nro_disks}, from tower {_from} to tower {_to}")
    print(f"Mover el disco {_nro_disks}, desde la torre {_from} a la torre {_to}")
    towersOfHanoi(_nro_disks-1, _from = _tmp, _to = _to, _tmp = _from)

if __name__ == "__main__":       
       # Execute
       towersOfHanoi(_nro_disks=3) # Define number of disks



       