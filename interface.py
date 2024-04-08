from circle import *

background_color = 'white'
pad = 10

def init_gui():
    player_container = tk.Frame(root, name='player', bg=background_color, padx=pad, pady=pad, highlightbackground="blue", highlightcolor="blue", highlightthickness=4)
    player_container.grid(pady=pad/2)
    player_label = tk.Label(player_container, text="Player", bg=background_color, pady=pad)
    player_score_label = tk.Label(player_container, text=f"Points: {size*piece*2}", bg=background_color, pady=pad, name='player_score')
    player_label.grid(row=0, column=0)
    player_score_label.grid(row=0, column=size-1)
    for i in range(2):
        for j in range(size):
            circle = CircleButton(player_container, color="blue", name=f"player_{i*size + j}", text=piece, bg=background_color)
            circle.grid(row=i+1, column=j if i==0 else i*size-j-1, padx=pad, pady=pad)

    computer_container = tk.Frame(root, name='computer', bg=background_color, padx=pad, pady=pad, highlightbackground="black", highlightcolor="black", highlightthickness=4)
    computer_container.grid(pady=pad/2)
    computer_label = tk.Label(computer_container, text="Computer", bg=background_color, pady=pad)
    computer_score_label = tk.Label(computer_container, text=f"Points: {size*piece*2}", bg=background_color, pady=pad, name='computer_score')
    computer_label.grid(row=0)
    computer_score_label.grid(row=0, column=size-1)
    for i in range(2):
        for j in range(size):
            circle = CircleButton(computer_container, color="red", name=f"computer_{i*size + j}", text=piece, bg=background_color)
            circle.grid(row=i+1, column=j if i==0 else i*size-j-1, padx=pad, pady=pad)

    popup_frame = tk.Frame(root, name='popup', bg=background_color, highlightbackground="black", highlightcolor="black", highlightthickness=1)
    popup_frame.place(relx=0.05, rely=0.3, relheight=0, relwidth=0)
    result_label = tk.Label(popup_frame, text="", name="result", font=("Arial", 15, "bold"), bg="white")
    restart_button = tk.Button(popup_frame, text="Restart", command=restart)
    exit_button = tk.Button(popup_frame, text="Exit", command=root.quit)
    result_label.pack(side="top", expand=True, pady=40)
    restart_button.pack(side="left", expand=True, pady=40)
    exit_button.pack(side="right", expand=True, pady=40)

    indication_label = tk.Label(root, text="", name="indication", bg="black", foreground="White", width=50)
    indication_label.grid()

def restart():
    initialization()
    init_gui()

init_gui()
root.mainloop()