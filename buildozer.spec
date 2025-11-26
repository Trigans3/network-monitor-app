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
android.archs = arm64-v8a

orientation = portrait

# Указываем пути к SDK и NDK
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.1.8937393

# Отключаем обновление SDK (мы уже установили вручную)
android.skip_update = True
android.accept_sdk_license = True

log_level = 2

[buildozer]
log_level = 2
