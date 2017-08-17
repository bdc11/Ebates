Ebates Assignment

Description
The script will use python to decode the viki API. The response of the API will be a JSON object containing a more key and response key. There are more JSON objects nested in response key and a flag key is inside the response key. We are interested in whether the HD key inside the flag key is either true or false. In order to reach the hd key nested in the flag key, we must first examine whether more key is true. If more key is true, there is more information available. This script will iterate through the API until no more data is available (more = false) and count the amount of times hd is true and false. Lastly, it will print out the amount of times hd is true and false. 

Name:
Email: 
Files:

I have included two commented-out debug lines. One will debug whether the script is able to connect to the API and the other will debug the count object. 

Python
I used python because code is easy to read and follow. The requests library also let's us easily connect to the API and parse it allowing for less code while still providing the goal of the assignment.  
I used the requsts module to connect to the API and set a counter to iterate the API url. I used a while loop increment the URL by a count of 1 continuously. In order to stop the loop from infinitely incrementing the page url, I set the while loop condition to more value is true. The loop will then search the page to see if more value is true, and if it is the loop will proceed to find and count the number of hd is true or false. The loop finally stopped at page 1000 when more is false.
