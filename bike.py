class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "price: {}".format(self.price)
        print "maximum speed: {}".format(self.max_speed)
        print "total miles: {}".format(self.miles)
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
        else:
            self.miles = 0;
        return self

bike = Bike(1000, 100)
bike.ride().ride().ride().reverse().displayInfo()
