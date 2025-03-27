# **URL Shortener - Django**  

A simple **URL Shortener** built with Django that allows users to shorten long URLs and redirect them using a short URL.

## **Features**
- Generate short URLs from long URLs  
- Store generated URLs in a database  
- Redirect users from short URLs to original long URLs  
- Django-based backend with form handling, using Forms.py

---

## **Tech Stack**
- **Backend:** Django, Python  
- **Database:** SQLite (default) / MySQL / PostgreSQL (configurable later)  
- **Frontend:** HTML (only for the First basic Utility , will be changed soon)

---

## **Installation and Setup**
### **1. Clone the Repository**
```bash
git clone https://github.com/trixsearch/linkbanale.git
cd linkbanale
```

### **2. Create a Virtual Environment**
```bash
python -m venv .venv
source .venv/bin/activate   # For macOS/Linux
# OR
.venv\Scripts\activate      # For Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Run the Development Server**
```bash
python manage.py runserver
```
Now, open your browser and visit **`http://127.0.0.1:8000/`**.

---

## **Usage**
1. Enter a long URL in the input field.
2. Click on "Shorten URL."
3. Copy the generated short URL.
4. Use the short URL to get redirected to the original URL.

---

## **Project Structure**
```
/url-shortener-django
│── /shortner
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│── /templates
│── /static
│── manage.py
│── requirements.txt
│── README.md
```

---

## **Endpoints**
| Method | URL Pattern          | Description |
|--------|----------------------|-------------|
| GET    | `/`                  | Home page (Shorten URL form) |
| POST   | `/`                  | Submit URL for shortening hitting Enter if in Browser |
| GET    | `/<shortUrl>/`        | Redirect to original URL |
| GET    | `/detail/<id>/`       | View details of a short URL |

---

## **Future Enhancements**
- Add user authentication for tracking URLs  
- Implement an API for generating short URLs  
- Integrate analytics for tracking URL clicks  
- Deploy on cloud platforms like Python Anywhere

---

## **Story Behind this Project**

I Basically developed the project to make basic Understanding , later I'm going to use the project in my upcoming projects, that's gonna be trixsearch


---

## **Author**
👤 **trixsearch**  
📧 Email: inforatme@gmail.com 
🔗 GitHub: [trixsearch](https://github.com/trixsearch)  

---

Let me know if you want any modifications! 🚀
