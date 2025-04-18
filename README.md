
 # ChatWithSQL 💬📊

This project is a **Streamlit web app** that allows users to ask natural language questions and receive **automatically generated SQL queries** using **Google Gemini AI**.
Gold Rate Query App — A Streamlit web app powered by Google Gemini AI that converts natural language questions into SQL queries to fetch real-time answers from a gold rate database. 

🔹 Enter questions like:  
    🤖 Example Questions You Can Ask
              What is the gold rate in Mumbai today?

              Show me all cities and their 24K rates.

              Which city has the highest gold price?

              Show gold rates on 2025-04-10.

🔹 The app:
- Uses `streamlit` for UI
- Uses `sqlite3` for database operations
- Uses `Google Generative AI (Gemini Pro)` for converting natural language to SQL






### 🛠 How to Run Locally

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gold-rate-app.git
cd gold-rate-app

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate   # Windows
    source venv/bin/activate  # macOS/Linux
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up `.env` with your Gemini API key:
    ```env
    GOOGLE_API_KEY=your_key_here
    ```
5.Create the Database
     Run the sql.py script to create and populate the gold_rate.db file.
  ```bash  
    python sql.py

5. Run the app:
     Once the app is running, go to http://localhost:8501 in your browser.
    ```bash
    streamlit run app.py
