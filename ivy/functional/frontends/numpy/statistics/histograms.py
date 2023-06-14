import ivy

def digitize(x, bins, right=False):
    if(right): 
        side = 'right'
    else:
        side = 'left'
    return ivy.searchsorted(bins, x, side = side)
    pass