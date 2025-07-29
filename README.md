# Refurbished Phone Listing App

This project is developed for *Memorly.AI* as part of the Python Developer assignment.  
It is a dummy web application built using Python and Flask to simulate listing refurbished phones across 3 e-commerce platforms, with specific logic for conditions, pricing, and profitability.



## Features

- Inventory management for in-stock and sold phones
- Platform-specific condition mapping
- Platform-wise fee deduction
- Profitability check (₹500 minimum profit required)
- Prevents listing out-of-stock or low-profit phones
- Dummy login screen for authentication
- Responsive and clean UI using HTML + CSS + Flask



## Platform Fee Rules

| Platform | Fee Type                     |
|----------|------------------------------|
| X        | 10% of price                 |
| Y        | 8% of price + ₹2 fixed       |
| Z        | 12% of price                 |

---

## Condition Mapping

| System Condition | Platform X | Platform Y         | Platform Z |
|------------------|------------|---------------------|------------|
| Like New         | New        | 3 Stars (Excellent) | New        |
| Good             | Good       | 2 Stars (Good)      | Good       |
| Fair             | Scrap      | 1 Star (Usable)     | As New     |


## Tech Stack

- *Language:* Python
- *Framework:* Flask
- *Frontend:* HTML, CSS
- *Data:* Python dictionary (in-memory)
- *Authentication:* Dummy login screen (no database)
- *Demo:* See below



##  Project Structure

<pre><code>

memorly-python-assignment/
├── app.py
├── logic.py
├── phones_data.py
├── requirements.txt
├── README.md
├── templates/
│   ├── login.html
│   └── dashboard.html
├── static/
│   └── style.css

</code></pre>


##  How to Run This App

### Step 1: Install Flask
<code><pre>pip install flask</code></pre>

### Step 2: Run the App
<code><pre>python app.py</code></pre>

### Step 3: Open in Browser
http://127.0.0.1:5000

### Step 4: Use the Login Page
<code><pre>
Username: admin
Password: 1234
</code></pre>


## Notes

No database or real API used — all logic is in memory

Code is modular and readable

Focused on condition mapping, pricing logic, and platform-specific rules



##  Developed By

*Afrin Shaik*  
Python Developer Candidate | Memorly.AI  
Email: shaikafrin676@gmail.com  
GitHub: https://github.com/Afrin950-shaik






