from functions import file_read

states,initial_state,accepting_states,alphabet,transitions=file_read("teste")
class NfaToDfa:
    def __init__(self,alphabet,initial_state,accepting_states,transitions,states):
        self.transitions = transitions
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.states=states
        self.list_adjacent=list()
        self.next_adjacent=initial_state+","

    def add_adjacent(self,value):
        list_=[]
        word=""
        for i in self.transitions:
            for state in self.next_adjacent.split(","):
                if state == i[0] and value in i and not i[-1] in list_:
                    word+=i[-1]
                    word+=","
                    list_.append(i[-1])
                
        self.list_adjacent[-1][self.next_adjacent].append(word)
    
    def verify_key(self,value):
        for dict in self.list_adjacent:
            if value in str(dict.keys()):
                
                return True
        return False

    


    def add_next_adjacent(self):
        for i in self.list_adjacent:
            for a in list(i.values())[0]:
                if not self.verify_key(a):
                    self.next_adjacent = a 
                    return True
        return False
        
    def start(self):
        self.list_adjacent.append({self.next_adjacent:[]})
        
        stop = True
        while  stop:
            for i in self.alphabet:
                
                self.add_adjacent(i)
                
            stop=self.add_next_adjacent()
            if not self.verify_key(self.next_adjacent):
                self.list_adjacent.append({self.next_adjacent:[]})
            
        print(self.list_adjacent)
        #print(self.transitions)
        
    
nfa_to_dfa=NfaToDfa(alphabet,initial_state[0],accepting_states,transitions,states).start()