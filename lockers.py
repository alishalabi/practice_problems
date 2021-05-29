"""

Create a program that simulates lockers in a gym locker room. Users should be able
to rent the closest available locker, and vacate their own locker at any time.
There should be a maximum number of lockers available.
"""

max_lockers = 50

class Locker:
    def __init__(self, max_lockers):
        self.max_lockers = max_lockers
        self.first_avail = 0
        self.capacity = 0
        self.all_lockers = {}
        for i in range(max_lockers):
            self.all_lockers[i] = False

    def rent(self):
        if self.capacity >= self.max_lockers:
            print("All lockers taken. Please vacate a locker before renting a new one.")
            return
        self.all_lockers[self.first_avail] = True
        self.capacity += 1
        while self.first_avail < self.max_lockers:
            curr = self.first_avail + 1
            if self.all_lockers[curr] == False:
                self.first_avail = curr
                return
        # Case: last locker, has capacity

    def vacate(self, spot):
        if self.all_lockers[spot] != True:
            print(f"Locker at spot {spot} is already empty")
            return
        self.all_lockers[spot] = False
        self.capacity -= 1
        if spot < self.first_avail:
            self.first_avail = spot




test = Locker(max_lockers)
test.rent()
test.rent()
test.rent()
test.vacate(0)
print(test.all_lockers)
print(test.first_avail)
