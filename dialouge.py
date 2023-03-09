import tkinter as tk


def create_dialogue_box():
    dialog = tk.Toplevel()
    dialog.geometry("186x271")
    dialog.title("Dialogue Box")
    image = tk.PhotoImage(file="G:\\Work\\FunProject\\two.png")
    dialog_label = tk.Label(dialog, image=image)
    dialog_label.image = image
    dialog_label.pack()

    # Schedule the creation of a new dialogue box in 1 second
    dialog.after(1000, create_dialogue_box)

    # Set protocol method to create a new dialog box on window close
    dialog.protocol("WM_DELETE_WINDOW", create_dialogue_box)


def update():
    root.update()
    root.after(10, update)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1020x574")
    root.title("Main Window")
    image = tk.PhotoImage(file="G:\\Work\\FunProject\\one.png")
    root_label = tk.Label(root, image=image)
    root_label.image = image
    root_label.pack()

    # Schedule the creation of the first dialogue box in 1 second
    root.after(1000, create_dialogue_box)

    # Set protocol method to create a new dialog box on window close
    root.protocol("WM_DELETE_WINDOW", create_dialogue_box)

    update()

    root.mainloop()
