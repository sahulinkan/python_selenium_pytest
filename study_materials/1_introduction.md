Selenium with Python - Introduction

Software testing is the process of finding defects in a software.
The goal is to release quality software to the customer/client.

1 ) Manual Testing
2 ) Automation Testing

Manual Testing - Testing software manually wheather it is working according to customer requirements or not.
Automation testing - Testing software by using automation tool.

MANUAL TESTING 
-----------------

Re-Testing
Regression Testing

Automation Testing
-------------------
Automation over comes the problems in manual testing.
                1) Reduce time
                2) Reduce human effort

AUT -> Application Under Test


    manual test case -> Automation tool -> AUT to be tested.

automation tool need test instruction to perform testing on application

how to convert manual test case to automation test case : By programming language

How to write automation test case ? By writing programming language- > Automation test script.

How automation tool will get data for test case ? test data attachment from excel file or test data files.


AUTOMATION TOOL : SELENIUM , PROGRAMMING LANGUAGE : PYTHON
-------------------------------------------------------------------

Advantages 
========================
1 ) Open source tool
2 ) Multiple operating system
3 ) supports multiple browser
4 ) Supports multiple language(java, python, c#, Ruby, Javascript etc..)
5 ) Integrate third party tools in to selenium

Disadvantages
==========================
1 ) desktop/window based application not supported (winapp,Robot API can be integrated with selenium )
2 ) limited to web applications - browsers ( selenium only designed for web browsers )
3 ) Mobile apps can not be automated 
4 ) Reporting not supported (pytest can be used with selenium )
5 ) graphs, captua not supported 
6 ) can not support excel file directly (python lib openpyxl can be added to use)
7 ) can not automate Angular JS application ( Protractor can be used along with selenium )

Note : selenium is not a single tool -----> collection of multiple component IDE,WebDriver, Grid, RC ( depricated ) ,etc ..

slenium started in 2004 

https://www.selenium.dev/ 