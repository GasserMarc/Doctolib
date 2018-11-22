import difflib
text1 = open("essai1.rb").readlines()
text2 = open("essai2.rb").readlines()
for line in difflib.unified_diff(text1, text2):
    print (line)

text1 = """The World's Shortest Books:
Human Rights Advances in China
"My Plan to Find the Real Killers" by OJ Simpson
"Strom Thurmond:  Intelligent Quotes"
America's Most Popular Lawyers
Career Opportunities for History Majors
Different Ways to Spell "Bob"
Dr. Kevorkian's Collection of Motivational Speeches
Spotted Owl Recipes by the EPA
The Engineer's Guide to Fashion
Ralph Nader's List of Pleasures
"""
text2 = """The World's Shortest Books:
Human Rights Advances in China
"My Plan to Find the Real Killers" by OJ Simpson
"Strom Thurmond:  Intelligent Quotes"
America's Most Popular Lawyers
Career Opportunities for History Majors
Different Ways to Sell "Bob"
Dr. Kevorkian's Collection of Motivational Speeches
Spotted Owl Recipes by the EPA
The Engineer's Guide to Passion
Ralph Nader's List of Pleasures
"""
# create a list of lines in text1
text1Lines = text1.splitlines(1)
text2Lines = text2.splitlines(1)

diffInstance = difflib.Differ()
diffList = list(diffInstance.compare(text1Lines, text2Lines))
print ('-'*50)
print ("Lines different in text1 from text2:")
for line in diffList:
  if (line[0] == '-'):
    print (line)

def compar(codeinitial,codecompar):
    Code1 = open(codeinitial).readlines()
    Code2 = open(codecompar).readlines()
    for line in difflib.unified_diff(Code1, Code2):
        print (line)

print(compar("EventCandidatA.rb","EventCandidatATest.rb"))

