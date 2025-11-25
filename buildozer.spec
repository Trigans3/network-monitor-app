[app]
title = Network Monitor
package.name = networkmonitor
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0
requirements = python3,kivy,requests,openssl,pyjnius,android

android.permissions = INTERNET,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE

fullscreen = 0
android.minapi = 21
android.api = 33
android.ndk = 25b

orientation = portrait

[buildozer]
log_level = 2
