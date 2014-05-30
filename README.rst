marionette-extension
====================

This repository contains Marionette in gecko extension form, intended for use
with FxOS devices. It includes an installation script which you can use, 
provided your phone is connected via ADB::

  source install_marionette_extension.sh VERSION

Where VERSION  is a supported version number, one of: 1.3 or 1.4.

If you need to install adb, see 
https://developer.mozilla.org/en-US/Firefox_OS/Debugging/Installing_ADB.

FirefoxOS v1.3 and v1.4 are currently supported.

Python Package
==============

This is also the 'marionette_extension' python package. Once you install this
package, you will have access to a command line program called
install_marionette which you can use like so::

  marionette_extension --help

Which will show you what installation options you have available to you.

If you need an example, this is how you can install Marionette on a v1.3 device::

  marionette_extension --install 1.3

You can also import the marionette_extension package into your python script
and use its install function to install marionette via a script. Example::

  from marionette_extension import install  
  install(FXOS_VERSION, adb=ADBPATH) # Replace FXOS_VERSION with a supported version, and you may use ADBPATH to specify your adb path. If not specified, it will assume 'adb' is on the $PATH

