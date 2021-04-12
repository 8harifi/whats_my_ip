import socket
import requests

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


r = requests.get("https://api.ipify.org")


print(f"Host name: {hostname}")
print(f"IP Address: {ip}")
print(f"Public IP Address: {r.text}")