# P2P-FShare
## Peer to Peers Folder Sharing Tool
P2P FSHARE is a simple folder sharing tool that allows the users to share a folder consisting of multiple files(.txt, .jpg, .png, etc ) with multiple peers at one go.

## EXECUTION PROCEDURE :
Ensure that the systems between which the folders have to be shared are on a common network. Note the local IP addresses of each system in the network.

### Sending a folder :
1. Ensure a Python3 interpreter is available on the command line and Tkinter can be imported by running python3 interpreter on the command line and then within the interpreter entering:
   import tkinter

   If there’s an error then install Tkinter for the host operating system.

2. Run the program by the entering the following command:
   python3 input.py

3. A window will pop up on the screen with a field for Server IP and buttons for sending, receiving and browsing the file system.

   Choose which folder to share by clicking on Browse button and then selecting the required folder from the file explorer window which pops up.

4. Click on Send and then click OK in the confirmation dialog box.


### Receiving a folder (by one or more systems) :
1. As in the case of sending file ensure that Python3 interpreter and Tkinter are working. Then run the following command to start the program from command line:
   python3 input.py

2. The same window as in the case of sending file will pop up. Here fill the Server IP field with the IP of the system which will be sending the file.

3. click on Browse button and select the folder where you want the files of the sent folder to be transferred.
4. click on Receive button.



