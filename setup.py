import os
import sys
from setuptools import setup
import distutils

class copy:
    def copyFiles(self):
        if os.name == "nt":   
            distutils.dir_util.copy_tree("HelloWorld","C:\\HelloWorld")
            
            if not os.path.exists("C:\\HelloWorld\\logs"):
                os.makedirs("C:\\HelloWorld\\logs")
        
        elif os.name == "posix":
            distutils.dir_util.copy_tree("HelloWorld","/var/www/HelloWorld")
            
            if not os.path.exists("/var/www/HelloWorld/logs"):
                os.makedirs("/var/www/HelloWorld/logs")


if __name__ == "__main__":
    c=copy()
    c.copyFiles()
    if sys.argv[1] == "install":        
        if os.name == 'nt':
            os.system("python %s %s" %(os.path.join(os.path.dirname(__file__),"dependency.py"),"install"))         
        elif os.name =='posix':
            os.system("sudo python %s %s" %(os.path.join(os.path.dirname(__file__),"dependency.py"),"install"))
    if sys.argv[1] == "help":
       print """The setup installs the package 'TxSmartQWebPortal' in \var\www incase of Linux OS and C:\\inetpub incase of Windows OS.
Also the setup installs the required dependencies to run the project.Use setup.py install command to run the setup"""
    
