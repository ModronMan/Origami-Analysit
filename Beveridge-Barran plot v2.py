######################################### IMPORTING MODULES ###########################################################
import matplotlib.pyplot as plt
import pandas as pd
########################################################################################################################
"""DICTIONARY OF PROTEINS"""
#--------------------------------- ORDERED ----------------------------------------------------------------------------#
ORDDICT = {'Melittin':{'mass':2846, 'dCCS' : 61, 'dZ' : 3},
           'Human beta-defensin 2':{'mass' : 4328, 'dCCS': 113, 'dZ': 4},
           'Lymphotactin 1-72':{'mass' : 8111, 'dCCS' : 560, 'dZ': 5},
           'Cytochrome C':{'mass' : 12229, 'dCCS' : 392, 'dZ': 4},
           'Haemoglobin-aplha holo monomer':{'mass' : 15743, 'dCCS' : 493, 'dZ': 4},
           'Ovalbumin reduced conformation 1':{'mass' : 44200, 'dCCS' : 382, 'dZ': 4},
           'Ovalbumin reduced conformation 2':{'mass' : 44200, 'dCCS' : 547, 'dZ': 3},
           'Ovalbumin intact conformation 1':{'mass' : 44287, 'dCCS' : 19, 'dZ': 2},
           'Ovalbumin intact conformation 2':{'mass' : 44287, 'dCCS' : 99, 'dZ': 3},
           'TTR tetramer':{'mass' : 55000, 'dCCS' : 144, 'dZ': 3},
           'Avidin tetramer':{'mass' : 64000, 'dCCS' : 47, 'dZ': 3},
           'BSA conformation 1':{'mass' : 66430, 'dCCS' : 345, 'dZ': 3},
           'BSA conformation 2':{'mass' : 66430, 'dCCS' : 446, 'dZ': 4},
           'Concanavalin A tetramer':{'mass' : 102000, 'dCCS' : 292, 'dZ': 4},
           'SAP Pentamer':{'mass' : 128000, 'dCCS' : 408, 'dZ': 5},
           'Lysozyme':{'mass' : 14314, 'dCCS' : 148, 'dZ': 3},
           'Myoglobin':{'mass': 17567, 'dCCS' : 102, 'dZ': 2},
           'Core UVR8 Monomer':{'mass' : 40150, 'dCCS' : 48, 'dZ': 2},
           'Core UVR8 Dimer':{'mass' : 80300, 'dCCS' : 29, 'dZ': 4},
           'Bovine Pancreatic Trypsin Inhibitor (BPTI)':{'mass' : 6531, 'dCCS' : 107, 'dZ': 2},
           'MtATP-phosphoribosyltransferase (MtATP-PRT) hexamer':{'mass' : 189374, 'dCCS' : 14, 'dZ': 2},
           'Insulin':{'mass' : 5730, 'dCCS' : 274, 'dZ': 3}}
#-------------------------------- DISORDERED --------------------------------------------------------------------------#
DISDICT = {'Ubiquitin denatured':{'mass':8556, 'dCCS' :970, 'dZ':8},
           'Lymphotactin': {'mass':10175, 'dCCS' :928, 'dZ':6},
           'N-terminal p53': {'mass':11162, 'dCCS' :1404, 'dZ':9},
           'alpha-synuclein': {'mass':14460, 'dCCS' :1577, 'dZ':16},
           'N-terminal MDM2': {'mass':14790, 'dCCS' :1489, 'dZ':11},
           'Haemoglobin-alpha apo monomer': {'mass':15126, 'dCCS' :2117, 'dZ':16},
           'Haemoglobin-beta apo monomer': {'mass':15867, 'dCCS' :1161, 'dZ':10},
           'beta-casein': {'mass':23944, 'dCCS' :4069, 'dZ':20},
           'p53 DNA binding domain': {'mass':24615, 'dCCS' :1609, 'dZ':9},
           'p53 DNA binding domain pH 1.5': {'mass':24615, 'dCCS' :4000, 'dZ':25},
           'Apolipoprotein C-II (ApoC-II)': {'mass':8959, 'dCCS' :542, 'dZ':3}}
#--------------------------------- NEW GUYS  --------------------------------------------------------------------------#
UNKDICT = {}
########################################################################################################################
"""GENERATE DATA SETS FOR PLOT FROM DICTIONARY"""
########################################################################################################################
"""MASS DATA SET"""
def mass_set(DICT):
    mass = []
    for i in DICT:
        mass.append(DICT[i]['mass'])
    return mass
########################################################################################################################
"""dCCS DATA SET"""
def ccs_set(DICT):
    ccs = []
    for i in DICT:
        ccs.append(DICT[i]['dCCS'])
    return ccs
########################################################################################################################
"""dZ DATA SET"""
def z_set(DICT):
    z = []
    for i in DICT:
        z.append(DICT[i]['dZ'])
    return z
########################################################################################################################
"""NAME DATA SET"""
def name_set(DICT1, DICT2):
    name = []
    for key in DICT1:
        name.append(key)
    for key in DICT2:
        name.append(key)
    return name
########################################################################################################################
"""PLOT MASS VS. dZ"""
def plot_Z(DICT1, DICT2):
    names = name_set(DICT1, DICT2)
    ################################################################################
    Ord_mass = mass_set(DICT1)
    Ord_z = z_set(DICT1)
    ################################################################################
    Dis_mass = mass_set(DICT2)
    Dis_z = z_set(DICT2)
    ################################################################################
    ################################################################################
    fig1, ax = plt.subplots()
    sc1 = plt.scatter(Ord_mass, Ord_z, color='g')
    annot1 = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                         bbox=dict(boxstyle="round", fc="w"),
                         arrowprops=dict(arrowstyle="->"))
    sc2 = plt.scatter(Dis_mass, Dis_z, color='b')
    annot2 = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                         bbox=dict(boxstyle="round", fc="w"),
                         arrowprops=dict(arrowstyle="->"))
    annot1.set_visible(False)
    annot2.set_visible(False)
    ################################################################################
    ################# GENERATING POP-UP LABELS FOR DATA POINTS #####################
    def update_annot1(ind):
        pos = sc1.get_offsets()[ind["ind"][0]]
        annot1.xy = pos
        text = "{}".format(" ".join([names[n] for n in ind["ind"]]))
        annot1.set_text(text)
        annot1.get_bbox_patch().set_alpha(0.4)
    ################################################################################
    def hover(event):
        vis = annot1.get_visible()
        if event.inaxes == ax:
            cont, ind = sc1.contains(event)
            if cont:
                update_annot1(ind)
                annot1.set_visible(True)
                fig1.canvas.draw_idle()
            else:
                if vis:
                    annot1.set_visible(False)
                    fig1.canvas.draw_idle()
    #################################################################################
    fig1.canvas.mpl_connect("motion_notify_event", hover)
    #################################################################################
    def update_annot2(ind):
        pos = sc2.get_offsets()[ind["ind"][0]]
        annot2.xy = pos
        text = "{}".format(" ".join([names[n] for n in ind["ind"]]))
        annot2.set_text(text)
        annot2.get_bbox_patch().set_alpha(0.4)
    #################################################################################
    def hover(event):
        vis = annot2.get_visible()
        if event.inaxes == ax:
            cont, ind = sc2.contains(event)
            if cont:
                update_annot2(ind)
                annot2.set_visible(True)
                fig1.canvas.draw_idle()
            else:
                if vis:
                    annot2.set_visible(False)
                    fig1.canvas.draw_idle()
    ##################################################################################
    fig1.canvas.mpl_connect("motion_notify_event", hover)
    ##################################################################################
    ################################## PLOT GRAPH ####################################
    plt.title('Molecular Weight vs. \u0394Z')
    plt.ylabel('\u0394Z')
    plt.xlabel('Molecular Weight/Da')
    plt.show()
########################################################################################################################
"""PLOT MASS VS. dCCS"""
def plot_CCS(DICT1, DICT2):
    names = name_set(DICT1, DICT2)
    ################################################################################
    Ord_mass = mass_set(DICT1)
    Ord_ccs = ccs_set(DICT1)
    ################################################################################
    Dis_mass = mass_set(DICT2)
    Dis_ccs = ccs_set(DICT2)
    ################################################################################
    ################################################################################
    fig1, ax = plt.subplots()
    sc1 = plt.scatter(Ord_mass, Ord_ccs, color='g')
    annot1 = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                         bbox=dict(boxstyle="round", fc="w"),
                         arrowprops=dict(arrowstyle="->"))
    sc2 = plt.scatter(Dis_mass, Dis_ccs, color='b')
    annot2 = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                         bbox=dict(boxstyle="round", fc="w"),
                         arrowprops=dict(arrowstyle="->"))
    annot1.set_visible(False)
    annot2.set_visible(False)

    ################################################################################
    ################# GENERATING POP-UP LABELS FOR DATA POINTS #####################
    def update_annot1(ind):
        pos = sc1.get_offsets()[ind["ind"][0]]
        annot1.xy = pos
        text = "{}".format(" ".join([names[n] for n in ind["ind"]]))
        annot1.set_text(text)
        annot1.get_bbox_patch().set_alpha(0.4)

    ################################################################################
    def hover(event):
        vis = annot1.get_visible()
        if event.inaxes == ax:
            cont, ind = sc1.contains(event)
            if cont:
                update_annot1(ind)
                annot1.set_visible(True)
                fig1.canvas.draw_idle()
            else:
                if vis:
                    annot1.set_visible(False)
                    fig1.canvas.draw_idle()

    #################################################################################
    fig1.canvas.mpl_connect("motion_notify_event", hover)

    #################################################################################
    def update_annot2(ind):
        pos = sc2.get_offsets()[ind["ind"][0]]
        annot2.xy = pos
        text = "{}".format(" ".join([names[n] for n in ind["ind"]]))
        annot2.set_text(text)
        annot2.get_bbox_patch().set_alpha(0.4)

    #################################################################################
    def hover(event):
        vis = annot2.get_visible()
        if event.inaxes == ax:
            cont, ind = sc2.contains(event)
            if cont:
                update_annot2(ind)
                annot2.set_visible(True)
                fig1.canvas.draw_idle()
            else:
                if vis:
                    annot2.set_visible(False)
                    fig1.canvas.draw_idle()

    ##################################################################################
    fig1.canvas.mpl_connect("motion_notify_event", hover)
    ##################################################################################
    ################################## PLOT GRAPH ####################################
    plt.title('Molecular Weight vs. \u0394CCS')
    plt.ylabel('\u0394CCS')
    plt.xlabel('Molecular Weight/Da')
    plt.show()
########################################################################################################################
plot_CCS(ORDDICT, DISDICT)
plot_Z(ORDDICT, DISDICT)
########################################################################################################################

########################################################################################################################
#######################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
