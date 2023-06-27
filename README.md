<h1 align="center">tdwnsv3</h1>
<p align="center"><a href="https://github.com/Simatwa/tdwnsv3"><img src="https://img.shields.io/static/v1?label=Github&message=Passing&logo=github&color=green" alt="Github"/></a>
<a href="https://pypi.org/project/tdwnsv3"><img src="https://img.shields.io/static/v1?label=Pypi&message=v1.9.2&color=yellow&logo=pypi" alt="pypi"/></a>
<a href="#"><img src="https://img.shields.io/static/v1?label=Coverage&message=80%&color=lime&logo=Coverage" alt="Coverage"/></a>
<a href="https://wakatime.com/badge/github/Simatwa/svinf3"><img src="https://wakatime.com/badge/github/Simatwa/svinf3.svg" alt="wakatime"/></a>
<a href="https://pepy.tech/project/tdwnsv3"><img src="https://static.pepy.tech/badge/tdwnsv3" alt="Downloads"/></a>
<a href="#"><img src="https://visitor-badge.glitch.me/badge?page_id=Simatwa.tdwnsv3&left_color=red&right_color=lime&left_text=Counts" alt="Visitors"/></a>
<a href="#"><img src="https://img.shields.io/static/v1?label=Code Style&message=Black&color=black&logo=Black" alt="Code-style"/></a>
</p>

> Access your files on the web.

![Web interface sample](https://github.com/Simatwa/tdwnsv3/raw/main/assets/web_interface_example.gif)

## [Independencies](https://github.com/Simatwa/tdwnsv3/raw/main/requirements.txt)

* Flask
* cryptography
* appdirs

## Features

- Simple commandline interface
- Web interface with multiple themes
- Serve as static files server - index.html
- Highly immune against variety of attacks
- Compatible with multiple devices and browsers
- Fully customizable web interface - css
- Upload and download files

## Installation 

- Choose your suit from the following ways:

1. From pip 
  
  ```sh
  $ pip install tdwnsv3
  ```

2. From source

 ```sh
 $ pip install git+https://github.com/Simatwa/tdwnsv3.git
 ```

 3. Cloning repo and install

  ```sh
  git clone https://github.com/Simatwa/tdwnsv3.git
  cd tdwnsv3
  sudo bash install.sh
  ```


## Usage ##

Either of the following ways will get you ready at the terminal environment

1. Package level
```
$ python -m tdwnsv3
```
2. `$ tdwnsv3`

<p align="center">By default, the server fires up with the following configurations:</p>

<table align='center'>
<thead>
<tr><th>Command  </th><th style="text-align: right;">  Default</th></tr>
</thead>
<tbody>
<tr><td>host     </td><td style="text-align: right;">    False</td></tr>
<tr><td>port     </td><td style="text-align: right;">     8000</td></tr>
<tr><td>no-sort     </td><td style="text-align: right;">   False</td></tr>
<tr><td>theme    </td><td style="text-align: right;">        3</td></tr>
<tr><td>upload   </td><td style="text-align: right;">    False</td></tr>
<tr><td>encrypt  </td><td style="text-align: right;">    False</td></tr>
<tr><td>session  </td><td style="text-align: right;">    False</td></tr>
</tbody>
</table>

> **Note** This is just a shallow display of the default configurations.

## wsgi 

Since Flask server runs at development environment, you may need to run the program on a server such as [Nginx](https://nginx.org) for efficiency.

```py
from tdwnsv3.tdwnsv3 import app

if __name__ == "__main__":
    app.run()
```

The [wsgi.py](https://github.com/Simatwa/tdwnsv3/raw/main/wsgi.py) script can be interfaced with **wsgi** such as **uwsgi** to run behind a *server* .
 * For  instance intergrating with `uwsgi` as stated in [docs](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html) :
 
 ```

$ uwsgi --http=0.0.0.0:8080 -w wsgi:app

```

<details>

<summary>

- Run  ```tdwnsv3 -h``` to view more configuration info as shown.

</summary>

```

usage: tdwnsv3 [-h] [-v] [-d DIR] [-a ALLOW] [-r RESTRICT] [-w WHITELIST]
               [-b BLACKLIST] [-t SPLIT] [-s 1 to 10] [-l 1 to 5] [-o LOG]
               [-ho HOME] [-st STATIC] [-up RECEIVE] [-se SESSION] [-th [1-3]]
               [-cs CSS] [-upp UPLOAD_PATH] [-upe UPLOAD_EXTENSION]
               [-ups UPLOAD_SIZE] [-upl upload_limit] [--upload-multiple]
               [--disable-aggressive] [--display-hidden] [--host] [--no-sort]
               [--view] [--strict] [--preload] [--upload] [--save-css]
               [--no-cache] [--encrypt] [--debug] [--index]
               [port]

Simple local-files server with security on top!

positional arguments:
  port                  Port to be used for hosting files

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d DIR, --dir DIR     Directory to be hosted
  -a ALLOW, --allow ALLOW
                        Host only certain entries
  -r RESTRICT, --restrict RESTRICT
                        Hide entries from being viewed
  -w WHITELIST, --whitelist WHITELIST
                        IP(s) to be excluded from restrictions - default :
                        None
  -b BLACKLIST, --brownlist BLACKLIST
                        IP(s) to be imposed the restrictions - default : all
  -t SPLIT, --split SPLIT
                        Separator for the entries allowed/restricted - default
                        [,]
  -s 1 to 10, --secure 1 to 10
                        Level of security on contents
  -l 1 to 5, --level 1 to 5
                        Logging level
  -o LOG, --log LOG     Filepath to log to
  -ho HOME, --home HOME
                        Home host subdomain path
  -st STATIC, --static STATIC
                        Static host subdomain path
  -up RECEIVE, --receive RECEIVE
                        Upload host subdomain path
  -se SESSION, --session SESSION
                        Maximum session time per user - (mins)
  -th [1-3], --theme [1-3]
                        Theme for displaying contents
  -cs CSS, --css CSS    Customize webpage with the CSS in path
  -upp UPLOAD_PATH, --upload-path UPLOAD_PATH
                        Path for saving uploaded files
  -upe UPLOAD_EXTENSION, --upload-extension UPLOAD_EXTENSION
                        Extensions of files to be uploaded
  -ups UPLOAD_SIZE, --upload-size UPLOAD_SIZE
                        Maximum file size to be uploaded - [MB]
  -upl upload_limit, --upload-limit-person upload_limit
                        Maximum files to be uploaded per IP
  --upload-multiple     Allow users to upload more than one file at a time.
  --disable-aggressive  Not to - Filter all entries with the restricted
                        keywords +
  --display-hidden      Show hidden files and directories
  --host                Host the files on the LAN
  --no-sort             Disable prettifying the display of contents
  --view                Files can be seen but can't be downloaded
  --strict              Only allow whitelisted & brownlisted IPs to access
                        server!
  --preload             Load videos before clicked
  --upload              Allow users to upload files
  --save-css            Saves the css data in path for future use
  --no-cache            Use currently passed parameters not previously saved;
                        content-caching disabled
  --encrypt             Encrypt URIs on the webpage
  --debug               Debug the web application in UI mode
  --index               Serve from index.html file

```

</details>

- Review [CHANGELOG](CHANGELOG.md)

## Acknowledgements

* [x] [Flask](https://github.com/pallets/flask) 
* [x] [Python](https://python.org)
