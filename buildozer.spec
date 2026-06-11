[app]
title =The Guessing Game
package.name = guessinggame
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# গিটহাব এনভায়রনমেন্টের জন্য রিকোয়ারমেন্টস একদম ক্লিন রাখা হলো
requirements = python3,kivy==master

orientation = portrait
fullscreen = 0

# Target Android API
android.api = 33
android.minapi = 24
android.ndk_api = 24

# গিটহাব বিল্ডের জন্য NDK সংস্করণ ফাঁকা রাখা ভালো, সে নিজে বেস্ট ও স্ট্যাবলটা টেনে নেবে
# android.ndk = 26b (এটি কমেন্ট আউট করে দেওয়া হলো)

android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
