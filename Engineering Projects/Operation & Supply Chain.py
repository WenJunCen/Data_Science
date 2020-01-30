import numpy as np

class QueueModel:

    def __init__(self, lamb, mu, c):
        self.lamb = float(lamb)
        self.mu = float(mu)
        self.c = int(c)
    @property
    def uRate(self):
        return self.lamb / (self.c * self.mu)

    @property
    def lenQueue(self):
        return (self.lamb ** 2) / (self.mu * (self.mu - self.lamb))

    @property
    def lenSystem(self):
        return self.lenQueue + self.lamb / self.mu

    @property
    def waitQueue(self):
        return round(self.lenQueue / self.lamb, 3)

    @property
    def waitSystem(self):
        return round(self.waitQueue + (1 / self.mu), 3)

    def prExactSys(self, n):
        return (1-self.uRate)*self.uRate**n

    def prAtLeastSys(self, n):
        return self.uRate**n

    def prWaitQueue(self, x):
        return self.uRate*np.exp**(-self.mu*(1-self.mu)*x)

    def prWaitSys(self, x):
        return np.exp**(-self.mu*(1-self.mu)*x)

    def modelProfile(self):
        print('The utilization rate is {}\n'.format(self.uRate) +
              'The average length of queue is {}\n'.format(self.lenQueue) +
              'The average length of system is {}\n'.format(self.lenSystem) +
              'The average wait of queue is {}\n'.format(self.waitQueue) +
              'The average wait of system is {}\n'.format(self.waitQueue)
              )
