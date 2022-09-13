# cookienapper
Python tool for kidnapping Chrome cookies from a target 

## Requirements
- Python3
- SOCKS proxy to target (might I interest you in [gTunnel](https://posts.specterops.io/get-your-socks-on-with-gtunnel-4a70a9b82b24)?)
- wscat installed on your host (`npm install -g wscat`)
- EditThisCookie extension in either Chrome or Firefox

## Usage
1. Kill all running Chrome sessions and then restore them with the Chrome debug port open (as seen in this [post](https://posts.specterops.io/hands-in-the-cookie-jar-dumping-cookies-with-chromiums-remote-debugger-port-34c4f468844e))
2. Edit cookienapper.py DEBUG_PORT variable to use the port you specified in previous step
3. `proxychains4 python3 cookienapper.py`
4. Copy the results from cookies.json and paste into the Import feature of EditThisCookie extension
5. ???
6. Profit (use cookies)

## References
- https://posts.specterops.io/hands-in-the-cookie-jar-dumping-cookies-with-chromiums-remote-debugger-port-34c4f468844e
