import random

class UpDecision:
    pass

class LeftDecision:
    pass

class RightDecision:
    pass

def f(t, L):
    for l in L:
        l -= v
    return L

def g(S, v_p):
    S += v_p
    return S

def h(t, v_p, L, S):
    if v_p[1] <= 0:
        for l in L:
            if s_y == L[1]:
                v_p[1] = -v_p[1]
            else:
                v_p[1] -= g
    return v_p

def k(D, v_p, S, L, H):
    r = random.randint(0, 3)
    return D[r]

def simulate():
    g = 9.8
    D = [UpDecision, LeftDecision, RightDecision]
    v = 0 # scroll velocity
    v_p = (0, 0)
    h = 0
    S = (0, 0) # player position
    L = [] # ledge vertices
    dchain = [] # decisions
    t = 0

    for t in xrange(0, 10000):
        h += v
        L = f(t, L)
        S = g(S, v_p)
        V_p = h(t, v_p, L, S)

        d = k(D, v_p, S, L, H) # in D
        v_p = d(v_p)
        dchain.append(d)

        if S_y <= 0:
            # losing condition
            break

    return (h, dchain)

print simulate()