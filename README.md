# crdebugfr
## Chrome Debugging arbitrary file read.
this tool fo exploiting Google Chrome with debug port enabled.

further read: [counter webdriver](https://medium.com/@knownsec404team/counter-webdriver-from-bot-to-rce-b5bfb309d148)

## Installation
```python
pip3 install websockets
pip3 install beautifulsoup4
chmod +x crdebugfr.py
```

## Usage
supply host and file to read.
```bash
./crdebugfr.py <ip>:<port> <file_to_read>
```
![image](https://github.com/zulfi0/crdebugfr/assets/68773572/0418b132-3bd2-42e7-87b7-529ac76b1b86)


## References
- https://medium.com/@knownsec404team/counter-webdriver-from-bot-to-rce-b5bfb309d148
- https://chromedevtools.github.io/devtools-protocol/tot/Runtime/#method-evaluate
- https://blog.pentesteracademy.com/chrome-debugger-arbitrary-file-read-1ff2c41320d1
