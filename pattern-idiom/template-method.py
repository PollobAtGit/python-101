# template method implementation

class Vehicle:
    def go_forward(self):
        self.start_engine()
        self.look_forward()

class AstonMartin(Vehicle):
    def start_engine(self):
        print('AstonMartin - start_engine')

    def look_forward(self):
        print('AstonMartin - look_forward')

class Jaguar(Vehicle):
    def start_engine(self):
        print('Jaguar- start_engine')

    def look_forward(self):
        print('Jaguar- look_forward')


AstonMartin().go_forward()
Jaguar().go_forward()
  
