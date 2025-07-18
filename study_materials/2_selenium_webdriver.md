Selenium WebDriver 
===================================

What is WebDriver ?

--> Webdriver is one of the component in Selenium
--> Webdriver is a module 
        firebox browser ---> Firefox()
        Chrome browser --> Chrome()
        Edge browser --> Edge()

--> Webdriver is an API

    ( GUI ) --> ( Application/web server / business logic / API ) --> ( Backend Data base )

    GUI Testing --> API Testing --> Database Testing or Backend Testing

    performance testing or non functional testing can be done at each level of architecture.

--> At Browser level AUT (application under test) 

    --> Automation code --> Webdriver --> Application
        --> web driver is taking those automation code and executing or interacting with the browser
        --> So here webdriver is acting as API only.

---- selenium 3.0
--> selenium client library (selenium python, selenium java, selenium Ruby etc..)
    --> selenium client library --> json --> browser driver
    --> client library communicate with browser driver via json wire protocol internally.

            --> client library -> json with web protocols --> browser driver --> w3c --> Browser

---- selenum 4.x
--> client library using w3c standards instead of using json with http protocols.
        --> client library -> w3c --> browser driver --> w3c --> Browser
--> download browser drivers for different browsers and keep them in one drive folder

--> create virtual env for the project
--> install selenium in your environment


