# burp-browser-profiles.py

![feature image](https://i.imgur.com/cOAlfyI.png)

burp-browser-profiles.py is a small script utility that will help you make better use of the embedded browser that comes by default with Burp. This is heavily inspired by [PwnFox](https://github.com/yeswehack/PwnFox), I wanted to have a similar tool to use with the embedded Burp browser

[![Twitter](https://img.shields.io/badge/-@rs__loves__bugs-%232B90D9?style=for-the-badge&logo=twitter&logoColor=white&label=twitter)](https://twitter.com/rs_loves_bugs)&nbsp;
[![Mastodon](https://img.shields.io/badge/-@rs__loves__bugs-%232B90D9?style=for-the-badge&logo=mastodon&logoColor=white&label=infosec.exchange)](https://infosec.exchange/@rs_loves_bugs)

## Features:

-allows you to create and maintain multiple Burp browser profiles

-allows you to run multiple Burp browser instances at the same time with different profiles

-allows you to specify a different proxy server for every Burp browser instance you have running

-allows you to specify a custom user agent for every Burp browser instance you have running

-allows you to differentiate the profiles between them with a different color used for the Burp browser window frame(blue, cyan, green, yellow, orange, red, magenta, pink)

-allows you in Burp to highlight with the same color the request from that specific profile(this feature requires installing a Burp extension)

-allows you to start the browser without remote debugging to try to bypass anti-bots checks 

# Instalation and requirements:

burp-browser-profiles.py was tested on Windows, Mac and Linux and will work with either Burp Professional or Burp Community Edition. You will need to have a working Python 3 installation(on Windows install from [here](https://www.microsoft.com/store/productId/9NRWMJP3717K), it won't work using Python from WSL) 

```
git clone https://github.com/rs-loves-bugs/burp-browser-profiles
```
```
cd burp-browser-profiles
```

To color highlight the requests in Burp please install either one of these two extensions:

PwnFox - [link to jar file](https://github.com/yeswehack/PwnFox/releases/download/v1.0.3/PwnFox.jar), highlighting enabled by default

Sharpener - [link to BApp Store](https://portswigger.net/bappstore/3c5025b0e19d419a8f339ee0c30391dd), then enable the highlighter(Sharpener -> Global Settings -> Supported Capabilities -> PwnFox Highlighter)   

# Usage:
Show the help menu:

```
python burp-browser-profiles.py
usage: bbp.py [-h] [-P PROFILE] [-p [PROXY]]
              [-c {blue,cyan,green,yellow,orange,red,magenta,pink}]
              [-u USER_AGENT] [-x] [-d] [-L] [-D DELETE_PROFILE]

Burp Browser Profiles

options:
  -h, --help            show this help message and exit
  -P PROFILE, --profile PROFILE
                        Create or open a profile
  -p [PROXY], --proxy [PROXY]
                        Specify a proxy server to use, will use 127.0.0.1:8080
                        by default
  -c {blue,cyan,green,yellow,orange,red,magenta,pink}, --color {blue,cyan,green,yellow,orange,red,magenta,pink}
                        Specify a color to use
  -u USER_AGENT, --user-agent USER_AGENT
                        Specify an user agent to use
  -x, --disable-proxy   Disable the proxy
  -d, --disable-remote-debugging
                        Disable remote debugging
  -L, --list-profiles   Disable the proxy
  -D DELETE_PROFILE, --delete-profile DELETE_PROFILE
                        Delete a profile
```

Create and run a profile named testing:
```
python burp-browser-profiles.py -P testing
```

List available profiles to use:
```
python burp-browser-profiles.py -L
```

Open and run an existing profile:
```
python burp-browser-profiles.py -P testing
```

Open and run an existing profile, use a color for the frame and highlight the requests from it:
```
python burp-browser-profiles.py -P testing -c red
```

Open and run an existing profile with a custom proxy:
```
python burp-browser-profiles.py -P testing -p localhost:9999
```

Open and run an existing profile with no proxy settings:
```
python burp-browser-profiles.py -P testing -x
```

Open and run an existing profile without remote debugging:
```
python burp-browser-profiles.py -P testing -d
```

Open and run an existing profile with a custom user agent:
```
python burp-browser-profiles.py -P testing -u "my user agent"
```

Delete a profile:
```
python burp-browser-profiles.py -D testing
```






