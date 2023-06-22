from pathlib import Path
from typing import List, Tuple
from json import loads, dump
from difference_models import *
from exceptions import *
from arabic import RASM_GROUP, TATWEEL, ANNOTATION




def write_out(out_dir: Path, obj: DifferenceReport):
    name1 = str(obj.source1).partition('.')[0]
    name2 = str(obj.source2).partition('.')[0]
    out_path = out_dir.joinpath(f'{name1}_vs_{name2}.json')
    with out_path.open('w', encoding='utf-8') as jsf:
        dump(obj, jsf, cls=customJSONEncoder, ensure_ascii=False, indent=4)


def find_verse_num_of_narration(chapter: dict, word_index: str):
    for verse_num in range( 1, len(chapter['verses'])+1 ):
        low_index, high_index = chapter['verses'][str(verse_num)]['indices']
        if low_index <= word_index <= high_index:
            return verse_num
    return 0 # Not found condition

'''
NOTE: A better name might be without_vowels as the intention is to only keep the consonant.
But I've seen some cases where this wouldn't be completely accurate either.
'''
def without_diacritics(word: str) -> str:
    ret = ''
    all_rasm_chars = RASM_GROUP.keys()
    for i in word:
        if (i in all_rasm_chars) or (i==' '):
            ret+=i
    return ret


def equal_rasm(word1: str, word2: str) -> Tuple[ bool, RasmDifference|None ]:
    word1_rasm = without_diacritics(word1)
    word2_rasm = without_diacritics(word2)

    if len(word1_rasm) != len(word2_rasm):
        #print(f"WARNING: equal_rasm length mismatch: word1: {word1} word2: {word2}")
        return (
            False, 
            RasmDifference(
                letter1=None,
                letter_index1=None,
                word1= word1_rasm,
                word_index1=None,
                ch_index1=None,
                letter2=None,
                letter_index2=None,
                word2= word2_rasm,
                word_index2=None,
                ch_index2=None
            )
        )
    # If each character is in the same rasm group as the other character then its a pass
    for i in range(0,len(word1_rasm)):
        if word1_rasm[i] not in RASM_GROUP[word2_rasm[i]]:
            return (
                False, 
                RasmDifference(
                    letter1= word1_rasm[i],
                    letter_index1= i,
                    word1= word1_rasm,
                    word_index1=None,
                    ch_index1=None,
                    letter2= word2_rasm[i],
                    letter_index2= i,
                    word2= word2_rasm,
                    word_index2=None,
                    ch_index2=None
                )
            )
    return (True, None)

'''
Assume the Rasm has already been checked and is equal. Only check if the consonants are different
'''
def equal_ijam(word1: str, word2: str) -> Tuple[ bool, IjamDifference|None ]:
    word1_cons = without_diacritics(word1)
    word2_cons = without_diacritics(word2)
    for i in range(0, len(word1_cons)):
        if word1_cons[i] != word2_cons[i]:
            return (
                False,
                IjamDifference(
                    letter1= word1_cons[i],
                    letter_index1= i,
                    word1= word1,
                    word_index1= None,
                    ch_index1=None,
                    letter2= word2_cons[i],
                    letter_index2= i,
                    word2= word2,
                    word_index2=None,
                    ch_index2=None,
                )
            )
    return (True, None)

'''
Assume the Rasm and Ijam have been checked and are equal. Only check unicode annotations
'''
def equal_harakat(word1: str, word2: str) -> Tuple[ bool, HarakatDifference|None ]:
    # Assuming rasm and ijam are the same then if anything is different then it can only be the harakat
    if word1 != word2:
        return (
            False,
            HarakatDifference(
                letter1=None,
                letter_index1=None,
                word1=word1,
                word_index1=None,
                ch_index1=None,
                letter2=None,
                letter_index2=None,
                word2=word2,
                word_index2=None,
                ch_index2=None,
            )
        )
    else:
        return (True, None)


'''
Need the ability to resync the current word index when comparing two texts because of extra words
I am designing this with variable tolerance for how many inserted/deleted words should be allowed before giving up
Should return the new indices of the closest next two words whose consonants match to pick back up contrasting.
These integers are the next common word positions.
'''
def resync(
            words1: List[str],
            index1: int,
            words2: List[str],
            index2: int,
            tolerance: int = 6
        ) -> Tuple[int, int, ResyncEvent|None]:
    '''
    On rasm difference, find the next common rasm word to resync to.
    The first and second returned ints are the next index1 and index2
    corresponding to the next matching rasm word in both word sequences.
    If extra words are found then ResyncEvent is returned in position 3 (index 2)
    If the very next word has matching rasm then None is returned in position 3 (index 2).
    '''
    
    # if the consonant difference only on this word?
    eq, _ = equal_rasm(words1[index1+1], words2[index2+1])
    if eq:
        return (index1+1, index2+1, None)

    slice1 = words1[ index1 : min(len(words1), index1+tolerance+1) ]
    slice2 = words2[ index2 : min(len(words2), index2+tolerance+1) ]
    
    for floor in range(0, min(len(slice1), len(slice2)) ):
        
        # slice1 perspective, compare to slice2 elements
        for i in range(0, len(slice2)):
            eq, _ = equal_rasm(slice1[floor], slice2[i])
            if eq:
                return (
                    index1+floor,
                    index2+i,
                    ResyncEvent(
                        words1= words1[index1:index1+floor],
                        indices1= (index1,index1+floor),
                        ch_index1=None,     # To be filled out by caller
                        words2= words2[index2:index2+i],
                        indices2=(index2,index2+i),
                        ch_index2= None     # To be filled out by caller
                    )
                )

        # slice2 perspective, compare to slice1 elements
        for i in range(0, len(slice1)):
            eq, _ = equal_rasm(slice2[floor], slice1[i])
            if eq:
                return (
                    index1+i,
                    index2+floor,
                    ResyncEvent(
                        words1= words1[index1:index1+i],
                        indices1= (index1,index1+i),
                        ch_index1=None,     # To be filled out by caller
                        words2= words2[index2:index2+floor],
                        indices2=(index2,index2+floor),
                        ch_index2= None     # To be filled out by caller
                    )
                )
    
    # could not resync
    return (
        min(index1+1, len(words1)-1),
        min(index2+1, len(words2)-1),
        None
    )


def handle_chapter(ch1: dict, ch1_index: int, ch2: dict, ch2_index: int, diffs: DifferenceReport):
    # Do chapter names match?
    if ch1['name'] != ch2['name']:
        # Add chapter name difference
        diffs.chapter_name_differences_detail.append( 
            ChapterNameDifference(
                name1= ch1['name'],
                ch_index1= ch1_index,
                name2= ch2['name'],
                ch_index2= ch2_index,
            )
        )
    
    chtxt1: List[str] = ch1['text'].split(' ')
    chtxt2: List[str] = ch2['text'].split(' ')

    # Do chapter lengths match?
    if len(chtxt1) != len(chtxt2):
        # add Word count difference
        diffs.word_count_differences_detail.append(
            WordCountDifference(
                count1=len(chtxt1),
                ch_index1= ch1_index,
                count2=len(chtxt2),
                ch_index2= ch2_index,
            )
        )

    # Compare each word in the chapter
    b1 = 0
    b2 = 0
    while (b1 < len(chtxt1)) and (b2 < len(chtxt2)):
        # The word to compare
        word1 = chtxt1[b1]
        word2 = chtxt2[b2]
        
        # If difference found
        if word1 != word2:
            # What kind of difference?

            # rasm?
            equal, diff = equal_rasm(word1, word2)
            if not equal:
                diff.word_index1 = b1
                diff.word_index2 = b2
                diff.ch_index1 = ch1_index
                diff.ch_index2 = ch2_index
                diffs.rasm_differences_detail.append(diff)
                
                # Also need to Resync because the Rasm doesn't match
                if b1+1 < len(chtxt1) and b2+1 < len(chtxt2):
                    b1, b2, _resync_event = resync(chtxt1, b1, chtxt2, b2)
                    if _resync_event is not None:
                        _resync_event.ch_index1 = a
                        _resync_event.ch_index2 = a
                        diffs.resync_events.append(_resync_event)
                    # Do not increment b1 & b2 they already found the next match in resync call
                    continue
            
            # ijam?
            equal, diff = equal_ijam(word1, word2)
            if not equal:
                # The ijam doesn't match
                diff.word_index1 = b1
                diff.word_index2 = b2
                diff.ch_index1 = ch1_index
                diff.ch_index2 = ch2_index
                diffs.ijam_differences_detail.append(diff)
            else:
                # harakat?
                equal, diff = equal_harakat(word1, word2)
                if not equal:
                    # The harakat doesn't match
                    diff.word_index1 = b1
                    diff.word_index2 = b2
                    diff.ch_index1 = ch1_index
                    diff.ch_index2 = ch2_index
                    diffs.harakat_differences_detail.append(diff)
                

        # go to next word
        b1+=1
        b2+=1
    # It may be possible some narrations have more words at the end than the other.
    # Make a note of these extra words in a resync event.
    if b1 != len(chtxt1) or b2 != len(chtxt2):
        diffs.resync_events.append(
            ResyncEvent(
                words1= chtxt1[b1:],
                indices1= (b1, len(chtxt1)),
                ch_index1= ch1_index,
                words2= chtxt2[b2:],
                indices2= (b2, len(chtxt2)),
                ch_index2= ch2_index,
            )
        )


if __name__ == '__main__':
    # Gather all available narrations from source
    src_path = Path('source')
    assert src_path.exists() and src_path.is_dir()
    out_dir = Path('differences/json')
    assert out_dir.exists() and out_dir.is_dir()

    all_jsons: List[Path] = []
    all_jsons.extend([x for x in src_path.rglob('*.json')])

    # Calculate total number of contrasts for progress bar
    print(f"Found {len(all_jsons)} JSON files.")
    total = 0
    for x in range(len(all_jsons)):
        total+=x
    print(f"There will be {total} contrasts made")

    # keep track of overall differences for analysis
    all_chapter_count_differences = 0
    all_chapter_name_differences = 0
    all_verse_count_differences = 0
    all_word_count_differences = 0
    all_rasm_differences = 0
    all_ijam_differences = 0
    all_harakat_differences = 0
    all_resync_count = 0


    # Cycle through them
    contrast_count = 0
    for i in range(len(all_jsons)-1):   # -1 don't compare the last one with itself
        for j in range(i+1,len(all_jsons)): # +1 don't compare the first one with itself
            q1 = all_jsons[i] # quran narration 1
            q2 = all_jsons[j] # quran narration 2
            contrast_count += 1
            print(f"Progress: {contrast_count} / {total}")
            print(f"Contrasting: {q1.name} vs. {q2.name}")

            # Differences for this contrast
            diffs = DifferenceReport(
                source1= q1.name,
                source2= q2.name,
                chapter_count_differences= 0,
                chapter_count_differences_detail= [],
                chapter_name_differences= 0,
                chapter_name_differences_detail= [],
                verse_count_differences= 0,
                verse_count_differences_detail= [],
                word_count_differences= 0,
                word_count_differences_detail= [],
                rasm_differences= 0,
                rasm_differences_detail= [],
                ijam_differences= 0,
                ijam_differences_detail= [],
                harakat_differences = 0,
                harakat_differences_detail = [],
                resync_count= 0,
                resync_events= []
            )

            js1 = loads(q1.read_text())
            js2 = loads(q2.read_text())
            chs1 = js1['chapters']
            chs2 = js2['chapters']

            # if chapter count doesn't match then there's no point in continuing within each chapter.
            # The offset could be totally messed up and every verse will look competely different.
            if len(chs1) != len(chs2):
                diffs.chapter_count_differences_detail.append( ChapterCountDifference(len(chs1), len(chs2)) )
                print("WARNING: Number of chapters don't match. Skipping.")
            
            # compare each chapter
            else:
                for a in range(1, len(chs1)):
                    ch1 = chs1[f'{a}']
                    ch2 = chs2[f'{a}']
                    handle_chapter(ch1, a, ch2, a, diffs)
                    


            # update counts in difference report
            diffs.chapter_count_differences= len(diffs.chapter_count_differences_detail)
            diffs.chapter_name_differences= len(diffs.chapter_name_differences_detail)
            diffs.verse_count_differences= len(diffs.verse_count_differences_detail)
            diffs.word_count_differences= len(diffs.word_count_differences_detail)
            diffs.rasm_differences= len(diffs.rasm_differences_detail)
            diffs.ijam_differences= len(diffs.ijam_differences_detail)
            diffs.harakat_differences = len(diffs.harakat_differences_detail)
            diffs.resync_count= len(diffs.resync_events)

            # update overall numbers
            all_chapter_count_differences += diffs.chapter_count_differences
            all_chapter_name_differences += diffs.chapter_name_differences
            all_verse_count_differences += diffs.verse_count_differences
            all_word_count_differences += diffs.word_count_differences
            all_rasm_differences += diffs.rasm_differences
            all_ijam_differences += diffs.ijam_differences
            all_harakat_differences += diffs.harakat_differences
            all_resync_count += diffs.resync_count

            # Write out this contrast doc to file
            write_out(out_dir, diffs)
        
    
    # Print overall metrics
    print('----------------------------------')
    print('----- OVERALL SUMMARY REPORT -----')
    print('----------------------------------')
    print(f"Overall chapter count differences: {all_chapter_count_differences}")
    print(f"Overall chapter name differences: {all_chapter_name_differences}")
    print(f"Overall verse count differences: {all_verse_count_differences}")
    print(f"Overall word count differences: {all_word_count_differences}")
    print(f"Overall rasm differences: {all_rasm_differences}")
    print(f"Overall ijam differences: {all_ijam_differences}")
    print(f"Overall harakat differences: {all_harakat_differences}")
    print(f"Overall resync events: {all_resync_count}")

    # Save summary report
    print("Saving Summary Report ...")
    summary = DifferenceReport(
        source1= 'SUMMARY',
        source2= 'REPORT',
        chapter_count_differences= all_chapter_count_differences,
        chapter_count_differences_detail= [],
        chapter_name_differences= all_chapter_name_differences,
        chapter_name_differences_detail= [],
        verse_count_differences= all_verse_count_differences,
        verse_count_differences_detail= [],
        word_count_differences= all_word_count_differences,
        word_count_differences_detail= [],
        rasm_differences= all_rasm_differences,
        rasm_differences_detail= [],
        ijam_differences= all_ijam_differences,
        ijam_differences_detail= [],
        harakat_differences= all_harakat_differences,
        harakat_differences_detail= [],
        resync_count= all_resync_count,
        resync_events= []
    )
    write_out(out_dir, summary)
    print("Saved. Exiting.")