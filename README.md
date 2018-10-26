# ![logo](/asset/LINE-sm.png) LINE Python

 [![Version 3.0.8](https://img.shields.io/badge/beta-3.0.8-brightgreen.svg "Version 3.0.8")](https://pypi.python.org/pypi/linepy) [![LICENSE](https://img.shields.io/badge/license-BSD%203%20Clause-blue.svg "LICENSE")](https://github.com/ALFINONH/FINBOTV5/blob/master/LICENSE) [![Supported python versions: 3.x](https://img.shields.io/badge/python-3.x-green.svg "Supported python versions: 3.x")](https://www.python.org/downloads/)
 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ALFINONH/FINBOTV5)


----

## Requirement

The linepy module only requires Python 3. You can download from [here](https://www.python.org/downloads/). 

## Installation

Installation is simple. It can be installed from pip using the following command:
```sh
$ pip install linepy
```
Or from the code:
```sh
$ python setup.py install
```

## Usage

```python
>>> from linepy import *
>>> line = LINE('EMAIL', 'PASSWORD')
>>> line.log("Auth Token : " + str(line.authToken))
```

## Updates

From pip using the following command:
```sh
$ pip install linepy --upgrade
```

# ই۝🄵🄸🄽 🄱🄾🅃۝ईई V5.0

![finbotv5.0](log.gif)

<a href="https://line.me/R/ti/p/~kangnur04"><img height="36" border="0" alt="Add Friend" src="https://scdn.line-apps.com/n/line_add_friends/btn/en.png"></a>

# ![logo](asset/imgs.png)
You can generate spotify token from [here](https://spotify-token-finder.herokuapp.com). 

    c.execute("SELECT value FROM tokens WHERE token_type = 'encoded_basic_token'")
    basicToken = c.fetchone()[0]
    c.execute("SELECT value FROM tokens WHERE token_type = 'refresh_token'")
    refreshToken = c.fetchone()[0]

    reqHeader = {'Authorization': 'Basic {}'.format(basicToken)}
    reqBody = {'grant_type': 'refresh_token', 'refresh_token': refreshToken}
    r = requests.post('https://accounts.spotify.com/api/token', headers=reqHeader, data=reqBody)
    resJson = r.json()
    
    newToken = resJson['access_token']
    # update token in db
    c.execute("UPDATE tokens SET value = ? WHERE token_type = 'access_token'", (newToken,))
    conn.commit()

```

The script pulls new translations (ts files) from transifex.
If some new translations are found,
it creates qm files and uploads them to S3.
It also compute a hash and the file size of the file and store them in a file (`details.json`)
which is also uploaded on S3.

MuseScore Resource Manager can then poll this file to check if there are new translations available.

Give thank's for author linepy FADHILRACHMAN
```
