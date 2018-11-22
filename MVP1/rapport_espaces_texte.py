

def ratio_spaces(code_candidat):
    with open(code_candidat,'r') as code:
        text = code.read()
        n = text.count(' ')
        N = len(text)
        return (n/N)* 100

'''print(ratio_spaces("EventCandidatA.rb"))
print(ratio_spaces("EventCandidateB.rb"))'''
