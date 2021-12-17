from pythonosc.udp_client import SimpleUDPClient

ip = "192.168.1.167"
port = 10023

client = SimpleUDPClient(ip, port)  # Create client

client.send_message("/ch/04/mix/on", 0)
#client.send_message("/some/address", [1, 2., "hello"])  # Send message with int, float and string
