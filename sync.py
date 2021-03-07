"""
This script is intended to sync audio/ media files between a local location and a remote location.
The script ignores files that have already been migrated.
"""

import os
from getpass import getpass

# define local and remote locations
config = {
  "local": "/path/to/Music/",
  "remote": "username@iporhostname:/path/to/Music/"
}

password = getpass()

# sync files from disk to remote
print('=== Syncing files from disk to remote drive ===')

try:
    os.system("sshpass -p %s rsync -a --ignore-existing --progress %s %s" %(password, config['local'], config['remote']))
except BaseException as ex:
    print("Unable to sync files from disk to remote drive. Error: %s" %(ex))
    sys.exit() 

# sync files from remote to disk
print('=== Syncing files from remote drive to disk ===')

try:
    os.system("sshpass -p %s rsync -a --ignore-existing --progress %s %s" %(password, config['remote'], config['local']))
except BaseException as ex:
    print("Unable to sync files from remote drive to disk. Error: %s" %(ex))
    sys.exit()

print('Success!')
