import re

# emails = [
#     "mverma6250@gmail.com",
#     "ramesh02@hotmail.com",
#     "sohansingh@gmail.com",
#     "swatirahane@outlook.com"
# ]

# masked_emails = []

# for email in emails:
#     parts = re.split(r'@', email)  # Split into username and domain
#     username = parts[0]
#     domain = parts[1]
    
#     if len(username) >= 2:
#         masked = username[0] + '*' * (len(username) - 2) + username[-1]
#     else:
#         masked = username[0] + '*'
    
#     masked_email = masked + '@' + domain
#     masked_emails.append(masked_email)

# print(masked_emails)



logs = [
    "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2",
    "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2",
    "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2",
    "/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22",
    "/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2",
    "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28",
    "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31",
    "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2"
]

unqIps = set()

for ips in logs:
    parts = ips.split('server/')
    unqipadderess = unqIps.add(parts[1])

print(list(unqIps))