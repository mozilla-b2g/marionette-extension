marionette-extension
====================

This repository contains Marionette in gecko extension form, intended for use
with FxOS devices. It includes an installation script which you can use, 
provided your phone is connected via ADB::

  source install_marionette_extension.sh

If you need to install adb, see 
https://developer.mozilla.org/en-US/Firefox_OS/Debugging/Installing_ADB.

Python Package
==============

This is also the 'marionette_extension' python package. Once you install this
package, you will have access to a command line program called
install_marionette which you can use to install the extension like so::

  install_marionette

You can also import the marionette_extension package into your python script
and use its install function to install marionette via a script. Example::

  from marionette_extension import install
  install()

