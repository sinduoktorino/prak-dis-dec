# Mengimpor class dari modul VectorClock.py yang sudah dibuat
from VectorClock import VectorClock

# Membuat simulasi dengan 3 proses
vc0 = VectorClock(num_processes=3, process_id=0)
vc1 = VectorClock(num_processes=3, process_id=1)
vc2 = VectorClock(num_processes=3, process_id=2)

print("--- Status Awal ---")
print(vc0)
print(vc1)
print(vc2)

# Proses 0 melakukan *local event*
vc0.increment()
print("\n--- Setelah P0 Increment ---")
print(vc0)

# Proses 0 mengirim pesan ke Proses 1
msg = vc0.send_message()
vc1.receive_message(msg)
print("\n--- Setelah P0 Mengirim Pesan ke P1 ---")
print(vc0)
print(vc1)

# Pengecekan Kausalitas
print("\n--- Hasil Pengecekan Kausalitas ---")
print(f"vc0 happens before vc1: {vc0.happens_before(vc1)}")
print(f"vc0 is concurrent with vc2: {vc0.is_concurrent(vc2)}")