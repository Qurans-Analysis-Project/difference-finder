'''
arabic-presentation-forms.py
This file includes the groupings of each character based on it's:
isolated, initial, medial, and final forms

Arabic Unicode charts Included:

Arabic Presentation Forms-A: Range: FB50–FDF
Link: https://www.unicode.org/charts/PDF/UFB50.pdf

Arabic Presentation Forms-B: Range:  FE70–FEFF
Link: https://www.unicode.org/charts/PDF/UFE70.pdf

'''

"""
Not when working with this data it is recommended to use a two-step process of taking the 
input character and checking which form it is in within its overall string:
isolated, initial, medial, and final forms
the unicode character with its proper form is then selected.
Theis character is then used to find the same rasm groups
"""

from arabic import *



JOINING_GROUPS = {
    #HAMZA 0621
    'ء': {"isolated":'\uFE80', "initial":None, "medial":None, "final":None},
    # ALEF WITH MADDA ABOVE 0622
    'آ': {"isolated":'\uFE81', "initial":None, "medial":None, "final":'\uFE82'},
    # ALEF WITH HAMZA ABOVE 0623
    'أ': {"isolated":'\uFE83', "initial":None, "medial":None, "final":'\uFE84'},
    # WAW WITH HAMZA ABOVE 0624
    'ؤ': {"isolated":'\uFE85', "initial":None, "medial":None, "final":'\uFE86'},
    # ALEF WITH HAMZA BELOW 0625
    'إ': {"isolated":'\uFE87', "initial":None, "medial":None, "final":'\uFE88'},
    # YEH WITH HAMZA ABOVE 0626
    'ئ': {"isolated":'\uFE89', "initial":'\uFE8B', "medial":'\uFE8C', "final":'\uFE8A'},
    # ALEF 0627
    'ا': {"isolated":'\uFE8D', "initial":None, "medial":None, "final":'\uFE8E'},
    # BEH 0628
    'ب': {"isolated":'\uFE8F', "initial":'\uFE91', "medial":'\uFE92', "final":'\uFE90'},
    # TEH MARBUTA 0629
    'ة': {"isolated":'\uFE93', "initial":None, "medial":None, "final":'\uFE94'},
    # TEH 062A
    'ت': {"isolated":'\uFE95', "initial":'\uFE97', "medial":'\uFE98', "final":'\uFE96'},
    # THEH 062B
    'ث': {"isolated":'\uFE99', "initial":'\uFE9B', "medial":'\uFE9C', "final":'\uFE9A'},
    # JEEM 062C
    'ج': {"isolated":'\uFE9D', "initial":'\uFE9F', "medial":'\uFEA0', "final":'\uFE9E'},
    # HAH 062D
    'ح': {"isolated":'\uFEA1', "initial":'\uFEA3', "medial":'\uFEA4', "final":'\uFEA2'},
    # KHAH 062E
    'خ': {"isolated":'\uFEA5', "initial":'\uFEA7', "medial":'\uFEA8', "final":'\uFEA6'},
    # DAL 062F
    'د': {"isolated":'\uFEA9', "initial":None, "medial":None, "final":'\uFEAA'},
    # THAL 0630
    'ذ': {"isolated":'\uFEAB', "initial":None, "medial":None, "final":'\uFEAC'},
    # REH 0631
    'ر': {"isolated":'\uFEAD', "initial":None, "medial":None, "final":'\uFEAE'},
    # ZAIN 0632
    'ز': {"isolated":'\uFEAF', "initial":None, "medial":None, "final":'\uFEB0'},
    # SEEN 0633
    'س': {"isolated":'\uFEB1', "initial":'\uFEB3', "medial":'\uFEB4', "final":'\uFEB2'},
    # SHEEN 0634
    'ش': {"isolated":'\uFEB5', "initial":'\uFEB7', "medial":'\uFEB8', "final":'\uFEB6'},
    # SAD 0635
    'ص': {"isolated":'\uFEB9', "initial":'\uFEBB', "medial":'\uFEBC', "final":'\uFEBA'},
    # DAD 0636
    'ض': {"isolated":'\uFEBD', "initial":'\uFEBF', "medial":'\uFEC0', "final":'\uFEBE'},
    # TAH 0637
    'ط': {"isolated":'\uFEC1', "initial":'\uFEC3', "medial":'\uFEC4', "final":'\uFEC2'},
    # ZAH 0638
    'ظ': {"isolated":'\uFEC5', "initial":'\uFEC7', "medial":'\uFEC8', "final":'\uFEC6'},
    # AIN 0639
    'ع': {"isolated":'\uFEC9', "initial":'\uFECB', "medial":'\uFECC', "final":'\uFECA'},
    # GHAIN 063A
    'غ': {"isolated":'\uFECD', "initial":'\uFECF', "medial":'\uFED0', "final":'\uFECE'},
    # FEH 0641
    'ف': {"isolated":'\uFED1', "initial":'\uFED3', "medial":'\uFED4', "final":'\uFED2'},
    # QAF 0642
    'ق': {"isolated":'\uFED5', "initial":'\uFED7', "medial":'\uFED8', "final":'\uFED6'},
    # KAF 0643
    'ك': {"isolated":'\uFED9', "initial":'\uFEDB', "medial":'\uFEDC', "final":'\uFEDA'},
    # LAM 0644
    'ل': {"isolated":'\uFEDD', "initial":'\uFEDF', "medial":'\uFEE0', "final":'\uFEDE'},
    # MEEM 0645
    'م': {"isolated":'\uFEE1', "initial":'\uFEE3', "medial":'\uFEE4', "final":'\uFEE2'},
    # NOON 0646
    'ن': {"isolated":'\uFEE5', "initial":'\uFEE7', "medial":'\uFEE8', "final":'\uFEE6'},
    # HEH 0647
    'ه': {"isolated":'\uFEE9', "initial":'\uFEEB', "medial":'\uFEEC', "final":'\uFEEA'},
    # WAW 0648
    'و': {"isolated":'\uFEED', "initial":None, "medial":None, "final":'\uFEEE'},
    # ALEF MAKSURA 0649
    'ى': {"isolated":'\uFEEF', "initial":None, "medial":None, "final":'\uFEF0'},
    # YEH 064A
    'ي': {"isolated":'\uFEF1', "initial":'\uFEF3', "medial":'\uFEF4', "final":'\uFEF2'},
}

# RASM GROUPS
HAMZA = ['\uFE80']
AIN_INITIAL = ['\uFECF','\uFECB']
BEH = ['\uFE8F','\uFE90','\uFE95','\uFE96','\uFE99','\uFE9A']
NOON = ['\uFEE6','\uFEE5']
AIN_ISOLATED = ['\uFECD','\uFECE','\uFEC9','\uFECA']
HAH = ['\uFE9D','\uFE9E','\uFEA1','\uFEA2','\uFEA5','\uFEA6']
VERTICAL_LINE = ['\uFE81','\uFE82','\uFE83','\uFE84','\uFE87','\uFE88','\uFE8D','\uFE8E','\uFEDF','\uFEE0']
DAL_FINAL = ['\uFEAA','\uFEAC']
TWEEZERS = ['\uFE9F','\uFEA0','\uFEA3','\uFEA4','\uFEA7','\uFEA8']
TAH = ['\uFEC1','\uFEC2','\uFEC3','\uFEC4','\uFEC5','\uFEC6','\uFEC7','\uFEC8']
WAW = ['\uFE85','\uFE86','\uFEED','\uFEEE']
QAF_ISOLATED = ['\uFED5','\uFED6']
QAF_INITIAL = ['\uFED3','\uFED7']
FEH_ISOLATED = ['\uFED1','\uFED2']
SEEN_ISOLATED = ['\uFEB1','\uFEB2','\uFEB5','\uFEB6']
SAD_ISOLATED = ['\uFEB9','\uFEBA','\uFEBD','\uFEBE']
SAD_INITIAL = ['\uFEBB','\uFEBC','\uFEBF','\uFEC0']
YEH = ['\uFE89','\uFE8A','\uFEEF','\uFEF0','\uFEF1','\uFEF2']
LAM = ['\uFEDD','\uFEDE']
KAF = ['\uFEDB','\uFEDC']
MEEM_ISOLATED = ['\uFEE1','\uFEE2']
WAVE_RIGHT = ['\uFE8B','\uFE91','\uFE97','\uFE9B','\uFEF3','\uFEE7']
REH = ['\uFEAD','\uFEAE','\uFEAF','\uFEB0']
DAL_ISOLATED = ['\uFEA9','\uFEAB']
HEH_MEDIAL = ['\uFEEC']
KAF_ISOLATED = ['\uFED9']
KAF_FINAL = ['\uFEDA']
WAVE_MIDDLE = ['\uFE8C','\uFE92','\uFE98','\uFE9C','\uFEF4','\uFEE8']
SEEN_MEDIAL = ['\uFEB3','\uFEB4','\uFEB7','\uFEB8']
HEH_ISOLATED = ['\uFEE9','\uFE93']
FEH_MEDIAL = ['\uFED4','\uFED8']
AIN_MEDIAL = ['\uFECC','\uFED0']
MEEM_INITIAL = ['\uFEE3','\uFEE4']
HEH_FINAL = ['\uFEEA','\uFE94']
HEH_INITIAL = ['\uFEEB']


# For each character, lookup its Rasm group
CONTEXTUAL_FORMS_RASM_GROUPS = {

}