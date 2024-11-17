import customtkinter as ctk
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from tkinter import messagebox

# Function to generate the PDF for the virtual ticket
def print_ticket():
    pdf_file = "Virtual_Ticket.pdf"
    c = canvas.Canvas(pdf_file, pagesize=A4)
    width, height = A4

    # Set the title and passenger information in the PDF
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 50, "Boarding At")

    # Boarding and destination details
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, "From: NEW DELHI (NDLS)")
    c.drawString(50, height - 100, "To: TIRUPATI (TPTY)")
    c.drawString(50, height - 120, "Departure: 20:10, 14-Dec-2024")
    c.drawString(300, height - 120, "Arrival: 04:40, 16-Dec-2024")

    # Train information
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 150, "Train No./Name: 12626 / KERALA EXPRESS")
    c.drawString(50, height - 170, "Class: Third AC Economy (3E)")

    # Passenger details
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 200, "Passenger Details")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 220, "Name: Shubhan")
    c.drawString(200, height - 220, "Age: 19")
    c.drawString(300, height - 220, "Gender: M")
    c.drawString(50, height - 240, "Booking Status: CNF/M1/61/Middle")

    # Payment details
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 270, "Payment Details")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 290, "Ticket Fare: ₹2,005.00")
    c.drawString(50, height - 310, "Travel Insurance Premium: ₹0.45")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 330, "Total Fare: ₹2,029.05")

    # Save the PDF
    c.save()
    messagebox.showinfo("PDF Generated", f"Virtual Ticket saved as {pdf_file}")

# Initialize the main application window
app = ctk.CTk()
app.title("Virtual Ticket")
app.geometry("600x600")

# Main title
title_label = ctk.CTkLabel(app, text="Boarding At", font=("Arial", 18, "bold"))
title_label.pack(pady=(10, 5))

# Top frame for boarding and destination details
top_frame = ctk.CTkFrame(app, width=550, height=120)
top_frame.pack(pady=10, padx=20, fill="x", expand=False)

# Display booking and destination information
from_label = ctk.CTkLabel(top_frame, text="From: NEW DELHI (NDLS)", font=("Arial", 12))
from_label.pack(anchor="w", padx=10)

to_label = ctk.CTkLabel(top_frame, text="To: TIRUPATI (TPTY)", font=("Arial", 12))
to_label.pack(anchor="w", padx=10)

# Travel dates and times
date_frame = ctk.CTkFrame(top_frame)
date_frame.pack(pady=10)

departure_label = ctk.CTkLabel(date_frame, text="Departure: 20:10, 14-Dec-2024", font=("Arial", 12))
departure_label.grid(row=0, column=0, padx=10)

arrival_label = ctk.CTkLabel(date_frame, text="Arrival: 04:40, 16-Dec-2024", font=("Arial", 12))
arrival_label.grid(row=0, column=1, padx=10)

# Middle frame for train information
middle_frame = ctk.CTkFrame(app, width=550, height=150)
middle_frame.pack(pady=10, padx=20, fill="x", expand=False)

train_number_label = ctk.CTkLabel(middle_frame, text="Train No./Name: 12626 / KERALA EXPRESS", font=("Arial", 12, "bold"))
train_number_label.pack(anchor="w", padx=10, pady=5)

class_label = ctk.CTkLabel(middle_frame, text="Class: Third AC Economy (3E)", font=("Arial", 12))
class_label.pack(anchor="w", padx=10)

# Passenger Details
passenger_frame = ctk.CTkFrame(app, width=550, height=100)
passenger_frame.pack(pady=10, padx=20, fill="x", expand=False)

passenger_title = ctk.CTkLabel(passenger_frame, text="Passenger Details", font=("Arial", 14, "bold"))
passenger_title.pack(anchor="w", padx=10, pady=5)

# Passenger information in a grid
passenger_info_frame = ctk.CTkFrame(passenger_frame)
passenger_info_frame.pack()

name_label = ctk.CTkLabel(passenger_info_frame, text="Name: Shubhan", font=("Arial", 12))
name_label.grid(row=0, column=0, padx=10)

age_label = ctk.CTkLabel(passenger_info_frame, text="Age: 19", font=("Arial", 12))
age_label.grid(row=0, column=1, padx=10)

gender_label = ctk.CTkLabel(passenger_info_frame, text="Gender: M", font=("Arial", 12))
gender_label.grid(row=0, column=2, padx=10)

booking_status_label = ctk.CTkLabel(passenger_info_frame, text="Booking Status: CNF/M1/61/Middle", font=("Arial", 12))
booking_status_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

# Payment Details
payment_frame = ctk.CTkFrame(app, width=550, height=150)
payment_frame.pack(pady=10, padx=20, fill="x", expand=False)

payment_title = ctk.CTkLabel(payment_frame, text="Payment Details", font=("Arial", 14, "bold"))
payment_title.pack(anchor="w", padx=10, pady=5)

ticket_fare_label = ctk.CTkLabel(payment_frame, text="Ticket Fare: ₹2,005.00", font=("Arial", 12))
ticket_fare_label.pack(anchor="w", padx=10)

insurance_fee_label = ctk.CTkLabel(payment_frame, text="Travel Insurance Premium: ₹0.45", font=("Arial", 12))
insurance_fee_label.pack(anchor="w", padx=10)

total_fare_label = ctk.CTkLabel(payment_frame, text="Total Fare: ₹2,029.05", font=("Arial", 12, "bold"))
total_fare_label.pack(anchor="w", padx=10)

# Print button
print_button = ctk.CTkButton(app, text="Print", command=print_ticket)
print_button.pack(pady=20)

# Start the main loop
app.mainloop()
