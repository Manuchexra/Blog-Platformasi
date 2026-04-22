# 📝 Blog Platformasi

Django asosida qurilgan to'liq funksional blog platformasi. Foydalanuvchilar ro'yxatdan o'tib, maqola yozishi, tahrirlashi, o'chirishi va izoh qoldirishi mumkin.

---

## ✨ Funksiyalar

| Funksiya | Tavsif |
|---|---|
| 📋 Maqolalar ro'yxati | Barcha maqolalarni ko'rish |
| 📄 Maqola tafsiloti | Bitta maqolani to'liq o'qish |
| ✍️ Maqola yozish | Tizimga kirgan foydalanuvchi uchun |
| ✏️ Maqola tahrirlash | Faqat muallif tahrirlay oladi |
| 🗑️ Maqola o'chirish | Faqat muallif o'chira oladi |
| 💬 Izoh qoldirish | Tizimga kirgan foydalanuvchilar uchun |
| 👤 Ro'yxatdan o'tish | Yangi hisob yaratish |
| 🔐 Tizimga kirish / chiqish | Autentifikatsiya |

---

## 🛠️ Texnologiyalar

- **Backend:** Python, Django
- **Frontend:** HTML, CSS (`styles.css`)
- **Ma'lumotlar bazasi:** SQLite (Django default)
- **Autentifikatsiya:** Django `auth` (login, logout, register)

---



## ⚙️ O'rnatish va ishga tushirish

### 1. Reponi klonlash

```bash
git clone https://github.com/Manuchexra/Blog-Platformasi.git
cd Blog-Platformasi
```

### 2. Virtual muhit yaratish

```bash
python -m venv venv

# Linux / Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 3. Kerakli kutubxonalarni o'rnatish

```bash
pip install -r requirements.txt
```

### 4. Migratsiyalarni bajarish

```bash
python manage.py migrate
```

### 5. (Ixtiyoriy) Admin foydalanuvchi yaratish

```bash
python manage.py createsuperuser
```

### 6. Serverni ishga tushirish

```bash
python manage.py runserver
```

Brauzerda oching 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔗 URL yo'nalishlari

| URL | Funksiya |
|---|---|
| `/` | Maqolalar ro'yxati |
| `/post/<pk>/` | Maqola tafsiloti |
| `/post/new/` | Yangi maqola yozish |
| `/post/<pk>/edit/` | Maqolani tahrirlash |
| `/post/<pk>/delete/` | Maqolani o'chirish |
| `/post/<pk>/comment/` | Izoh qo'shish |
| `/register/` | Ro'yxatdan o'tish |
| `/login/` | Tizimga kirish |
| `/logout/` | Tizimdan chiqish |

---

## 🔒 Ruxsatlar

- Maqola **yozish**, **tahrirlash**, **o'chirish** va **izoh qoldirish** uchun tizimga kirgan bo'lish shart (`@login_required`).
- Maqolalarni **ko'rish** esa barcha foydalanuvchilar uchun ochiq.

---
