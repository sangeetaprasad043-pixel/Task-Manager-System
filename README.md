# **Task Management System**

A professional **Full-Stack Task Management System** developed using **Python (Flask)** and **SQLite**. The application features a dynamic web interface, secure user authentication, and role-based dashboard functionality designed for organizational workflow management.

---

### **### 🚀 Key Features**
* **Role-Based Access Control (RBAC):**
    * **Admin:** Automatically assigned to the first registered user. Admins can create tasks, assign them to team members, view all activities, and delete tasks.
    * **User:** Access to a personalized dashboard to view and mark assigned tasks as 'Completed'.
* **Dynamic Dashboard:** * **Status Filtering:** Real-time filtering (All, Pending, Completed) using GET requests.
    * **Pagination:** Efficiently displays 5 tasks per page to ensure fast loading and clean UI.
* **Security & Authentication:** * **Password Hashing:** Uses `PBKDF2:SHA256` hashing for secure credential storage.
    * **Session Management:** Powered by `Flask-Login` to protect routes and handle user states.
* **Modern UI:** Responsive design built with **Bootstrap 5**, featuring interactive badges and intuitive navigation.

---

### **### 🛠️ Tech Stack**
* **Frontend:** HTML5, CSS3 (Bootstrap 5), Jinja2 Templating
* **Backend:** Python 3.10+, Flask
* **Database:** SQLite (SQLAlchemy ORM)
* **Testing:** Unittest Framework

---

### **### 📂 Project Structure**
Based on the current development environment:
```text
TASK_MANAGER_PROJECT/
├── instance/               # Database directory
│   └── task_manager.db     # SQLite relational database
├── templates/              # UI Components (Jinja2)
│   ├── login.html          # Login interface (Bootstrap)
│   ├── register.html       # Signup interface (Bootstrap)
│   ├── dashboard.html      # Filtered & Paginated Task List
│   └── create_task.html    # Admin Task Assignment UI
├── venv/                   # Python Virtual Environment
├── app.py                  # Main Application Entry Point
├── config.py               # Security & DB Configurations
├── models.py               # DB Schema (User & Task Models)
├── routes.py               # Backend Logic & Auth Routes
└── test_app.py             # Automated Testing Script
```

---

### **### 🚦 API & Logic Flow**

| Route | Method | Access | Description |
| :--- | :--- | :--- | :--- |
| `/register` | GET/POST | Public | New user signup; first user becomes Admin. |
| `/login` | GET/POST | Public | Authenticates credentials using hashed passwords. |
| `/dashboard`| GET | Private | Displays tasks based on user role and filter. |
| `/task/new` | GET/POST | Admin | Form to assign a new task to a specific user. |
| `/task/complete/<id>`| GET | All | Updates task status to 'Completed'. |
| `/task/delete/<id>` | GET | Admin | Permanently removes a task record. |

---

### **### ✅ Quality Assurance (Testing)**
The project includes a robust test suite (`test_app.py`) using **Unittest**.
* **Covers:** User Registration, Login Flow, Admin Auto-assignment, and Task CRUD logic.
* **Environment:** Uses an in-memory SQLite database for safe and isolated testing.

---

### **### ⚙️ Installation & Setup**

1.  **Activate Environment:**
    ```bash
    .\venv\Scripts\activate
    ```
2.  **Install Requirements:**
    ```bash
    pip install flask flask-sqlalchemy flask-login
    ```
3.  **Run Application:**
    ```bash
    python app.py
    ```
4.  **Run Automated Tests:**
    ```bash
    python test_app.py
    ```

---

### **### 📝 Author**
**Sangeeta** *Master of Computer Applications (MCA)*

---
