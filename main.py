
from functions import file_read
from nfa import NFA
from dfa import DFA
from convert_NFA_to_DFA import NfaToDfa


value_="bba"
value_=list(value_)

states,initial_state,accepting_states,alphabet,transitions=file_read("automatonfa")
nfa=NFA(alphabet,initial_state[0],accepting_states,transitions,value_,states).start()
#print(nfa)

states,initial_state,accepting_states,alphabet,transitions=file_read("automatodfa")
dfa=DFA(alphabet,initial_state[0],accepting_states,transitions,value_).start()
#DFA.crete_image()
#print(dfa)

nfa_to_dfa=NfaToDfa(alphabet,initial_state[0],accepting_states,transitions,states).start()





