**Friendly chat server so you can chat with your friends without even needing browser access**

1. Run server.py and follow instructions: make sure you use your **private** ip address
2. On the other user's machine, type in 'nc [server ip] 8000'    
**Note**: This program requires Netcat to run, which is not installed on Windows by default, so install it if you need to (refer to section below)        
4. **Only works if both devices are on the same network, currently working to improve**

Commands:

/recent: View the most recent message        
/exit: Exit the chat

**For Windows computers**:    

1. Download the Git for Windows installer from git-scm.com         
2. Run 'Git-<version>-64-bit.exe /VERYSILENT /NORESTART /SILENT /SP-' in Command Prompt      
3. Verify with 'git --version'
4. Download this repo with 'git clone https://github.com/shliu888/chat-server-for-school.git'           
5. After downloading this repo, use "cd" to see which directory you are in. **Run the script only from this directory**     
6. Run 'python3 install_netcat.py'
7. Run 'ipconfig' 
8. Run 'python3 server.py'      
9. Enter the IP of your computer when prompted         
10. On the computer you want to communicate with, enter "nc [server ip] 8000" (install Netcat if needed)      
