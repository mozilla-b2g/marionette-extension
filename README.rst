marionette-extension
====================

This repository contains Marionette in gecko extension form, intended for use
with FxOS devices. It includes an installation script which you can use, 
provided your phone is connected via ADB::

  source install_marionette_extension.sh VERSION

Where VERSION  is a supported version number, one of: 1.3, 1.4, 2.0, 2.1, 2.2, or 2.5.

If you need to install adb, see 
https://developer.mozilla.org/en-US/Firefox_OS/Debugging/Installing_ADB.

FirefoxOS v1.3 through v2.5 are currently supported.


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


How to add a new version?
==============

0. Create a new folder indicating your new gecko version
1. > hg clone https://hg.mozilla.org/mozilla-central/

Starting now, please reference on the files and folder structure of previous marionette-extension version
2. Go to mozilla-central folder and find /testing/specialpowers(mozilla-central) and copy them into special-powers@mozilla.org folder
3. Copy all the .js files in /testing/marionette(mozilla-central) to marionette@mozilla.org/chrome/content
4. Copy chrome.manifest and install.rdf from previous version of marionette-extension to marionette@mozilla.org folder
5. Copy testing/marionette/components/marionettecomponent.js(mozilla-central) to /marionette@mozilla.org/components and rename it to marionetteextensioncomponent.js
6. Do this to marionetteextensioncomponent.js:
* replace MARIONETTE_CONTRACTID value with "@mozilla.org/marionetteextension;1"
* change the profile-after-change listener to always start Marionette and not be dependent on build flags or command lines
      this.enabled = true;
      this.logger.info("marionette enabled via extension");
      // We want to suppress the modal dialog that's shown
      // when starting up in safe-mode to enable testing.
      if (Services.appinfo.inSafeMode) {
        this.observerService.addObserver(this, "domwindowopened", false);
      }
* change the component name from MarionetteComponent to MarionetteExtensionComponent

7. request of putting this on pypi for faster installation
