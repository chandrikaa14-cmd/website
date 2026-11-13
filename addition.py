import tkinter as tk
from decimal import Decimal, InvalidOperation
from tkinter import ttk


def add_numbers():
    try:
        first_number = Decimal(first_entry.get())
        second_number = Decimal(second_entry.get())

        if not first_number.is_finite() or not second_number.is_finite():
            raise InvalidOperation
    except InvalidOperation:
        result_label.config(text="Enter valid numbers in both boxes.")
        return

    result_label.config(text=f"Result: {first_number + second_number}")


root = tk.Tk()
root.title("Addition Calculator")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding=16)
main_frame.grid()

ttk.Label(main_frame, text="First number:").grid(row=0, column=0, sticky="w", pady=4)
first_entry = ttk.Entry(main_frame, width=20)
first_entry.grid(row=0, column=1, pady=4)

ttk.Label(main_frame, text="Second number:").grid(row=1, column=0, sticky="w", pady=4)
second_entry = ttk.Entry(main_frame, width=20)
second_entry.grid(row=1, column=1, pady=4)

ttk.Button(main_frame, text="=", command=add_numbers).grid(
    row=2, column=0, columnspan=2, pady=8
)
result_label = ttk.Label(main_frame, text="Result:")
result_label.grid(row=3, column=0, columnspan=2)

first_entry.focus()
root.bind("<Return>", lambda _event: add_numbers())
root.mainloop()
