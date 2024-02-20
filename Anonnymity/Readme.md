# MAC Address Changer

## Overview
This Python script is designed to change the MAC (Media Access Control) address of a network interface on a Linux system. It takes the interface name and the new MAC address as input and uses the `ifconfig` command to change the MAC address.

## Usage
To use this script, follow these steps:
1. Open a terminal.
2. Navigate to the directory containing the script.
3. Run the script with the following command:
``` bash
python mac_changer.py -i [interface] -m [new_mac_address]
```
Replace `[interface]` with the name of the interface whose MAC address you want to change and `[new_mac_address]` with the new MAC address you want to assign to the interface.

## Requirements
- Python 2.7 or later
- Linux operating system

## Installation
No installation is required. Simply download the script and run it using Python.

## Options
- `-i` or `--interface`: Specifies the name of the network interface whose MAC address you want to change.
- `-m` or `--mac`: Specifies the new MAC address that you want to assign to the interface.

## Functions
1. `get_arguments()`: Parses the command-line arguments and returns the options.
2. `change_mac(interface, new_mac_address)`: Changes the MAC address of the specified interface to the new MAC address.
3. `current_mac(interface)`: Retrieves the current MAC address of the specified interface.

## Example
Here's an example of how to use the script:
``` bash
python mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

## Notes
- This script should be run with root privileges (`sudo` or as the root user) to change the MAC address.
- Changing the MAC address of a network interface may cause network connectivity issues or violate network policies. Use it responsibly and only on networks you own or have permission to modify.

## References
- [ifconfig man page](https://man7.org/linux/man-pages/man8/ifconfig.8.html)
- [Python subprocess module documentation](https://docs.python.org/3/library/subprocess.html)
- [Python optparse module documentation](https://docs.python.org/2/library/optparse.html)

## Author
Vishesh Singh

## License
This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Version History
- [Version 1.0](https://github.com/your-username/mac-changer/releases/tag/v1.0): Initial release

## Feedback
If you have any feedback or suggestions for improving this script, please open an issue on the [GitHub repository](https://github.com/visheshoffice/cybersecurity-projects/).
