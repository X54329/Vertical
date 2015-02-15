# Vertical Plan

* Game Simulation
* Neural Network Design
* Helpful Animations
* Computer Control of Game
* Split Screen

## Simulator
	g      = constant
	D      = [up, down, left, right]
	V      = (0, 0)
	V_p    = (0, 0)
	h      = 0
	S      = (0, 0)
	L      = [] // ledge vertices
	dchain = [] // decisions
	t      = 0
	for t in 0..infinity
		h  += v
		l   = f(t, L)
		S   = g(t, S, V_p)
		V_p = h(t, V_p, L, S)
		
		d   = k(D, V_p, S, L, H) is in D
		V_p = d(V_p)
		dchain.append(d)
		
		if S_y <=0:
			fail()
			break

	return h, dchain
