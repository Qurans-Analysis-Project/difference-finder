# difference-finder
Find the differences between each available pair of narrations.

**Note 1** this code is only capable of finding all arabic textual variants. It is not capable of filtering them down to only differences of meaning. That will need to be done by humans.

**Note 2** As of writing this version is not yet capable of factoring in arabic presentation forms. Meaning Rasm difference counts will contain false positives. Manual review confirms there are still many true rasm differences. A presentation form is when two consecutive letters combine to create a single different letter.The rasm of the new single letter might be the same while having been spelled with differing sets of two consecutive letters.

## source
source contains the quranic narrarations parsed into JSON format from the [textual-conversion repository](https://github.com/Qurans-Analysis-Project/textual-conversion) 

## differences
This directory contains the difference reports in JSON format for each pairing of quranic narrarations as well as a compilation report in XLSX format.

## bin
The script(s) used to contrast the narrations 
