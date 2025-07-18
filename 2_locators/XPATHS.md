XPATH
=====================

xpath is defined as XML path.
it is a syntax or language for finding any element on the web page using XML path expression.
XPATH is used to find the location of any element on the web page using HTML DOM structure.
XPATH will go through the nodes in DOM structure and find the element.

XPATH can be used to navigate through elements and attributes in DOM.
XPATH is an address of the element.

very effective compared to other locators

Types of XPATHS
========================

1 ) Absolute / Full xpath   :  Ex : /html/body/nav/div/div/div[2]/ul/li[2]/a/button
2 ) Relative / Partial xpath : Ex : //*[@id="navbarSupportedContent"]/div[2]/ul/li[2]/a/button

## difference between full and partial xpath or absolute and relative xpath 
==============================================================================

relative xpath does not start from html root node,rather it jumps to node we are searching directly.

full or absolute xpath always starts from the root html node always.

In relative xpath we have to give the attribute explicitly.

relative xpath syntax : "//tagname[@attribute='value']" so here the xpath goes to the element directly. does not start from the beginning.
relative xpath always starts with double slash "//"

absolute xpath or full xpath : starts with single '/'.
                            : full path do not use attribute


## How to write XPATHS Manually
====================================

absolute xpath : /html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a

relative xpath : syntax of writing : start with double slash "//tagname[attribute='value']"

                    Ex : "//input[@id='small-searchterms']"

** mostly used xpath is relative xpath
** relative xpath is more stable than absolute xpath
** as absolute always starts from the beginning . it takes time as well
** if new element added in between by developer then the flow will break, so absolute xpath is unstable.
** prefer to use relative xpath.

## How to capture xpath automatically ? 
===========================================

1 ) use browser in built option to copy the xpath of any element
2 ) extension selector hub available for all browsers we can use ,it gives all kind of locators as well.
3 ) How to use selector hub in browser 

## XPATH OPTIONS
=======================

and ex : "//input[@type='search' and @class='search-keyword' ]"
or ex : "//input[@type='search' or @class='search-keyword' ]"
contains() ex: //a[contains(@class,'cart-header-navlink')]
starts-with() ex: //span[starts-with(@class,'r')]
text() ex: //a[text()='Flight Booking']


