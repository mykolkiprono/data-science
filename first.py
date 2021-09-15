import re
text = '''ajkdcbdknskudb jgfmerlbnab.858cb8685vb cl5n76k7Hal44cb 
656-455-847
767.857.564
Hamac;kndcnabc d;baHadlblan; j adjbasjl m x/ jncadjak'''
sentence = 'start a sentence and then bring it to an end'
pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d")
matches = pattern.finditer(text)
for match in matches:
    print(match)

