import json
import os
import shutil
import socket
import urllib2
from datetime import datetime
from distutils import spawn

from fabric.api import local

INTERNET_TEST_URL = 'https://www.google.com'

"""
    REQUIREMENTS:
        - install pip with distribute (http://packages.python.org/distribute/)
        - sudo pip install Fabric
"""


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


with open('.bowerrc') as data_file:
    data = json.load(data_file)

BOWER_DIR = 'bower_components' if 'directory' not in data else data['directory']
NODE_DIR = 'node_modules'
TEMP_DIR = 'temp'
APP_DIR = 'app'
LIB_DIR = os.path.join(APP_DIR, 'lib')


def install():
    if is_internet_on():
        if not check_virtualenv():
            local("pip install virtualenv")
        if not check_gulp():
            local("npm install -g gulp")
        if not check_bower():
            local("npm install -g bower")
        local("python run.py -d")
        local("npm install")
        local("bower install")
        local("gulp serve-gae")
    else:
        print bcolors.FAIL + 'ERROR : ' +  'You have no internet connection.' + bcolors.ENDC


def update():
    local("python run.py -d")
    local("npm install")
    local("bower install")


def run():
    local("gulp serve-gae")


def clean():
    bad_endings = ['pyc', 'pyo', '~']
    print_out(
        'CLEAN FILES ' + bcolors.ENDC,
        'Removing files: %s' % ', '.join(['*%s' % e for e in bad_endings]),
    )
    for root, _, files in os.walk('.'):
        for filename in files:
            for bad_ending in bad_endings:
                if filename.endswith(bad_ending):
                    remove_file_dir(os.path.join(root, filename))


def reset():
    clean()
    if not check_gulp():
        local('gulp clean')
    else:
        print bcolors.WARNING + "Warning: Gulp is not installed locally (can not run clean job of gulp)." + bcolors.ENDC

    remove_file_dir(NODE_DIR)
    remove_file_dir(BOWER_DIR)
    remove_file_dir(TEMP_DIR)
    remove_file_dir(LIB_DIR)


def is_internet_on():
    try:
        urllib2.urlopen(INTERNET_TEST_URL, timeout=2)
        return True
    except (urllib2.URLError, socket.timeout):
        return False


def check_virtualenv():
    return bool(spawn.find_executable('virtualenv')), 'virtualenv', '#virtualenv'


def check_bower():
    return bool(spawn.find_executable('bower')), 'bower', '#bower'


def check_gulp():
    return bool(spawn.find_executable('gulp')), 'gulp', '#gulp'


def print_out(script, filename=''):
    timestamp = datetime.now().strftime('%H:%M:%S')
    if not filename:
        filename = '-' * 46
        script = script.rjust(12, '-')
    print '[%s] %12s %s' % (timestamp, script, filename)


def remove_file_dir(file_dir):
    if os.path.exists(file_dir):
        if os.path.isdir(file_dir):
            shutil.rmtree(file_dir)
        else:
            os.remove(file_dir)
