# دریافت چهار عدد از کاربر
a = float(input("عدد اول را وارد کنید: "))
b = float(input("عدد دوم را وارد کنید: "))
c = float(input("عدد سوم را وارد کنید: "))
d = float(input("عدد چهارم را وارد کنید: "))

# پیدا کردن بزرگ‌ترین عدد
max_num = a  # فرض می‌کنیم عدد اول بزرگ‌ترین است
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c
if d > max_num:
    max_num = d

print("بزرگ‌ترین عدد:", max_num)