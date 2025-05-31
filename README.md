# 🦷 Bright Smile Dental Chatbot – Tkinter + Groq Edition 😁

Hello there, kind human !
Welcome to the official repository of **Bright Smile Dental Chatbot** – a friendly virtual assistant for your dental clinic queries. Built with 💙 using **Python**, **Tkinter**, and powered by the brains of **Groq LLaMA 3** 🦙💡 (so it never runs out of answers... unlike my phone battery 🔋).

---

## 🚀 How to Run This Project Locally

Follow these steps, and I promise no cavities! 🪥

```bash
# Step 1: Clone the repository
git clone https://github.com/Nerdyziz/Dental_Clinic_AI_ChatBot.git
cd Dental_Clinic_AI_ChatBot

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Set your Groq API key
To keep things secure and professional, I’ve used an environment variable for the Groq API key.

### Here’s what you need to do:
1. Go to [https://console.groq.com](https://console.groq.com) and sign up (it’s free).
2. Click on **API Keys**, then **Generate Key**.
3. Set it in your terminal:

**For Mac/Linux:**
```bash
export GROQ_API_KEY=your_key_here


# Step 4: Run the chatbot
python main.py
```

---

## 🧠 What This Chatbot Does (a.k.a. "The Logic in My Magic")

This chatbot is more than just a pretty smile 😎. Here's what I’ve done, broken down into sparkling little pieces:

### ✅ 1. **Five Predefined FAQ Responses (Because that was the project brief 😇)**

The chatbot knows the answers to these questions:

* What are your working hours?
* Where are you located?
* Do you accept insurance?
* How can I book an appointment?
* What services do you offer?

If the user asks any of these, the bot instantly replies with a hard-coded answer using a Python dictionary (aka **rule-based chatbot logic**).

---

### 🤖 2. **"I Don’t Know This Yet…" – But Actually, I Do 😏**

If the user asks **anything outside those 5 questions**, the chatbot politely says:

> “Sorry, don’t know this yet.”

...But here's the twist! 🧙‍♂️
I don’t want my bot to *actually* be clueless, so I gave it a **superpower** by integrating the **Groq LLaMA 3 API**, a super smart language model.

So secretly, when the user asks a non-FAQ question, Groq jumps in behind the scenes and answers it!

This ensures the bot never runs out of dental facts, jokes, or even advice on toothbrush brands 🪥✨.

### 💬 3. **Conversational Memory**

I’ve used a list called `messages[]` that keeps track of everything the user and assistant said. This way, Groq always knows the context — just like a good dentist remembers your sweet tooth history 🍬.

---

### 👋 4. **Bye = Bot Naps 💤**

When the user says:

> `bye`, `exit`, `quit`, `farewell`, `thank you`, etc…

The bot doesn't just reply — it **shuts down gracefully**.

I've used:

```python
root.after(5000, root.destroy)
```

This means: after 5 seconds of saying goodbye, the chatbot gently closes its GUI window — just enough time for a dramatic farewell 😢.

---

## 🎨 GUI That Doesn’t Hurt Your Eyes

* Made with **Tkinter**, it has:

  * A clean, soft-colored chat area
  * A stylish title with a cute tooth emoji 🦷
  * Scrollable chat window
  * Entry box and send button
  * Preloaded instructions so the user isn’t left wondering what to ask

It’s lightweight, fast, and doesn’t require braces!

---

## 🪄 Why This is More Than Just a Basic Bot

This isn’t just a few `if` statements and a smile.
I’ve combined **rule-based logic** with **AI superpowers** to make this chatbot:

* **Reliable** (always knows the important stuff)
* **Scalable** (can answer *everything* dental-related)
* **Polite and user-friendly**
* **Visually appealing**
* And **gracefully exits** when you're done

I’ve built this thinking like a real developer — future-proofing it with Groq, modular logic, and clean UI. Plus, it was a lot of fun 🧃!

---

## 🤝 Dear Interviewer...

I hope you enjoyed this creative walkthrough. I’ve poured a lot of thought into making this chatbot smart, friendly, and aligned with real-world clinic needs.
It’s not just a project — it’s a reflection of how I think: with **clarity, creativity, and a little bit of humor**. I look forward to discussing it with you!.
Honestly speaking taken some help from ChatGPT regarding integration of Groq API as I have just started with python. But all the other things like logic, GUI Interface, its all original like my Teeth! 😁

---

## 📦 File Structure

```
Dental_Clinic_AI_ChatBot/
├── main.py       # Main Python file
├── requirements.txt    # To install dependencies
└── README.md           # You're reading this!
```

---

**Thanks a ton for reading!**
If you smiled while reading this, the bot’s already done its job 😉

Stay awesome,
**Aziz Sunelwala [RBU CSE] 🧠🦷**

---
