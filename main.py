def calc_pi(limit):  # Generator function
    """
    Prints out the digits of PI
    until it reaches the given limit
    """

    q, r, t, k, n, b = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
        if 4 * q + r - t < n * t:
            # yield digit
            yield n
            # insert period after first digit
            if counter == 0:
                yield '.'
            # end
            if decimal == counter:
                print('')
                break
            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * b
            nn = (q * (7 * k) + 2 + (r * b)) // (t * b)
            q *= k
            t *= b
            b += 2
            k += 1
            n = nn
            r = nr


def pi_print(limit):  # Wrapper function
    # Calls CalcPi with the given limit
    pi_digits = calc_pi(int(limit))

    i = 0

    # Prints the output of calcPi generator function
    # Inserts a newline after every 40th number
    for d in pi_digits:
        print(d, end='')
        i += 1
        if i == 40:
            print("")
            i = 0


def pi_list(limit):
    l_pi = list(calc_pi(limit))
    return l_pi[:1] + l_pi[2:]
