from NKA import state, epsilon, printAllStates, alphabet
# 0 (011)* or 1
def bad(printStates=False):
    # STATES
    global alphabet
    p = state(alphabet, False, "p")
    q0 = state(alphabet, False, "q1")
    q1 = state(alphabet, False, "q1")
    q2 = state(alphabet, False, "q2")
    q3 = state(alphabet, False, "q3")
    q4 = state(alphabet, False, "q4")
    q5 = state(alphabet, True, "q5")
    q6 = state(alphabet, False, "q6")
    q7 = state(alphabet, True, "q7")
    s = state(alphabet, True, "s")
    
    states = [p, s, q1, q2, q3, q4, q5, q6, q7]

    #printAllStates(states)

    # TRANSITIONS
    p.addTransition("epsilon", q6)
    p.addTransition("epsilon", q0)
    
    
    q6.addTransition("1", q7)

    q0.addTransition("0", q1)

    q1.addTransition("epsilon", s)

    s.addTransition("epsilon", q2)

    q2.addTransition("0", q3)

    q3.addTransition("1", q4)

    q4.addTransition("1", q5)

    q5.addTransition("epsilon", q2)

    if printStates: printAllStates(states)

    return p

def good(printStates=False):
    global alphabet
    start = state(alphabet, False, "start")
    justone = state(alphabet, True, "justone")
    good = state(alphabet, True, "good")
    step1 = state(alphabet, False, "step1")
    step2 = state(alphabet, False, "step2")

    states = [start, justone, good, step1, step2]

    #printAllStates(states)

    # TRANSITIONS
    start.addTransition("1", justone)
    start.addTransition("0", good)
    good.addTransition("0", step1)
    step1.addTransition("1", step2)
    step2.addTransition("1", good)
    
    if printStates: printAllStates(states)

    return start

def johnathan(printStates=False):
    # STATES
    global alphabet
    p0 = state(alphabet, True, "p0")
    p1 = state(alphabet, True, "p1")
    p2 = state(alphabet, True, "p2")

    states = [p0, p1, p2]

    #printAllStates(states)

    # TRANSITIONS
    p0.addTransition("1", p1)
    
    p1.addTransition("epsilon", p0)
    p1.addTransition("0", p2)

    p2.addTransition("epsilon", p0)
    p2.addTransition("0,1", p1)
    

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
    s.addTransition("epsilon", p0)

    p0.addTransition("1", p1)
    
    p1.addTransition("epsilon", p0)
    p1.addTransition("0", p2)

    p2.addTransition("epsilon", p0)
    p2.addTransition("0,1", p1)
    

    if printStates: printAllStates(states)

    return s