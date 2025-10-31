import tkinter as tk
from dataclasses import dataclass
import random


@dataclass
class Thing:
    name: str
    value: int


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Rankings")
        self.root.geometry("800x600")

        self.thing_list = self.get_thing_list()
        self.current_thing_1 = 0
        self.current_thing_2 = 0
        self.get_new_things()

        self.left_button_text = tk.StringVar()
        self.right_button_text = tk.StringVar()
        self.left_button_text.set(self.thing_list[self.current_thing_1].name)
        self.right_button_text.set(self.thing_list[self.current_thing_2].name)

        self.setup_ui()

    def setup_ui(self):
        self.title = tk.Label(root, text="Wähle eins:")
        self.title.pack(side=tk.TOP, fill=tk.X, pady=30)

        self.quit_button = tk.Button(root, text="Enden", command=self.quit)
        self.quit_button.pack(side=tk.BOTTOM, padx=30, pady=30)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill=tk.BOTH, expand=True)

        self.left_button = tk.Button(self.button_frame, textvariable=self.left_button_text, command=lambda: self.click(self.current_thing_1), bg="#3355dd", activebackground="#3355cc")
        self.right_button = tk.Button(self.button_frame, textvariable=self.right_button_text, command=lambda: self.click(self.current_thing_2), bg="#dd3355", activebackground="#cc3355")
        self.left_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=30, pady=30)
        self.right_button.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=30, pady=30)

    def get_new_things(self) -> None:
        self.current_thing_1 = random.randint(0, len(self.thing_list) - 1)
        self.current_thing_2 = random.randint(0, len(self.thing_list) - 1)

        while self.current_thing_1 == self.current_thing_2:
            self.current_thing_2 = random.randint(0, len(self.thing_list) - 1)

    def click(self, index) -> None:
        self.thing_list[index].value += 1 
        self.get_new_things()
        self.left_button_text.set(self.thing_list[self.current_thing_1].name)
        self.right_button_text.set(self.thing_list[self.current_thing_2].name)
        print("clicked")

    def get_thing_list(self) -> list[Thing]:
        thing_list = []

        file = open("list.txt")

        for thing in file.read().split("\n"):
            if thing.strip():
                thing_list.append(Thing(thing, 0))

        return thing_list

    def quit(self) -> None:
        print(self.thing_list)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
