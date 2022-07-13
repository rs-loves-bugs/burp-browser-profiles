# burp-browser-profiles

![feature image](https://i.imgur.com/cOAlfyI.png)

burp-browser-profiles is a small shell script utility that will help you make better use of the embedded browser that comes by default with Burp. This is heavily inspired by [PwnFox](https://github.com/yeswehack/PwnFox), I wanted to have a similar tool to use with the embedded Burp browser

[![Twitter Follow](https://img.shields.io/twitter/follow/rs_loves_bugs?style=flat-square)](https://twitter.com/rs_loves_bugs)

## Features:

-allows you to create and maintain multiple Burp browser profiles

-allows you to run multiple Burp browser instances at the same time with different profiles

-allows you to specify a different proxy server for every Burp browser instance you have running

-allows you to specify a custom user agent for every Burp browser instance you have running

-allows you to differenciate the profiles between them with a different color used for the Burp browser window frame(blue, cyan, green, yellow, orange, red, magenta, pink)

-allows you in Burp to highlight with the same color the request from that specific profile(this feature requires installing a Burp extension)

# Instalation:

burp-browser-profiles was tested on Mac and Linux and will work with either Burp Professional or Burp Community Edition

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
./burp-browser-profiles
Syntax: ./burp-browser-profiles [options]

    -P <profile_name> (required) Create or open a profile
    -p <adress:port>             Specify a proxy server to use, will use localhost:8080 by default
    -c <color_name>              Specify a color to use(blue, cyan, green, yellow, orange, red, magenta, pink), no color is used by default
    -u <user_agent>              Specify an user agent to use

    -L                           List available profiles
    -D <profile_name>            Delete a profile
    -h                           Help
```

Create and run a profile named testing:
```
./burp-browser-profiles -P testing
```

List available profiles to use:
```
./burp-browser-profiles -L
```

Open and run an existing profile:
```
./burp-browser-profiles -P testing
```

Open and run an existing profile, use a color for the frame and highlight the requests from it:
```
./burp-browser-profiles -P testing -c red
```

Open and run an existing profile with a custom proxy:
```
./burp-browser-profiles -P testing -p localhost:9999
```

Open and run an existing profile with a custom user agent:
```
./burp-browser-profiles -P testing -u "my user agent"
```

Delete a profile:
```
./burp-browser-profiles -D testing
```
# TODO

Port to a Burp extension






