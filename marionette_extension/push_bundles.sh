#!/bin/bash

if [ -z "$1" ]; then
  echo "You must specify a version number"
  exit 1
fi

VERSION=$1
ADB=$2

if [ -z "$3" ]; then
  PKG_DIR="bundles/$VERSION"
else
  PKG_DIR="$3/$VERSION"
fi

use_adb() {
  ACTION=$1
  EXTRA_EXPLANATION=$2
  shift 2
  echo "Executing $@"
  $ADB $@
  if [ $? != 0 ]; then
    echo "Could not $ACTION. Is it listed on 'adb devices'?"
    echo "If not, please follow README instructions to setup adb on the device."
    echo "If it is listed in 'adb devices', is the device rooted, and is the screen unlocked?"
    if [ ! -z "$EXTRA_EXPLANATION" ]; then
      echo $EXTRA_EXPLANATION
    fi
    exit 1
  fi
}
echo "Executing remount"
OUT=`adb remount`
if [[ $OUT == *failed* ]]; then
  echo "Could not remount. Is the device listed on 'adb devices'?"
  echo "If not, please follow README instructions to setup adb on the device."
  echo "If it is listed in 'adb devices', is the device rooted, and is the screen unlocked?"
  echo "If this still fails, try running 'adb root' before running the tests"
  exit 1
fi
use_adb "push special-powers to the device" "" push $PKG_DIR/special-powers\@mozilla.org /system/b2g/distribution/bundles/special-powers\@mozilla.org
use_adb "push marionette to the device" "" push $PKG_DIR/marionette\@mozilla.org /system/b2g/distribution/bundles/marionette\@mozilla.org
use_adb "call adb shell to stop b2g" "" shell stop b2g
use_adb "call adb shell to start b2g" "" shell start b2g
echo "waiting for b2g to start"
TRIES=30
while [ $TRIES -gt 0 ]; do
  sleep 5
  echo "checking if b2g has started"
  use_adb "call adb shell to check b2g-ps" "" shell b2g-ps | grep b2g
  if [ $? == 0 ]; then
    break
  fi
  let TRIES=TRIES-1
done
if [ $TRIES == 0 ]; then
  echo "b2g did not start up!"
  exit 1
fi
use_adb "forward adb port" "If it is rooted, is port 2828 already in use? Try 'nc -z localhost 2828'" forward tcp:2828 tcp:2828
