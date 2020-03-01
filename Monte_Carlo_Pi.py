import random
import numpy as np
import matplotlib.pyplot as plt

class Monte_Carlo_pi:

    """
    Estimates the value of Pi by repeatedly generating random
    points and checking if they are within the range of a circle.
    """

    def __init__(self):

        self.xvals = []
        self.yvals = []
        self.hits = []


    def pi(self, iters=1000000):
        """
        Performs Monte Carlo Pi Estimation
        
        Parameters:
            iters: The number of interation to run the algorithm

        Returns:
            Estimated value of pi
            

        >>> pi()
        3.13994
        >>> pi(100)
        3.04
        >>> pi(1000000000)
        3.14177276
        """

        self.xvals = []
        self.yvals = []
        self.hits = []
        attempts = iters
        hits = 0

        for _ in range(iters):

            xval = random.random()
            yval = random.random()

            self.xvals.append(xval)
            self.yvals.append(yval)

            if xval**2 + yval ** 2 < 1:
                hits += 1
                self.hits.append('Red')

            else:
                self.hits.append('Blue')
                

        return 4 * hits / attempts 

    def plot(self, num_points=1000):
        """
        Plots the random points with colors representing
        whether the point landed or missed the circle

        Paramaters:
            num_points: the amount of points to show on the graph
        """

        circle_x = np.linspace(0, 1, 500)
        circle_y = np.sqrt(1 - circle_x**2)

        plt.xlim([0,1])
        plt.ylim([0,1])
        plt.title("Monte Carlo Pi Estimation")
        

        plt.plot(circle_x, circle_y)
        plt.scatter(self.xvals[0:num_points], self.yvals[0:num_points], c=self.hits[0:num_points])

        plt.show()
