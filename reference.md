### Injesting a new source text
Because the Arabic-Presentation-Forms file contains os many ligatures and I assume [BLAH BLAH BLAH]
By reducing the number of ligatures that need to grouped at a time we hope that grouping mistakes can be avoided and unneccesary work can be avoided.

1. Add the new unicode source file to source.py
2. Run the bin/find-ligatures.py file and find the output for that new unicode file in the tmp/ligatures.json file.
3. Add those specific ligatures into the arabic-presentation-forms.py groups.
