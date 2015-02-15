import random

def up(v):
    v[1] += 5
    return v

def left(v):
    v[0] -= 5
    return v

def right(v):
    v[0] += 5
    return v

def f(t, L):
    for l in L:
        l -= v
    return L

def g(S, v_p):
    S[0] += v_p[0]
    S[1] += v_p[1]
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
    r = random.randint(0, 2)
    return D[r]

def simulate():
    G = 9.8
    D = [up, left, right]
    v = 1 # scroll velocity
    v_p = [0, 0]
    H = 0
    S = [0, 0] # player position
    L = [] # ledge vertices
    dchain = [] # decisions
    t = 0

    for t in xrange(0, 10000):
        H += v
        L = f(t, L)
        S = g(S, v_p)
        v_p = h(t, v_p, L, S)

        d = k(D, v_p, S, L, H) # in D
        v_p = d(v_p)
        dchain.append(d)

        if S[1] <= 0:
            # losing condition
            break

    return (H, dchain)

print simulate()