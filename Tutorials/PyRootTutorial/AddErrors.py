import numbers, array, ROOT

def get_error(e,N):
    if e is None:
        error = ROOT.nullptr
    elif isinstance(e, numbers.Number):
        error = array.array('d',[e]*N)
    else:
        assert len(e) == N
        error = array.array('d',e)
    return error

def AddErrors(g,ex = None,ey = None):
    """Takes a TGraph and turns it into a TGraphErrors with either
    fixed or array errors."""
    N = g.GetN()
    xbuf = g.GetX() # Returns a "read-write buffer" which is a dumb array.
    xbuf.SetSize(N) # So we have to tell it what size it is.
    x = array.array('d',xbuf)
    ybuf = g.GetY()
    ybuf.SetSize(N)
    y = array.array('d',ybuf)

    xerror = get_error(ex,N)
    yerror = get_error(ey,N)

    ge = ROOT.TGraphErrors(N,x,y,xerror,yerror)
    ge.SetName(g.GetName()+"_e")
    return ge
