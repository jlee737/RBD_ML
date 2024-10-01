import numpy as np

def One_Hot(seq_type, sequence):
    encoding = []
    
    AA_dict = {"A":0, "R":1, "N":2, "D":3, "C":4, 
               "E":5, "Q":6, "G":7, "H":8, "I":9, 
               "L":10, "K":11, "M":12, "F":13, "P":14, 
               "S":15, "T":16, "W":17, "Y":18, "V":19}
    
    base_dict = {"A":0, "C":1, "G":2, "T":3}
    
    if seq_type == "Base Pair":
        for base in sequence:
            encode = np.zeros(4)
            encode[base_dict[str(base)]] = 1

            encoding.append(encode)

    elif seq_type == "Amino Acid":
        for base in sequence:
            encode = np.zeros(20)
            encode[AA_dict[str(base)]] = 1

            encoding.append(encode)

    encoding = np.vstack(encoding)

    return encoding
