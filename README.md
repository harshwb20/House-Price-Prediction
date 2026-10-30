\# 🏠 House Price Prediction Web Application



A Machine Learning-based web application that predicts house prices based on housing and geographical features. The application provides user authentication, a personalized dashboard, house price prediction, and prediction history.



\## 📌 Project Overview



The House Price Prediction application is developed using \*\*Python Flask, Machine Learning, and MySQL\*\*.



Users can create an account, sign in, access their personalized dashboard, enter house-related details, and get an estimated house price. The application also stores prediction history in a MySQL database, allowing users to view their previous predictions.



\## ✨ Features



\### 1. User Authentication

\- User Registration (Sign Up).

\- User Login (Sign In).

\- Session-based authentication.

\- Dashboard access after successful login.

\- Logout functionality.



\### 2. User Dashboard

\- Personalized dashboard after login.

\- Input form for house-related information.

\- Displays previous house price predictions.

\- Maintains individual prediction history for each user.



\### 3. House Price Prediction

\- Predicts house prices using a trained Machine Learning model.

\- Accepts eight input features.

\- Displays the predicted house price.

\- Stores prediction details in the MySQL database.



\### 4. Prediction Result

\- Displays the estimated house price.

\- Shows the prediction result after submitting house details.



\## 🛠️ Technologies Used



| Technology | Purpose |

|---|---|

| Python | Backend programming |

| Flask | Web application framework |

| Machine Learning | House price prediction |

| Scikit-learn | Machine Learning model |

| NumPy | Numerical operations |

| Joblib | Loading the trained ML model |

| MySQL | Database management |

| MySQL Connector | Python-MySQL connectivity |

| HTML5 | Web page structure |

| CSS3 | Styling and layout |

| Bootstrap | Responsive UI (if used) |

| Jinja2 | Dynamic HTML rendering |



\## 📊 Input Features



The application uses the following eight features for house price prediction:



| Feature | Description |

|---|---|

| MedInc | Median income of the area |

| HouseAge | Median house age |

| AveRooms | Average number of rooms |

| AveBedrms | Average number of bedrooms |

| Population | Population of the area |

| AveOccup | Average household occupancy |

| Latitude | Geographical latitude |

| Longitude | Geographical longitude |



\## 📁 Project Structure



```text

House-Price-Prediction/

│

├── app.py

├── house\_model.pkl

├── requirements.txt

├── README.md

│

├── templates/

│   ├── login.html

│   ├── signup.html

│   ├── dashboard.html

│   └── result.html

│

└── static/

&#x20;   ├── css/

&#x20;       └── style.css

&#x20;   

```



\## 🗄️ Database



\*\*Database Name:\*\* `housepriceprediction\_app`



The application uses two MySQL tables:



\*\*1. Users Table\*\*

\- Stores registered user information.

\- Maintains username, email, password, and user ID.



\*\*2. Predictions Table\*\*

\- Stores house price prediction details.

\- Maintains the user ID associated with each prediction.

\- Stores input features and predicted house price.

\- Helps users view their previous prediction history.



\## ⚙️ Application Workflow



1\. The user opens the web application.

2\. The user creates an account using the Sign Up page.

3\. The registered user logs in using email and password.

4\. Flask validates the login credentials using MySQL.

5\. After successful authentication, the user is redirected to the dashboard.

6\. The user enters the required housing information.

7\. Flask collects the input values and converts them into a NumPy array.

8\. The trained Machine Learning model predicts the house price.

9\. The predicted price is displayed on the result page.

10\. Prediction details are stored in MySQL.

11\. Users can view their previous predictions on their dashboard.



\## 🚀 Installation and Setup



\### Step 1: Clone the Repository



```bash

git clone https://github.com/your-username/House-Price-Prediction.git

```



\### Step 2: Navigate to Project Directory



```bash

cd House-Price-Prediction

```



\### Step 3: Create a Virtual Environment



```bash

python -m venv venv

```



Activate the environment:



\*\*Windows:\*\*

```bash

venv\\Scripts\\activate

```



\### Step 4: Install Dependencies



```bash

pip install -r requirements.txt

```



\### Step 5: Configure MySQL Database



Create the database `housepriceprediction\_app` in MySQL and configure the database connection details in `app.py`.



Ensure the required `users` and `predictions` tables are available.



\### Step 6: Run the Application



```bash

python app.py

```



Open your browser and visit:



```text

http://127.0.0.1:5000/

```



\## 📦 Requirements



Create a `requirements.txt` file containing:



```text

Flask

mysql-connector-python

numpy

joblib

scikit-learn

```



\## 🔮 Future Enhancements



\- Password hashing for improved security.

\- Admin dashboard for managing users and predictions.

\- Graphical representation of prediction history.

\- Improved user interface and responsive design.

\- Integration of additional Machine Learning algorithms.

\- Export prediction reports.



\## 👨‍💻 Author



\*\*Harsh Wadibhasme\*\*



\---



⭐ If you find this project useful, consider giving it a star!

