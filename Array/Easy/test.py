import socket

def get_local_ip():
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Connect to a public IP address
        sock.connect(('8.8.8.8', 80))
        # Get the local IP address
        local_ip = sock.getsockname()[0]
        return local_ip
    except socket.error:
        return None
    finally:
        # Close the socket
        sock.close()

# Call the function to get the local IP address
ip_address = get_local_ip()
if ip_address:
    print("Local IP address:", ip_address)
else:
    print("Unable to determine the local IP address.")
