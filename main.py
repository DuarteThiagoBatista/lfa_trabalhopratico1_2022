

def add_list(list_,name):
    list_add=[]
    for i in list_:
        if i.split()[0] == name:
            break
        list_add.append(i.split()[0])     
    return list_add

def split_list(list_transitions):
    list_return=[]
    for i in list_transitions:
        list_=[]
        list_.append(i.split(":")[0])
        split_=i.split(":")[1].split(">")[0]
        for  a in split_.split(","):
            list_.append(a)
        list_.append(i.split(":")[1].split(">")[1])
        list_return.append(list_)
    return list_return

with open("./automato.txt","r") as file_txt:
    file = file_txt.readlines()
    for i in range(len(file)):
        if file[i].split()[0] =="#states":
            states=add_list(file[i+1:],"#initial")

        elif file[i].split()[0] == "#initial":
            initial=add_list(file[i+1:],"#accepting")

        elif file[i].split()[0] == "#accepting":
            accepting=add_list(file[i+1:],"#alphabet")
        
        elif file[i].split()[0] == "#alphabet":
            alphabet=add_list(file[i+1:],"#transitions")

        elif file[i].split()[0] == "#transitions":
            transitions=add_list(file[i+1:],"")
        

    print(f"states = {states}")
    print(f"initial = {initial}")
    print(f"accepting = {accepting}")
    print(f"alphabet = {alphabet}")
    
    split_transitions=split_list(transitions)
    print(f"transitions = {split_transitions}")
    print(f"transitions = {transitions}")
    json={
  "alphabet": alphabet,
  "states": states,
  "initial_state": initial[0],
  "accepting_states": accepting,
  "transitions": split_transitions
}
