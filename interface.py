from circle import *

player_container = tk.Frame(root, name='player')
player_container.grid(pady=20)

for i in range(2):
    for j in range(size):
        circle = CircleButton(player_container, color="blue", name=f"player_{i*size + j}", text=piece)
        circle.grid(row=i, column=j if i==0 else i*size-j-1, padx=10, pady=10)

vertical_separator = tk.Frame(root, bg="black", height=5, width=500)
vertical_separator.grid()

computer_container = tk.Frame(root, name='computer')
computer_container.grid(pady=20)

for i in range(2):
    for j in range(size):
        circle = CircleButton(computer_container, color="red", name=f"computer_{i*size + j}", text=piece)
        circle.grid(row=i, column=j if i==0 else i*size-j-1, padx=10, pady=10)

root.mainloop()