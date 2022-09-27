
class NfaToDfa:
    def __init__(self,alphabet,initial_state,accepting_states,transitions,input_,states):
        self.transitions = transitions
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.input_ = input_
        self.states=states
        
    