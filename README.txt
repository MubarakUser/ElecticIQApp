This framework is implemented using the below tools/language:
Python
Selenium
Behave(BDD)

BDD uses Ghekin language to write feature files and test scenarios/functions are written under ./Feature/steps folder

Environment:
-----------

Linux

Pre-requisites:
1. Install latest chrome browser
2. Install latest chrome driver wich is compatible with installed chrome browser version.
Please move the downloaded chromedriver to './Resources/chrome_linux/'

Steps to execute:
-----------------

1. Clone the git repository https://github.com/MubarakUser/ElecticIQApp.git
2. Change the directory to ElecticIQApp
3. Run pip3 install -r requirements.txt(This will donwload the dependencies)
4. Run "Behave ./features --no-capture
5. we will be able to see the results in console

For html reporting:
-------------------
1. Run behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports

2. Here AllureReports is folder name

3. it will generate .json files in the above folder

4. Donwload allure commandliner, we need this because to generate html report from the json files where
we just created

https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.0/

5. Download zip file

6. set the below in environmental variables

7. Run allure serve .\ElecticIQApp

8. Tt will start the server and open up browser with html report










