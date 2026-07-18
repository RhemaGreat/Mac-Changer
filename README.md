# MAC Address Changer

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Linux](https://img.shields.io/badge/Platform-Linux-success)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

MAC Address Changer is a Python command-line utility that automates viewing and updating the MAC address of a network interface on Linux systems.

The project demonstrates Python scripting, command-line argument parsing, and interaction with Linux networking tools. It is intended for educational purposes, system administration, and authorized testing in laboratory environments.

---

## Features

- Display the current MAC address of a network interface
- Update the MAC address of a selected interface
- Command-line interface
- Input validation
- Clear status messages
- Lightweight implementation

---

## Technologies

- Python 3
- Linux
- subprocess
- argparse
- Regular Expressions (re)

---

## Repository Structure

```
Mac-Changer/
│
├── mac_changer.py
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.9+
- Linux
- Root privileges

No third-party Python packages are required unless your implementation specifies otherwise.

---

## Usage

Display the help menu:

```bash
python3 mac_changer.py --help
```

Example usage:

```bash
sudo python3 mac_changer.py --interface eth0 --mac 00:11:22:33:44:55
```

---

## Learning Objectives

This project demonstrates:

- Linux networking fundamentals
- MAC address concepts
- Command-line argument parsing
- Python automation
- System administration scripting

---

## Ethical Use

Only change the MAC address of devices that you own or are explicitly authorized to manage.

---

## Future Improvements

- Automatic MAC address generation
- Restore original MAC address
- Interface auto-detection
- Vendor-aware MAC generation
- Better error handling
- Logging
- Unit tests
- Cross-platform support (where applicable)

---

## Contributing

Contributions and suggestions are welcome through GitHub Issues and Pull Requests.

---

## Author

**Rhema Great**

GitHub: https://github.com/RhemaGreat

---

## License

Licensed under the MIT License.
