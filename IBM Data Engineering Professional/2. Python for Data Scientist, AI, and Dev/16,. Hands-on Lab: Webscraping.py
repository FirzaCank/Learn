!mamba install bs4==4.10.0 -y
!pip install lxml==4.6.4
!mamba install html5lib==1.1 -y
# !pip install requests==2.26.0

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

#Store string in variable HTML
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, "html.parser")

#method prettify() to display the HTML in the nested structure:
print(soup.prettify())
#output
<!DOCTYPE html>
<html>
 <head>
  <title>
   Page Title
  </title>
 </head>
 <body>
  <h3>
   <b id="boldest">
    Lebron James
   </b>
  </h3>
  <p>
   Salary: $ 92,000,000
  </p>
  <h3>
   Stephen Curry
  </h3>
  <p>
   Salary: $85,000, 000
  </p>
  <h3>
   Kevin Durant
  </h3>
  <p>
   Salary: $73,200, 000
  </p>
 </body>
</html>

------------------------------------------------------------------------------------------------------------
#Tag title

tag_object=soup.title
print("tag object:",tag_object)

#output
tag object: <title>Page Title</title>
  



#we can see the tag type <code>bs4.element.Tag</code>
print("tag object type:",type(tag_object))
#output
tag object type: <class 'bs4.element.Tag'>

  
  
  
tag_object=soup.h3
tag_object
#output
<h3><b id="boldest">Lebron James</b></h3>

------------------------------------------------------------------------------------------------------------
#Children, Parents, and Siblings

#access the child of the tag or navigate down the branch 
tag_child =tag_object.b
tag_child

#output
<b id="boldest">Lebron James</b>



#Access the parent with the  parent
parent_tag=tag_child.parent
parent_tag
#output
<h3><b id="boldest">Lebron James</b></h3>

#this is identical to
tag_object
#output
<h3><b id="boldest">Lebron James</b></h3>

#tag_object parent is the body element.
tag_object.parent
#output
<body><h3><b id="boldest">Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body>
     
#tag_object sibling is the paragraph element
sibling_1=tag_object.next_sibling
sibling_1
#output
<p> Salary: $ 92,000,000 </p>

#sibling_2 is the header element which is also a sibling of both sibling_1 and tag_object
sibling_2=sibling_1.next_sibling
sibling_2
#output
<h3> Stephen Curry</h3>

------------------------------------------------------------------------------------------------------------
#HTML ATTRIBUTES

#If the tag has attributes, the tag id="boldest" has an attribute id whose value is boldest. 
#You can access a tag’s attributes by treating the tag like a dictionary:
tag_child['id']
#output
'boldest'



#access that dictionary directly as attrs
tag_child.attrs
#output
{'id': 'boldest'}



#obtain the content if the attribute of the tag using the Python get() method.
tag_child.get('id')
#output
'boldest'

------------------------------------------------------------------------------------------------------------
#Navigable String

tag_string=tag_child.string
tag_string
#output
'Lebron James'



#verify the type is Navigable String
type(tag_string)
#output
bs4.element.NavigableString



#A NavigableString is just like a Python string or Unicode string, to be more precise.
#The main difference is that it also supports some BeautifulSoup features. We can covert it to sting object in Python:
unicode_string = str(tag_string)
unicode_string
#output
'Lebron James'

------------------------------------------------------------------------------------------------------------
#FILTER
#Filters allow you to find complex patterns, the simplest filter is a string.
#In this section we will pass a string to a different filter method and Beautiful Soup will perform a match against that exact string.

#Consider the following HTML of rocket launchs:
%%html
<table>
  <tr>
    <td id='flight' >Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
   </tr>
  <tr> 
    <td>1</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>
    <td>80 kg</td>
  </tr>
</table>

#OUTPUT
Flight No	Launch site	Payload mass
1	Florida	300 kg
2	Texas	94 kg
3	Florida	80 kg



#We can store it as a string in the variable table:
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, "html.parser")

------------------------------------------------------------------------------------------------------------
#find All
#The find_all() method looks through a tag’s descendants and retrieves all descendants that match your filters.
#The Method signature for find_all(name, attrs, recursive, string, limit, **kwargs)

#Name
table_rows=table_bs.find_all('tr')
table_rows
#output
[<tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>,
 <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr>,
 <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>,
 <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr>]



first_row =table_rows[0]
first_row
#output
<tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>



#The type is tag
print(type(first_row))
#output
<class 'bs4.element.Tag'>



#we can obtain the child
first_row.td
#output
<td id="flight">Flight No</td>



for i,row in enumerate(table_rows):
    print("row",i,"is",row)
#output
row 0 is <tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>
row 1 is <tr> <td>1</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a></a></a></td><td>300 kg</td></tr>
row 2 is <tr><td>2</td><td><a href="https://en.wikipedia.org/wiki/Texas">Texas</a></td><td>94 kg</td></tr>
row 3 is <tr><td>3</td><td><a href="https://en.wikipedia.org/wiki/Florida">Florida<a> </a></a></td><td>80 kg</td></tr>
