Ebates Assignment

Description

- The script will use python to decode the viki API.

- The response of the API will be a JSON object containing a more key and response key. 

- There are more JSON objects nested in response key. Inside the response key there is a flag key with a hd key inside the flag key.

- It will isolate and evaluate the hd key to see whether it returns true or false and to count the amounts of each.

- The script will iterate through the pages of the link by modifying the URL. It will continuously update the URL as long as more key returns true and will stop iterating once more key returns false. 


Name: Brandon 

Email: bdc11122@gmail.com

Files:


Python

- I used python because code is easy to read and follow. 

- The requests library let's us easily connect to the API and parse it.

- I set a counter to iterate the API url by updating the URL to the next page of data. This was accomplished by using a while loop to continuously increment it by 1. 

- In order to stop the loop from infinitely incrementing the page url, I set the while loop condition to more value is true. 

- The loop will then search the page to see if more value is true, and if it is the loop will proceed to find and count the number of times hd key is true or false. The loop finally stopped at page 1000 when more is false.
