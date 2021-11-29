# Lucy's choreographers
Alice Montori  alice.montori2@studio.unibo.it

Marta Stella   marta.stella@studio.unibo.it

## Instructions
To execute in the virtual machine:

**1. Install VLC and GIT:**
```bash
  sudo apt-get update
  sudo apt-get install vlc git
```
**2. Download the repository:**
```bash
  git clone 
```
**3. Get the needed Python3 tools:**
```bash
  cd "Lucy's choreographers"
  pip3 install -U pip setuptools
  sudo apt-get install python3-venv
```
**4. Prepare the virtual environment:**
```bash
  python3 -m venv venv
```
**5. Install the Python3 dependencies:**
```bash
  . venv/bin/activate
  pip3 install -r requirements.txt
  deactivate
```
**6. Run the script:**
```bash
  cd "Lucy's choreographers"
  . venv/bin/activate
  python3 main.py localhost <port>
  deactivate
```
**To run the script, Choreograph must be opened with a proper virtual robot available for external connections**

