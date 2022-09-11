from NKA import formalLanguage, eq, isDKA, checkValidity
import examples.first as first
import examples.somenewguys as sng

NKA1 = sng.johnathan()
NKA2 = sng.brock()

#Language1 = formalLanguage(NKA1)

print(eq(NKA1, NKA2, report=True))
#print("For johnathan: ", checkValidity(NKA1, "", True))
#print("For brock: ", checkValidity(NKA2, "", True))


#print(isDKA(NKA1))
#print(isDKA(NKA2))

#print("Language 1:\n")
#for word in Language1:
    #print(word)

"""
print("Language 2")
for word in Language2:
    print(word)"""