#!/usr/bin/env python
# Tool: Md5 Hash Decrypter
# Coded by: Marco Benz <Malek Ktiti>
# Team: FsocietyTN
##Contact:"Ktiti.malek@mail.ru".
import sys
import time
import urllib2
import urllib 
import re
import hashlib
#--------------------------------------------------------
class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
#--------------------------------------------------------
if len(sys.argv) < 2:
  print '\nUsage:'
  print '\t%s --00DAT [hash..] ' % sys.argv[0]
  sys.exit(1)
def banner():
  print bcolors.OKGREEN+ '''
  __       __      _______   ________  __    __  ________       
 |  \     /  \    |       \ |        \|  \  |  \|        \      
 | $$\   /  $$    | $$$$$$$\| $$$$$$$$| $$\ | $$ \$$$$$$$$      
 | $$$\ /  $$$    | $$__/ $$| $$__    | $$$\| $$    /  $$       
 | $$$$\  $$$$    | $$    $$| $$  \   | $$$$\ $$   /  $$        
 | $$\$$ $$ $$    | $$$$$$$\| $$$$$   | $$\$$ $$  /  $$         
 | $$ \$$$| $$ __ | $$__/ $$| $$_____ | $$ \$$$$ /  $$___       
 | $$  \$ | $$|  \| $$    $$| $$     \| $$  \$$$|  $$    \      
  \$$      \$$ \$$ \$$$$$$$  \$$$$$$$$ \$$   \$$ \$$$$$$$$
        +=============================================+
        |....... FsocietyTN Md5 Hash Decrypter .......|
        +---------------------------------------------+
'''
option   = sys.argv[1]
passwd   = sys.argv[2]
if option == '--00DAT':
    try:
      banner()
      def myaddr():
        site = 'http://md5.my-addr.com/'
        rest = 'md5_decrypt-md5_cracker_online/md5_decoder_tool.php'
        para = urllib.urlencode({'md5':passwd})
        req  = urllib2.Request(site+rest)
        try:
          fd   = urllib2.urlopen(req, para)
          data = fd.read()
          match= re.search('(Hashed string</span>: )(\w+.\w+)', data)
          if match: print bcolors.OKBLUE+'[+] Found %s\t\t[#]Password: %s' % (site, match.group(2))
          else: print bcolors.FAIL+'[-] site: %s\t\t\tPassword: Not Found' % site
        except urllib2.URLError: print bcolors.FAIL+'[*] site: %s \t\t[#] Error: Not Found' % site
      myaddr()
    except KeyboardInterrupt: print '\nTerminated by user ...'