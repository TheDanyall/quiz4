[app]

# عنوان اپليکيشن
title = English Quiz

# نام پکيج
package.name = englishquiz

# دامنه معکوس براي پکيج
package.domain = org.example

# نسخه اپليکيشن - فرمت X.Y.Z
version = 1.0.0

# نسخه کد - بايد عدد باشد
version.code = 1

# نسخه پايتون مورد نياز
requirements = python==3.8.10,kivy==2.3.1

# آيکون اپليکيشن
#icon.filename = %(source.dir)s/data/icon.png

# فايل اصلي اپليکيشن
source.dir = .

# فايل اصلي اجرايي
source.main = main.py

# جهت‌گيري صفحه (portrait يا landscape)
orientation = portrait

# ويژگي‌هاي مورد نياز
android.permissions = INTERNET

# نسخه اندرويد SDK
#android.sdk = 23

# نسخه اندرويد API
android.api = 31

android.minapi = 21

# نسخه NDK
#android.ndk = 23b

# android.build_tools_version =

# معماري‌هاي پشتيباني شده
android.archs = arm64-v8a
buildozer.require_artifact = apk

# غيرفعال کردن انيميشن‌هاي پيش‌فرض
android.window_soft_input_mode = adjustResize

# گزينه‌هاي build
[buildozer]

# آدرس مخزن log
log_level = 2

# پوشه ساخت
build_dir = ./.buildozer

# پوشه خروجي
bin_dir = ./bin