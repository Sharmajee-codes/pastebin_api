# importing the requests library
import requests
import csv
import time

# defining the api-endpoint 
API_ENDPOINT = "http://pastebin.com/api/api_post.php"

# your API key here
API_KEY = "9759beb19e35284d874b1b7a38fb6c43"


csvfile = open('sample.csv', 'r', encoding="Latin-1")
reader = csv.DictReader(csvfile)
out = reader


# your source code here


source_code = out

# data to be sent to api
data = {'api_dev_key':API_KEY,
		'api_option':'paste',
		'api_paste_code':source_code,
		'api_paste_format':'python'}

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)

# extracting response text 
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)



from twilio.rest import Client

#Find these values at https://twilio.com/user/account
account_sid = "AC6b47e19ec0753d96a3a2653525a39d47"
auth_token = "9aac62d3a94937acc363c2bffd0dd1d9"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+919992854050",
    from_="+1 855-910-9894 ",
    body="\nThe pastebin URL is : %s"%pastebin_url)
print("Done!")

time.sleep(2000000000000000000000000000000000000)