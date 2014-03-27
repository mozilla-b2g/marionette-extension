# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup
from setuptools import find_packages

PACKAGE_VERSION = '0.1'
deps = ['']
        
setup(name='install_marionette',
      version=PACKAGE_VERSION,
      description="Installs Marionette as an extension on an FxOS device",
      classifiers=[],
      keywords='mozilla',
      author='Mozilla Automation and Testing Team',
      author_email='tools@lists.mozilla.org',
      url='https://github.com/mozilla-b2g/fxos-certsuite',
      license='MPL',
      packages=['install_marionette'],
      include_package_data=True,
      zip_safe=False,
      install_requires=deps,
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      install_marionette = install_marionette.installer:cli
      """)
