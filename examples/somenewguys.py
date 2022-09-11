from NKA import state, epsilon, printAllStates, alphabet

def johnathan(printStates=False):
    # STATES
    global alphabet
    p0 = state(alphabet, True, "p0")
    p1 = state(alphabet, True, "p1")
    p2 = state(alphabet, True, "p2")

    states = [p0, p1, p2]

    #printAllStates(states)

    # TRANSITIONS
    p0.addTrasition("1", p1)
    
    p1.addTrasition("epsilon", p0)
    p1.addTrasition("0", p2)

    p2.addTrasition("epsilon", p0)
    p2.addTrasition("0,1", p1)
    

    if printStates: printAllStates(states)

    return p0

def brock(printStates=False):
    # STATES
    global alphabet
    s = state(alphabet, True, "s")
    p0 = state(alphabet, False, "p0")
    p1 = state(alphabet, True, "p1")
    p2 = state(alphabet, True, "p2")

    states = [s, p0, p1, p2]

    #printAllStates(states)

    # TRANSITIONS
    s.addTrasition("epsilon", p0)

    p0.addTrasition("1", p1)
    
    p1.addTrasition("epsilon", p0)
    p1.addTrasition("0", p2)

    p2.addTrasition("epsilon", p0)
    p2.addTrasition("0,1", p1)
    

    if printStates: printAllStates(states)

    return s