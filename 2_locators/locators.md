Locators
==========================

Identify element
action

2 types of locators

--> Built in
    --> id = ID
    --> name = NAME
    --> Linkedtext = LINK_TEXT
    --> Partial link = PARTIAL_LINK_TEXT
    --> class Name = CLASS_NAME
    --> Tag Name =TAG_NAME

--> Customised Locators
    --> CSS Selector 
        --> Tag and ID
        --> Tag and Class
        --> Tag and attribute
        --> Tag,class and attribute
    --> XPath
        --> Absolute XPath
        --> Relative XPath


single element --> driver.find_element() returns only the first matched element
multiple elements --> driver.find_elements()
            -- > use the CLASS_NAME OR TAG_NAME , XPATH, CSS SELECTORS to get multiple elements



