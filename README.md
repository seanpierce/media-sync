# Media Sync
A python script to sync audio assets between an external drive and a remote sever. The script assumes that ssh is enabled on the remote server and there is a user set up to access the server via ssh.

## Installation
```shell
git clone [this repo]
```

## Dependencies
* Python
* sshpass: install on Mac by running `brew install hudochenkov/sshpass/sshpass`

## Configuration
Add the paths to the two locations that are intended to be sync'd to the config dict in sync.py file.
```python
config = {
  "local": "/path/to/Music/",
  "remote": "username@iporhostname:/path/to/Music/"
}
```

## Usage
* run `python [path/to/]sync.py`
* Enter the password for the ssh user that has access to the remote server
