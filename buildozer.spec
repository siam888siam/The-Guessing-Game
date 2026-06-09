[app]

title = Guessing Game
package.name = guessinggame
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# রিকোয়ারমেন্টস (python3 এবং kivy master)
requirements = python3, kivy==master

orientation = portrait
fullscreen = 0

# (int) Target Android API
android.api = 33

# (int) Minimum API 
android.minapi = 24

# 🚀 NDK সংস্করণ নির্দিষ্ট করে দেওয়া (যাতে লেটেস্ট r28c এরর না দেয়)
android.ndk = 26b
android.ndk_api = 24

# স্বয়ংক্রিয়ভাবে লাইসেন্স গ্রহণ
android.accept_sdk_license = True

# আর্কিটেকচার 
android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1