import random
import math

class Monte_Carlo_Integration(object):
    """
    Performs Monte Carlo Integration
    Calculates definite integrals by random sampling
    """


    def __init__(self):
        pass

    def integrate(self, left, right, num_iters=1000):
        """
        Integrates fuction on given range

        Parameters:
            left: Left bound for integration
            right: Right bound for integration
            num_iters: Interations of Monte Carlo Integration

        Returns:
            Estimated definite integral

        >>> f = lambda x: x
        >>> mc.integrate(f, 0, 1, 1000)
        0.4984162575459102

        >>> f = lambda x: math.cos(x)
        >>> mc.integrate(f, 0, math.pi, 1000)
        0.005460417815199725
        """
        
        total = 0

        for _ in range(num_iters):

            val = random.random() * (right-left) + left
            total += f(val)

        return total / num_iters
