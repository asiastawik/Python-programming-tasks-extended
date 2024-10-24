import numpy as np
import matplotlib.pyplot as plt

N = 500  # system size
M = 400  # number of trajectories
mu = 0.009  # probability of a marker on each edge

delta = np.zeros((M, N))  # array to store the values of delta

for k in range(M):
    # initialize the system with all black balls
    balls = np.zeros(N, dtype=int)
    balls[0] = N

    # simulate the evolution of the system for M time steps
    for t in range(1, N + 1):
        # move the balls and flip colors if there is a marker
        for i in range(N):
            j = (i + 1) % N  # index of the neighboring site
            if np.random.rand() < mu:
                balls[i], balls[j] = balls[j], balls[i]  # swap the balls
                balls[i] = N - balls[i]  # flip the color of the ball at site i

        # calculate the value of delta
        delta[k, t - 1] = balls[0] - balls.sum() // 2

    print(f"Trajectory {k + 1}/{M} completed.")

# plot the trajectories of delta as a function of time
plt.figure()
for k in range(M):
    plt.plot(delta[k])
plt.xlabel("Time")
plt.ylabel("Delta")
plt.show()
