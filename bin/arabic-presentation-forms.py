'''
arabic-presentation-froms.py
In a previous version it was said stated we do not need to include the Arabic Presentation Forms unicode charts because
"no source text uses a unicode character in their ranges.". The team has decided to include these documents for two reasons:

    1) While this may be true thusfar for the sources from qurancomplex.gov.sa
    This may not always be true for all texts in the future as the team hopes to gather more texts.
    
    2) More importantly we must understand that unicode represents some characters using multiple characters. These are
    called ligatures. What is important to note for this project is ligatures can have the same Rasm when displayed with different
    Ijam and Harakat. So just because two unicode letters don't match another two unicode letters from another text doesn't mean
    when displayed they have a rasm difference. So without including these ligatures to perform checks then we will have many
    false positives in the rasm differences that might should have been Ijam differences or possibly even no difference at all.

Arabic Unicode charts Included:

Arabic Presentation Forms-A: Range: FB50–FDF
Link: https://www.unicode.org/charts/PDF/UFB50.pdf

Arabic Presentation Forms-B: Range:  FE70–FEFF
Link: https://www.unicode.org/charts/PDF/UFE70.pdf

'''

# RASM GROUPS
ARABIC_LIGATURE_YEH_WITH_HAMZA_ABOVE_1 = ['ﯪ','ﯫ']
ARABIC_LIGATURE_YEH_WITH_HAMZA_ABOVE_2 = ['ﯬ','ﯭ']
ARABIC_LIGATURE_YEH_WITH_HAMZA_ABOVE_3 = ['ﯮ','ﯯ','ﯰ','ﯱ','ﯲ','ﯳ','ﯴ','ﯵ']
ARABIC_LIGATURE_YEH_WITH_HAMZA_ABOVE_4 = ['ﯶ','ﯷ','ﯹ','ﯺ']
ARABIC_LIGATURE_YEH_WITH_HAMZA_ABOVE_5 = ['ﯸ','ﯻ']
ARABIC_LETTER_FARSI_YEH_1 = ['ﯼ','ﯽ']
ARABIC_LETTER_FARSI_YEH_2 = ['ﯾ','ﯿ']
ARABIC_LIGATURE_YEH_WITH_HAMZA_ABOVE_7 = ['\uFC03','\uFC04']
ARABIC_LIGATURE_BEH_YEH_WITH_HAMZA_ABOVE_1 = ['\uFC00','\uFC01','\uFC05',
                                          '\uFC06','\uFC07','\uFC0B',
                                          '\uFC0C','\uFC0D','\uFC11']
ARABIC_LIGATURE_BEH_YEH_WITH_HAMZA_ABOVE_2 = ['\uFC02','\uFC08','\uFC0E',
                                              '\uFC12']
ARABIC_LIGATURE_BEH = ['\uFC09','\uFC0A','\uFC0F','\uFC10','\uFC13',
                      '\uFC14']
ARABIC_LIGATURE_JEEM_1 = ['\uFC15','\uFC17','\uFC19','\uFC1A']
ARABIC_LIGATURE_JEEM_2 = ['\uFC16','\uFC18','\uFC1B']
ARABIC_LIGATURE_SEEN_1 = ['\uFC1C','\uFC1D','\uFC1E']
ARABIC_LIGATURE_SEEN_2 = ['\uFC1F']
ARABIC_LIGATURE_SAD_1 = ['\uFC20','\uFC22','\uFC23','\uFC24']
ARABIC_LIGATURE_SAD_2 = ['\uFC21','\uFC25']
ARABIC_LIGATURE_TAH_1 = ['\uFC26']
ARABIC_LIGATURE_TAH_2 = ['\uFC27', '\uFC28']
ARABIC_LIGATURE_AIN_1 = ['\uFC29','\uFC2B']
ARABIC_LIGATURE_AIN_2 = ['\uFC2A','\uFC2C']
ARABIC_LIGATURE_FEH_1 = ['\uFC2D','\uFC2E','\uFC2F','\uFC33']