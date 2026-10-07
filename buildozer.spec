[app]
title = Python Calculator
package.name = pycalculator
package.domain = org.example

source.dir = .
source.include_exts = py
source.exclude_patterns = test_*.py

version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
