# tdwnsv3 #

```

'########:'########::'##:::::'##:'##::: ##::'######::'##::::'##::'#######::
... ##..:: ##.... ##: ##:'##: ##: ###:: ##:'##... ##: ##:::: ##:'##.... ##:
::: ##:::: ##:::: ##: ##: ##: ##: ####: ##: ##:::..:: ##:::: ##:..::::: ##:
::: ##:::: ##:::: ##: ##: ##: ##: ## ## ##:. ######:: ##:::: ##::'#######::
::: ##:::: ##:::: ##: ##: ##: ##: ##. ####::..... ##:. ##:: ##:::...... ##:
::: ##:::: ##:::: ##: ##: ##: ##: ##:. ###:'##::: ##::. ## ##:::'##:::: ##:
::: ##:::: ########::. ###. ###:: ##::. ##:. ######::::. ###::::. #######::
:::..:::::........::::...::...:::..::::..:::......::::::...::::::.......:::

```

- **tdwnsv3** is [Python](https://python.org) program for hosting local-files on net (***LAN***).


## Independencies  ##

* Flask
* cryptography

Review [requirements](requirements.txt)

## installation ##
 
1.Linux 

- Running the following commands at the terminal will get you ready.

```
$ git clone https://github.com/Simatwa/tdwnsv3.git
$ bash install.sh

```

2.Windows
- If you haven't installed the required packages then you can 
**Download** 64-bit executables [here](#).


## Usage ##

- `$ tdwnsv` will fire up the server with the following default configurations:

<table style='text-align:center;'>
<thead>
<tr><th>Command  </th><th style="text-align: right;">  Default</th></tr>
</thead>
<tbody>
<tr><td>host     </td><td style="text-align: right;">    False</td></tr>
<tr><td>port     </td><td style="text-align: right;">     8000</td></tr>
<tr><td>sort     </td><td style="text-align: right;">    False</td></tr>
<tr><td>theme    </td><td style="text-align: right;">        2</td></tr>
<tr><td>upload   </td><td style="text-align: right;">    False</td></tr>
<tr><td>encrypt  </td><td style="text-align: right;">    False</td></tr>
<tr><td>session  </td><td style="text-align: right;">    False</td></tr>
</tbody>
</table>

- Adding ```--sort``` to the commands parsed  will prettify the display. i.e
 
 ```
 $ tdwnsv3 --sort 

 ```

* *This is just a shallow display of the default configurations.*

## wsgi ##

- Since Flask server runs at development environment, you may need to run the program on a server such as [Nginx](https://nginx.org) for efficiency.
- The [wsgi](wsgi.py) script can be interfaced with **wsgi** such as **uwsgi** to run behind a *server* .
 * For  instance intergrating with `uwsgi` as stated in [docs](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html) :
 
 ```

$ uwsgi --http=0.0.0.0:8080 -w wsgi:app

```

- Run  ```tdwnsv3 -h``` to view more configuration info as shown.

```
usage: tdwnsv3 [-h] [-v] [-d DIR] [-a ALLOW] [-r RESTRICT] [-w WHITELIST] [-b BLACKLIST] [-t SPLIT] [-s 1 to 10] [-l 1 to 5] [-o LOG]
               [-ho HOME] [-st STATIC] [-up RECEIVE] [-se SESSION] [-th [1,2]] [-cs CSS] [-upp UPLOAD_PATH] [-upe UPLOAD_EXTENSION]
               [-ups UPLOAD_SIZE] [-upl upload_limit] [--host] [--sort] [--aggressive] [--view] [--strict] [--preload] [--upload]
               [--save-css] [--no-cache] [--encrypt] [--debug]
               [port]

Simple local-files server with security as main priority!

positional arguments:
  port                  Port to be used for hosting files

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d DIR, --dir DIR     Directory to be hosted
  -a ALLOW, --allow ALLOW
                        Host only certain entries
  -r RESTRICT, --restrict RESTRICT
                        Hide entries from being viewed
  -w WHITELIST, --whitelist WHITELIST
                        IP(s) to be excluded from restrictions - default : None
  -b BLACKLIST, --brownlist BLACKLIST
                        IP(s) to be imposed the restrictions - default : all
  -t SPLIT, --split SPLIT
                        Separator for the entries allowed/restricted - default [,]
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
  -th [1,2], --theme [1,2]
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
  --host                Host the files on the LAN
  --sort                Prettify the display of the contents
  --aggressive          Filter all entries with the restricted keywords
  --view                Files can be seen but can't be downloaded
  --strict              Only allow whitelisted & brownlisted IPs to access server!
  --preload             Load videos before clicked
  --upload              Allow users to upload files
  --save-css            Saves the css data in path for future use
  --no-cache            Use currently parsed parameters not previously saved
  --encrypt             Encrypt URIs on the webpage
  --debug               Debug the web application in UI mode

```


## Acknowledgements ##

* [x] [Flask](https://github.com/pallets/flask) 
* [x] [Python](https://python.org)