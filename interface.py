from circle import *

background_color = 'white'
pad = 10

player_container = tk.Frame(root, name='player', bg=background_color, padx=pad, pady=pad)
player_container.grid(pady=pad/2)
player_label = tk.Label(player_container, text="Player", bg=background_color, pady=pad)
player_score_label = tk.Label(player_container, text=f"Points: {count_pioners(player)}", bg=background_color, pady=pad, name='player_score')
player_label.grid(row=0, column=0)
player_score_label.grid(row=0, column=size-1)
for i in range(2):
    for j in range(size):
        circle = CircleButton(player_container, color="blue", name=f"player_{i*size + j}", text=piece, bg=background_color)
        circle.grid(row=i+1, column=j if i==0 else i*size-j-1, padx=pad/2, pady=pad/2)

computer_container = tk.Frame(root, name='computer', bg=background_color, padx=pad, pady=pad)
computer_container.grid(pady=pad/2)
computer_label = tk.Label(computer_container, text="Computer", bg=background_color, pady=pad)
computer_score_label = tk.Label(computer_container, text=f"Points: {count_pioners(computer)}", bg=background_color, pady=pad, name='computer_score')
computer_label.grid(row=0)
computer_score_label.grid(row=0, column=size-1)
for i in range(2):
    for j in range(size):
        circle = CircleButton(computer_container, color="red", name=f"computer_{i*size + j}", text=piece, bg=background_color)
        circle.grid(row=i+1, column=j if i==0 else i*size-j-1, padx=pad/2, pady=pad/2)

result_label = tk.Label(root, text="", name="result", bg="black", foreground="White", width=50)
result_label.grid()
print(result_label)

root.mainloop()