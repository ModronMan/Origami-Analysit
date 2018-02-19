"""THIS PROGRAM CALCULATES THE CCS BOUNDARIES FOR A GIVEN AMINO ACID SEQUENCE"""
import pandas as pd
import math
""""THIS FUNCTION READS A SEQUENCE INPUT FILE AND RETURNS A LIST"""
def get_file(filepath=''):
    headers = ['Sequence']
    data = pd.read_csv(filepath, names=headers)
    sequence = data['Sequence'].tolist()
    return sequence
########################################################################################################################
def get_count():
    sequence = get_file('150AlaSeq.csv')
    AADICT = {'A': {'Residue':71.08, 'Vol':92, 'Count': 0},
              'R': {'Residue':156.19, 'Vol':225, 'Count': 0},
              'N': {'Residue':114.11, 'Vol':135, 'Count': 0},
              'D': {'Residue':115.09, 'Vol':125, 'Count': 0},
              'C': {'Residue':103.15, 'Vol':106, 'Count': 0},
              'E': {'Residue':129.12, 'Vol':155, 'Count': 0},
              'Q': {'Residue':128.13, 'Vol':161, 'Count': 0},
              'G': {'Residue':57.05, 'Vol':66, 'Count': 0},
              'H': {'Residue':137.14, 'Vol':167, 'Count': 0},
              'I': {'Residue':113.16, 'Vol':169, 'Count': 0},
              'L': {'Residue':113.16, 'Vol':168, 'Count': 0},
              'K': {'Residue':128.18, 'Vol':171, 'Count': 0},
              'M': {'Residue':131.20, 'Vol':171, 'Count': 0},
              'F': {'Residue':147.18, 'Vol':203, 'Count': 0},
              'P': {'Residue':97.12, 'Vol':129, 'Count': 0},
              'S': {'Residue':87.08, 'Vol':99, 'Count': 0},
              'T': {'Residue':101.11, 'Vol':122, 'Count': 0},
              'W': {'Residue':186.22, 'Vol':240, 'Count': 0},
              'Y': {'Residue':163.13, 'Vol':203, 'Count': 0},
              'V': {'Residue':99.13, 'Vol':142, 'Count': 0}}
    for i in sequence:
        AADICT[i]['Count'] += 1
    return AADICT
########################################################################################################################
def get_mass():
    AADICT = get_count()
    mass = 0
    for i in AADICT:
        mass += AADICT[i]['Count'] * AADICT[i]['Residue']
    return mass
########################################################################################################################
def get_vol():
    AADICT = get_count()
    total = 0
    for i in AADICT:
        total += AADICT[i]['Count'] * AADICT[i]['Vol']
    return total
########################################################################################################################
def get_span():
    AADICT = get_count()
    span = 0
    for i in AADICT:
        span += AADICT[i]['Count']
    return span
########################################################################################################################
def get_lower():
    mass = get_mass()
    pi = math.pi
    vol = mass/0.904 # where 0.904 is the protein density
    r = ((3 * vol) / (4 * pi)) ** (1 / 3)
    CCS = pi * (r ** 2)
    return CCS
########################################################################################################################
def get_higher():
    span = get_span()
    vol = get_vol()
    pi = math.pi
    total = vol / span
    r = (total / (pi * 3.63)) ** (1 / 2)
    length = 3.63 * span
    CCS = (4 / pi) * r * length + 2 * (r ** 2)
    return CCS
########################################################################################################################
def low_scaling():
    lower = get_lower()
    factor = 1.19
    lower = lower * factor
    return lower
########################################################################################################################
def high_scaling():
    higher = get_higher()
    factor = 1.19
    higher = higher * factor
    return higher
########################################################################################################################
print(low_scaling())




