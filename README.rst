
python-electron
===============================================

This is a very simple Python library to interface with the Electron-Packager command line tool.


Key concepts
===============================================
- Interact with the Electron-Packager directly from Python
- Enables building and archiving Electron applications from your Python code


Usage
===============================================

Example::

   import electron

   application = electron.App(
       APPLICATION_NAME,
       APPLICATION_FOLDER
   )
   application.build('android') # or any installed platform
   application.archive('ios') # or any installed platform
