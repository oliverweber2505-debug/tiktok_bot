[app]

# (str) Title of your application
title = TikTok Bot

# (str) Package name
package.name = tiktokbot

# (str) Package domain (needed for android packaging)
package.domain = org.tiktokbot

# (str) Source files to include (let it include python files and assets)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to include (let it empty to include all files)
source.include_patterns = assets/*,images/*.png

# (list) Application requirements
# Achte darauf, dass wichtige Bibliotheken wie requests oder kivy hier stehen, falls dein Skript sie nutzt
requirements = python3,kivy,requests

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 30

# (str) Android NDK version to use
android.ndk = 25b

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = corrigé)
warn_on_root = 1
