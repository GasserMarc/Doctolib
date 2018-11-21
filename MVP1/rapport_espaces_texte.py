

def ratio_spaces(Code_candidat):
    with open(Code_candidat,'r') as code:
        text = code.read()
        n = text.count(' ')
        N = len(text)
        return (n/N)* 100

'''print(ratio_spaces("EventCandidatA.rb"))
print(ratio_spaces("EventCandidateB.rb"))'''
