from NKA import formalLanguage, eq, isDKA
import examples.first as first

NKA1 = first.anotherOne()
NKA2 = first.tommy()

#Language1 = formalLanguage(NKA1, 2)

print(eq(NKA1, NKA2, report=True))

#print(isDKA(NKA1))
#print(isDKA(NKA2))
"""
print("Language 1")
for word in Language1:
    print(word)

print("Language 2")
for word in Language2:
    print(word)"""