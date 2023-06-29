# Smilescape Dental Web Application - Python & Django
**Heroku Deployed Application:** https://smilescape-ff81c76613c8.herokuapp.com/
## Brief Summary
- Personal Django Project to create a **Full Stack Web Application**.
- This project has **garnered significant attention from esteemed local dentists**, who have **expressed a keen interest in commissioning my skills to develop a web application tailored to their specific needs**.
## 🎯Aims and Motivation
- The **primary goal** of this project entailed the development of a comprehensive **Full Stack Web Application**, meticulously crafted during my **own personal time**, and **subsequently deployed** to **amplify my prowess** in both **Frontend and Backend technologies**.
- **Motivated** by an **unrelenting passion for knowledge and personal growth**, I undertook the creation of a **sophisticated Full Stack Web Application in order to expand my expertise in Frontend and Backend technologies**. The project has **garnered attention from local dentists**, who have **expressed a keen interest in my work**.
## ⚙️Technologies, Requirements and Software Tools
### Programming and Scripting Languages
- Python3
- Django Framework
- HTML5
- CSS3
- SCSS
- JavaScript & jQuery
### Pip Requirements
- Heroku (Deployment)
- asgiref==3.7.2 ; python_version >= '3.7'
- dj-database-url==0.5.0
- django==3.0.2
- django-on-heroku==1.1.2
- gunicorn==20.1.0
- psycopg2-binary==2.9.6 ; python_version >= '3.6'
- python-decouple==3.8
- pytz==2023.3
- setuptools==68.0.0 ; python_version >= '3.7'
- sqlparse==0.4.4 ; python_version >= '3.5'
- whitenoise==5.0.1
### Other Software Tools
- **Heroku** was used to **deploy the web application**.
- **Git** was used as a **Version Control System (VCS)** to **maintain a history of the software project**.
- **GitHub** was used to **host and maintain history of the project**.
## ✏️Design
### Web Application Wireframes
- **Wireframes** were **created to depict how the individual web pages would look from an architectural	perspective**.
- **Wireframes** were used as an **interestion** to the web applications **Information Architecture** and the **visual and infomration design**.
### Frontend Technology Stack
- **HTML** was utilised for **constructing templates and laying the foundation of the web application**, as well as **generating Django Templates** for each web page. **Django Template Tags** were used to **display information configured from the backend**.
- **CSS and SCSS** were employed to **enhance the website's visual appeal**, giving it a **polished and modern appearance** that is both **attractive and professional**.
- **JavaScript and jQuery** were **closely integrated** to **elevate** the frontend of this web application, **incorporating modern animations** such as **smooth transitions** and **interactive mouse events**. This was done to **enhance the user experience** and create a more **engaging, modern and dynamic web application**.
#### Frontend Technology Stack Summarisation Diagram:
<img width="714" alt="Screenshot 2023-06-29 at 10 38 33 pm" src="https://github.com/Saad1929/Smilescape-Dental-Website/assets/108022733/392fd76a-4472-4cfa-9668-8b61acd86f21">

### Backend Technology Stack
- **Python** was employed as the **backend programming language** for this web application, and the **Django Web Application framework** was utilised to develop the application. This combination allowed for **efficient server-side processing, seamless data management, and streamlined communication** between the **frontend and the backend components of the web application**.
#### Configuring Django Emails 
- **Django's Email capabilities** were utilised to **enable users to contact the dental practice for any sort of query as well as allowing patients to book appointments**. The **backend utilised specific Django Python functions** to **extract details from the contact and booking forms submitted through the frontend**.
#### Using SMTP4Dev (Testing)
- **SMTP4Dev** was utilised to **test the backend configuration of the contact and booking forms**. By using **SMTP4Dev**, **comprehensive testing was conducted** to ensure that the forms and backend data extraction were **fully functional** before **testing with different email providers**.
- To use SMTP4Dev, **Docker** was utilised with the following command: **`docker run --rm -it -p 3000:80 -p 2525:25 rnwood/smtp4dev`**. This command enabled the **containerisation of SMTP4Dev**, allowing it to **run and be accessed through specified ports for testing purposes**.
- SMTP4Dev Github: https://github.com/rnwood/smtp4dev

#### Using SMPT4 with Gmail
The following steps were used to connect SMTP4 with Gmail for this web application:
1. To work with SMTP4 with Gmail Email Provider, SMTP4 was downloaded using Docker and configured.
2. Settings.py was edited to allow the web application to recognsie and work with SMTP4.
Settings for Settings.py: 
SMTP server: smtp.gmail.com
Port: 587
TLS encryption
Authenticated  Gmail account credentials (username and application password)
3. Views.py was edited to connect to the send_mail function.

#### Backend Technology Stack SMTP4Dev Summarisation Diagram:
<img width="520" alt="Screenshot 2023-06-25 at 6 41 04 pm" src="https://github.com/Saad1929/Smilescape-Dental-Website/assets/108022733/b2542172-8f4d-484a-9562-9ac2d4ed030e">

## 🚀Heroku Deployment
- Upon completion of the web application, **Heroku** was utilised to **deploy** it to the internet. This allowed the **application to be accessible and functional online**.
- A **Procfile** was created which **specifies the commands** that are **executed by Heroku when deploying the website**.
- **Settings.py** was tweaked to **enable Heroku usage**. These changes can be found in **commit 9991a5f, labelled "Heroku Settings"**.
- A **requirements.txt** file was created and the code was **pushed up to Heroku** which **deployed the web application**.
**Heroku Deployed Application:** https://smilescape-ff81c76613c8.herokuapp.com/
