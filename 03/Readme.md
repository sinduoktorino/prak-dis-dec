# Praktikum 03 — Sistem Terdistribusi

| Informasi | Detail |
|---|---|
| **NIM** | 255410033 |
| **Nama** | Mohamad Sindu Oktorino |

---

## Daftar Isi

- [Tujuan Praktikum](#tujuan-praktikum)
- [Dasar Teori](#dasar-teori)
- [Praktikum](#praktikum)
  - [3.1 Sinkronisasi Waktu](#31-sinkronisasi-waktu)
  - [3.2 Vector Clock](#32-vector-clock)
  - [3.3 Problem Tanpa Sinkronisasi](#33-problem-tanpa-sinkronisasi)
    - [3.3.1 Data Race / Race Conditions](#331-data-race--race-conditions)
    - [3.3.2 Deadlock](#332-deadlock)
  - [3.4 Algoritma Raft](#34-algoritma-raft)
- [Kesimpulan](#kesimpulan)

## Tujuan Praktikum

_Tambahkan tujuan praktikum di sini._

## Dasar Teori

_Tambahkan ringkasan dasar teori di sini._

## Praktikum

### 3.1 Sinkronisasi Waktu

Instal [NetTime](https://www.timesynctool.com/), lalu gunakan aplikasi tersebut untuk menyinkronkan waktu dengan server NTP.

#### Unduhan

![Tampilan unduhan NetTime](dwnld1.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

#### Langkah setup

**Langkah 1**

![Setup NetTime - langkah 1](setup1.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

**Langkah 2**

![Setup NetTime - langkah 2](setup2.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

**Langkah 3**

![Setup NetTime - langkah 3](setup3.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

**Langkah 4**

![Setup NetTime - langkah 4](setup4.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

**Langkah 5**

![Setup NetTime - langkah 5](setup5.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

**Langkah 6**

![Setup NetTime - langkah 6](setup6.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

### 3.2 Vector Clock

#### Simulasi Vector Clock

![Output simulasi Vector Clock](output1.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

#### Tugas Vector Clock

![Output tugas Vector Clock](outputtugasvc.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

### 3.3 Problem Tanpa Sinkronisasi

![Output problem tanpa sinkronisasi](output2.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

#### 3.3.1 Data Race / Race Conditions

**Contoh race condition**

![Output race condition](output3.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

**Diagram race condition**

![Diagram race condition](diagram1.jpeg)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

**Pencegahan dengan lock (`race-conditions-02.py`)**

![Output pencegahan race condition dengan lock](output4.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

**Hasil tambahan**

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

#### 3.3.2 Deadlock

**Contoh deadlock**

![Output deadlock](output5.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

**Diagram deadlock**

![Diagram deadlock](diagram2.jpeg)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

**Pencegahan dengan timeout (`deadlock-02.py`)**

![Output pencegahan deadlock dengan timeout](output6.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

**Hasil tambahan**

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

### 3.4 Algoritma Raft

#### Konfigurasi dan simulasi

![Algoritma Raft - langkah 1](raft1.png)

![Algoritma Raft - langkah 2](raft2.png)

![Algoritma Raft - langkah 3](raft3.png)

![Algoritma Raft - langkah 4](raft4.png)

![Algoritma Raft - langkah 5](raft5.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

#### Diagram Raft

![Diagram algoritma Raft](diagram3.jpeg)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

#### Output program

![Output Raft - bagian 1](outputraft1.png)

![Output Raft - bagian 2](outputraft2.png)

![Output Raft - bagian 3](outputraft3.png)

![Output Raft - bagian 4](outputraft4.png)

> **Pembahasan:** _Tuliskan hasil dan pembahasan di sini._

## Kesimpulan

_Tuliskan kesimpulan praktikum di sini._
