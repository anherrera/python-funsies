from transitions import Machine
import random


class CrazyWife(object):
	states = ['angry', 'sad', 'happy', 'sleeping', 'drinking']

	def __init__(self, name):
		self.name = name
		self.coffees_drank = 0
		self.machine = Machine(model=self, states=self.states, initial='sleeping')

		# She always wakes up happy
		self.machine.add_transition(trigger='wake_up', source='sleeping', dest='happy')

		self.machine.add_transition('bad_name', '*', 'angry')

		self.machine.add_transition('fight', '*', 'sad')

		self.machine.add_transition('hug', 'sad', 'happy', conditions=['is_forgiving'])

		self.machine.add_transition('go_out', '*', 'drinking', before='get_dressed')

		self.machine.add_transition('drink_too_much', 'drinking', 'sleeping', after='drink_coffee')

	def drink_coffee(self):
		print("Well, I better drink a coffee")
		self.coffees_drank += 1

	def get_dressed(self):
		print("Geez, I look terrible. Let me get dressed.")

	def is_forgiving(self):
		return random.random() < 0.5


# From code wars
class Automaton(object):
	def __init__(self, states, transitions, initial):
		self.states = states
		self.transitions = transitions
		self.state = initial

	def read_commands(self, commands):
		for act in commands:
			possibles = [item for item in self.transitions if item['condition'] is self.state and item['action'] is act]
			if len(possibles) == 1:
				self.state = possibles[0]['result']

		return self.state == 'q2'


trans = [
	{'condition': 'q1', 'action': '1', 'result': 'q2'},
	{'condition': 'q2', 'action': '0', 'result': 'q3'},
	{'condition': 'q3', 'action': '0', 'result': 'q2'},
	{'condition': 'q3', 'action': '1', 'result': 'q2'}
]

my_automaton = Automaton(['q1', 'q2', 'q3'], trans, 'q1')

# Do anything necessary to set up your automaton's states, q1, q2, and q3.
print(my_automaton.read_commands(["1"]))
print(my_automaton.read_commands(["1", "0", "0", "1"]))
