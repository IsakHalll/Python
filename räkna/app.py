time = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0,45]
distance = [0.009, 0.04, 0.096, 0.175, 0.278, 0.404, 0.556, 0.728, 0.926]

def velocity(s_one, t_one, s_two, t_two):
    result = float(((s_two - s_one) / (t_two - t_one)))
    print(result)

for i in range(0, len(time)):
    velocity(time[i+1], time[i], distance[i+1], distance[i])
