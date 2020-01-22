class QueueModel:

    def __init__(self, lamb, mu, c):
        self.lamb = float(lamb)
        self.mu = float(mu)
        self.c = int(c)

    def uRate(self):
        return self.lamb / (self.c * self.mu)

    def lenQueue(self):
        return (self.lamb ** 2) / (self.mu * (self.mu - self.lamb))

    def lenSystem(self):
        return self.lenQueue() + self.lamb / self.mu

    def waitQueue(self):
        return round(self.lenQueue() / self.lamb, 3)

    def waitSystem(self):
        return round(self.waitQueue() + (1 / self.mu), 3)

    def modelProfile(self):
        print('The utilization rate is {}\n'.format(self.uRate()) +
              'The average length of queue is {}\n'.format(self.lenQueue()) +
              'The average length of system is {}\n'.format(self.lenSystem()) +
              'The average wait of queue is {}\n'.format(self.waitQueue()) +
              'The average wait of system is {}\n'.format(self.waitQueue())
              )


class InventoryModel:

    def __init__(self, price, quantity, cost):
        pass

    @staticmethod
    def Notsure(self):
        pass