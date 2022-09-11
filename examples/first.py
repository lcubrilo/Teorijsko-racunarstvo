from NKA import state, epsilon, printAllStates, alphabet

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
    start.addTransition("1", good) #PRVO MORAM IMATI JEDAN
    #
    good.addTransition("0,1", nepar)

    good.addTransition("0", par) #PARNI MORA BITI NULA, neparni sta hoce

    #
    nepar.addTransition(epsilon, good) #POVRATAK U GOOD
    #
    par.addTransition(epsilon, good)
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
    start.addTransition("1", nepar) #PRVO MORAM IMATI JEDAN
    
    nepar.addTransition("0", par)

    par.addTransition("0,1", nepar)
  

    if printStates: printAllStates(states)

    return start

def anotherOne(printStates = True):
    # STATES
    global alphabet
    start = state(alphabet, False, "start")
    good1 = state(alphabet, True, "good1")
    good2 = state(alphabet, True, "good2")

    states = [start, good1, good2]

    #printAllStates(states)

    # TRANSITIONS
    start.addTransition("1", start) 
    start.addTransition("0", good1)
    
    good1.addTransition("0", good2)

    good2.addTransition("1", start)
    good2.addTransition("0", good2)
  

    if printStates: printAllStates(states)

    return start

def tommy(printStates = True):
    # STATES
    global alphabet
    q0 = state(alphabet, False, "q0")
    q1 = state(alphabet, False, "q1")
    q2 = state(alphabet, True, "q2")

    states = [q0, q1, q2]

    #printAllStates(states)

    # TRANSITIONS
    q0.addTransition("0", q1) 
    q0.addTransition("0", q2)
    q0.addTransition("1", q0)
    
    
    q1.addTransition("0", q0)
    q1.addTransition("0", q1)
    q1.addTransition("0", q0)
    

    q2.addTransition("0", q2)
    q2.addTransition(epsilon, q1)
    q2.addTransition("0", q0)
  

    if printStates: printAllStates(states)

    return q0

def billy(printStates = True):
    # STATES
    global alphabet
    start = state(alphabet, False, "start")
    step = state(alphabet, False, "step")
    mid = state(alphabet, False, "mid")
    end = state(alphabet, True, "end")

    states = [start, step, mid, end]

    #printAllStates(states)

    # TRANSITIONS
    start.addTransition("0,epsilon", mid) 
    
    start.addTransition("1", step)

    step.addTransition("1", mid)

    mid.addTransition("1", end)
  

    if printStates: printAllStates(states)

    return start