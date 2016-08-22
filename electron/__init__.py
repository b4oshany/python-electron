# -*- coding: utf-8 -*-
from __future__ import absolute_import
__version__ = '1.0.1'

import os
import re
import subprocess
import shutil

from .decorators import for_all_methods, chdir_context


@for_all_methods(chdir_context)
class App(object):
    path = None
    name = None
    debug = False
    electron_version = __version__


    # We need to initialize the application with the path of the root
    # of the project
    def __init__(self, name, path, debug=False, *args, **kwargs):
        self.path = path
        self.name = name
        self.debug = debug
        super(App, self).__init__(*args, **kwargs)


    def archive(self, electron_path, archive_type='zip'):
        for f in os.listdir(electron_path):
            folder = os.path.join(electron_path, f)
            if os.path.isdir(folder):
                shutil.make_archive("%s/%s" % (electron_path, f),
                                    archive_type, folder)

    def build(self, platform, overwrite=True, asar=True, output=None, arch="ia32"):
        """Build the Electron application.

        Arguments:
            platform (string)           Platform to build the application for.
                                        Allowed values: linux, win32, darwin, all

            output (string)             Output directory of the application.

            arch (string)               Bit version to build.
                                        Allowed values: ia32, x64, all

            overwrite (boolean)         Overwrite previous application build

            asar (boolean)              An asar archive is a simple tar-like format
                                        that concatenates files into a single file.
                                        Electron can read arbitrary files from it without
                                        unpacking the whole file.
        """
        cmd_params = ['electron-packager',
                      self.path,
                      self.name,
                      "--platform=%s" % platform,
                      "--version=%s" % self.electron_version,
                      "--arch=%s" % arch
                     ]
        if overwrite:
            cmd_params.append('--overwrite')
        if asar:
            cmd_params.append('--asar')
        if output:
            cmd_params.append("--out=%s" % output)
        else:
            cmd_params.append("--out=%s" % self.path)

        return_code = subprocess.call(cmd_params, shell=self.debug)

        if return_code == 0:
            self.archive(electron_path=output)
        else:
            return False
