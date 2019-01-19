# MISSION STATEMENT

### System Description

![System description](https://github.com/adkulas/ece651-group-project/blob/Updating-Mission-Statement/overall_system.png)

The goal of this project is to build a Cloud-based personal health management system. Server-side application is deployed on a cloud service-based cloud server. The frontend is a smartphone app.In the first phase, an Android phone is considered as a client device, it is possible to expand to an iPhone app in the next phase. Also, the initial version of the system will only capture blood pressure and heart rate information. Once this data is succesfully captured and processed, the system capabilities could expand to add more information such as gym workout information, etc.

### Backend

![Backend](https://github.com/adkulas/ece651-group-project/blob/Updating-Mission-Statement/backend.png)

On the server side, all data received from the mobile app will be stored into a database indexed by the user’s name, date of birth or etc. The server shall be able to run a data analysis process to show, analyze and detect risk based on user data trend. Server application shall also be able to show a visual representation of user data via graphs or other on a webpage. It will enable doctors to monitor or review patient’s health status, evaluate and make decisions based on that health information.

### Android mobile app

![Frontend](https://github.com/adkulas/ece651-group-project/blob/Updating-Mission-Statement/frontend.png)

The Android phone app will provide data input functionalities for this system.  It can input blood pressure and heart rate information manually, or input via OCR (optical character recognition) based text auto reading from an image which is taken by phone camera. Android phone shall collect this blood pressure information – high, low, pulse, store most recent data on the phone and at the same time forward this information to the server and store them on the server permanently. Application also shall be able to visualize user data on the graph within GUI.

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
