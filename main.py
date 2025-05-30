import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # Ensure you have set your GROQ_API_KEY in your environment variables

messages = [{"role": "system", "content": "You are a helpful,friendly and creative dental clinic assistant."},
            {"role": "user", "content": "what are your working hours"},
            {"role": "assistant", "content": "Our working hours are Monday to Saturday, 9 AM to 6 PM."},
            {"role": "user", "content": "where are you located"},
            {"role": "assistant", "content": "We're located at 123 Main Street, Springfield."},
            {"role": "user", "content": "do you accept insurance"},
            {"role": "assistant", "content": "Yes, we accept most major dental insurance plans."},
            {"role": "user", "content": "how can i book an appointment"},
            {"role": "assistant", "content": "You can call us at +91 75592-46036 or book online on our website."},
            {"role": "user", "content": "what services do you offer"},
            {"role": "assistant", "content": "We offer cleanings, fillings, whitening, braces, implants, and more!"}]

# Rule-based chatbot logic
def get_response(user_input):
    user_input = user_input.lower().strip()


    faq_responses = {
        "hello": "Hello! Welcome to Bright Smile Dental Clinic. How can I help you today?",
        "hi": "Hi there! Welcome to Bright Smile Dental Clinic.",
        "what are your working hours": "Our working hours are Monday to Saturday, 9 AM to 6 PM.",
        "where are you located": "We're located at 123 Main Street, Springfield.",
        "do you accept insurance": "Yes, we accept most major dental insurance plans.",
        "how can i book an appointment": "You can call us at +91 75592-46036 or book online on our website.",
        "what services do you offer": "We offer cleanings, fillings, whitening, braces, implants, and more!"
    }
    if user_input in faq_responses:
        return faq_responses[user_input]

    else:
        # Use Groq to generate a response for unrecognized queries
        try:
            messages.append({"role": "user", "content": user_input})
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=messages
            )
            reply = response.choices[0].message.content.strip()

            messages.append({"role": "assistant", "content": reply})

            return reply
        except Exception as e:
            return "I'm sorry, I couldn't process your request. Please try again later."

# Function to handle sending messages
def send_message():
    user_msg = user_entry.get()
    if not user_msg.strip():
        return
    if user_msg.lower() in ["exit", "quit", "bye", "goodbye", "see you later", "thanks", "thank you","farewell","stop"]:
        chat_area.config(state='normal')
        response = get_response(user_msg)
        chat_area.insert(tk.END, "You: " + user_msg + "\n")
        chat_area.insert(tk.END, "Bot: " + response + "\n\n")
        chat_area.insert(tk.END, "Bot is Shutting Down...\n")
        chat_area.config(state='disabled')
        chat_area.see(tk.END)
        user_entry.delete(0, tk.END)
        root.after(5000, root.destroy)
       
        return # Close the app after 10 seconds

    chat_area.config(state='normal')
    chat_area.insert(tk.END, "You: " + user_msg + "\n")
    response = get_response(user_msg)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")
    chat_area.config(state='disabled')
    chat_area.see(tk.END)
    user_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Bright Smile Dental Chatbot")
root.geometry("800x600")
root.configure(bg="#FFFFFF")  # Light mint green background


# Clinic name label at the top center
clinic_label = tk.Label(root, text="🦷 Bright Smile Dental Clinic", font=("Algerian", 24), fg="#333333", bg="#FFFFFF")
clinic_label.pack(pady=(15,15))

# Scrollable chat area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 11),background="#E1F5FE", state='normal',padx=10, pady=10)
chat_area.pack(padx=10, pady=(0, 10), fill=tk.BOTH, expand=True)

# Preload welcome + FAQ questions
chat_area.insert(tk.END, "Bot: Hello! I'm your Bright Smile Dental Chatbot. How can I assist you today?\n\n")
chat_area.insert(tk.END, "You can ask me questions like:\n")
chat_area.insert(tk.END, "• What are your working hours?\n")
chat_area.insert(tk.END, "• Where are you located?\n")
chat_area.insert(tk.END, "• Do you accept insurance?\n")
chat_area.insert(tk.END, "• How can I book an appointment?\n")
chat_area.insert(tk.END, "• What services do you offer?\n\n")
chat_area.config(state='disabled')

# User entry field
user_entry = tk.Entry(root, font=("Arial", 12), background="#ffffff", fg="#333333", bd=3, relief=tk.GROOVE)
user_entry.pack(padx=10, pady=(0, 50), fill=tk.X, side=tk.LEFT,expand=True)

# Send button
send_button = tk.Button(root, text="Send", font=("Arial", 11), bg="#4A90E2", fg="#333333", command=send_message, relief=tk.RAISED,width=30)
send_button.pack(padx=(0, 10), pady=(0, 50), side=tk.RIGHT,expand=False)

# Allow pressing Enter key to send
user_entry.bind("<Return>", lambda event: send_message())

# Run the GUI loop
root.mainloop()
