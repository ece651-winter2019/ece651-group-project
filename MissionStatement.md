# MISSION STATEMENT

### Overview

The goal of this project is to build a Cloud-based personal health management system.

### System Description

![System description](https://github.com/adkulas/ece651-group-project/blob/Updating-Mission-Statement/overall_system.png)

Server-side application is deployed on a cloud service-based cloud server. The frontend is a smartphone app. In the first phase, an Android phone is considered as a client device, it is possible to expand to an iPhone app in the next phase. Also, the initial version of the system will only capture blood pressure and heart rate information. Once this data is succesfully captured and processed, the system capabilities could expand to add more information such as gym workout information, etc.

### Backend

![Backend](https://github.com/adkulas/ece651-group-project/blob/Updating-Mission-Statement/backend.png)

On the server side, all data received from the mobile app will be stored into a database indexed by the user’s name, date of birth or etc. The server shall be able to run a data analysis process to show, analyze and detect risk based on user data trend. Server application shall also be able to show a visual representation of user data via graphs or other on a webpage. It will enable doctors to monitor or review patient’s health status, evaluate and make decisions based on that health information.

### Android mobile app

![Frontend](https://github.com/adkulas/ece651-group-project/blob/Updating-Mission-Statement/frontend.png)

The Android phone app will provide data input functionalities for this system. It can input blood pressure and heart rate information manually, or input via OCR (optical character recognition) based text auto reading from an image which is taken by phone camera. Android phone shall collect this blood pressure information – high, low, pulse, store most recent data on the phone and at the same time forward this information to the server and store them on the server permanently. Application also shall be able to visualize user data on the graph within GUI.

### Software stack

Languages
* Python
* Javascript
* C#

Web Frameworks
* Pyramid
* Django
* Flask

Frontend
* Vue.js
* React
* Ember

Versioning tools
* GitHub :octocat: 

## Team and responsibilities

Name | Responsibility
------------ | -------------
Adam Kulas | Continuous integration
Megi Mejdrechova | Device sensors
Tong Liu | Device sensors
Ammar Ahmed | Database desing
Gabe Richard | Data processing
Samuel Akuma | Backend development
Juan Carrillo | Frontend development

### Methods and tools for project management

General goal of our project is to learn how to implement software engineering approach in a process of software development. We will be focused on organizing our activities in such a manner, so that our work will be efficient and high quality. 

Our project is limited in time and there is no customer with a clear, set specification. The chosen model will therefore be evolutionary iterative. This approach allows us to work step by step towards a final personal health management system. At the beginning of each step we will specify new requirements for the given period of time and then go through the complete process of design, coding, testing and release. Thanks to that, our system will be growing from a simple one with basic functionalities to one of a final complexity reachable in the given time limit.

The length of our project steps will be two weeks with regular personal meetings where we will be discussing feedback from the previous step and goals for the following one. Goals will be defined in a form of user stories. Abandoned or not yet implemented ideas will be archived as well. 

Since our software includes development of a web and mobile application, a part of our project will be prototyping. We will create several wire frames to simulate user interface.

We will be using agile technics for team collaboration with the advantage of parallel working, so that the development of our software is faster. Each team member will be responsible for a specific part of the development according to his skills and previous experience. In order to get feedback from team members working on closely related tasks, there will be on demand meetings.

Communication within our team is supported by Slack, allowing us to divide the chats into channels based on the topic – general, cloud server development, app development etc.

All our work will be managed by GitHub project. We will use its tools for creating shared documents, keeping track of our progress and mainly for version control of our source code. We would also like to implement automated tests with help of Github.
