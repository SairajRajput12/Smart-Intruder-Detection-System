---

# Intrusion Detection System

## Overview
This project is an Intrusion Detection System (IDS) developed using Python and OpenCV. It utilizes machine learning algorithms for facial recognition to detect intruders in a specified area. When an intruder is detected and moves out of the designated area, the system captures frames from when they entered and saves them on the local machine. Additionally, an SMS notification is sent to the owner to alert them of the intrusion.

## Features
- Face recognition using OpenCV and machine learning algorithms.
- Detection of intruders entering a specified area.
- Capturing frames of intruders upon entry and saving them locally.
- Sending SMS notifications to the owner when an intrusion is detected.
  
## Requirements
- Python 3.x
- OpenCV library
- Machine learning libraries (e.g., scikit-learn)
- SMS API (e.g., Twilio)

## Installation
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up the SMS API credentials (e.g., Twilio) in the `config.py` file.
4. Run the `main.py` script to start the intrusion detection system.

## Usage
1. Adjust the parameters in the `config.py` file according to your requirements, such as the area to monitor and SMS notification settings.
2. Run the `main.py` script to start the intrusion detection system.
3. Monitor the system for intrusions and check the saved frames and SMS notifications as needed.

## Contributing
Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request with your changes.



---

