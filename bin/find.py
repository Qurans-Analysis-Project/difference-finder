from pathlib import Path
from typing import List
from json import loads, dumps


ARABIC_CONSONANTS = [
    'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق',
    'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي'
]


def write_out(out_dir: Path, obj: dict):
    name1 = str(obj['source1']).partition('.')[0]
    name2 = str(obj['source2']).partition('.')[0]
    out_path = out_dir.joinpath(f'{name1}_vs_{name2}.json')
    out_path.write_text(dumps(obj))

def find_verse_num_of_narration(chapter: dict, word_index: str):
    for verse_num in range( 1, len(chapter['verses'])+1 ):
        low_index, high_index = chapter['verses'][str(verse_num)]['indices']
        if low_index <= word_index <= high_index:
            return verse_num
    return 0 # Not found condition


if __name__ == '__main__':
    # Gather all available narrations from source
    src_path = Path('source')
    assert src_path.exists() and src_path.is_dir()
    out_dir = Path('differences')
    assert out_dir.exists() and out_dir.is_dir()

    all_jsons: List[Path] = []
    all_jsons.extend([x for x in src_path.rglob('*.json')])

    print(f"Found {len(all_jsons)} JSON files.")
    total = 0
    for x in range(len(all_jsons)):
        total+=x
    print(f"There will be {total} contrasts made")

    # keep track of overall differences
    all_narrarations_difference_count = 0

    # Cycle through them
    contrast_count = 0
    for i in range(len(all_jsons)-1):   # -1 don't compare the last one with itself
        for j in range(i+1,len(all_jsons)): # +1 don't compare the first one with itself
            q1 = all_jsons[i] # quran narration 1
            q2 = all_jsons[j] # quran narration 2
            contrast_count += 1
            this_pair_difference_count = 0
            print(f"Progress: {contrast_count} / {total}")
            print(f"Contrasting: {q1.name} vs. {q2.name}")
            
            diffs = {
                'source1': q1.name,
                'source2': q2.name
            }

            js1 = loads(q1.read_text())
            js2 = loads(q2.read_text())
            chs1 = js1['chapters']
            chs2 = js2['chapters']
            
            # if chapter count doesn't match then there's no point in continuing within each chapter.
            # The offset could be totally messed up and every verse will look competely different.
            if len(chs1) != len(chs2):
                diffs['chapter_count_match?'] = False
                diffs['chapter_counts'] = [len(chs1), len(chs2)]
                write_out(out_dir)
                print("WARNING: Number of chapters don't match. Skipping.")
                continue # move to next pair
            diffs['chapter_count_match?'] = True
            diffs['chapter_counts'] = [len(chs1)]
            diffs['chapters'] = {}
            
            # compare each chapter
            for a in range(1, len(chs1)):
                ch1 = chs1[f'{a}']
                ch2 = chs2[f'{a}']
                diffs['chapters'][a] = {}
                diffs['chapters'][a]['diffs'] = []

                # Do chapter names match?
                if ch1['name'] != ch2['name']:
                    diffs['chapters'][a]['name'] = {
                        'match': False,
                        'names': [ch1['name'],ch2['name']]
                        }
                else:
                    diffs['chapters'][a]['name'] = {
                        'match': True,
                        'names': [ch1['name']]
                        }
                
                chtxt1: List[str] = ch1['text'].split(' ')
                chtxt2: List[str] = ch2['text'].split(' ')

                # Compare each word in the chapter
                txt_diffs = []
                for b in range(len(chtxt1)):
                    word1 = chtxt1[b]
                    word2 = chtxt2[b]
                    
                    # If difference found
                    if word1 != word2:
                        all_narrarations_difference_count += 1
                        this_pair_difference_count += 1
                        verse_index_1 = find_verse_num_of_narration(ch1, b)
                        verse_index_2 = find_verse_num_of_narration(ch2, b)

                        txt_diffs.append({
                            'word_index': b,
                            'word1': word1,
                            'word2': word2,
                            'word1_narraration_verse':verse_index_1,
                            'word2_narraration_verse':verse_index_2
                        })
                # Put all differences in the chapter
                diffs['chapters'][a]['diffs'] = txt_diffs

            # Write out this contrast doc to file
            write_out(out_dir, diffs)
            # Notify differences in this pair
            print(f"Differences count in this pair/contrast: {this_pair_difference_count}")
        
    # Print overall metrics
    print(f"Overall difference count: {all_narrarations_difference_count}")

