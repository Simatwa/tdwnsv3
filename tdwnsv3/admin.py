from flask_admin.contrib.fileadmin import FileAdmin
import os.path as op
from flask_admin import Admin


class FileManagerAdmin(FileAdmin):
    can_mkdir = True
    can_upload = True
    can_delete = True


def AdminEndpoint(dir, args, app):
    # Flask setup here
    if args.swatch and not args.swatch.lower() == "none":
        app.config["FLASK_ADMIN_SWATCH"] = args.swatch
    admin = Admin(app, name="TDWNSV3", template_mode=args.template)
    path = op.join(dir, "")
    admin.add_view(FileAdmin(path, "", name="File Manager"))
    return app


"""
class Args:
	
	swatch=None
	template ='bootstrap3'
	
from flask import Flask
app = Flask(__name__)

app = AdminEndpoint('__pycache__',Args,app)
app.run()
"""
