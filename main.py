import socket

def scan_ports(target, start_port, end_port):
    """Scans ports on the target host and returns a list of open ports."""
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                sock.connect((target, port))
                open_ports.append(port)
                print(f"Port {port}: OPEN")
        except Exception as e:
            # Log or print a more informative error message for debugging
            print(f"Error scanning port {port}: {e}")

    return open_ports


def main():
    """Prompts for the target IP address and port range, then performs a port scan."""
    # Prompt for target IP address
    target_ip = input("Enter the target IP address: ")

    # Define port range
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    # Perform port scan
    open_ports = scan_ports(target_ip, start_port, end_port)

    # Print the list of open ports
    print("Open ports:", open_ports)


if __name__ == "__main__":
    main()
