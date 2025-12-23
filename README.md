🧭 Telugu Local Guide – The Local Guide (Week 5)

A simple AI-powered Local Guide that understands **Hyderabad’s local slang, street food culture, and traffic patterns** using **Kiro** and a **custom context file**.

This project was built as part of **Week 5: The Local Guide** challenge under **AI for Bharat**.

---

## 🚀 Project Overview

Generic AI assistants often fail to understand **local language, culture, and city-specific behavior**.  
This project solves that problem by teaching Kiro about **Hyderabad’s local nuances** using a custom context file.

All local intelligence comes **exclusively from `.kiro/product.md`** — no hardcoded logic and no external data sources.

---

## 🎯 Theme

**Week 5 Theme:** The Local Guide  

**Objective:**  
Build a tool that understands a specific city or culture by relying on a **custom context file** to guide AI responses.

---

## ✨ Features

- 🗣️ Understands **Telugu local slang**
- 🍽️ Recommends **popular Hyderabad street food**
- 🚦 Explains **area-wise traffic patterns**
- 🧠 Uses **only custom context** (no generic AI knowledge)
- 🔁 Easily extendable to other cities by updating `product.md`

---

## 🧠 How Kiro Is Used

Kiro is used to:
- Load local knowledge from `.kiro/product.md`
- Answer user queries using **only that context**
- Prevent hallucinations by restricting responses to provided data

Every user query explicitly passes the custom context file to Kiro.

---

## 📁 Project Structure

telugu-local-guide/
│
├── .kiro/
│ └── product.md # Custom local context (core of the project)
│
├── app.py # Flask backend
├── templates/
│ └── index.html # Simple frontend UI
│
├── requirements.txt
└── README.md

yaml
Copy code

> ⚠️ Important: The `.kiro` directory is included in the repository and is **NOT ignored**.

---

## 🧾 Custom Context (`product.md`)

The `.kiro/product.md` file contains:
- Local Telugu slang and meanings  
- Popular street food spots  
- Area-wise traffic patterns and peak hours  
- Cultural habits and language style  

This file is the **only source of local knowledge** for the application.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **AI Engine:** Kiro  
- **Context Source:** `.kiro/product.md`

---

## ▶️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/telugu-local-guide
cd telugu-local-guide
```
2️⃣ Install Dependencies
```bash
Copy code
pip install -r requirements.txt
```
3️⃣ Run the Application
```bash
Copy code
python app.py
```
4️⃣ Open in Browser
arduino
```
Copy code
http://localhost:5000
```
🧪 Sample Queries
Try asking:

What does "Lite teesko" mean?

Best street food place in Hyderabad?

Is Madhapur traffic heavy in the evening?

Explain one cultural habit of people here

⚡ How Kiro Accelerated Development
Eliminated the need for complex rule-based logic

Enabled fast iteration by simply updating product.md

Allowed local intelligence without retraining models

Reduced overall development time

# Challenge Submission

Challenge: Kiro Week 5 – Local Guide

Program: AI for Bharat (Hack2Skill)

Author: TANNA SOUMYA

#License

Open-source, for educational and learning purposes.
