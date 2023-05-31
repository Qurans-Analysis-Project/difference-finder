from pathlib import Path
from typing import List
from json import loads, dumps


def write_out(out_dir: Path, obj: dict):
    name1 = str(obj['source1']).partition('.')[0]
    name2 = str(obj['source2']).partition('.')[0]
    out_path = out_dir.joinpath(f'{name1}_vs_{name2}.json')
    out_path.write_text(dumps(obj))


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

    # Cycle through them
    contrast_count = 0
    for i in range(len(all_jsons)-1):   # -1 don't compare the last one with itself
        for j in range(i+1,len(all_jsons)): # +1 don't compare the first one with itself
            q1 = all_jsons[i] # quran narration 1
            q2 = all_jsons[j] # quran narration 2
            contrast_count += 1
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
                
                vs1 = ch1['verses']
                vs2 = ch2['verses']
                # Does verse count match?
                if len(vs1) != len(vs2):
                    diffs['chapters'][a]['verse_count_match?'] = False
                    diffs['chapters'][a]['verse_counts'] = [len(vs1), len(vs2)]
                    print(f"WARNING: Number of verses don't match in chapter {a}. Skipping.")
                    continue # Go to next chapter
                diffs['chapters'][a]['verse_count_match?'] = True
                diffs['chapters'][a]['verse_counts'] = [len(vs1)]
                diffs['chapters'][a]['verses'] = {}
                
                for b in range(1, len(vs1)):
                    v1 = vs1[f'{b}']['words']
                    v2 = vs2[f'{b}']['words']
                    diffs['chapters'][a]['verses'][b] = {}

                    # Do number of words match?
                    if len(v1) != len(v2):
                        diffs['chapters'][a]['verses'][b]['word_count_match?'] = False
                        diffs['chapters'][a]['verses'][b]['word_count'] = [len(v1), len(v2)]
                        print(f"WARNING: Number of words don't match in chapter {a} verse {b}. Skipping.")
                        continue # Go to next verse
                    diffs['chapters'][a]['verses'][b]['word_count_match?'] = True
                    diffs['chapters'][a]['verses'][b]['word_count'] = [len(v1)]

                    # Compare words
                    word_diffs = []
                    for c in range(len(v1)):
                        w1 = v1[c]
                        w2 = v2[c]
                        if w1 != w2:
                            word_diffs.append((w1,w2))
                    diffs['chapters'][a]['verses'][b]['diffs'] = word_diffs

            write_out(out_dir, diffs)

