#!/bin/bash

pkg update -y && pkg upgrade -y
pkg install git python -y

# ลบของเก่าถ้ามี เพื่อแก้บั๊ก clone ไม่ได้
rm -rf spam-a-IP

# clone repo ของมึง
git clone https://github.com/boonkongbanpao-sudo/spam-a-IP.git

# เข้าโฟลเดอร์
cd spam-a-IP

# รันไฟล์หลักของมึง
python3 spam-a-IP.py
