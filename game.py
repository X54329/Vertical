class UpDecision:
    pass

class LeftDecision:
    pass

class RightDecision:
    pass

def simulate():
    g = 9.8
    D = [UpDecision, LeftDecision, RightDecision]
    V = 0
    V_p = (0, 0)
    h = 0
    S = (0, 0) # player position
    L = [] # ledge vertices
    dchain = [] # decisions
    t = 0

    for t in 0..9e99
        h += v
        l = f(t, L)
        S = g(t, S, V_p)
        V_p = h(t, V_p, L, S)

        d = k(V_p, S, L, H) # in D
        V_p = d(V_p)
        dchain.append(d)

        if S_y <= 0:
            # losing condition
            break

    return (h, dchain)
