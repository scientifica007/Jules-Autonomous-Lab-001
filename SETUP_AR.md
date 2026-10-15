# دليل التشغيل الآمن — Jules Autonomous Lab 001

## 1. مستودع جديد تمامًا

1. في GitHub أنشئ مستودعًا جديدًا باسم `Jules-Autonomous-Lab-001` واجعل **Visibility: Private**.
2. لا تفعّل README أو `.gitignore` تلقائيًا (كلاهما ضمن الحزمة).
3. على Ubuntu فك ضغط الحزمة وافتح الطرفية داخل المجلد الرئيسي.
4. نفذ (استبدل `YOUR_GITHUB_USERNAME` باسم حسابك):

```bash
git init -b main
git add .
git commit -m "Initial isolated Jules test laboratory"
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/Jules-Autonomous-Lab-001.git
git push -u origin main
```

إذا طلب GitHub تسجيل الدخول، استخدم طريقة المصادقة المعتمدة لديك، وليس كلمة المرور العادية.

## 2. صلاحيات Jules

1. انتقل إلى https://jules.google.com وسجل الدخول بحساب Google AI Pro.
2. عند ربط GitHub اختر **Only select repositories** ثم حدد المستودع التجريبي وحده.
3. إذا سبق ومنحته كل المستودعات: GitHub → Settings → Applications → Google Labs Jules → Configure → Repository access → Only select repositories.
4. لا تفعّل أي MCP connectors ولا تنقل ملفات من أعمالك الحالية.
5. إن أمكن، فعّل حماية فرع `main` ومنع الدمج دون مراجعة، وعطّل Auto-merge.

## 3. التجربة الأولى

- في Jules اختر المستودع التجريبي.
- انسخ مضمون `TASKS/01-ruleworld-manual.md` إلى مهمة Jules.
- عندما يعرض خطة العمل راجع نطاقها.
- بعد الإنجاز اطلب PR، راجع الملفات والاختبارات قبل الدمج. حتى لو نجحت المهمة **لا تدمجها في اليوم الأول**؛ سجل النتائج أولًا.

## 4. المرحلة الثانية: العمل أثناء الغياب

- بعد نجاح الاختبار الأول، أنشئ Scheduled Task بالتعليمة الموجودة في `TASKS/04-scheduled-maintenance.md`.
- في اختبار السبعة أيام، اختر تكرارًا يوميًا لمدة خمسة أيام فقط بعد نجاح المهمة اليدوية، ثم أوقف الجدولة بنفسك. إذا أصبحت المراجعة متراكمة فحوّلها إلى أسبوعية.
- لا تطلب مهام إضافية مجدولة لنفس الملفات بالتوازي.
- راجع النتائج في Jules وGitHub وسجلها في `evaluation/scorecard.csv`.

## 5. اختبار الاقتراحات الاستباقية

- افتح Proactivity داخل صفحة Codebase التجريبية في Jules وفعّلها.
- يحتوي المشروع على TODO محددة لتوفير أهداف للاقتراحات؛ اعتماد المقترحات وتشغيلها خطوة منفصلة.

## 6. إنهاء التجربة

- أوقف Scheduled Tasks وProactivity.
- اسحب الصلاحية من إعدادات تطبيق Jules في GitHub.
- احتفظ بالمستودع أو أرشفه. لا تنقل نتائج Jules إلى مشاريعك الفعلية دون مراجعة.
