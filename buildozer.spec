[app]
title = QRLogger
package.name = qrlogger
package.domain = org.example
source.dir = .
source.include_exts = py,wav
version = 0.1
requirements = kivy,opencv-python,pyzbar,pytesseract,openpyxl,numpy
android.permissions = CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.archs = armeabi-v7a, arm64-v8a
android.ant_dir = /usr/share/ant
# Force Buildozer to use Build-Tools 30.0.2 (which we installed above)
android.build_tools_version = 30.0.2

# Also ensure you target the same SDK
android.api = 31
