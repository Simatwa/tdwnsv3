#!/usr/bin/python3
"""'
MIT License

Copyright (c) 2023 Simatwa Caleb

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import argparse, os
from . import __info__, __author__, __version__


def args_handler():
    parser = argparse.ArgumentParser(description=__info__)
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s v{__version__}",
    )
    parser.add_argument(
        "port",
        nargs="?",
        action="store",
        help="Port to be used for hosting files",
        type=int,
        default=8000,
    )
    parser.add_argument(
        "-d", "--dir", help="Directory to be hosted", default=os.getcwd()
    )
    parser.add_argument("-a", "--allow", help="Host only certain entries", default="")
    parser.add_argument(
        "-r", "--restrict", help="Hide entries from being viewed", default=""
    )
    parser.add_argument(
        "-w",
        "--whitelist",
        help="IP(s) to be excluded from restrictions - default : None",
        default="",
    )
    parser.add_argument(
        "-b",
        "--brownlist",
        help="IP(s) to be imposed the restrictions - default : all",
        default="",
        dest="blacklist",
    )
    parser.add_argument(
        "-t",
        "--split",
        help="Separator for  the entries allowed/restricted - default [,]",
        default=",",
    )
    parser.add_argument(
        "-s",
        "--secure",
        help="Level of security on contents",
        choices=[1, 2, 3, 5, 6, 7, 8, 9, 10],
        metavar="1 to 10",
        default=2,
        type=int,
    )
    parser.add_argument(
        "-l",
        "--level",
        help="Logging level",
        choices=[1, 2, 3, 4, 5],
        metavar="1 to 5",
        default=2,
        type=int,
    )
    parser.add_argument("-o", "--log", help="Filepath to log to")
    parser.add_argument("-ho", "--home", help="Home host subdomain path")
    parser.add_argument("-st", "--static", help="Static host subdomain path")
    parser.add_argument("-up", "--receive", help="Upload host subdomain path")
    parser.add_argument(
        "-se",
        "--session",
        help="Maximum session time per user - (mins) ",
        type=float,
        default=45,
    )
    parser.add_argument(
        "-th",
        "--theme",
        help="Theme for displaying contents",
        type=int,
        choices=[1, 2, 3, 4],
        metavar="[1-4]",
        default=4,
    )
    parser.add_argument("-cs", "--css", help="Customize webpage with the CSS in path")
    parser.add_argument(
        "-upp",
        "--upload-path",
        help="Path for saving uploaded files",
    )
    parser.add_argument(
        "-upe",
        "--upload-extension",
        help="Extensions of files to be uploaded",
    )
    parser.add_argument(
        "-ups",
        "--upload-size",
        help="Maximum file size to be uploaded - [MB]",
        default=100,
        type=int,
    )
    parser.add_argument(
        "-upl",
        "--upload-limit-person",
        help="Maximum files to be uploaded per IP",
        type=int,
        default=10,
        metavar="upload_limit",
    )
    parser.add_argument(
        "--upload-multiple",
        help="Allow users to upload more than one file at a time.",
        action="store_true",
    )
    parser.add_argument(
        "--disable-aggressive",
        dest="aggressive",
        help="Not to - Filter all entries with  the restricted keywords +",
        action="store_false",
    )
    parser.add_argument(
        "--display-hidden",
        action="store_true",
        help="Show hidden files and directories",
    )
    parser.add_argument("--host", help="Host the files on the LAN", action="store_true")
    parser.add_argument(
        "--no-sort",
        help="Disable prettifying the display of contents",
        action="store_true",
    )
    parser.add_argument(
        "--view", help="Files can be seen but can't be downloaded", action="store_true"
    )
    parser.add_argument(
        "--strict",
        help="Only allow whitelisted & brownlisted IPs to access server!",
        action="store_true",
    )
    parser.add_argument(
        "--preload", help="Load videos before clicked", action="store_true"
    )
    parser.add_argument(
        "--upload", help="Allow users to upload files", action="store_true"
    )
    parser.add_argument(
        "--save-css",
        help="Saves the css data in path for future use",
        action="store_true",
        dest="save_css",
    )
    parser.add_argument(
        "--no-cache",
        help="Use currently passed parameters not previously saved; content-caching disabled",
        action="store_true",
        dest="no_cache",
    )
    parser.add_argument(
        "--encrypt", help="Encrypt URIs on the webpage", action="store_true"
    )
    parser.add_argument(
        "--debug", help="Debug the web application in UI mode", action="store_true"
    )
    parser.add_argument(
        "--index", action="store_true", help="Serve from index.html file"
    )
    return parser.parse_args()


args = args_handler()
from flask import *
from werkzeug.utils import secure_filename
import logging as log
from .html_prettier import prettify
from .style import style_handler
from .javascript import data as javascript
from sys import argv
import base64
from .fav import data as favicon
from .sec_server import credentials, new_cookie, verifiers
import re
from cryptography.fernet import Fernet
from .ciphersuite import encryption
from urllib.parse import unquote


def log_modify_handler():
    lv1 = {1: log.DEBUG, 2: log.INFO, 3: log.WARNING, 4: log.ERROR, 5: log.CRITICAL}
    log_configs = {
        "format": "%(asctime)s - %(levelname)s : %(message)s",
        "datefmt": "%d-%b-%Y %H:%M:%S",
        "level": lv1.get(args.level),
    }
    if args.log:
        log_configs["filename"] = args.log
    log.basicConfig(**log_configs)
    log.debug(f"Done modifying logging  - log_file_path={args.log}")


log_modify_handler()


def verify_dir(dir):
    if dir[0] != "/" and os.path.isdir(dir):
        dir = os.path.join(os.getcwd(), dir)
    log.info(f"Hosting from - {dir}")
    return dir


dir = verify_dir(args.dir)

html_style = style_handler(log, args)
javascript = javascript(args).data
restricted = args.restrict.split(args.split)
log.debug(f"Restricted paths  - {restricted}")
allowed = args.allow.split(args.split)
log.debug(f"Allowed paths - {allowed}")
whitelist = args.whitelist.split(args.split)
log.debug(f"Whitelisted IPs - {whitelist}")
blacklist = args.blacklist.split(args.split)
log.debug(f"Brownlisted IPs - {blacklist}")
secu = args.secure
log.debug(f"Security level {args.secure}")
config = credentials(args.secure)
cookie_jar, first_cookie, upload_counter = {}, {}, {}
key_one, key_two = new_cookie(6), new_cookie(7)
sec_headers = {
    "X-Frame-Options": "DENY, SAMEORIGIN",
    "X-XSS-Protection": "1; mode=block",
    "X-Content-Type-Options": "nosniff",
    "X-Permitted-Cross-Domain-Policies": "none",
    "Content-Security-Policy": "base-uri 'self'; block-all-mixed-content;",
    "Cache-Control": "no-cache" if args.no_cache else "public",
    "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
    "Access-Control-Allow-Credentials": "true",
    "Referrer-Policy": "same-origin",
}

favicon1 = base64.b64decode(favicon.encode())


def mod_server_configs():
    if args.static:
        log.debug(f"Static subdomain [{args.static}]")
        config["static"] = args.static
    if args.receive:
        log.debug(f"Upload subdomain [{args.receive}]")
        config["upload"] = args.receive
    if args.home:
        log.debug(f"Home subdomain [{args.home}]")
        config["home"] = args.home
    if args.css:
        if not os.path.isfile:
            log.error(f'Exception occurred while loading CSS filepath "{args.css}" ')
        else:
            log.debug(f'CSS filepath "{args.css}" ')


mod_server_configs()

encryption_key = Fernet.generate_key()
if args.secure < 6:
    log.debug(f'Encryption key  "{encryption_key.decode()}" ')
encryptor = encryption(encryption_key, args, config)

get_cookie = lambda v: request.cookies.get(v)

app = Flask(
    __name__,
    template_folder=dir,
)


def config_app():
    if args.upload_path:
        if os.path.isdir(args.upload_path):
            pth = args.upload_path
            if not pth.startswith("/"):
                pth = os.path.join(os.getcwd(), pth)
        else:
            pth = os.path.join(os.getcwd(), args.upload_path)
            try:
                os.mkdir(pth)
            except:
                try:
                    os.makedirs(pth)
                except Exception as e:
                    log.error(f'Failed to create "{pth} - {e}')
        app.config["UPLOAD_PATH"] = pth
        log.debug(f"Upload path - {pth}")
    if args.upload_extension:
        app.config["UPLOAD_EXTENSIONS"] = args.upload_extension.split(args.split)
        log.debug(f"Upload allowed extensions - {args.upload_extension}")
    app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * args.upload_size
    log.debug(f"Maximum upload size limit - {args.upload_size}MB")
    log.debug(f"Maximum upload times limit per person - {args.upload_limit_person}")


config_app()


@app.after_request
def add_headers(response):
    if response.status_code in (200, 201, 202, 301, 302, 304):
        for key, value in sec_headers.items():
            response.headers[key] = value
    if response.content_type.split(";")[0] in (
        "application/json",
        "application/xml",
        "text/html",
    ):
        response.headers["Cache-Control"] = "must-revalidate; charset=utf-8"
    return response


def alert(msg, back=True, reload=False):
    return f'<script>alert("{str(msg)}");{"history.back();" if back else ""}{"window.location.reload();" if reload else ""}</script>'


@app.errorhandler(500)
def internal_error(e):
    return str(e), 500


@app.errorhandler(404)
def not_found(e):
    return alert(e), 404


@app.errorhandler(403)
def forbidden(e):
    return alert(e), 403


@app.errorhandler(401)
def unauthorised(e):
    return alert(e), 401


# Controls all the restriction_params
def remove_restricted(entries: list) -> list:
    address, rp = get_real_ip(), []
    if not args.display_hidden:
        for entry in entries.copy():
            if entry.startswith("."):
                entries.remove(entry)
    if args.strict:
        if address in whitelist:
            rp = entries
        elif address in blacklist:
            rp = control(entries)
        else:
            rp = []
            abort(403)
    else:
        if address in whitelist:
            rp = entries
        else:
            rp = control(entries)
    return rp


# Control function 1
def control(entries: list) -> list:
    if not entries:
        return []
    if entries[0].endswith("home"):
        path = dir
    else:
        path = os.path.join(dir, entries[0])

    if args.view:
        if os.path.isfile(path):
            entries = controller(entries)
        return entries
    else:
        return controller(entries)


# Control function 2
def controller(entries: list) -> list:
    if args.allow:
        entries = soup_allow(entries)
    if args.restrict:
        entries = soup_restrict(entries)
    return entries


# Handles allow param
def soup_allow(entries: list) -> list:
    resp = []
    if not args.aggressive:
        for val in allowed:
            for entry in entries.copy():
                if val.lower() in entry.lower() and not entry in resp:
                    resp.append(entry)
    else:
        for val in allowed:
            for entry in entries.copy():
                if val in entry and not entry in resp:
                    resp.append(entry)
    return resp


# Handles restrict param
def soup_restrict(entries: list) -> list:
    if args.aggressive:
        for val in restricted:
            for entry in entries.copy():
                if val.lower() in entry.lower():
                    entries.remove(entry)
    else:
        for val in restricted:
            for entry in entries.copy():
                if val in entry:
                    entries.remove(entry)
    return entries


def wrap_path(abs_path: str, dir: str):
    try:
        contents, code = remove_restricted(os.listdir(abs_path)), 200
        if secu > 2:
            rp = re.sub(
                "\s\s",
                "",
                re.sub(
                    "\n", "", prettify(contents, abs_path, dir, args, config, encryptor)
                ),
            )
        elif secu == 2:
            rp = re.sub(
                "\s\s", "", prettify(contents, abs_path, dir, args, config, encryptor)
            )
        else:
            rp = prettify(contents, abs_path, dir, args, config, encryptor)
    except Exception as e:
        rp, code = alert(e), 403
    finally:
        return rp, code


# Verifies if cookie exists and makes response
def respond_to_user(resp):
    if any([args.aggressive, args.secure >= 4]) and not has_login():
        abort(401)
    return resp


# Assign cookie to user
def add_new_user():
    """Generates cookie values"""
    cookie_value1, cookie_value2 = new_cookie(16), new_cookie(32)
    cookie_jar[cookie_value1] = cookie_value2
    return cookie_value1, cookie_value2


def has_login() -> bool:
    """Checks if user has login"""
    rp = False
    try:
        if cookie_jar[get_cookie(key_one)] == get_cookie(key_two):
            rp = True
    except:
        pass
    finally:
        return rp


@app.route("/", methods=["GET"])
def home():
    verify = verifiers(request, config)
    return verify.redirect_home()


@app.route(f'/{config["hidden_dir"]}/<file>', methods=["GET"])
def hidden_dir(file):
    if file == "js":
        rp = make_response(
            Response(
                f"""function ajhsvysbjuhajannqyafeeusbbeg() {{window.location.replace('/{config["home"]}/home');}}""",
                mimetype="application/javascript",
            )
        )
        id, cookie_value = new_cookie(7), new_cookie(36)
        first_cookie[id] = cookie_value
        rp.set_cookie("id", id, (args.session * 30))
        rp.set_cookie(config["first"], cookie_value, (args.session * 30))
    else:
        rp = abort(401)
    return rp


# Gets clients_real_ip
def get_real_ip():
    headers_list = request.headers.getlist("X-Forwarded-For")
    return headers_list[0] if headers_list else request.remote_addr


@app.route(f'/{config["static"]}/favicon.ico', methods=["GET"])
def favico():
    return favicon1


@app.route(f'/{config["static"]}/style/style.css', methods=["GET"])
def style_css():
    return respond_to_user(Response(html_style.css(), mimetype="text/css"))


@app.route(f'/{config["static"]}/javascript/script.js', methods=["GET"])
def script_js():
    return respond_to_user(Response(javascript, mimetype="application/javascript"))


@app.route(f'/{config["home"]}/<path:path>', methods=["GET"])
def path_handler(path):
    check_path = encryptor.handle_cipher(path, dec=True)
    if not path in ("home"):
        if check_path[0]:
            path = unquote(check_path[1]) if args.encrypt else check_path[1]
            if path.startswith("home"):
                path = path[5:]
        else:
            abort(404)
    path1 = os.path.join(dir, path)
    if remove_restricted([path1]) or path == "home":
        if not args.display_hidden and path.split("/")[-1].startswith("."):
            abort(401)
        if os.path.isfile(path1):
            return respond_to_user(send_file(path1))
        elif os.path.isdir(path1) and not args.index:
            return respond_to_user(wrap_path(path1, path))
        else:
            if path == "home":
                try:
                    if first_cookie[get_cookie("id")] == get_cookie(config["first"]):
                        pass
                    else:
                        abort(401)
                except Exception as e:
                    abort(401)
                else:
                    if args.index:
                        if os.path.exists(os.path.join(dir, "index.html")):
                            resp = make_response(render_template("index.html"))
                        else:
                            abort(404)
                    else:
                        resp = make_response(wrap_path(dir, path))
                    if not has_login():
                        cookie1, cookie2 = add_new_user()
                        resp.set_cookie(
                            key_one,
                            cookie1,
                            max_age=args.session * 60,
                        )
                        resp.set_cookie(
                            key_two,
                            cookie2,
                            max_age=args.session * 60,
                        )
                    return resp
            abort(404)
    else:
        abort(403)


@app.route(f'/{config["upload"]}', methods=["POST"])
def upload():
    if not args.upload:
        abort(401)

    folder = (
        request.form[config.get("folder_name")]
        if not args.upload_path
        else args.upload_path
    )
    response_data = {"saved": 0, "code": 501, "msg": "Internal server-error!"}
    all_files = request.files.getlist(config.get("data_name"))
    if not args.upload_multiple and len(all_files) > 1:
        abort(413)
    for binary in all_files:
        try:
            try:
                count = upload_counter[get_real_ip()]
            except:
                count = 1
                upload_counter[get_real_ip()] = count
            if args.upload_path:
                folder = app.config["UPLOAD_PATH"]
            fnm = secure_filename(binary.filename)
            path = os.path.join(folder, fnm)
            if upload_counter[get_real_ip()] > args.upload_limit_person:
                abort(413)
            if args.upload_extension:
                splt = os.path.splitext(fnm)
                if len(splt) > 1 and splt[1] in app.config["UPLOAD_EXTENSIONS"]:
                    pass
                else:
                    abort(400)
            upload_counter[get_real_ip()] = count + 1
            binary.save(path)
        except Exception as e:
            msg, code, saved = (
                f"Failed to save file! {e} Files saved [{response_data['saved']}]",
                501,
                0,
            )
        else:
            msg, code, saved = (
                f"File uploaded succesfully! {fnm} ({args.upload_limit_person-count}) upload space remaining! Files saved [{response_data['saved']+1}]",
                200,
                1,
            )
        finally:
            response_data["msg"] = msg
            response_data["code"] = code
            response_data["saved"] = response_data["saved"] + saved
    return (
        respond_to_user(
            alert(
                response_data["msg"],
                reload=True if response_data["code"] == 200 else False,
            )
        ),
        response_data["code"],
    )


def main():
    log.debug("Server configured ready to start!")
    try:
        if args.host:
            app.run(host="0.0.0.0", port=args.port, debug=args.debug, threaded=True)
        else:
            app.run(port=args.port, debug=args.debug)
    except Exception as e:
        log.exception(e)


if __name__ == "__main__":
    main()
