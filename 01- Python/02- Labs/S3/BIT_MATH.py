
def SET_BIT(REG , BITNO ):
    REG = REG | (1<<BITNO)
    return REG

def CLR_BIT(REG , BITNO ):
    REG = REG & ~(1<<BITNO)
    return REG

def GET_BIT(REG , BITNO ):
    REG = 1 & (REG >> BITNO)
    return REG

def TOG_BIT(REG , BITNO ):
    REG ^= (1<<BITNO)
    return REG

