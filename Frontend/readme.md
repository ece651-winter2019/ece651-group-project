## Setup for Frontend Development Environment
This Frontend App uses Angular 7.x. 

### Before installing Nodejs
It is recommended to remove previous versions of Nodejs and npm before proceeding.
```
sudo apt-get purge nodejs npm
```
Then add the repository for the 8.x version of Nodejs. More details [here](https://github.com/nodesource/distributions#debinstall).
```
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
```
If the system throws the following error regarding the Google Repository:
```
E: Repository 'http://dl.google.com/linux/chrome/deb stable Release' changed its 'Origin' value from 'Google, Inc.' to 'Google LLC'
```
Then run
```
sudo apt update
```
And try adding the Nodejs repository again

### Install Nodejs
Install Nodejs, npm will also be installed automatically.
```
sudo apt-get install -y nodejs
```
Check versions
```
node -v
npm  -v
```
Should output
```
v8.15.0
6.4.1
```
respectively

### Install Angular client
```
sudo npm install -g @angular/cli
```
