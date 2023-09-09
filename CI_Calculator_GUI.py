from tkinter import *
def clear_all():
    principal_field.delete(0,END)
    rate_field.delete(0,END)
    time_field.delete(0,END)
    compound_interset.delete(0,END)

    principal_field.focus_set()

def Calculate_ci():
    principal = int(principal_field.get())
