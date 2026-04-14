```markdown
# 🚀 Code Bundler & Project Tree Scripts

مجموعة من سكربتات Python المصممة لمشاريع (React, Node.js, Express TS, Flutter) لتجميع الأكواد وتوليد هيكلية المشروع في ملفات نصية سهلة القراءة.

## 📋 المتطلبات الأساسية
* يجب تثبيت **Python 3.x** على جهازك
* تأكد من إضافة Python إلى مسار النظام (Environment Variables)
* تأكد من تثبيت **Node.js** و **npm** لمشاريع Express TS

---

## 📦 محتويات الحزمة

| الملف | الوصف |
| :--- | :--- |
| `for-react.py` | تجميع كود React |
| `for-node.py` | تجميع كود Node.js |
| `for-express-ts.py` | تهيئة مشروع Express TypeScript + MongoDB |
| `for-flutter.py` | تجميع كود Flutter |
| `get-root-file.py` | توليد شجرة المجلدات |
| `init-backend/` | أداة متكاملة لتهيئة مشاريع Express TS |

---

## 💻 إعداد الاختصارات (Setup Shortcuts)

### 🪟 Windows (PowerShell)
1. افتح PowerShell واكتب:
   ```powershell
   notepad $PROFILE
   ```
2. أضف الأوامر التالية (مع تعديل المسار `C:\Scripts` للمكان الفعلي للملفات):
   ```powershell
   function bundle-react { python "C:\Scripts\for-react.py" }
   function bundle-node { python "C:\Scripts\for-node.py" }
   function init-backend { python "C:\Scripts\init-backend\init-backend.py" }
   function bundle-flutter { python "C:\Scripts\for-flutter.py" }
   function get-tree { python "C:\Scripts\get-root-file.py" }
   
   # اختصارات سريعة
   Set-Alias br bundle-react
   Set-Alias bn bundle-node
   Set-Alias ib init-backend
   Set-Alias bf bundle-flutter
   Set-Alias gt get-tree
   ```

---

### 🍎 macOS & 🐧 Linux
1. افتح ملف الإعدادات (`~/.zshrc` أو `~/.bashrc`):
   ```bash
   nano ~/.zshrc
   ```
2. أضف الـ Aliases التالية:
   ```bash
   alias br='python3 /path/to/scripts/for-react.py'
   alias bn='python3 /path/to/scripts/for-node.py'
   alias ib='python3 /path/to/scripts/init-backend/init-backend.py'
   alias bf='python3 /path/to/scripts/for-flutter.py'
   alias gt='python3 /path/to/scripts/get-root-file.py'
   ```

---

## 🛠️ كيفية الاستخدام (Usage)

| الأمر | الوصف | ملف المخرجات |
| :--- | :--- | :--- |
| `br` | تجميع كود **React** | `react_code.txt` |
| `bn` | تجميع كود **Node.js** | `node_code.txt` |
| `ib` | **تهيئة مشروع Express TypeScript + MongoDB** | مشروع كامل جاهز |
| `bf` | تجميع كود **Flutter** | `mobile-code.txt` |
| `gt` | توليد شجرة مجلدات المشروع مع التعليقات | `app-root.md` |

---

## 🚀 تهيئة مشروع Express TypeScript + MongoDB

أداة متكاملة لإنشاء مشروع Express TypeScript مع MongoDB جاهز للتطوير.

### المميزات
- ✅ هيكل مجلدات احترافي (config, controllers, middleware, models, routes, services, utils)
- ✅ مصادقة JWT مدمجة (تسجيل وتسجيل دخول)
- ✅ نموذج User مع تشفير كلمة المرور
- ✅ اتصال MongoDB باستخدام Mongoose
- ✅ Middleware للتحقق من الصلاحيات
- ✅ Error handling مركزي
- ✅ متغيرات بيئة جاهزة

### الاستخدام
```bash
# تشغيل الأداة
ib

# أو
python3 init-backend/init-backend.py

# اتبع التعليمات
? Project name (default: express-ts-mongo): my-awesome-api
? Run 'npm install' now? (Y/n): Y

# بعد الانتهاء
cd my-awesome-api
cp .env.example .env
# قم بتعديل MONGO_URI و JWT_SECRET في ملف .env
npm run dev
```

### هيكل المشروع المُنشأ
```
my-awesome-api/
├── src/
│   ├── config/         # اتصال قاعدة البيانات وإعدادات البيئة
│   ├── controllers/    # معالجة الطلبات
│   ├── middleware/     # التحقق من المصادقة والصلاحيات
│   ├── models/         # نماذج Mongoose
│   ├── routes/         # مسارات API
│   ├── services/       # منطق الأعمال
│   ├── utils/          # دوال مساعدة
│   ├── app.ts          # تهيئة Express
│   └── server.ts       # نقطة الدخول
├── .env.example        # مثال لمتغيرات البيئة
├── package.json        # التبعيات والscripts
├── tsconfig.json       # إعدادات TypeScript
└── README.md           # توثيق المشروع
```

### الـ API Endpoints المتاحة
| الطريقة | المسار | الوصف |
| :--- | :--- | :--- |
| POST | `/api/auth/register` | تسجيل مستخدم جديد |
| POST | `/api/auth/login` | تسجيل الدخول |
| GET | `/api/users/profile` | جلب بيانات المستخدم (يتطلب token) |
| GET | `/health` | فحص صحة الخادم |

---

## 📝 أمثلة إضافية

### تجميع كود React
```bash
cd my-react-app
br
# ينتج ملف react_code.txt يحتوي على جميع الأكواد
```

### تجميع كود Node.js
```bash
cd my-node-api
bn
# ينتج ملف node_code.txt
```

### توليد شجرة المشروع
```bash
gt
# ينتج ملف app-root.md بهيكل المجلدات مع تعليقاتك
```

---

## 🤝 المساهمة

يمكنك تعديل السكربتات حسب احتياجاتك:
- أضف امتدادات ملفات جديدة في قوائم الاستبعاد/التضمين
- غير مسار ملفات المخرجات
- أضف قوالب جديدة في مجلد `init-backend/templates/`

---

## 📄 الترخيص

هذا المشروع مفتوح المصدر - يمكنك استخدامه وتعديله بحرية.

---
**Happy Coding!** 🚀
```