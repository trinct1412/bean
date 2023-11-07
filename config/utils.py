import os
import setuptools
from configurations import Configuration, values

APPS_FILES = [
    'admin.py',
    'apps.py',
    'models.py',
]

APPS_DIRS = [
    'admin',
    'apps',
    'models',
    'templatetags'
]


def isapp(path):
    if os.path.exists(os.path.join(path, 'management', 'commands')):
        return os.path.join(path)
    if not os.path.exists(os.path.join(path, '__init__.py')):
        return False
    for app_file in APPS_FILES:
        fullpath = os.path.join(path, app_file)
        if os.path.exists(fullpath) and os.path.isfile(fullpath):
            return True
    for app_dir in APPS_DIRS:
        fullpath = os.path.join(path, app_dir, '__init__.py')
        if os.path.exists(fullpath) and os.path.isfile(fullpath):
            return True


def discover_apps(path):
    """return a list of apps"""
    apps = []
    for package in setuptools.find_packages(os.path.abspath(path)):
        if 'views' not in package and 'urls' not in package:
            if isapp(os.path.join(path, package.replace('.', os.sep))):
                apps.append(package)
    return apps


def getlines(path):
    if not path:
        return []
    return list(filter(None, open(path).read().splitlines()))


class InstalledAppsMixin:
    INSTALLED_APPS = values.ListValue([])
    INSTALLED_APPS_FILE = values.Value(None)
    INSTALLED_APPS_FILES = values.ListValue([])
    INSTALLED_APPS_DISCOVER = values.Value(True)

    @classmethod
    def setup(cls):
        super(InstalledAppsMixin, cls).setup()
        f_list = cls.INSTALLED_APPS_FILES or [cls.INSTALLED_APPS_FILE]
        for f in filter(None, f_list):
            for lst in getlines(f):
                if lst.strip() and lst.strip() not in cls.MIDDLEWARE:
                    cls.INSTALLED_APPS.append(lst.strip())
        if cls.INSTALLED_APPS_DISCOVER:
            path = cls.BASE_DIR if hasattr(cls, 'BASE_DIR') else os.getcwd()
            for app in discover_apps(path):
                if app not in cls.INSTALLED_APPS:
                    cls.INSTALLED_APPS.append(app)


class InstalledAppsConfiguration(InstalledAppsMixin, Configuration):
    pass
