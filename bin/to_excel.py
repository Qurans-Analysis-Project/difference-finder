from pathlib import Path
import pandas as pd
from typing import List
from json import load


OUTPATH = Path("differences/excel/temp") # Temp gets replaced by call to .withname()


def find_verse_num_of_narration(chapter: dict, word_index: str):
    for verse_num in range( 1, len(chapter['verses'])+1 ):
        low_index, high_index = chapter['verses'][str(verse_num)]['indices']
        if low_index <= word_index <= high_index:
            return verse_num
    return 0 # Not found condition

def find_source_path(name: str, sources: List[Path]) -> Path:
    for src in sources:
        if src.name == name:
            return src
    raise FileNotFoundError("Source JSON file not found")


def write_out(
        outpath: Path,
        fname: str,
        intro: pd.DataFrame,
        resync: pd.DataFrame,
        rasm: pd.DataFrame,
        ijam: pd.DataFrame,
        harakat: pd.DataFrame,
        names: pd.DataFrame,
        word_count: pd.DataFrame,
        verse_count: pd.DataFrame,
        chapter_count: pd.DataFrame
    ) -> None:
    writer = pd.ExcelWriter( outpath.with_name(f"{fname}.xlsx"), engine="xlsxwriter")
    intro.to_excel(writer, sheet_name="Overview")
    resync.to_excel(writer, sheet_name="Resync (Added-Removed words)")
    rasm.to_excel(writer, sheet_name="Rasm")
    ijam.to_excel(writer, sheet_name="Ijam")
    harakat.to_excel(writer, sheet_name="Harakat")
    names.to_excel(writer, sheet_name="Chapter Names")
    word_count.to_excel(writer, sheet_name="Word Count")
    verse_count.to_excel(writer, sheet_name="Verse Count")
    chapter_count.to_excel(writer, sheet_name="Chapter Count")
    writer.close()


if __name__ == '__main__':
    # differences jsons
    diffs_src_path = Path('differences/json')
    assert diffs_src_path.exists() and diffs_src_path.is_dir()
    # output directory
    out_dir = Path('differences/excel/')
    assert out_dir.exists() and out_dir.is_dir()

    all_diffs_jsons: List[Path] = []
    all_diffs_jsons.extend([x for x in diffs_src_path.rglob('*.json')])

    # Calculate total number of contrasts for progress bar
    print(f"Found {len(all_diffs_jsons)} JSON files.")

    current_quran_index = 0
    for js in all_diffs_jsons:
        current_quran_index += 1
        print(f"Working on Quran {current_quran_index} / {len(all_diffs_jsons)}")
        with js.open('rt', encoding='utf-8') as jsf:
            diffs = load(jsf)
        
        # Intro/Overview
        intro_df = pd.DataFrame(columns=['Source 1',
                                      'Source 2',
                                      '# Resync Events (Added/Removed Words)',
                                      '# Rasm Differences',
                                      '# Ijam Differences',
                                      '# Harakat Differences',
                                      '# Chapter Name Differences',
                                      '# Word Count Differences',
                                      '# Verse Count Differences',
                                      '# Chapter Count Differences',
                                      ])
        dat = {
            'Source 1':[diffs["source1"]],
            'Source 2':[diffs["source2"]],
            '# Resync Events (Added/Removed Words)':[diffs["resync_count"]],
            '# Rasm Differences':[diffs["rasm_differences"]],
            '# Ijam Differences':[diffs["ijam_differences"]],
            '# Harakat Differences':[diffs["harakat_differences"]],
            '# Chapter Name Differences':[diffs["chapter_name_differences"]],
            '# Word Count Differences':[diffs["word_count_differences"]],
            '# Verse Count Differences':[diffs["verse_count_differences"]],
            '# Chapter Count Differences':[diffs["chapter_count_differences"]],
        }
        intro_df = intro_df.from_dict(dat)


        # Resync
        resync_df = pd.DataFrame(columns=['Words 1', 'Words 2',
                                          'Word Indices 1', 'Word Indices 2',
                                          'Chapter # 1', 'Chapter # 2'
                                          ])
        rearranged_columns_data = []
        for record in diffs["resync_events"]:
            rearranged_columns_data.append({
                'Words 1': record["words1"],
                'Words 2': record["words2"],
                'Word Indices 1': record["indices1"],
                'Word Indices 2': record["indices2"],
                'Chapter # 1': record["ch_index1"],
                'Chapter # 2': record["ch_index2"],
            })
        resync_df = resync_df.from_records(rearranged_columns_data)
        

        # Rasm
        rasm_df = pd.DataFrame(columns=['Letter 1','Letter 2',
                                        'Word 1', 'Word 2',
                                        'Letter Index 1', 'Letter Index 2',
                                        'Word Index 1', 'Word Index 2',
                                        'Chapter # 1', 'Chapter # 2'
                                        ])
        rearranged_columns_data = []
        for record in diffs["rasm_differences_detail"]:
            rearranged_columns_data.append({
                'Letter 1': record["letter1"],
                'Letter 2': record["letter2"],
                'Word 1': record["word1"],
                'Word 2': record["word2"],
                'Letter Index 1': record["letter_index1"],
                'Letter Index 2': record["letter_index2"],
                'Word Index 1': record["word_index1"],
                'Word Index 2': record["word_index2"],
                'Chapter # 1': record["ch_index1"],
                'Chapter # 2': record["ch_index2"]
            })
        rasm_df = rasm_df.from_records(rearranged_columns_data)
        

        # Ijam
        ijam_df = pd.DataFrame(columns=['Letter 1','Letter 2',
                                        'Word 1', 'Word 2',
                                        'Letter Index 1', 'Letter Index 2',
                                        'Word Index 1', 'Word Index 2',
                                        'Chapter # 1', 'Chapter # 2'
                                        ])
        rearranged_columns_data = []
        for record in diffs["ijam_differences_detail"]:
            rearranged_columns_data.append({
                'Letter 1': record["letter1"],
                'Letter 2': record["letter2"],
                'Word 1': record["word1"],
                'Word 2': record["word2"],
                'Letter Index 1': record["letter_index1"],
                'Letter Index 2': record["letter_index2"],
                'Word Index 1': record["word_index1"],
                'Word Index 2': record["word_index2"],
                'Chapter # 1': record["ch_index1"],
                'Chapter # 2': record["ch_index2"]
            })
        ijam_df = ijam_df.from_records(rearranged_columns_data)


        # Harakat
        harakat_df = pd.DataFrame(columns=['Letter 1','Letter 2',
                                            'Word 1', 'Word 2',
                                            'Letter Index 1', 'Letter Index 2',
                                            'Word Index 1', 'Word Index 2',
                                            'Chapter # 1', 'Chapter # 2'
                                            ])
        rearranged_columns_data = []
        for record in diffs["harakat_differences_detail"]:
            rearranged_columns_data.append({
                'Letter 1': record["letter1"],
                'Letter 2': record["letter2"],
                'Word 1': record["word1"],
                'Word 2': record["word2"],
                'Letter Index 1': record["letter_index1"],
                'Letter Index 2': record["letter_index2"],
                'Word Index 1': record["word_index1"],
                'Word Index 2': record["word_index2"],
                'Chapter # 1': record["ch_index1"],
                'Chapter # 2': record["ch_index2"]
            })
        harakat_df = harakat_df.from_records(rearranged_columns_data)


        # Chapter Name
        chapter_name_df = pd.DataFrame(columns=['Name 1', 'Name 2',
                                                'Chapter # 1', 'Chapter # 2',
                                                ])
        rearranged_columns_data = []
        for record in diffs["chapter_name_differences_detail"]:
            rearranged_columns_data.append({
                'Name 1': record["name1"],
                'Name 2': record["name2"],
                'Chapter # 1': record["ch_index1"],
                'Chapter # 2': record["ch_index2"],
            })
        chapter_name_df = chapter_name_df.from_records(rearranged_columns_data)


        # Word Count Differnces
        word_count_df = pd.DataFrame(columns=['Count 1', ' Count 2',
                                              'Chapter # 1', 'Chapter # 2',
                                              ])
        rearranged_columns_data = []
        for record in diffs["word_count_differences_detail"]:
            rearranged_columns_data.append({
                'Count 1': record["count1"],
                'Count 2': record["count2"],
                'Chapter # 1': record["ch_index1"],
                'Chapter # 2': record["ch_index2"],
            })
        word_count_df = word_count_df.from_records(rearranged_columns_data)


        # Verse Count Differences
        verse_count_df = pd.DataFrame(columns=['Count 1', 'Count 2',
                                                'Chapter Index 1', 'Chapter Index 2'
                                                ])
        rearranged_columns_data = []
        for record in diffs["verse_count_differences_detail"]:
            rearranged_columns_data.append({
                'Count 1': record["count1"],
                'Count 2': record["count2"],
                'Chapter Index 1': record["ch_index1"],
                'Chapter Index 2': record["ch_index2"]
            })
        verse_count_df = verse_count_df.from_records(rearranged_columns_data)


        # Chapter Count Differences
        chapter_count_df = pd.DataFrame(columns=['Count 1', 'Count 2'])
        rearranged_columns_data = []
        for records in diffs["chapter_count_differences_detail"]:
            rearranged_columns_data.append({
                'Count 1': record["count1"],
                'Count 2': record["count2"],
            })
        chapter_count_df = chapter_count_df.from_records(rearranged_columns_data)

        print("Writing out ...")
        write_out(
            outpath=OUTPATH,
            fname=js.name.split('.')[0],
            intro=intro_df,
            resync=resync_df,
            rasm=rasm_df,
            ijam=ijam_df,
            harakat=harakat_df,
            names=chapter_name_df,
            word_count=word_count_df,
            verse_count=verse_count_df,
            chapter_count=chapter_count_df
        )
        print("Complete. Exiting ...")