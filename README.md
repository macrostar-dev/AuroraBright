# 🌌 Aurora Bright

<p align="center">
  <img src="https://img.shields.io/badge/Status-Beta-orange?style=for-the-badge" alt="Status Beta">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

---

> [!IMPORTANT]
> **Project Purpose:** This is a **Beta** version developed exclusively for **testing and learning**. It serves as a personal laboratory to practice the integration of Flask, SQLAlchemy, and responsive web design.

**Aurora Bright** is a web-based platform designed to centralize professional profiles. It provides a simplified space where users can showcase their work profile, including descriptions and social media links, categorized by industry to improve visibility.

---

## 🚀 Key Features

- **👤 Profile Management:** Users can register their name, description, and profile picture.
- **🔗 Social Integration:** Direct links to Instagram, Facebook, and other platforms.
- **📂 Smart Categories:** Automated filtering for fields like Programming, Accounting, Baking, and more.
- **📱 Fully Responsive:** A seamless experience across mobile and desktop devices.
- **💾 Database Persistence:** Robust data handling using SQLAlchemy ORM.

---

## 🛠️ Tech Stack

| Technology | Role |
| :--- | :--- |
| **Python** | Backend Logic |
| **Flask** | Web Framework & Routing |
| **SQLAlchemy** | Database Management (ORM) |
| **Jinja2** | Dynamic HTML Templating |
| **CSS3** | Custom styling with Dark Mode gradients |

---

## 📂 Project Structure & HTML Setup

For Flask to recognize your files, your project **must** be organized as follows:

```text
aurora-bright/
├── main.py              # Main Flask logic
├── static/              # Static assets
│   └── css/
│       └── style.css    # Custom styles & gradients
├── templates/           # HTML folder (Mandatory for render_template)
│   ├── index.html       # Home & Category selection
│   ├── about.html       # Project info
│   ├── cate.html        # Category display view
│   └── new_entry.html   # Profile creation form
└── simple_db.db        # SQLite database (Auto-generated)
   ```bash

¡Entendido perfectamente! Perdona la confusión anterior. Aquí tienes exactamente esa sección que me pasaste, pero convertida a **Markdown puro** para que GitHub la renderice correctamente con negritas, listas y bloques de código:

---

## ⚙️ Local Setup

Follow these steps to get the environment ready:

### 1. Install Dependencies

```bash
pip install flask flask_sqlalchemy

```

### 2. Initialize the Database

Since the project uses SQLAlchemy, you need to create the database file and tables before the first run. Execute this command in your terminal:

```bash
python -c "from main import app, db; app.app_context().push(); db.create_all()"

```

### 3. Run the Application

Start the local development server:

```bash
python main.py

```

Once running, open your browser and go to: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📝 Usage Notes

* **Templates:** All `.html` files provided in this repository must stay inside the `templates/` folder for the `render_template` function to work.
* **Images:** The "Profile Picture" field in the form expects a valid image URL.
* **Testing:** This is a standalone beta; the database is local (SQLite) and will be created in the root folder as `simple_db.db`.

<p align="center">
<b>Developed entirely by me as a personal learning project.</b>
</p>

---

   pip install flask flask_sqlalchemy

