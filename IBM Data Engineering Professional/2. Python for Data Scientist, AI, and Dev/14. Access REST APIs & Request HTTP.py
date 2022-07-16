import requests
import os 
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)
r.status_code

#output
<Response [200]>

------------------------------------------------------------------------------------------------------------------------
#REQUEST HEADER AND BODY
print(r.request.headers)

#OUTPUT
{'User-Agent': 'python-requests/2.28.1', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive',
 'Cookie': '_abck=CF31AF5CAB370D15CFA81D83D66831D4~-1~YAAQz2UzuOOuWPqBAQAAahhFBwj1w5+QEWvdMOC/fhbWoVcfr6OrvjE2tSuQ5LRf3j8MxCiIF+yoI2zyFLqOiyYKLJj0H3bPQK1wSTst0q8U0nOpbcWjkrNNVBcZkgmPrcWKD1+VjsoEs8NeFVR6T2uplkP7yuoweAPoip/+ZOOsO/yPEwAcrDPRpqMMIeJPfrel541jLgZttvoaC2fLoDwBPtB35O7RTtw2N2VVA+kutcx2bHedllRg0d+3zi6LSZgr0LIjNCenR7d5V+lJBqYWdqF7fkQ+kYPgArHqSIy/g6QMhP/ZFdtNcJyNDZv5P/S5c2EywU6Q0Y6ZSwfa2+CX7HeIAY+BR+dk3LU9YHkg7zlLfok=~-1~-1~-1; bm_sz=C0DD7B37280F4EC971AB05E23853E4C9~YAAQz2UzuOSuWPqBAQAAahhFBxBByAnKOG6tj68Htb/ztKUUv9ZVlrpvfCaYrYixrDlXkw1pL3YnAMZVpe41fAECWhSjnH9RsDQjtSDhsOl5eTBsveZeEo3uFISlmMqr707L84Q8qWoOimsJhomYRDdGmDYt59GBei+DV5d31tnIi5SwCRYdUVJaY8w43j5ASPbB9KFR34D7Nx7lqdrIoNR2KscmcxE5CuqODB/6qi7xvAwm4HC02pf4C7TxQF0ssr50RNykYirHxV3c2opDA7qj+8fvxO/JTrLw7InamkQ=~3359282~3683141'}




#REQUEST BODY - You can view the request body, in the following line, as there is no body for a get request we get a None:
print("request body:", r.request.body)

#output
request body: None
  
------------------------------------------------------------------------------------------------------------------------
# VIEW RESPONSE ATTRIBUTE HEADER - You can view the HTTP response header using the attribute headers. This returns a python dictionary of HTTP response headers.
header=r.headers
print(r.headers)

#output
{'Cache-Control': 'max-age=301', 'Expires': 'Fri, 15 Jul 2022 16:46:25 GMT', 'Last-Modified': 'Fri, 15 Jul 2022 16:31:10 GMT', 'ETag': '"17159-5e3da8bb904f3"', 'Accept-Ranges': 'bytes', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'X-Akamai-Transformed': '9 19596 0 pmb=mTOE,2', 'Date': 'Sat, 16 Jul 2022 13:49:05 GMT', 'Content-Length': '19759', 'Connection': 'keep-alive', 'Vary': 'Accept-Encoding', 'x-content-type-options': 'nosniff', 'X-XSS-Protection': '1; mode=block', 'Content-Security-Policy': 'upgrade-insecure-requests', 'Strict-Transport-Security': 'max-age=31536000'}



#SPECIFIC KEY - We can obtain the date the request was sent using the key Date
header['date']
#output
'Sat, 16 Jul 2022 13:49:05 GMT'

#Content-Type indicates the type of data:
header['Content-Type']
#output
'text/html'


------------------------------------------------------------------------------------------------------------------------
#You can also check the encoding:
r.encoding
#output
'ISO-8859-1'



#As the Content-Type is text/html we can use the attribute text to display the HTML in the body. We can review the first 100 characters:
r.text[0:100]
#output
'<!DOCTYPE html><html lang="en-US"><head><meta name="viewport" content="width=device-width"/><meta ch'


------------------------------------------------------------------------------------------------------------------------
#You can load other types of data for non-text requests, like images. Consider the URL of the following image:
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r=requests.get(url)
print(r.headers)

#output
{'Date': 'Sat, 16 Jul 2022 14:15:46 GMT', 'X-Clv-Request-Id': 'f17e6aab-1d35-4758-8d30-f2a7689d004d', 'Server': 'Cleversafe', 'X-Clv-S3-Version': '2.5', 'Accept-Ranges': 'bytes', 'x-amz-request-id': 'f17e6aab-1d35-4758-8d30-f2a7689d004d', 'Cache-Control': 'max-age=0,public', 'ETag': '"a831e767d02efd21b904ec485ac0c769"', 'Content-Type': 'image/png', 'Last-Modified': 'Thu, 16 Jun 2022 16:00:05 GMT', 'Content-Length': '21590'}



#We can see the 'Content-Type'
r.headers['Content-Type']
#output
'image/png'



#An image is a response object that contains the image as a bytes-like object.
#As a result, we must save it using a file object. First, we specify the file path and name
path=os.path.join(os.getcwd(),'image.png')
path
#output
'/resources/labs/image.png'



#We save the file, in order to access the body of the response we use the attribute content then save it using the open function and write method:
with open(path,'wb') as f:
 f.write(r.content)
    
Image.open(path)  #view the image
#output
sebuah gambar

------------------------------------------------------------------------------------------------------------------------
#QUESTION 1
#In the previous section, we used the wget function to retrieve content from the web server as shown below. Write the python code to perform the same task.
#The code should be the same as the one used to download the image, but the file name should be 'Example1.txt'.

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path = os.path.join(os.getcwd(), 'example1.txt')
r = requests.get(url)
with open(path,'wb') as f:
 f.write(r.content)
 
------------------------------------------------------------------------------------------------------------------------
#Get Request with URL Parameters

url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r = requests.get(url_get,params=payload)
r.url
#output
'http://httpbin.org/get?name=Joseph&ID=123'

print("request body:", r.request.body)
print(r.status_code)
#output
request body: None
200



#View the response text
print(r.text)
#output
{
  "args": {
    "ID": "123", 
    "name": "Joseph"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.28.1", 
    "X-Amzn-Trace-Id": "Root=1-62d2d22f-76b8a3e5690055176b323273"
  }, 
  "origin": "150.239.85.244", 
  "url": "http://httpbin.org/get?name=Joseph&ID=123"
}



#content type
r.headers['Content-Type']
#output
'application/json'



#As the content 'Content-Type' is in the JSON format we can use the method json(), it returns a Python dict:
r.json()
#output
{'args': {'ID': '123', 'name': 'Joseph'},
 'headers': {'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Host': 'httpbin.org',
  'User-Agent': 'python-requests/2.28.1',
  'X-Amzn-Trace-Id': 'Root=1-62d2d22f-76b8a3e5690055176b323273'},
 'origin': '150.239.85.244',
 'url': 'http://httpbin.org/get?name=Joseph&ID=123'}




#The key args has the name and values:
r.json()['args']
#output
{'ID': '123', 'name': 'Joseph'}

------------------------------------------------------------------------------------------------------------------------
#POST
url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)
#OUTPUT
POST request URL: http://httpbin.org/post
GET request URL: http://httpbin.org/get?name=Joseph&ID=123

  

#compare the POST and GET request body, we see only the POST request has a body:
print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)
#output
POST request body: name=Joseph&ID=123
GET request body: None
 


r_post.json()['form']
#output
{'ID': '123', 'name': 'Joseph'}
