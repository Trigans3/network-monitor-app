[app]
title = Network Monitor
package.name = networkmonitor
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 1.0
requirements = python3,kivy,requests,pyjnius,android

android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE

fullscreen = 0
android.minapi = 21
android.api = 33
android.arch = arm64-v8a

orientation = portrait

android.skip_update = False
android.accept_sdk_license = True

log_level = 1

[buildozer]
log_level = 1
