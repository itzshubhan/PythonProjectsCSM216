import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import customtkinter
from PIL import Image
import subprocess

customtkinter.set_appearance_mode("System")

app = customtkinter.CTk()
app.resizable(False, False) 
app.geometry("800x440")
app.title('Booking System')

def train():
    app.destroy()
    subprocess.run(['python', 'train.py'])

# Function to execute on button click
def button_function():
    from_station = from_station_entry.get()
    to_station = to_station_entry.get()
    travel_date = entry3.get()
    travel_class = entry_class.get()
    
    # Uncomment if you want to call an external script
    # app.destroy()
    # subprocess.run(['python', 'train.py'])

# Autocomplete functions
def on_keyrelease(event, entry, listbox, values):
    query = entry.get().lower()
    if query == "":
        listbox.place_forget()
        return
    filtered_values = [(code, name) for code, name in values if query in code.lower() or query in name.lower()]
    update_listbox(listbox, filtered_values, entry)

def update_listbox(listbox, values, entry):
    listbox.delete(0, tk.END)
    if values:
        listbox.config(height=min(5, len(values)))  # Limit max height to 5 items
        listbox.place(x=entry.winfo_x(), y=entry.winfo_y() + entry.winfo_height())
        for code, name in values:
            listbox.insert(tk.END, f"{code} - {name}")
    else:
        listbox.place_forget()

def on_select(event, entry, listbox):
    selected = listbox.get(tk.ACTIVE)
    code, name = selected.split(" - ")
    entry.delete(0, tk.END)
    entry.insert(0, name)  # Insert station name into the entry
    listbox.place_forget()

# Define stations as a list of tuples
stations = [
    ('NDLS', 'New Delhi'),
    ('CSTM', 'Mumbai CST'),
    ('MAS', 'Chennai Central'),
    ('SBC', 'Bangalore City'),
    ('HWH', 'Howrah'),
    ('LKO', 'Lucknow'),
    ('ADI', 'Ahmedabad'),
    ('BCT', 'Mumbai Central'),
    ('PUNE', 'Pune Junction'),
    ('JP', 'Jaipur'),
    ('HYB', 'Hyderabad Deccan'),
    ('BZA', 'Vijayawada Junction'),
    ('CNB', 'Kanpur Central'),
    ('VSKP', 'Visakhapatnam'),
    ('NGP', 'Nagpur'),
    ('CBE', 'Coimbatore Junction'),
    ('JUC', 'Jalandhar City'),
    ('PGW', 'Phagwara'),
    ('TUP', 'Tirupur')
]

# Load and resize the background image
try:
    bg_image = Image.open("./assets/background.jpg")
    bg_image = bg_image.resize((600, 440))
    img1 = customtkinter.CTkImage(bg_image)  # Use CTkImage
except FileNotFoundError:
    print("Image file './assets/background.jpg' not found.")
    img1 = None

# Load the magnifying glass icon
try:
    search_icon = Image.open("./assets/magnifying_glass.png")
    search_icon = search_icon.resize((20, 20))
    search_icon_img = customtkinter.CTkImage(search_icon)  # Use CTkImage
except FileNotFoundError:
    print("Image file './assets/magnifying_glass.png' not found.")
    search_icon_img = None

# Set background label
l1 = customtkinter.CTkLabel(master=app, image=img1 if img1 else None)
l1.place(x=0, y=0, relwidth=1, relheight=1)

# Create frame
frame = customtkinter.CTkFrame(master=app, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Use grid layout
frame.grid_rowconfigure(0, weight=2)
frame.grid_rowconfigure(1, weight=2)
frame.grid_rowconfigure(2, weight=2)
frame.grid_rowconfigure(3, weight=2)
frame.grid_rowconfigure(4, weight=2)
frame.grid_columnconfigure(0, weight=2)

# Add widgets
l2 = customtkinter.CTkLabel(master=frame, text="Book Tickets", font=('Century Gothic', 20))
l2.grid(row=0, column=0, pady=10, padx=30, sticky="nsew")

# Function to create autocomplete entry
def create_autocomplete_entry(master, values):
    entry = customtkinter.CTkEntry(master)
    listbox = tk.Listbox(master, height=0)  # Start with height 0
    listbox.place_forget()

    entry.bind('<KeyRelease>', lambda event: on_keyrelease(event, entry, listbox, values))
    listbox.bind('<ButtonRelease-1>', lambda event: on_select(event, entry, listbox))

    return entry, listbox

# Create autocomplete entries for 'From' and 'To'
from_station_entry, from_listbox = create_autocomplete_entry(frame, stations)
from_station_entry.grid(row=1, column=0, pady=10, padx=30, sticky="ew")

to_station_entry, to_listbox = create_autocomplete_entry(frame, stations)
to_station_entry.grid(row=2, column=0, pady=10, padx=30, sticky="ew")

# Create horizontal frame for date selection
date_frame = customtkinter.CTkFrame(master=frame)
date_frame.grid(row=3, column=0, pady=5, padx=30, sticky="ew")

l7 = customtkinter.CTkLabel(master=date_frame, text="Select Date:", font=('Century Gothic', 15))
l7.pack(side="left", padx=5)

entry3 = DateEntry(master=date_frame, width=15, background="darkblue", foreground="white", borderwidth=2)
entry3.pack(side="left", padx=10)

entry_class = customtkinter.CTkOptionMenu(master=frame, values=["Select class/coach", "Sleeper", "General"], width=220)
entry_class.set("Select class/coach")
entry_class.grid(row=4, column=0, pady=10, padx=30, sticky="ew")

# Add search button
button1 = customtkinter.CTkButton(master=frame, width=120, text="Search Train", command=train,
                                   corner_radius=6,
                                   image=search_icon_img, compound="right")
button1.grid(row=5, column=0, pady=10, padx=30, sticky="ew")

app.mainloop()


