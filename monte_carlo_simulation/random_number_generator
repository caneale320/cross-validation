rand_count = 0
seed = 1000


def gen_number():
    """
    :return: a randomly generated number from 0 to 1 using values a, seed, c, and K
    """

    global seed
    global rand_count
    
    a = 24693
    c = 3967
    K = 2**15

    x_i = (a*seed + c) % K
    seed = x_i

    u_i = x_i/K
    
    rand_count += 1

    return u_i
