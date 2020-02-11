class Bus(object):
     passengers = set()
     def add_passenger(self, person):
        self.passengers.add(person)

bus1 = Bus()
bus2 = Bus()
bus1.add_passenger('abe')
bus2.add_passenger('bertha')
bus1.passengers  # returns ['abe', 'bertha']
bus2.passengers  # also ['abe', 'bertha']

print(bus1.passengers,bus2.passengers)