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
