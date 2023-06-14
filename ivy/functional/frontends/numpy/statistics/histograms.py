import ivy

def digitize(x, bins, right=False):
    if(right): 
        side = 'left'
    else:
        side = 'right'
    return ivy.searchsorted(bins, x, side = side)
    pass