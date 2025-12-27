[app]
title = My Google Client
package.name = mygoogle
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
fullscreen = 0
android.permissions = INTERNET
# ВАЖНО: Настройки для старых телефонов
android.minapi = 19
android.archs = armeabi-v7a
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1