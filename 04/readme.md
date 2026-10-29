**👤 Nama:** Mohamad Sindu Oktorino

**🎓 NIM:** 255410033

## 🎯 TUJUAN PRAKTIKUM
Praktikum ini bertujuan untuk memahami konsep konsistensi dan replikasi data pada sistem terdistribusi menggunakan PostgreSQL dan Apache Ignite. Praktikum ini juga bertujuan untuk mempelajari konfigurasi database menggunakan Docker, menguji sinkronisasi data ant server, serta memahami penerapan High Availability dan replikasi pada cluster.

## 📚 DASAR TEORI
Sistem terdistribusi merupakan sistem yang terdiri atas beberapa komputer atau layanan yang bekerja sama untuk menjalankan suatu fungsi. Replikasi data merupakan proses menyalin dan menyinkronkan data pada beberapa server atau node agar data tetap tersedia dan dapat diakses sesuai peran masing-masing.
Streaming Replication pada PostgreSQL menggunakan server primary sebagai server utama yang menerima perubahan data, kemudian meneruskan perubahan tersebut ke server replica. Replica dapat menyediakan akses baca dan dapat dipromosikan menjadi primary ketika diperlukan.
Apache Ignite menggunakan cluster yang terdiri atas beberapa node untuk mengelola dan mendistribusikan data. Dalam konfigurasi pada praktikum ini, beberapa node berada dalam satu cluster dan dapat diakses melalui endpoint masing-masing. Docker digunakan untuk menjalankan layanan tersebut dalam container, sedangkan Docker Compose membantu mengatur beberapa container melalui satu file konfigurasi.

## 🧪 PRAKTIKUM

### 🐳 4.1.1 Instalasi Docker

1. Instal docker melalui website docker docs

<img src="images/dwnld1.png" width="700">

**📝 Pembahasan:**
Pada langkah pertama, Docker diunduh melalui situs resminya untuk menyediakan lingkungan yang dibutuhkan dalam menjalankan PostgreSQL. Docker memungkinkan layanan database berjalan dalam container sehingga konfigurasi server dapat dikelola tanpa instalasi PostgreSQL secara langsung pada sistem operasi utama.

2. Proses instalasi

<img src="images/setup1.png" width="700">

**📝 Pembahasan:**
Proses instalasi dilakukan melalui Docker Desktop. 

<img src="images/setup2.png" width="700">
<img src="images/install2.png" width="700">

**📝 Pembahasan:**
Setelah instalasi selesai, Docker Desktop dijalankan agar Docker Engine dapat digunakan untuk menjalankan container.

**🔎 Cek versi docker yang digunakan**

<img src="images/info1.png" width="700">
<img src="images/info2.png" width="700">

**📝 Pembahasan:**
Pemeriksaan versi Docker dilakukan menggunakan perintah docker --version untuk mengetahui versi perangkat lunak yang terpasang. Perintah docker compose version digunakan untuk memeriksa versi Docker Compose.



**🔎 Cek docker info**

```text
C:\Users\SINDU>docker info
Client:
 Version:    29.9.2
 Context:    desktop-linux
 Debug Mode: false
 Plugins:
  agent: Docker AI Agent Runner (Docker Inc.)
    Version:  v1.152.0
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-agent.exe
  ai: Docker AI Agent - Ask Gordon (Docker Inc.)
    Version:  v1.33.0
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-ai.exe
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.38.1
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-buildx.exe
  compose: Docker Compose (Docker Inc.)
    Version:  v5.6.1
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-compose.exe
  debug: Get a shell into any image or container (Docker Inc.)
    Version:  0.49.0
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-debug.exe
  desktop: Docker Desktop commands (Docker Inc.)
    Version:  4.97.0
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-desktop.exe
  dhi: CLI for managing Docker Hardened Images (Docker Inc.)
    Version:  v0.0.9
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-dhi.exe
  extension: Manages Docker extensions (Docker Inc.)
    Version:  v0.2.32
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-extension.exe
  init: Creates Docker-related starter files for your project (Docker Inc.)
    Version:  v1.4.1
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-init.exe
  mcp: Docker MCP Plugin (Docker Inc.)
    Version:  v0.44.2
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-mcp.exe
  model: Docker Model Runner (Docker Inc.)
    Version:  v1.2.9
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-model.exe
  offload: Docker Offload (Docker Inc.)
    Version:  v0.7.21
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-offload.exe
  pass: Docker Pass Secrets Manager Plugin (beta) (Docker Inc.)
    Version:  v0.3.2
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-pass.exe
  sandbox: "docker sandbox" is deprecated, use Docker Sandboxes instead (Docker Inc.)
    Version:  v0.13.0
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-sandbox.exe
  scout: Docker Scout (Docker Inc.)
    Version:  v1.27.0
    Path:     C:\Users\SINDU\.docker\cli-plugins\docker-scout.exe
    Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 1
 Server Version: 29.9.2
 Storage Driver: overlayfs
  driver-type: io.containerd.snapshotter.v1
 Logging Driver: local
 Cgroup Driver: cgroupfs
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Discovered Devices:
  cdi: docker.com/gpu=webgpu
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 nvidia runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: b7a25261e029d68978bbf290df0a62fc819b3c51
 runc version: v1.5.2-0-g29dd3dc2
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.18.54.1-microsoft-standard-WSL2
 Operating System: Docker Desktop
 OSType: linux
 Architecture: x86_64
 CPUs: 4
 Total Memory: 7.688GiB
 Name: docker-desktop
 ID: 6fe02c15-3eac-4a8a-9a1e-2ae5274caa07
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 HTTP Proxy: http.docker.internal:3128
 HTTPS Proxy: http.docker.internal:3128
 No Proxy: hubproxy.docker.internal
 Labels:
  com.docker.desktop.address=npipe://\\.\pipe\docker_cli
 Experimental: false
 Insecure Registries:
  hubproxy.docker.internal:5555
  127.0.0.0/8
  ::1/128
 Live Restore Enabled: false
 Firewall Backend: iptables
```

**📝 Pembahasan:**
Pemeriksaan menggunakan perintah docker info menampilkan informasi mengenai Docker Engine, sistem operasi, arsitektur, jumlah CPU, memori, dan kondisi container. Hasil tersebut menunjukkan bahwa Docker Desktop telah tersedia dan dapat digunakan sebagai lingkungan praktikum.

### 🗂️ 4.1.2 Struktur direktori file

```text
streaming-replication/
├── 00_init.sql
├── docker-compose.yaml
└── env.sh

1 directory, 3 files
```

**📄 00_inite.sql**

<img src="images/initsql.png" width="700">

**📝 Pembahasan:**
File 00_init.sql berisi perintah SQL untuk membuat pengguna bernama replicator yang memiliki hak replikasi serta membuat physical replication slot bernama replication_slot. Pengguna dan slot tersebut diperlukan untuk mendukung proses pengiriman data dari primary ke replica.

**🐳 docker-compose.yml**

<img src="images/doccomp.png" width="700">

**📝 Pembahasan:**
File docker-compose.yaml digunakan untuk menentukan konfigurasi layanan PostgreSQL primary dan replica, termasuk image, port, variabel lingkungan, serta parameter replikasi.

**⚙️ env.sh**

<img src="images/envs.png" width="700">

**📝 Pembahasan:**
File env.sh berisi alias perintah untuk mempersingkat pengoperasian Docker, seperti menjalankan container, menghentikan layanan, memeriksa container, dan melihat log.


### ▶️ 4.1.3 Menjalankan docker

1.

<img src="images/sql2.png" width="700">

**📝 Pembahasan:**
Pada langkah pertama, layanan PostgreSQL dijalankan menggunakan Docker Compose dari direktori yang berisi konfigurasi. Docker akan menyiapkan container primary dan replica berdasarkan pengaturan yang telah dibuat.

2.

<img src="images/sql3.png" width="700">

<img src="images/sql4.png" width="700">

<img src="images/sql5.png" width="700">

**📝 Pembahasan:**
Dilakukan pemeriksaan terhadap proses pengaktifan layanan dan kondisi container. Pemeriksaan ini bertujuan untuk memastikan bahwa kedua layanan PostgreSQL berhasil dijalankan. Status container dan log digunakan untuk mengetahui apakah terdapat masalah selama proses inisialisasi.

5.

<img src="images/sql6.png" width="700">

**📝 Pembahasan:**
Setelah container berjalan, layanan primary berfungsi menerima operasi baca dan tulis, sedangkan replica berfungsi sebagai server standby yang mengikuti perubahan data dari primary. Dengan demikian, kedua server dapat bekerja sesuai perannya dalam konfigurasi streaming replication.

### 🧪 4.1.4 Pengujian

<img src="images/sql7.png" width="700">

<img src="images/sql8.png" width="700">

**📝 Pembahasan:**
Pengujian dilakukan untuk memastikan bahwa PostgreSQL telah menjalankan proses replikasi dengan benar. Pemeriksaan dilakukan melalui informasi status replikasi dan aktivitas database pada server primary serta replica

<img src="images/sql10.png" width="700">

**📝 Pembahasan:**
Pada pemeriksaan status replica, nilai true pada indikator yang digunakan menunjukkan bahwa server berada dalam mode standby atau recovery. Kondisi tersebut menandakan bahwa server menjalankan peran replica dan belum berfungsi sebagai primary untuk operasi tul

**📋 Sebelum pembuatan table**

**🔑 Primary**

<img src="images/sql11.png" width="700">

**📝 Pembahasan:**
Sebelum tabel dibuat, kondisi database diperiksa pada server primary dan replica sebagai pembanding awal. 

**✏️ Manipulasi data pada primary**

<img src="images/sql12.png" width="700">

**📝 Pembahasan:**
Selanjutnya, tabel dibuat dan data dimasukkan melalui server primary. Hasil perubahan tersebut kemudian diperiksa pada server replica.

<img src="images/sql13.png" width="700">

**📝 Pembahasan:**
Data yang muncul pada replica menunjukkan bahwa perubahan pada primary telah diteruskan melalui proses replikasi. Pengujian ini membuktikan bahwa konfigurasi dapat menyinkronkan data antara server utama dan server standby.

### 🛡️ 4.1.5 High-Availability

<img src="images/tes1.png" width="700">

**📝 Pembahasan:**
Pada tahap ini, praktikum mempelajari mekanisme High Availability dengan mensimulasikan kondisi ketika server primary berhenti beroperasi. Dalam kondisi tersebut, replica dapat dipromosikan menjadi primary agar mampu menerima operasi baca dan tulis. Promosi dilakukan menggunakan fungsi pg_promote(). Fungsi tersebut mengubah replica dari kondisi standby menjadi server utama yang dapat menerima perubahan data. Langkah ini menunjukkan cara mengalihkan peran server ketika primary mengalami gangguan.

<img src="images/stop1.png" width="700">

**📝 Pembahasan:**
Setelah pengujian selesai, seluruh container dihentikan menggunakan Docker Compose. Penghentian layanan dilakukan untuk mengakhiri praktikum dan memastikan container tidak terus berjalan ketika sudah tidak diperlukan.

### 🔁 4.2 Replika pada master-master

**🗂️ Struktur direktori file**

```text
04/
├── sql/
│   ├── current_catalog.sql
│   ├── ee_and_cust.sql
│   ├── invoices.sql
│   ├── media_and_genre.sql
│   ├── schema.sql
│   └── tracks.sql
├── docker-compose.yaml
└── env.sh
```

**⚙️ env.sh**

<img src="images/envs1.png" width="700">

**📝 Pembahasan:**
File env.sh berisi alias untuk menjalankan layanan, memeriksa container, dan membuka Apache Ignite CLI. Alias tersebut bertujuan mempersingkat penulisan perintah selama praktikum.

#### ▶️ 4.2.1 Menjalankan docker compose

<img src="images/ign1.png" width="700">
<img src="images/ign2.png" width="700">
**📝 Pembahasan:**
Pada langkah ini, Docker Compose digunakan untuk menjalankan tiga node Apache Ignite berdasarkan konfigurasi yang telah dibuat. Ketika dijalankan pertama kali, Docker mengunduh image yang diperlukan sebelum membuat dan menjalankan container.

**🌐 Tes ip**

<img src="images/ign3.png" width="700">

**📝 Pembahasan:**
Setelah proses tersebut selesai, kondisi container diperiksa untuk memastikan ketiga node telah aktif. Pemeriksaan alamat IP dilakukan menggunakan perintah docker inspect agar informasi jaringan setiap container dapat diketahui. Setiap node memiliki endpoint administratif yang dipetakan melalui port 10300, 10301, dan 10302. Port tersebut digunakan untuk mengakses masing-masing node melalui komputer host. Pengujian ini menjadi persiapan sebelum cluster diinisialisasi dan perintah SQL dijalankan.

#### ⚙️ 4.2.2 Instalasi cluster

```text
docker run --rm -it --network=host -e LANG=C.UTF-8 -e LC_ALL=C.UTF-8 apacheignite/ignite:3.1.0 cli
```

<img src="images/ai1.png" width="700">

<img src="images/ai2.png" width="700">

<img src="images/ai3.png" width="700">

**📝 Pembahasan:**
Inisialisasi cluster dilakukan dengan menjalankan Apache Ignite CLI melalui container. Setelah CLI terbuka, perintah inisialisasi diberikan dengan nama cluster ignite3 dan kelompok Meta Storage yang terdiri atas node1, node2, dan node3. Proses ini bertujuan membentuk cluster agar ketiga node dapat bekerja sebagai satu kesatuan. Setelah inisialisasi berhasil, CLI dapat digunakan untuk mengakses cluster melalui salah satu endpoint node.
Cluster yang telah diinisialisasi menjadi lingkungan untuk menjalankan perintah SQL dan menguji propagasi perubahan data antarnode. Inisialisasi tidak perlu diulangi setiap kali CLI dibuka kembali selama cluster yang sudah dibuat tetap tersedia.

#### 💻 4.2.2 Eksekusi file Sql

<img src="images/ai4.png" width="700">

**📝 Pembahasan:**
Pada tahap ini, file SQL yang tersedia dalam direktori sql digunakan untuk menyiapkan struktur dan data pada Apache Ignite. File tersebut mencakup skema database, data pelanggan, tagihan, katalog, serta informasi musik.

<img src="images/ai5.png" width="700">

**📝 Pembahasan:**
Selanjutnya, perintah SELECT * FROM system.tables WHERE schema = 'PUBLIC'; dijalankan untuk memeriksa tabel pada skema PUBLIC. Hasil query digunakan untuk memastikan bahwa tabel telah terdaftar di dalam cluster.

<img src="images/ai6.png" width="700">

**📝 Pembahasan:**
Direktori SQL dihubungkan ke container agar file dapat diakses oleh Apache Ignite CLI. Setelah koneksi ke cluster berhasil dilakukan, perintah SQL dijalankan untuk membuat struktur tabel dan mengisi data sesuai isi file yang digunakan.

<img src="images/ai7.png" width="700">


**📝 Pembahasan:**
Setelah itu, koneksi dilakukan melalui node lain untuk memeriksa apakah data dan struktur tabel yang telah dibuat juga tersedia pada node tersebut. Hasil pemeriksaan pada endpoint 10301 dan 10302 digunakan untuk mengamati propagasi data dalam cluster. Pengujian ini menunjukkan bahwa perubahan dapat diakses melalui node lain sesuai mekanisme pengelolaan data Apache Ignite.

<img src="images/ai8.png" width="700">

**📝 Pembahasan:**
Query analisis penjualan bulanan digunakan untuk menghitung jumlah tagihan, jumlah pelanggan, total pendapatan, dan rata-rata nilai transaksi berdasarkan bulan. Query tersebut mengelompokkan data berdasarkan tahun dan bulan, kemudian mengurutkan hasil berdasarkan periode terbaru.

<img src="images/ai12.png" width="700">

**📝 Pembahasan:**
Pengujian ini memperlihatkan bahwa data yang telah disiapkan dapat digunakan untuk menjalankan query analitis melalui cluster Apache Ignite. Hasilnya juga membantu memeriksa ketersediaan data pada node yang digunakan untuk menjalankan query.

<img src="images/down1.png" width="700">

**📝 Pembahasan:**
Setelah seluruh pengujian selesai, layanan Apache Ignite dihentikan menggunakan perintah Docker Compose. Langkah ini mengakhiri proses praktikum dan menghentikan container yang menjalankan ketiga node. Penghentian layanan dilakukan setelah pemeriksaan data dan query selesai.

## ✅ KESIMPULAN
Praktikum ini menunjukkan penerapan replikasi data pada dua teknologi yang berbeda. PostgreSQL menggunakan pola primary dan replica untuk menyinkronkan perubahan data serta mendukung pemulihan layanan melalui promosi replica menjadi primary. Apache Ignite menggunakan cluster tiga node untuk mengelola data dan memungkinkan pemeriksaan hasil perubahan melalui beberapa endpoint. Docker dan Docker Compose membantu menjalankan serta mengelola layanan database dalam container. Pengujian melalui pembuatan tabel, manipulasi data, pemeriksaan status replikasi, dan eksekusi query memberikan pemahaman mengenai proses sinkronisasi data pada sistem terdistribusi. Praktikum ini juga memperlihatkan pentingnya pemeriksaan status layanan dan hasil query untuk memastikan konfigurasi berjalan sesuai tujuan.
