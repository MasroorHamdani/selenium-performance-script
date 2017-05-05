# selenium-performance-script
How to write performance script in selenium

###To setup local environment dependencies
1. Install python3.
   sudo apt-get install python3
2. See if it works and show version as 3.x.x
   python3
3. Install python3-dev
   sudo apt-get install python3-dev
4. Install python-virtualenv
   sudo apt-get install python-virtualenv
6. Create virtual environment.
   virtualenv pyvenv
7. Set its path
   virtualenv -p /usr/bin/python3.4 pyvenv
8. Activate it.
   source pyvenv/bin/activate
9. Install dependencies:
   pip3 install -r requirements.txt
10. Run selenium test cases
   python selenium-test/selenium/test_selenium.py