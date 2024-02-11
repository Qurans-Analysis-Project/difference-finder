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
    # Arabic Presentation Forms-A
    # ALEF 0671
    'ٱ': {"isolated":'\uFB50', "initial":None, "medial":None, "final":'\uFB51'},
    # BEEH 067B
    'ﭒ': {"isolated":'\uFB52', "initial":'\uFB54', "medial":'\uFB55', "final":'\uFB53'},
    # PEH 067E
    'پ': {"isolated":'\uFB56', "initial":'\uFB58', "medial":'\uFB59', "final":'\uFB57'},
    # BEHEH 0680
    'ڀ': {"isolated":'\uFB5A', "initial":'\uFB5C', "medial":'\uFB5D', "final":'\uFB5B'},
    # TTEHEH 067A
    'ﭞ': {"isolated":'\uFB5E', "initial":'\uFB60', "medial":'\uFB61', "final":'\uFB5F'},
    # TEHEH 067F
    'ٿ': {"isolated":'\uFB62', "initial":'\uFB64', "medial":'\uFB65', "final":'\uFB63'},
    # TTEH 0679
    'ٹ': {"isolated":'\uFB66', "initial":'\uFB68', "medial":'\uFB69', "final":'\uFB67'},
    # VEH 06A4
    'ڤ': {"isolated":'\uFB6A', "initial":'\uFB6C', "medial":'\uFB6D', "final":'\uFB6B'},
    # PEHEH 06A6
    'ﭮ': {"isolated":'\uFB6E', "initial":'\uFB70', "medial":'\uFB71', "final":'\uFB6F'},
    # DYEH 0684
    'ﭲ': {"isolated":'\uFB72', "initial":'\uFB74', "medial":'\uFB75', "final":'\uFB73'},
    # NYEH 0683
    'ڃ': {"isolated":'\uFB76', "initial":'\uFB78', "medial":'\uFB79', "final":'\uFB77'},
    # TCHEH 0686
    'چ': {"isolated":'\uFB7A', "initial":'\uFB7C', "medial":'\uFB7D', "final":'\uFB7B'},
    # TCHEHEH 0687
    'ﭾ': {"isolated":'\uFB7E', "initial":'\uFB80', "medial":'\uFB81', "final":'\uFB7F'},
    # DDAHAL 068D
    'ڍ': {"isolated":'\uFB82', "initial":None, "medial":None, "final":'\uFB83'},
    # DAHAL 068C
    'ڌ': {"isolated":'\uFB84', "initial":None, "medial":None, "final":'\uFB85'},
    # DUL 068E
    'ڎ': {"isolated":'\uFB86', "initial":None, "medial":None, "final":'\uFB87'},
    # DDAL 0688
    'ﮈ': {"isolated":'\uFB88', "initial":None, "medial":None, "final":'\uFB89'},
    # JEH 0698
    'ﮊ': {"isolated":'\uFB8A', "initial":None, "medial":None, "final":'\uFB8B'},
    # RREH 0691
    'ﮌ': {"isolated":'\uFB8C', "initial":None, "medial":None, "final":'\uFB8D'},
    # KEHEH 06A9
    'ک': {"isolated":'\uFB8E', "initial":'\uFB90', "medial":'\uFB91', "final":'\uFB8F'},
    # GAF 06AF
    'ﮒ': {"isolated":'\uFB92', "initial":'\uFB94', "medial":'\uFB95', "final":'\uFB93'},
    # GUEH 06B3
    'ڳ': {"isolated":'\uFB96', "initial":'\uFB98', "medial":'\uFB99', "final":'\uFB97'},
    # NGOEH 06B1
    'ڱ': {"isolated":'\uFB9A', "initial":'\uFB9C', "medial":'\uFB9D', "final":'\uFB9B'},
    # NOON GHUNNA 06BA
    'ں': {"isolated":'\uFB9E', "initial":None, "medial":None, "final":'\uFB9F'},
    # RNOON 06BB
    'ﮠ': {"isolated":'\uFBA0', "initial":'\uFBA2', "medial":'\uFBA3', "final":'\uFBA1'},
    # HEH WITH YEH ABOVE 06C0
    'ۀ': {"isolated":'\uFBA4', "initial":None, "medial":None, "final":'\uFBA5'},
    # HEH GOAL 06C1
    'ہ': {"isolated":'\uFBA6', "initial":'\uFBA8', "medial":'\uFBA9', "final":'\uFBA7'},
    # HEH DOACHASHMEE 06BE
    'ھ': {"isolated":'\uFBAA', "initial":'\uFBAC', "medial":'\uFBAD', "final":'\uFBAB'},
    #  YEH BARREE 06D2
    'ﮮ': {"isolated":'\uFBAE', "initial":None, "medial":None, "final":'\uFBAF'},
    # YEH BARREE WITH HAMZA ABOVE 06D3
    'ۓ': {"isolated":'\uFBB0', "initial":None, "medial":None, "final":'\uFBB1'},
    # NG 06AD
    'ڭ': {"isolated":'\uFBD3', "initial":'\uFBD5', "medial":'\uFBD6', "final":'\uFBD4'},
    # U 06C7
    'ۇ': {"isolated":'\uFBD7', "initial":None, "medial":None, "final":'\uFBD8'},
    # OE 06C6
    'ۆ': {"isolated":'\uFBD9', "initial":None, "medial":None, "final":'\uFBDA'},
    # YU 06C8
    'ﯛ': {"isolated":'\uFBDB', "initial":None, "medial":None, "final":'\uFBDC'},
    # U WITH HAMZA ABOVE 0677
    'ٷ': {"isolated":'\uFBDD', "initial":None, "medial":None, "final":None},
    # VE 06CB
    'ۋ': {"isolated":'\uFBDE', "initial":None, "medial":None, "final":'\uFBDF'},
    # KIRGHIZ OE 06C5
    'ﯠ': {"isolated":'\uFBE0', "initial":None, "medial":None, "final":'\uFBE1'},
    # KIRGHIZ YU 06C9
    'ۉ': {"isolated":'\uFBE2', "initial":None, "medial":None, "final":'\uFBE3'},
    # E 06D0
    'ې': {"isolated":'\uFBE4', "initial":'\uFBE6', "medial":'\uFBE7', "final":'\uFBE5'},
    # UIGHUR KAZAKH KIRGHIZ ALEF MAKSURA 0649
    'ﻯ': {"isolated":None, "initial":'\uFBE8', "medial":'\uFBE9', "final":None},

    # Arabic Presentation Forms-B
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
# Column 1
HAMZA = ['\uFE80']
AIN_INITIAL = ['\uFECF','\uFECB']
BEH = ['\uFE8F','\uFE90','\uFE95','\uFE96','\uFE99','\uFE9A','\uFB52','\uFB53','\uFB56','\uFB57',
    '\uFB5A','\uFB5B','\uFB5E','\uFB5F','\uFB62','\uFB63','\uFB66','\uFB67']
NOON = ['\uFEE6','\uFEE5','\uFB9E','\uFB9F','\uFBA0','\uFBA1']
AIN_ISOLATED = ['\uFECD','\uFECE','\uFEC9','\uFECA']
HAH = ['\uFE9D','\uFE9E','\uFEA1','\uFEA2','\uFEA5','\uFEA6','\uFB72','\uFB73','\uFB76','\uFB77',
    '\uFB7A','\uFB7B','\uFB7E','\uFB7F']
# Column 2
VERTICAL_LINE = ['\uFE81','\uFE82','\uFE83','\uFE84','\uFE87','\uFE88','\uFE8D','\uFE8E','\uFEDF',
    '\uFEE0','\uFB50','\uFB51']
DAL_FINAL = ['\uFEAA','\uFEAC','\uFB83','\uFB85','\uFB87','\uFB89']
TWEEZERS = ['\uFE9F','\uFEA0','\uFEA3','\uFEA4','\uFEA7','\uFEA8','\uFB74','\uFB75','\uFB78',
    '\uFB79','\uFB7C','\uFB7D','\uFB80','\uFB81']
TAH = ['\uFEC1','\uFEC2','\uFEC3','\uFEC4','\uFEC5','\uFEC6','\uFEC7','\uFEC8']
# Column 3
WAW = ['\uFE85','\uFE86','\uFEED','\uFEEE','\uFBD7','\uFBD8','\uFBD9','\uFBDA','\uFBDB','\uFBDC',
    '\uFBDD','\uFBDE','\uFBDF','\uFBE0','\uFBE1','\uFBE2','\uFBE3']
QAF_ISOLATED = ['\uFED5','\uFED6']
FEH_ISOLATED = ['\uFED1','\uFED2','\uFB6A','\uFB6B','\uFB6E','\uFB6F']
QAF_INITIAL = ['\uFED3','\uFED7','\uFB70','\uFB6C']
QAF_MEDIAL = ['\uFED4','\uFED8','\uFB6D','\uFB71']
MEEM_INITIAL = ['\uFEE3','\uFEE4']
AIN_MEDIAL = ['\uFECC','\uFED0']
HEH_ISOLATED = ['\uFEE9','\uFE93','\uFBA4','\uFBA6']
# Column 4
YEH = ['\uFE89','\uFE8A','\uFEEF','\uFEF0','\uFEF1','\uFEF2','\uFBE4','\uFBE5']
LAM = ['\uFEDD','\uFEDE']
KAF = ['\uFEDB','\uFEDC','\uFBD5','\uFBD6','\uFB8E','\uFB8F','\uFB90','\uFB91','\uFB92','\uFB93',
    '\uFB94','\uFB95','\uFB96','\uFB97','\uFB98','\uFB99','\uFB9A','\uFB9B','\uFB9C','\uFB9D']
MEEM_ISOLATED = ['\uFEE1','\uFEE2']
SEEN_ISOLATED = ['\uFEB1','\uFEB2','\uFEB5','\uFEB6']
SAD_ISOLATED = ['\uFEB9','\uFEBA','\uFEBD','\uFEBE']
SAD_INITIAL = ['\uFEBB','\uFEBC','\uFEBF','\uFEC0']
# Column 5
WAVE_RIGHT = ['\uFE8B','\uFE91','\uFE97','\uFE9B','\uFEF3','\uFEE7','\uFB54','\uFB58','\uFB5C',
    '\uFB60','\uFB64','\uFB68','\uFBE6','\uFBE8','\uFBA2']
REH = ['\uFEAD','\uFEAE','\uFEAF','\uFEB0','\uFB8A','\uFB8B','\uFB8C','\uFB8D']
DAL_ISOLATED = ['\uFEA9','\uFEAB','\uFB82','\uFB84','\uFB86','\uFB88']
KAF_ISOLATED = ['\uFED9','\uFBD3']
KAF_FINAL = ['\uFEDA','\uFBD4']
HEH_MEDIAL = ['\uFEEC']
# Column 6
WAVE_MIDDLE = ['\uFE8C','\uFE92','\uFE98','\uFE9C','\uFEF4','\uFEE8','\uFB55','\uFB59','\uFB5D',
    '\uFB61','\uFB65','\uFB69','\uFBA3','\uFBE7','\uFBE9']
SEEN_MEDIAL = ['\uFEB3','\uFEB4','\uFEB7','\uFEB8']
HEH_FINAL = ['\uFEEA','\uFE94','\uFBA5']
HEH_INITIAL = ['\uFEEB','\uFBAA','\uFBAB','\uFBAC','\uFBAD']
HEH_GOAL_FINAL = ['\uFBA7']
HEH_GOAL_INITIAL = ['\uFBA8']
HEH_GOAL_MEDIAL = ['\uFBA9']
YEH_BARREE = ['\uFBAE','\uFBAF','\uFBB0','\uFBB1']


# For each character, lookup its Rasm group
CONTEXTUAL_FORMS_RASM_GROUPS = {
    
}