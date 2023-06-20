from enum import Enum
from dataclasses import dataclass, is_dataclass, asdict
from typing import Tuple, List
from json import JSONEncoder


@dataclass
class ChapterCountDifference():
    count1: int
    count2: int

@dataclass
class ChapterNameDifference():
    name1: str
    ch_index1: int
    name2: str
    ch_index2: int

@dataclass
class VerseCountDifference():
    count1: int
    ch_index1: int
    count2: int
    ch_index2: int

@dataclass
# To discover what the additional/removed words were look at the ResyncEvents
class WordCountDifference():
    count1: int
    ch_index1: int
    count2: int
    ch_index2: int


# Script differences. These should be rare.
# NOTE: These are different from extra/fewer words.
# If whole words are discovered added/removed in the texts then those are found in ResyncEvents
@dataclass
class RasmDifference():
    letter1: str|None       # The letter in question without vowel diacritics
    letter_index1: int|None # The index of the letter in question without the vowel diacritics
    word1: str              # The word under contrast without vowel diacritics
    word_index1: int        # the word index in the chapter text
    ch_index1: int          # The chapter number
    letter2: str|None
    letter_index2: int
    word2: str
    word_index2: int
    ch_index2: int

# The dots to clarify consonants. There should be many of these
@dataclass
class IjamDifference():
    letter1: str        # The letter in question without vowel diacritics
    letter_index1: int  # The index of the letter in question without the vowel diacritics
    word1: str          # The word under contrast without vowel diacritics
    word_index1: int    # the word index in the chapter text
    ch_index1: int      # The chapter number
    letter2: str
    letter_index2: int
    word2: str
    word_index2: int
    ch_index2: int

# The marks to clarify vowels. There should be many of these
@dataclass
class HarakatDifference():
    letter1: str        # The letter in question without vowel diacritics
    letter_index1: int  # The index of the letter in question without the vowel diacritics
    word1: str          # The word under contrast without vowel diacritics
    word_index1: int    # the word index in the chapter text
    ch_index1: int      # The chapter number
    letter2: str
    letter_index2: int
    word2: str
    word_index2: int
    ch_index2: int
    
@dataclass
class ResyncEvent():
    words1: str
    indices1: Tuple[int,int]    # The index of the first word in words1 in the chapter text (inclusive) and the final word in words1 of the chapter text (also inclusive)
    ch_index1: int
    words2: str
    indices2: Tuple[int,int]    # The index of the first word in words2 in the chapter text (inclusive) and the final word in words2 of the chapter text (also inclusive)
    ch_index2: int

@dataclass
class DifferenceReport():
    source1: str
    source2: str
    chapter_count_differences: int
    chapter_count_differences_detail: List[ChapterCountDifference]
    chapter_name_differences: int
    chapter_name_differences_detail: List[ChapterNameDifference]
    verse_count_differences: int
    verse_count_differences_detail: List[VerseCountDifference]
    word_count_differences: int
    word_count_differences_detail: List[WordCountDifference]
    rasm_differences: int
    rasm_differences_detail: List[RasmDifference]
    ijam_differences: int
    ijam_differences_detail: List[IjamDifference]
    harakat_differences: int
    harakat_differences_detail: List[HarakatDifference]
    resync_count: int
    resync_events: List[ResyncEvent]


class customJSONEncoder(JSONEncoder):
    def default(self, o):
        if is_dataclass(o):
            return asdict(o)
        return super.default(o)