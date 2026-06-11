[app]
title = The Guessing Game
package.name = guessinggame
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0

android.api = 31
android.minapi = 21
android.ndk_api = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
