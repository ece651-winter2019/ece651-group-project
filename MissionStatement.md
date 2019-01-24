# MISSION STATEMENT

### Overview

The goal of this project is to build a cloud-based personal health management system. Personalized health management system can help patients to track their health related data comfortably, increase prevention, detect risks and make the communication between patient and doctor easier and more efficient.

### System Description

![System description](https://github.com/adkulas/ece651-group-project/blob/Updating-Mission-Statement/overall_system.png)

Server-side application is deployed on a service-based cloud server. The frontend is a smartphone app. In the first phase, an Android phone is considered as a client device, it is possible to expand to an iPhone app in the next phase. Also, the initial version of the system will only capture blood pressure and heart rate information. Once this data is succesfully captured and processed, the system capabilities could expand to add more information such as gym workout information, etc.

### Backend

![Backend](https://github.com/adkulas/ece651-group-project/blob/Updating-Mission-Statement/backend.png)

On the server side, all data received from the mobile app will be stored into a database indexed by the user’s name, date of birth or other. The server shall be able to run a data analysis process to show, analyze and detect risks based on user data trends. Server application shall also be able to show a visual representation of user data via graphs or other on a webpage. This webpage interface would enable doctors to monitor or review patient’s health status, evaluate and make decisions based on that health information.

### Mobile app

![Frontend](https://github.com/adkulas/ece651-group-project/blob/master/frontend_rev2.png)

The Android phone app will provide data input functionalities for this system. It would be able to input blood pressure and heart rate information manually, or input via OCR (optical character recognition) based text, auto reading from an image which is taken by phone camera. Android phone shall collect this blood pressure information – high, low, pulse, store most recent data on the phone and at the same time forward this information to the server and store them on the server permanently. Application shall also be able to visualize user data on a graph within the GUI.

### Server Side Software stack

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

### Mobile App Development Environment
* IDE: Android Studio
* Language: Java

## Team and responsibilities

Name | Responsibility
------------ | -------------
Adam Kulas | Continuous integration
Tong Liu | App development/OCR
Ammar Ahmed | Database design
Gabriel Richard | App development/Data processing
Samuel Akuma | Backend development/Server Setup
Juan Carrillo | Web App Development

### Methods and tools for project management

General goal of our project is to learn how to implement software engineering approach in a software development process. We will be focused on organizing our activities in such a manner, such thatt our work will be efficient and high quality. 

Our project is limited in time and there is no customer with a clear, set specification. The chosen development model will therefore be evolutionary iterative. This approach allows us to work step by step towards a final required specfication list appropriate for the personal health management system. At the beginning of each step we will specify new requirements for the given period of time and then go through the complete process of design, coding, testing and release. Thanks to that, our system will be growing from a simple minimum viable product with basic functionalities to one of a final complexity, reachable in the given time limit.

The length of our project sprints will be two weeks with regular weekly meetings where we will be discussing any issues or difficulties experienced during the current sprint and feedback based on the previous sprint's progress. Upcoming milestones will then be re-evaluated and the task list will be re-prioritized. Tasks will be defined in a form of user stories. Not yet implemented ideas will be archived in a backlog as well. Abandoned tasks will be archived and commented on as to why the tasks were abandoned.

Since our software includes development of a web and mobile application, a part of our project will be prototyping. We will create several wire frames to simulate user interfaces.

We will be using agile techniques for team collaboration with the advantage of parallel working, so that the development of our software is more efficient. Each team member will be responsible for a specific part of the development process, according to his skills and previous experience. In order to get feedback from team members working on closely related tasks, there will be on demand meetings.

Communication within our team is supported by Slack, allowing us to divide the chats into channels based on the topic – general, cloud server development, app development etc.

All our work will be managed via Github. We will use its tools for creating shared documents, keeping track of our progress and mainly for version control of our source code. We would also like to implement automated tests with help of Github related services such as Travis CI.
