# **Little Lemon - Django Full Stack Project**
### 🚀 **How to Run the Project on Mac**

This project is the final assessment for the **Full Stack Developer course by Meta**.
It includes a **Django backend** and a **MySQL database**.

---

## **📌 1. Install Required Tools**
Before starting, make sure you have **Homebrew** installed. If not, install it with:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then, install **Python**, **pipx**, **MySQL**, and **pipenv**:
```sh
brew install python pipx mysql
pipx ensurepath
pipx install pipenv
```

---

## **📌 2. Set Up MySQL Database**
1️⃣ **Start MySQL Server** (if not already running):
```sh
brew services start mysql
```

2️⃣ **Create the database and user**:
```sh
mysql -u root -p
```
Then, in the MySQL console, run:
```sql
CREATE DATABASE littlelemon;
CREATE USER 'django_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'django_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```
Replace `'password'` with your desired password.

---

## **📌 3. Set Up the Django Project**
1️⃣ **Clone or extract the project**:
If using **Git**, run:
```sh
git clone <repository_url>
cd littlelemon
```
If you have a **ZIP file**, extract it and navigate to the project folder:
```sh
cd path/to/littlelemon
```

2️⃣ **Create and activate a virtual environment** using `pipenv`:
```sh
pipenv shell
```

3️⃣ **Install dependencies**:
```sh
pipenv install
```

---

## **📌 4. Configure Database Connection**
Open the **`settings.py`** file (`littlelemon/settings.py`) and ensure the `DATABASES` section matches your MySQL setup:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'USER': 'django_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Replace `'password'` with the actual MySQL password you set earlier.

---

## **📌 5. Apply Migrations and Create Superuser**
Run database migrations:
```sh
python manage.py makemigrations
python manage.py migrate
```

Create a superuser for the Django admin panel:
```sh
python manage.py createsuperuser
```
Enter your **username, email, and password** when prompted.

---

## **📌 6. Run the Django Server**
Start the development server:
```sh
python manage.py runserver
```
The server will start at:
👉 **http://127.0.0.1:8000/**

---

## **📌 7. Test the Project**
Now, visit these URLs to check if the project is working correctly:

- **Home Page:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Booking Page:** [http://127.0.0.1:8000/book](http://127.0.0.1:8000/book)
- **Reservations API (JSON):** [http://127.0.0.1:8000/bookings](http://127.0.0.1:8000/bookings)
- **Django Admin Panel:** [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

To log in to the admin panel, use the superuser credentials created in **Step 5**.

---

## **📌 8. (Optional) Open the Project in VS Code**
If you're using **VS Code**, you can open the project directory by running:
```sh
code .
```
If the `code` command is not recognized, add it to your system path:
```sh
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
```

---

## **🌟 Summary**
✅ Installed dependencies and database
✅ Configured MySQL and Django
✅ Applied migrations and created a superuser
✅ Successfully started the Django server
✅ Tested the project in a web browser

Now your **Little Lemon** project is running! 🚀
If you encounter any issues, double-check the setup steps or restart your MySQL server.

---

### **📌 Additional Commands**
💡 **Restart MySQL if needed**:
```sh
brew services restart mysql
```

💡 **Check MySQL user privileges**:
```sh
mysql -u root -p -e "SELECT User, Host FROM mysql.user;"
```

💡 **Reinstall dependencies (if needed)**:
```sh
pipenv install --dev
```

---

Enjoy working on **Little Lemon**! 😊🚀

