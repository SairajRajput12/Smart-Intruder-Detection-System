from twilio.rest import Client

# Read text from the credentials file and store in data variable
with open('credential.txt', 'r') as myfile:
  data = myfile.read()

print(data) 
# Convert data variable into dictionary
info_dict = eval(data)

# Your Account SID from twilio.com/console
account_sid = info_dict['account_sid']

# Your Auth Token from twilio.com/console
auth_token  = info_dict['auth_token']

# Set client and send the message


client = Client(account_sid, auth_token)
message = client.messages.create( to =info_dict['your_num'], from_ = info_dict['trial_num'], body= "What's Up Man")