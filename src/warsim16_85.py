import base64
from Lemon16_85 import *
import os
import math

class save():
    def playerCompile(self, attributes: list) -> bytes:
        ### Atrributes containes in the following order:
        ### Name
        ### Gold
        ### Land
        ### Elites
        ### Soldiers
        ### Peasants
        ### War Info
        ### War info is a list within the list
        ply = '{\n'
        ply += attributes[0] + '\n'
        ply += str(attributes[1]) + '\n'
        ply += str(attributes[2]) + '\n'
        ply += str(attributes[3]) + '\n'
        ply += str(attributes[4]) + '\n'
        ply += str(attributes[5]) + '\n'
        warInf = attributes[6]
        for i in range(len(warInf)):
            ply += str(warInf[i]) + '\n'
        ply += '}\n'
        return Encode(ply)
