import tkinter as tk
from tkinter import messagebox
from speech_to_text import get_diagnosis
from utils import save_patient_record, load_patients

class MedicalApp:
    def __init__(self, master):
        self.master = master
        master.title("Medical App")
        
        self.label = tk.Label(master, text="Patient Registration")
        self.label.pack()

        self.register_button = tk.Button(master, text="Register Patient", command=self.register_patient)
        self.register_button.pack()

        self.book_appointment_button = tk.Button(master, text="Book Appointment", command=self.book_appointment)
        self.book_appointment_button.pack()

    def register_patient(self):
        # Logic for patient registration
        messagebox.showinfo("Info", "Patient Registered")

    def book_appointment(self):
        # Logic for booking appointments
        messagebox.showinfo("Info", "Appointment Booked")

root = tk.Tk()
app = MedicalApp(root)
root.mainloop()