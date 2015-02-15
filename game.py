import random

def up(v_player):
    v_player[1] += 5
    return v_player

def left(v_player):
    v_player[0] -= 5
    return v_player

def right(v_player):
    v_player[0] += 5
    return v_player

def f(t, ledges, v_scroll):
    for ledge in ledges:
        ledge[1] -= v_scroll
    return ledges

def g(position_player, v_player):
    position_player[0] += v_player[0]
    position_player[1] += v_player[1]
    return position_player

def h(t, v_player, ledges, position_player, v_scroll, gravity):
    v_player[1] = v_player[1] - gravity
    if v_player[1] <= 0:
        for ledge in ledges:
            if position_player[1] == ledge[1]:
                v_player[1] = -v_scroll
            else:
                v_player[1] -= gravity
    else:
        v_player[1] -= gravity
    return v_player

def k(decisions, v_player, position_player, ledges, score):
    r = random.randint(0, 2)
    return decisions[r]

def generate_ledges(ledges):
    random.seed(h)
    need_to_gen = False
    for ledge in ledges:
        if ledge[1] == 0:
            need_to_gen = True
    if need_to_gen:
        l = [random.random()*50, random.random()*100]
    return ledges

def simulate():
    gravity = 5
    decisions = [up, left, right]
    v_scroll = 1 # scroll velocity
    v_player = [0, 0] # [0] is x, [1] is y
    score = 0
    position_player = [0, 0] # player position
    ledges = generate_ledges([]) # ledge vertices
    decision_history = [] # decisions
    t = 0

    for t in xrange(0, 10000):

        # update environment

        score += v_scroll
        ledges = generate_ledges(f(t, ledges, v_scroll))
        position_player = g(position_player, v_player)
        v_player = h(t, v_player, ledges, position_player, v_scroll, gravity)

        # make decision

        decision = k(decisions, v_player, position_player, ledges, score)
        v_player = decision(v_player)
        decision_history.append(decision)

        # check losing condition

        if position_player[1] < 0:
            break

    return (score, decision_history)

print simulate()[0]