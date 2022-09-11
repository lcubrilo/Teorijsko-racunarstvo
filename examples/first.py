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
