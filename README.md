# Loyiha: Corporate CRM

## Komponentlar

### Korxona (core app)

**Settings:** [settings.py](core/settings.py)

### URLs

**Asosiy URLs:** [urls.py](core/urls.py)

**Qrcode URLs:** [urls.py](qrcode/urls.py)

**CRM URLs:** [urls.py](crm/urls.py)

**Foydalanuvchi tasdiqlash URLs:** [urls.py](userverification/urls.py)

### Modellar

**Qrcode Modellar:**
- [Category](qrcode/models.py)
- [Product](qrcode/models.py)

**CRM Modellar:**
- [Activity](crm/models.py)
- [CreateProduct](crm/models.py)
- [UtilzedProduct](crm/models.py)

**Foydalanuvchi tasdiqlash Modellari:**
- [UserProfile](userverification/models.py)

### Serializatorlar

**Qrcode Serializatorlar:**
- [ProductSerializer](qrcode/serializer.py)

**CRM Serializatorlar:**
- [ProductSerializer](crm/serializer.py)
- [CreateProductSerializer](crm/serializer.py)
- [UtilzedProductSerializer](crm/serializer.py)

**Foydalanuvchi tasdiqlash Serializatorlari:**
- [UserProfileSerializer](userverification/serializer.py)
- [UserSerializer](userverification/serializer.py)

### Views

**Qrcode Views:**
- [ProductView](qrcode/views.py)
- [UserProductView](qrcode/views.py)

**CRM Views:**
- [CreateProduct](crm/views.py)
- [UtilizedProduct](crm/views.py)
- [CreateProductTable](crm/views.py)

**Foydalanuvchi tasdiqlash Views:**
- [SendOTPAPI](userverification/views.py)
- [VerifyOTPAPI](userverification/views.py)
- [UserProfilePut](userverification/views.py)

### SMS Yuborish Moduli

**Eskiz SMS Yuborish Moduli:**
- [eskiz_sms_send](eskiz_sms_send.py)

### Hashlash Moduli

**MD5 Hashlash Moduli:**
- [md5_hash](md5_hash.py)

## O'rnatish

1. Python o'rnatilganligini tekshiring.
2. Virtual muhitni yaratish: `python -m venv venv`
3. Muhitni faollashtirish: 
   - Windows uchun: `venv\Scripts\activate`
   - Linux / macOS uchun: `source venv/bin/activate`
4. Loyihaning joylashuvi bo'yicha o'ting: `cd joylashuvingiz`
5. Loyiha kerakli kutubxonalarni o'rnatish uchun: `pip install -r requirements.txt`
6. Migrations va loyiha ishga tushirish: 
   - `python manage.py makemigrations`
   - `python manage.py migrate`
7. Loyiha serverini ishga tushirish: `python manage.py runserver`

Loyiha `http://127.0.0.1:8000/` manzilida ishlaydi.

## Murojaat

Agar savollar yoki takliflar bo'lsa, iltimos, [Menga](https://t.me/U1_UXdesigner)ga murojaat qiling.

Rahmat!
