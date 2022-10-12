import pydot
from  functions import file_read


class DFA:
    def __init__(self,alphabet,initial_state,accepting_states,transitions,input_):
        self.transitions=transitions
        self.alphabet=alphabet
        self.initial_state=initial_state
        self.accepting_states=accepting_states
        self.input_=input_

    def verify_transitions(self,value):
        for i in self.transitions:
            if self.initial_state == i[0] and value in i:
                self.initial_state = i[-1]
                return True
        return False

    def start(self):
        for i in self.input_:
            if  not self.verify_transitions(i):
                return False
        
        if self.initial_state in self.accepting_states:
            return True
        return False
    
    def crete_image():
        states,initial_state,accepting_states,alphabet,transitions,stransitions=file_read("automatodfa")
        graphs = pydot.Dot('my_graph', graph_type='digraph', bgcolor='white')
        for i in states:
            if i in initial_state:
                graphs.add_node(pydot.Node('fake' ,style="invisible"))
                if i in accepting_states:
                    graphs.add_node(pydot.Node(i,root="true", shape="doublecircle"))
                else:
                    graphs.add_node(pydot.Node(i,root="true"))
                graphs.add_edge(pydot.Edge('fake',i, style="bold"))  
            elif i in accepting_states:
                graphs.add_node(pydot.Node(i,shape="doublecircle"))
            else:
                graphs.add_node(pydot.Node(i, shape='circle'))
        
        for i in stransitions:
            a=i.split(":")
            from_=a[0]
            to=a[1].split(">")[1]
            alphabet_=a[1].split(">")[0]
            graphs.add_edge(pydot.Edge(from_,to ,label=alphabet_ ))


        graphs.write_png('dfa.png')
        