# TPO
<p>🏢Website developed for training and placement office to help them organize and motivate students much more efficiently. Also, to help them get better job opportunities.</p>
<br>

## Home page
![tp1](https://user-images.githubusercontent.com/17935364/93354040-364d4480-f85a-11ea-90b1-4e64da8c7865.png)



![tp2](https://user-images.githubusercontent.com/17935364/93354157-55e46d00-f85a-11ea-8cbb-bc28872f3c2e.png)

## Statistics related to placements
![tp3](https://user-images.githubusercontent.com/17935364/93354185-5aa92100-f85a-11ea-880c-75b369a46889.png)


## Chatbot handling FAQ of students
![tp4](https://user-images.githubusercontent.com/17935364/93354196-5d0b7b00-f85a-11ea-886f-1ef8acff5c7a.png)


## Statistics
![tp5](https://user-images.githubusercontent.com/17935364/93354208-60066b80-f85a-11ea-9593-40aecfe9bf0f.png)


## Registration for an event
![tp6](https://user-images.githubusercontent.com/17935364/93354246-6a286a00-f85a-11ea-9d87-9598b207b7ee.png)


## Admin related functions like adding users
![tp7](https://user-images.githubusercontent.com/17935364/93354269-6f85b480-f85a-11ea-88fa-ca117752b7aa.png)

![tp8](https://user-images.githubusercontent.com/17935364/93354282-74e2ff00-f85a-11ea-84a4-922d3815cb1f.png)












<h2>Getting Started</h2>
<p>Steps:</p>
<ol>
<li>Clone/pull/download this repository</li>
<li>Create a virtualenv with <code>virtualenv env</code> and install dependencies</li>
<li>Configure your .env files.</li>
<li>Activate the virtual env using <code>Scripts/activate</code></li>
<li>You've setup the virtual env and you're good to run the project.</li>
</ol>
<h2>Installation</h2>
<pre>pip install django</pre>
<pre>pip install django-bulma</pre>
<h2>Login</h2>

You can access the django admin page at http://127.0.0.1:8000/admin and login with username 'admin' and the password as admin123.
Also a new admin user can be created using
<pre>python manage.py createsuperuser</pre>
<h2>Usage</h2>
Go to TPO_website folder and run
<pre>python manage.py runserver</pre>
Then go to the browser and enter the url http://127.0.0.1:8000/


<h2>This project includes:</h2>


->Our project consists of sign in and login page for students as well for admin.

->Then comes the upcoming events section where the students can login for the events such as Training for Internships, Machine Learning, AR/VR and so on.

->Then it displays the list of current companies where you can apply for the role that you wished for.

->Also, it shows the results of the current rounds of the company.

-> We have also designed statistics of the previous years using chart.js and the user can also download the report of previous years.

->Lastly, we have implemented a chatbot so that the students can ask any questions regarding placement and current companies rounds, tentative dates or package.

