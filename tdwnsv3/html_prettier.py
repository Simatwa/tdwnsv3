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
import os, urllib, html


def make_navigator(dir, home_dir):
    # dir = "DCIM/Bugjaege/hello"
    resp = f'<a class="listed_dir" href="/{home_dir}/home">Home</a>'
    splitted = dir.split("/")
    for x in range(len(splitted)):
        if len(splitted) == 1 or not bool(splitted[x].strip()):
            break
        url = os.path.join(*["/" + home_dir] + splitted[: x + 1])
        resp = resp + "/" + f'<a class="listed_dir" href="{url}/">{splitted[x]}</a>'
    return resp


# out = make_navigator("","files")
# print(out)
def prettify(
    contents: list, path: str, dir: str, args: object, config: dict, encryptor: object
) -> str:
    r = []
    enc = "utf-8"
    static = config["static"]
    fmtlink = lambda uri: encryptor.handle_cipher(
        uri, enc=True, path=os.path.join(dir, uri)
    )[1]
    folders, videos, audios, photos, programs, documents, etc = (
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    )

    title = '<span style="color:cyan;">Directory </span>%s' % dir
    r.append(
        '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
        '"http://www.w3.org/TR/html4/strict.dtd">'
    )
    r.append("<html><head>")
    r.append(
        '<meta http-equiv="Content-Type" '
        'content="text/html; charset=%s"></meta>' % enc
    )
    r.append(
        '<meta content="width=width-device, initial-scale=1.0" name="viewport"></meta>'
        f'<link rel="icon" type="image/x-icon" href="/{static}/favicon.ico"></link>'
        f'<link rel="stylesheet" href="/{static}/style/style.css"></link>'
        f'<script type="text/javascript" src="/{static}/javascript/script.js"></script>'
    )
    r.append("<title>Directory %s</title></head>" % dir)
    r.append("<body><p class='nav'>%s</p;><hr/>" % make_navigator(dir, config["home"]))

    preload = "none"
    if args.preload:
        preload = "metadata"
    for name in contents:
        fullname = os.path.join(path, name)
        displayname = linkname = name
        # Append / for directories or @ for symbolic links
        if os.path.isdir(fullname):
            displayname = name + "/"
            linkname = name + "/"
        if os.path.islink(fullname):
            displayname = name + "@"
            # Note: a link to a directory displays with @ and links with /
        if args.no_sort:
            if "/" in displayname:
                r.append(
                    '<p><a class="dir" href="%s">%s</a></p>'
                    % (
                        urllib.parse.quote(linkname, errors="surrogatepass"),
                        html.escape(displayname, quote=False),
                    )
                )
            else:
                r.append(
                    '<p><a class="file" href="%s">%s</a></p>'
                    % (
                        urllib.parse.quote(linkname, errors="surrogatepass"),
                        html.escape(displayname, quote=False),
                    )
                )
        else:
            if "/" in displayname:
                displayname = displayname.replace("/", "")
                folders.append(
                    '<button><a class="dir" href="%s">%s</a></button>'
                    % (
                        fmtlink(urllib.parse.quote(linkname, errors="surrogatepass")),
                        html.escape(displayname, quote=False),
                    )
                )
            else:
                link = fmtlink(urllib.parse.quote(linkname, errors="surrogatepass"))
                linknm = html.escape(displayname, quote=False)
                if len(linknm) > 30:
                    linknm = linknm[0:30] + "..."
                if displayname.endswith(("mp4", "3gpp", "mkv", "3gp")):
                    rp = f"""<div id='info' class='vida'><p class='doc'>{linknm}</p>
            			<video preload='{preload}' controls>
            			<source src="{link}" type="video/mp4"></video>{'<br>'*2}</div>"""
                    videos.append(rp)
                elif displayname.endswith(
                    ("jpg", "jpeg", "png", "img", "webm", "gif", "svg")
                ):
                    rp = f"""<div id='info' class='pic'><p class='doc'>{linknm}</p><img height='auto' width='auto' src='{link}' alt='{linknm}'/></div>"""
                    photos.append(rp)
                elif displayname.endswith(("mp3", "wav", "m4a")):
                    rp = f"""<div id='info' class='aud'><p class='doc'>{linknm}</p><audio controls>
            			<source src="{link}" type="audio/mp3">
            			</audio></div>"""
                    audios.append(rp)
                elif displayname.endswith(
                    (
                        ".py",
                        ".c",
                        ".html",
                        ".css",
                        ".cxx",
                        ".js",
                        ".xml",
                        ".htm",
                        ".pl",
                        ".yaml",
                        ".sh",
                        ".bash",
                        ".zsh",
                        ".bat",
                        ".rst",
                        ".cpp",
                        ".php",
                        ".jar",
                        ".jv",
                        ".config",
                        ".json",
                        ".dat",
                        ".conf",
                        ".resolv",
                        "yml",
                        ".rb",
                        ".ini",
                        ".apk",
                        ".exe",
                        ".deb",
                    )
                ):
                    programs.append(
                        '<li class="doc"><a class="file" href="%s">%s</a></li>'
                        % (link, linknm)
                    )
                elif displayname.endswith(
                    ("pdf", "docx", "csv", "txt", "md", "db", "bin", "xlsx")
                ):
                    documents.append(
                        '<li class="doc"><a class="file" href="%s">%s</a></li>'
                        % (link, linknm)
                    )
                else:
                    etc.append(
                        '<li class="doc"><a class="file" href="%s">%s</a></li>'
                        % (link, linknm)
                    )

            if name == contents[len(contents) - 1]:
                dt = [folders, videos, audios, photos, programs, documents, etc]
                tl = lambda a: f"<h3>{a}</h3>"
                hd = [
                    "Folders",
                    "Videos",
                    "Audios",
                    "Photos",
                    "Programs",
                    "Documents",
                    "Etcs",
                ]
                for x in range(len(dt)):
                    if dt[x]:
                        dt[x].sort()
                        r.append(tl(hd[x]))
                        if x == 0:
                            r.append('<div class="folders">')
                        if x == 1:
                            r.append(
                                """<div><input id='cp' type='search' name='me' placeholder='Search videos in this folder...' onkeyup='query()'></input></div>"""
                            )
                        r.extend(dt[x])
                        if x == 0:
                            r.append("</div>")
    r.append(
        f"""
        <marquee>You can upload files to this folder.</marquee>
        <form method='POST' action='/{config['upload']}' enctype="multipart/form-data" onsubmit='return notify()'>
        <input type='file' id='bin' name='{config['data_name']}' {'multiple' if args.upload_multiple else ''}/>
        <input type='hidden' name='{config['folder_name']}' value='{path}/'>
        <input type='submit' value='Upload'/>
        </form>"""
        if args.upload
        else ""
    )
    r.append(
        """<hr><div class="container"><footer>
		 <a class='but' href='#' target='self' onclick='refresh()'>Refresh Page</a>
        <p style="color:red;font-size:160%;font-family:cursive;">Regards <a href='https://github.com/Simatwa' target='_blank'>Smartwa</a></p></footer></div>
       """
    )
    r.append("</body></html>")
    return "".join(r)
