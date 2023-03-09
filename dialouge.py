import tkinter as tk


def create_dialogue_box():
    dialog = tk.Toplevel()
    dialog.geometry("186x271")
    dialog.title("HELLO!!")
    image = tk.PhotoImage(file="G:\\Work\\FunProject\\two.png")
    dialog_label = tk.Label(dialog, image=image)
    dialog_label.image = image
    dialog_label.pack()

    dialog.after(1000, create_dialogue_box)

    dialog.protocol("WM_DELETE_WINDOW", create_dialogue_box)


def update():
    main_dialouge.update()
    main_dialouge.after(10, update)


if __name__ == '__main__':
    main_dialouge = tk.Tk()
    main_dialouge.geometry("1020x574")
    main_dialouge.title("ARE YOU A ONE OR A ZERO?")
    image = tk.PhotoImage(file="G:\\Work\\FunProject\\one.png")
    main_dialouge_label = tk.Label(main_dialouge, image=image)
    main_dialouge_label.image = image
    main_dialouge_label.pack()

    main_dialouge.after(1000, create_dialogue_box)

    main_dialouge.protocol("WM_DELETE_WINDOW", create_dialogue_box)

    update()

    main_dialouge.mainloop()
