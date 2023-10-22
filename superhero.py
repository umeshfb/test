from transitions import Machine

class go_to():
    states = ['drone_off','go_to_location_start','go_to_location_stop','debug', 'in_mission']
    def __init__(self):
        self.machine = Machine(model=self, states=go_to.states, initial='drone_off')

        self.machine.add_transition(trigger='start_flight', source='drone_off', dest='go_to_location_start')

        self.machine.add_transition(trigger='stop_flight', source='go_to_location_start', conditions=['start_drone'])
        self.machine.add_transition(trigger='stop_flight', source='go_to_location_start', dest='drone_off')

        def start_drone(self):
            print('starting_drone')

a = go_to()
print(a.state)
a.start_flight()
print(a.state)
a.stop_flight()
print(a.state)