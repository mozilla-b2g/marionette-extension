# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup
from setuptools import find_packages

PACKAGE_VERSION = '0.4.4'
deps = ['mozdevice']
        
setup(name='marionette_extension',
      version=PACKAGE_VERSION,
      description="Installs Marionette as an extension on an FxOS device",
      classifiers=[],
      keywords='mozilla',
      author='Mozilla Automation and Testing Team',
      author_email='tools@lists.mozilla.org',
      url='https://github.com/mozilla-b2g/fxos-certsuite',
      license='MPL',
      packages=['marionette_extension'],
      include_package_data=True,
      zip_safe=False,
      install_requires=deps,
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      marionette_extension = marionette_extension.installer:cli
      """)
