#!/usr/bin/env python
# Fixes the issue of duplicate Google Chrome Icons in Elementary OS Freya
# Uses method described in http://itsfoss.com/rid-google-chrome-icons-dock-elementary-os-freya/
import os
import getpass

def update_chrome(file_name, line_num, text):
    with open(file_name, 'r')as line:
    	lines = line.readlines()
    	lines[line_num] = text
    
    with open(file_name, 'w') as out:
	    out.writelines(lines)

user_name = getpass.getuser()
chrome_config = '/home/{}/.local/share/applications/google-chrome.desktop'.format(user_name)
os.system('cp /usr/share/applications/google-chrome.desktop {}'.format(os.path.dirname(chrome_config)))
update_chrome(chrome_config, 5, 'StartupWMClass=Google-chrome-stable\nGenericName=Web Browser\n')
