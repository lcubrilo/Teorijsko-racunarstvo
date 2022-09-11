# Word generation
def generateWords(alphabet, n):
    letters = ""
    for letter in alphabet: letters+=letter
    
    from itertools import product
    return ["".join(item) for item in product(letters, repeat=n)]

# NKA definition
epsilon = "epsilon"
class state:
    def __init__(self, alphabet, acceptable, name):
        global epsilon
        self.transitions = {epsilon:[]}
        for letter in alphabet:
            self.transitions[letter] = []
        self.acceptable = acceptable
        self.name = name
    
    def __str__(self):
        return self.name
    
    def anyBranchEmpty(self):
        for letter in self.transitions:
            if self.transitions[letter] == []:
                return True
        return False

    def addTransitions(self, letters, state2):
        for letter in letters.split(","):
            if not self.addTrans(letter, state2): return False
        
        return True

    def addTrans(self, letter, state2):
        if letter not in self.transitions:
            return False
        self.transitions[letter].append(state2)
        return True
    
    def addTrasition(self, letter, state2):
        if len(letter.split(",")) != 1: return self.addTransitions(letter, state2)
        return self.addTrans(letter, state2)
    
    def passThru(self, input, path):
        #No input
        addToPath = "--> {} --{}".format(self, input[0] if input != "" else "epsilon")
        if input == "": 
            path += addToPath
            if self.acceptable: # We're done, classic situation
                #REMOVING SOME EXTRA STUFF
                indexx = path.rindex('--'); path = path[:indexx]
                return True, path
            elif self.transitions[epsilon] != []: # We're not acceptable, but can teleport thru epsilons
                for state in self.transitions[epsilon]:
                    ret = state.passThru(input[1:], path)
                    if ret[0]: #If any teleport gives good result, we're fine
                        return ret
                return False, path #None of them gave a good result, fail
            else: #There are not epsilons to teleport thru
                return False, path

        # Normal input, go thru first letter, and pass thru rest of the input
        for state in self.transitions[input[0]]:
            ret = state.passThru(input[1:], path+addToPath)
            if ret[0]: #If this path was good for us, great
                return ret
        
        # My input did not work here, maybe I should teleport elsewhere and retry it
        for state in self.transitions[epsilon]:
            ret = state.passThru(input, path + "--> {} --epsilon".format(self))
            if ret[0]: #If any teleport gives good result, we're fine
                return ret

        return False, path + addToPath#No paths were good
    
    def printState(self):
        TF = str(self.acceptable)[0]
        msg = TF + " " + str(self)
        for letter in self.transitions:
            if self.transitions[letter] == []: continue
            msg += "\n\t{}:[".format(letter)
            for state in self.transitions[letter]:
                msg += str(state) + ", "
            msg = msg[:-2] +"]"
        print(msg)

    def couldBeADKAState(self):
        for t in self.transitions:
            if len(self.transitions[t]) != 1:
                return False
        return True

def printAllStates(states):
    print("\n-------------------\nSTATES: ")
    for s in states:
        s.printState()

def checkValidity(start, input, report=False):
    ret = start.passThru(input, "")

    valid = "a valid" if ret[0] else "not a valid"

    if report: print("{} is {} input via path {}".format(input, valid, ret[1]))

    return ret[0]

def eq(NKA1, NKA2, alphabet, report = False, n = 5):
    counterExamples = ""
    for i in range(n):
        for word in generateWords(alphabet, i):
            if checkValidity(NKA1, word) != checkValidity(NKA2, word):
                # Give reports
                counterExamples += "{}, ".format(word)

    if report: print(counterExamples[:-2])
    return counterExamples == ""

def isDKA(A):
    if A.couldBeADKAState() == False: return False

    for t in A.transitions:
        if isDKA(A.transitions[t]) == False:
            return False

    return True

# My example
def oneNKA(printStates = True):    
    # STATES
    global alphabet
    start = state(alphabet, False, "start")
    good = state(alphabet, True, "good")
    nepar = state(alphabet, False, "nepar")
    par = state(alphabet, False, "par")

    states = [start, good, nepar, par]

    #printAllStates(states)

    # TRANSITIONS
    start.addTrasition("1", good) #PRVO MORAM IMATI JEDAN
    #
    good.addTrasition("0,1", nepar)

    good.addTrasition("0", par) #PARNI MORA BITI NULA, neparni sta hoce

    #
    nepar.addTrasition(epsilon, good) #POVRATAK U GOOD
    #
    par.addTrasition(epsilon, good)
    #
    if printStates: printAllStates(states)
    
    return start

def twoNKA(printStates = True):
    # STATES
    global alphabet
    start = state(alphabet, False, "start")
    nepar = state(alphabet, True, "nepar")
    par = state(alphabet, True, "par")

    states = [start, nepar, par]

    #printAllStates(states)

    # TRANSITIONS
    start.addTrasition("1", nepar) #PRVO MORAM IMATI JEDAN
    
    nepar.addTrasition("0", par)

    par.addTrasition("0,1", nepar)
  

    if printStates: printAllStates(states)

    return start

########## MAIN #############

alphabet = ["0", "1"]
NKA1 = oneNKA()
NKA2 = twoNKA()
print(eq(NKA1, NKA2, alphabet, report=True))

print(isDKA(NKA1))
print(isDKA(NKA2))