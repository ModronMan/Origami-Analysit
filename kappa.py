"""THIS SIMPLE CODE USES THE LOCALCIDER PROGRAM DEVELOPED BY THE LAB OF ROHIT PAPPU AT WASHINGTON UNIVERSITY IN
   ST. LOUIS <http://pappulab.wustl.edu> TO CALCULATE THE KAPPA PARAMETER OF AN AMINO ACID SEQUENCE.
                                 ALL CREDIT GOES TO THEM FOR THIS WORK"""
####-IMPORT MODULES-####################################################################################################
from localcider.sequenceParameters import SequenceParameters
########################################################################################################################
###-FUNCTION-###########################################################################################################
def get_kappa(sequence):
####-CREATE A SEQUENCEOBJECT FROM THE AMINO ACID SEQUENCE-##############################################################
    SeqOb = SequenceParameters(sequence)
####-KAPPA RANGES: 0 < K < 1 --------------- LOW KAPPA:EXTENDED ---- HIGH KAPPA:COMPACTED --------------################
    kappa = SeqOb.get_kappa()
    return kappa
#########################################REFERENCE######################################################################
"""

[1] A. S. Holehouse, R. K. Das, J. N. Ahad, M. O. G. Richardson and R. V Pappu, Biophys. J., 2017, 112, 16–21.

"""
########################################################################################################################
