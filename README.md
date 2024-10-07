
# Food Ordering System

این پروژه یک سیستم سفارش غذا است که به کاربران امکان می‌دهد غذا و نوشیدنی‌های مختلف را سفارش دهند. این سیستم شامل مدیریت مشتریان، غذاها، نوشیدنی‌ها، سفارشات و پرداخت‌ها می‌باشد.

## ساختار پروژه

پروژه به چند بخش اصلی تقسیم شده است:

- **مدل‌ها (model/)**: شامل تعاریف مدل‌های داده‌ای.
  - `admin.py`
  - `customer.py`
  - `food.py`
  - `drink.py`
  - `order.py`
  - `payment.py`

- **مخزن‌ها (repositorie/)**: شامل پیاده‌سازی CRUD برای هر مدل.
  - `admin_repository.py`
  - `customer_repository.py`
  - `food_repository.py`
  - `drink_repository.py`
  - `order_repository.py`
  - `payment_repository.py`

- **کنترلرها (controller/)**: شامل منطق کنترل و مدیریت درخواست‌ها.
  - `admin_controller.py`
  - `customer_controller.py`
  - `food_controller.py`
  - `drink_controller.py`
  - `order_controller.py`
  - `payment_controller.py`

- **لایه خدمات (service/)**: شامل منطق کسب‌وکار و پردازش داده‌ها.
  - `admin_service.py`
  - `customer_service.py`
  - `food_service.py`
  - `drink_service.py`
  - `order_service.py`
  - `payment_service.py`



- **توسعه GUI (main.py)**: شامل پیاده‌سازی رابط کاربری با استفاده از Tkinter.
  

## ساختار تیم

متین شاه‌آبادی: مسئولیت کلی پروژه و مدیریت GitHub.

آیدا شمس: مدیریت مشتریان.

بردیا زاغری: مدیریت غذاها.

مینا رضایی: مدیریت نوشیدنی‌ها.

امیر شایان امامی‌پور: مدیریت سفارشات.

زهرا خسروی: مدیریت پرداخت‌ها.

مهربد مهربانی: توسعه و طراحی رابط کاربری.
## 


تست و نگهداری
تست کلی برنامه (جریان کامل سفارش) باید انجام شود.
خطاها و مشکلات شناسایی و رفع شوند.
بهبودهای لازم در رابط کاربری و تجربه کاربری انجام شود.
