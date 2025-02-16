
from PyInstaller.utils.hooks import collect_submodules, collect_data_files


icon_path = "imags\\tent_ico_.ico"

# استيراد جميع الوحدات داخل المجلدات
hidden_imports = collect_submodules('app')
hidden_imports += collect_submodules('app.views')
hidden_imports += collect_submodules('app.controllers')
hidden_imports += collect_submodules('app.services')
hidden_imports += collect_submodules('babel.numbers')
hidden_imports +=['babel.numbers']


# جمع جميع الملفات المطلوبة (مثل ملفات قاعدة البيانات أو ملفات ثابتة)
datas = [
    ('views/forest-dark.tcl', 'views'),  # (المسار الأصلي، المسار داخل البرنامج)
    ('views/forest-dark', 'views/forest-dark'),
    ('imags/', 'imags'),
    ('venv/Lib/site-packages/babel/numbers.py', 'babel'),
    ('db/CampMartyrs.db', 'db'),
]
datas += collect_data_files('db', include_py_files=True)
datas += collect_data_files('app.views.forest-dark', includes=['*.png'])
datas += collect_data_files('app.imags', includes=['*.png'])
datas += collect_data_files('app.imags', includes=['*.ico'])
datas += collect_data_files('app.views', includes=['*.tcl'])
datas += collect_data_files('app.views')

# إنشاء التحليل (Analysis) للمشروع
a = Analysis(
    ['main.py'],  # الملف الرئيسي لتشغيل المشروع
    pathex=['.'],     # المسار الرئيسي للمشروع
    binaries=[],      # ملفات ثنائية إضافية إن وجدت
    datas=datas,      # بيانات إضافية (مثل قواعد البيانات)
    hiddenimports=hidden_imports,  # استيرادات مخفية
    hookspath=[],     # مسارات hooks مخصصة (إذا لزم الأمر)
    hooksconfig={},
    runtime_hooks=[], # runtime hooks إن وجدت
    excludes=['PyQt6', 'PyQt5', 'pyside6'],      # وحدات مستثناة (إذا كنت تريد استثناء مكتبات)
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False
)

# دمج الوحدات
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# إنشاء الملف التنفيذي
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CampMartyrs',  # اسم المشروع
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # استخدم True إذا كنت تريد نافذة طرفية (Console)، أو False لتطبيق بدون طرفية
    icon = icon_path
)

# جمع كل شيء في ملف واحد
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CampMartyrs'
)