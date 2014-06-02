#!/bin/bash

pushd marionette_extension 
source push_bundles.sh $1 adb
popd
