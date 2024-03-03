import requests

print('imported succesfully')


# apiSecrete = "637ff89ec87ce7d861a4b94ef4322191b3d7e4ed" 
# device_id = "00000000-0000-0000-9943-bb661bd63709" 
# phone  = "+919359876429" 
# message = "No God ! Only man in the blue sky !!!!.\n I am Homelander I will do what the fuck i want!!"

# message = {
#     "secret": apiSecrete, 
#     "mode":"devices", 
#     "device":device_id, 
#     "sim":1, 
#     "priority":1, 
#     "phone":phone, 
#     "message":message
# }

# r = requests.post(url = "https://www.cloud.smschef.com/api/send/sms",params=message) 

# result = r.json() 
# print(result) 


# another way:

resp = requests.post('https://textbelt.com/text', {
  'phone': '+919359876429',
  'message': 'Hello world',
  'key': 'textbelt',
})

