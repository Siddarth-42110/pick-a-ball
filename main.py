import random
def pick_ball_experiment():
    balls = ['Blue', 'Red', 'Green']

    result = random.choice(balls)

    pro = balls.count('Red')/len(balls)
    print("Probability of picking red ball is:", pro)

    if result == 'Red':
        return 'red ball was picked'
    else:
        return 'better luck next time'
    
res = pick_ball_experiment()
print(res)