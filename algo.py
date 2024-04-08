import copy
import tkinter as tk

# params
size = 3
piece = 2
profondeur = 4
animation_delai = 500
root = tk.Tk()
root.title("Katro")

# build relation
dif = [2*i+1 for i in range(size)]
rel = [i+dif[len(dif)-1-i] if i<size else i-dif[i-len(dif)] for i in range(size*2)]

def initializeBoard(s, p):
    return [['*' for j in range(p)] for i in range(s*2)]

def count_pioners(p):
    return sum([len(i) for i in p])

def step1(p, o, id, widget_p, isComputer, counter=0):
    global profondeur
    temp = counter

    if ((counter==0 and len(p[id])>0) or len(p[id])>1) and count_pioners(o)!=0:
        counter+=1
        e = len(p[id])
        p[id].clear()

        # update interface
        name_widget_p = ''.join(widget_p.split('_')[:-1]) + '_' + str(id)
        root.nametowidget(name_widget_p).clear()
        root.after(animation_delai, step2, p, o, id+1, e, widget_p, isComputer, counter)
        root.nametowidget('.player.player_score').config(text=f"Points: {count_pioners(player)}")
        root.nametowidget('.computer.computer_score').config(text=f"Points: {count_pioners(computer)}")

    elif count_pioners(o)==0 and isComputer:
        root.nametowidget('.indication').config(text="Computer win!")
        root.nametowidget('.popup').place_configure(relheight=0.4, relwidth=0.9)
        root.nametowidget('.popup.result').config(text="Computer win!")

    elif count_pioners(o)==0 and not isComputer:
        root.nametowidget('.indication').config(text="Player win!")
        root.nametowidget('.popup').place_configure(relheight=0.4, relwidth=0.9)
        root.nametowidget('.popup.result').config(text="Player win!")

    elif temp!=0 and not isComputer and count_pioners(p)!=0:
        # update UI
        root.nametowidget('.player').configure(highlightbackground="black", highlightcolor="black")
        root.nametowidget('.computer').configure(highlightbackground="red", highlightcolor="red")
        root.nametowidget('.indication').config(text=f"Computer chose id: {id+1}")

        id = minimax(profondeur, True, o, p)
        step1(o, p, id, '.computer.computer_'+str(id), True)
    else:
        # update UI
        root.nametowidget('.indication').config(text="Your Turn!")
        root.nametowidget('.player').configure(highlightbackground="blue", highlightcolor="blue")
        root.nametowidget('.computer').configure(highlightbackground="black", highlightcolor="black")
        


def step2(p, o, id, e, widget_p, isComputer, counter):
    global size
    if id >= size*2:
        id %= size*2
    p[id] += '*'
    e -= 1

    # update interface
    name_widget_p = ''.join(widget_p.split('_')[:-1]) + '_' + str(id)
    root.nametowidget(name_widget_p).add_element()
    root.nametowidget('.player.player_score').config(text=f"Points: {count_pioners(player)}")
    root.nametowidget('.computer.computer_score').config(text=f"Points: {count_pioners(computer)}")

    if e>0:
        root.after(animation_delai, step2, p, o, id+1, e, widget_p, isComputer, counter)
    else:
        root.after(animation_delai, step3, p, o, id, widget_p, isComputer, counter)

def step3(p, o, id, widget_p, isComputer, counter):
    widget_o = '.player.player_' if isComputer else '.computer.computer_'
    if ((not isComputer and id in range(size, size*2)) or (isComputer and id in range(size))) and len(p[id])>1:
        if o[ rel[id] ] != []:
            p[id] += o[ rel[id] ]
            o[ rel[id] ].clear()

            # update interface
            name_widget_p = ''.join(widget_p.split('_')[:-1]) + '_' + str(id)
            name_widget_o = widget_o + str(rel[id])
            e_o = root.nametowidget(name_widget_o).get_element()
            root.nametowidget(name_widget_o).clear()
            root.after(animation_delai, root.nametowidget(name_widget_p).add_element(e_o))
        
        elif (not isComputer and o[:size] == [[] for i in range(size)]) or (isComputer and o[size:size*2] == [[] for i in range(size)]) and o[id] != []:
            p[id] += o[id]
            o[id].clear()
            
            # update interface
            name_widget_p = ''.join(widget_p.split('_')[:-1]) + '_' + str(id)
            name_widget_o = widget_o + str(id)
            e_o = root.nametowidget(name_widget_o).get_element()
            root.nametowidget(name_widget_o).clear()
            root.after(animation_delai, root.nametowidget(name_widget_p).add_element(e_o))
    
    root.nametowidget('.player.player_score').config(text=f"Points: {count_pioners(player)}")
    root.nametowidget('.computer.computer_score').config(text=f"Points: {count_pioners(computer)}")
    root.after(animation_delai, step1, p, o, id, widget_p, isComputer, counter)
            


# algorithm for moving the pionner of player
def move(p, o, id, widget_p, isComputer):
    counter = 0
    while ((counter == 0 and len(p[id])>0) or len(p[id])>1) and count_pioners(o)!=0:
        counter+=1
        e = len(p[id])
        e_t = e
        p[id].clear()            
            
        for i in range(id+1, id+1+e):
            if i >= size*2:
                i %= size*2
            p[i] += '*'
            e_t -= 1

        id = i

        if ((not isComputer and id in range(size, size*2)) or (isComputer and id in range(size))) and len(p[id])>1:
            if o[ rel[id] ] != []:
                p[id] += o[ rel[id] ]
                o[ rel[id] ].clear()
                    

            elif (not isComputer and o[:size] == [[] for i in range(size)]) or (isComputer and o[size:size*2] == [[] for i in range(size)]) and o[id] != []:
                p[id] += o[id]
                o[id].clear()           


# minimax algorithm
def minimax(pr, estMax, p, o):
    if pr==0 or count_pioners(p)==0 or count_pioners(o)==0:
        return count_pioners(p)

    if estMax:
        v, etat = {}, {}
        
        # check the valid move
        for i in range(0, size*2):
            if len(p[i])>0:
                x = copy.deepcopy(p)
                y = copy.deepcopy(o)
                move(x, y, i, '.computer.computer_'+str(i), True)
                etat.update({i:(x,y)})
        
        for key, values in etat.items():
            v1, v2 = values
            v.update({minimax(pr-1, False, copy.deepcopy(v1), copy.deepcopy(v2)):key})
        
        result = max(v.keys())
        id_result = v.get(result)
        return id_result if pr == profondeur else result

    else:
        v, etat = {}, {}
        
        # check the valid move
        for i in range(0, size*2):
            if len(p[i])>0:
                x = copy.deepcopy(o)
                y = copy.deepcopy(p)
                move(x, y, i,'.player.player_'+str(i), False)
                etat.update({i:(x,y)})
        
        for key, values in etat.items():
            v1, v2 = values
            v.update({minimax(pr-1, True, copy.deepcopy(v2), copy.deepcopy(v1)):key})

        result = min(v.keys())
        return result
    


# initialization
def initialization():
    global player
    global computer
    player = initializeBoard(size, piece)
    computer = initializeBoard(size, piece)

initialization()


def start(widget):
    global computer
    global player
    id = int(widget.split('_')[-1])
    step1(player, computer, id, '.player.player_'+str(id), False)