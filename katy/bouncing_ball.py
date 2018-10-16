def bouncingBall(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:

        counter = 1

        while h * bounce >= window:
            counter += 2
            h *= bounce
        return counter
    return -1

#
# Three conditions must be met for a valid experiment:
#
# Float parameter "h" in meters must be greater than 0
# Float parameter "bounce" must be greater than 0 and less than 1
# Float parameter "window" must be less than h.


assert bouncingBall(3, 0.66, 1.5) == 3
assert bouncingBall(30, 0.66, 1.5) == 15