# 🍽️ Food Ordering System

<p align="center">
  <a href="#"><img src="https://badges.strrl.dev/visits/power0matin/Food-ordering?style=flat&labelColor=333333&logoColor=E7E7E7&label=Visits&logo=github" alt="Visits badge" /></a>
  <a href="#"><img src="https://img.shields.io/github/stars/power0matin/Food-ordering?style=flat&labelColor=333333&logoColor=E7E7E7&color=EEAA00&label=Stars&logo=github" alt="Stars badge" /></a>
  <a href="#"><img src="https://img.shields.io/github/repo-size/power0matin/Food-ordering?style=flat&labelColor=333333&logoColor=E7E7E7&color=007BFF&label=Repo%20Size&logo=github" alt="Repo size badge" /></a>
</p>

این پروژه یک **سیستم سفارش غذا** است که به کاربران امکان می‌دهد غذا و نوشیدنی‌های مختلف را سفارش دهند.
این سیستم شامل بخش‌های مدیریت مشتریان، غذاها، نوشیدنی‌ها، سفارشات، پرداخت‌ها و میزها می‌باشد.


## 🧭 ساختار پروژه

پروژه به چند بخش اصلی تقسیم شده است:

### 📦 مدل‌ها (`model/`)

شامل تعاریف مدل‌های داده‌ای:

* `admin.py` — مدیریت اطلاعات مدیران سیستم
* `customer.py` — مدیریت اطلاعات مشتریان
* `food.py` — مدیریت اطلاعات غذاها
* `drink.py` — مدیریت اطلاعات نوشیدنی‌ها
* `order.py` — مدیریت سفارشات مشتریان
* `payment.py` — مدیریت پرداخت‌ها
* `table.py` — مدیریت اطلاعات میزها


### 🗃️ مخزن‌ها (`repository/`)

شامل پیاده‌سازی CRUD عمومی در یک فایل برای تمامی مدل‌ها:

* `crud_repository.py` — مخزن عمومی برای تمامی مدل‌ها


### 🧠 کنترلرها (`controller/`)

شامل منطق کنترل و مدیریت درخواست‌ها:

* `admin_controller.py` — کنترل و مدیریت مدیران
* `customer_controller.py` — کنترل و مدیریت مشتریان
* `food_controller.py` — کنترل و مدیریت غذاها
* `drink_controller.py` — کنترل و مدیریت نوشیدنی‌ها
* `order_controller.py` — کنترل و مدیریت سفارشات
* `payment_controller.py` — کنترل و مدیریت پرداخت‌ها
* `table_controller.py` — کنترل و مدیریت میزها


### 🧾 لایه خدمات (`service/`)

شامل منطق کسب‌وکار و پردازش داده‌ها:

* `admin_service.py` — سرویس مربوط به مدیران
* `customer_service.py` — سرویس مربوط به مشتریان
* `food_service.py` — سرویس مربوط به غذاها
* `drink_service.py` — سرویس مربوط به نوشیدنی‌ها
* `order_service.py` — سرویس مربوط به سفارشات
* `payment_service.py` — سرویس مربوط به پرداخت‌ها
* `table_service.py` — سرویس مربوط به میزها


### 🖼️ توسعه رابط کاربری (`app.py`)

پیاده‌سازی **رابط کاربری گرافیکی** با استفاده از Tkinter.


## 👥 ساختار تیم

* **متین شاه‌آبادی** — مدیریت مدیران، مسئولیت کلی پروژه و مدیریت GitHub
* **آیدا شمس** — مدیریت مشتریان
* **بردیا زاغری** — مدیریت غذاها
* **مینا رضایی** — مدیریت نوشیدنی‌ها
* **امیر شایان امامی‌پور** — مدیریت سفارشات
* **زهرا خسروی** — مدیریت پرداخت‌ها
* **مهربد مهربانی** — مدیریت میزها


## 🧪 تست و نگهداری

* ✅ تست کلی برنامه (جریان کامل سفارش) باید انجام شود.
* 🐞 خطاها و مشکلات شناسایی و رفع شوند.
* 🧭 بهبودهای لازم در رابط کاربری و تجربه کاربری صورت گیرد.

## 📬 Contact

**Matin Shahabadi (متین شاه‌آبادی / متین شاه آبادی)**

* Website: [matinshahabadi.ir](https://matinshahabadi.ir)
* Email: [me@matinshahabadi.ir](mailto:me@matinshahabadi.ir)
* GitHub: [power0matin](https://github.com/power0matin)
* LinkedIn: [matin-shahabadi](https://www.linkedin.com/in/matin-shahabadi)

