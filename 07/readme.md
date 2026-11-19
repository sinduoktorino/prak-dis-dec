**NIM  : 255410033**
**Nama : Mohamad Sindu Oktorino**


## Tujuan Praktikum

Praktikum ini bertujuan untuk memahami konsep Cloud Computing dan pembagian layanan XaaS, yaitu SaaS, PaaS, dan IaaS. Praktikum juga bertujuan untuk mempraktikkan proses pembuatan Containerized App dari aplikasi Flask, membangun serta menjalankannya menggunakan Docker dan Podman, serta mempelajari pemetaan port agar aplikasi di dalam container dapat diakses melalui browser.

## Dasar Teori

Cloud Computing merupakan model penyediaan sumber daya komputasi yang dapat digunakan melalui layanan. Layanan ini umumnya dikelompokkan menjadi SaaS untuk penggunaan aplikasi melalui layanan, PaaS untuk pengembangan dan pengelolaan aplikasi, serta IaaS untuk penyediaan sumber daya infrastruktur seperti server, penyimpanan, dan jaringan.

Containerized App atau aplikasi berbasis container adalah aplikasi yang dikemas beserta dependensinya sehingga dapat dijalankan secara konsisten pada berbagai lingkungan. Docker dan Podman merupakan mesin container yang dapat membangun image dari Dockerfile, menjalankan aplikasi di dalam container, serta mengatur akses jaringan dengan pemetaan port. Dockerfile berisi petunjuk pembentukan image, sedangkan port mapping digunakan untuk menghubungkan port aplikasi pada container dengan port pada sistem host.

## Praktik

- Membuat folder home `src`

<img src="images/pengantar.png" width="700">

Pembahasan:

Aplikasi Flask tutorial disiapkan pada direktori kerja di bawah folder src. Direktori tutorial kemudian disalin ke folder flask-app agar menjadi proyek mandiri yang dapat dimodifikasi dan dikemas sebagai container.

### 1. Membuat Env Python 3.14.4

<img src="images/python.png" width="700">

Pembahasan:

Lingkungan virtual Python dibuat untuk proyek flask-app agar dependensi aplikasi terisolasi. Penggunaan Python 3.14.4 memastikan aplikasi dan paket yang dibangun menggunakan versi interpreter sesuai kebutuhan praktikum.

### 2. Install Paket yang Diperlukan

<img src="images/installpip.png" width="700">

Pembahasan:

Perintah uv pip install -e . digunakan untuk memasang proyek Flask beserta seluruh dependensi yang tercantum pada konfigurasi proyek secara editable. Setelah proses instalasi selesai, database lokal perlu diinisialisasi agar fitur penyimpanan aplikasi tersedia.

Jalankan aplikasi tersebut setelah inisialisasi database.

<img src="images/tespip.png" width="700">

Pembahasan:

Perintah flask --app flaskr init-db membuat struktur database yang dibutuhkan aplikasi, sedangkan flask --app flaskr run menjalankan server pengembangan Flask pada port 5000. Aplikasi kemudian dapat diuji secara lokal dan ditandai berhasil jika halaman Flask dapat dibuka pada browser.

Lihat hasilnya pada browser.

<img src="images/tes.png" width="700">

Pembahasan:

Halaman aplikasi menampilkan daftar posting tanpa data awal dan menyediakan menu Register serta Log In. Menu tersebut digunakan untuk menguji proses pembuatan akun dan autentikasi pengguna pada aplikasi Flask.

### 3. Membuat Aplikasi Menjadi CA dengan Docker

<img src="images/dockerfile.png" width="700">

Pembahasan:

Dockerfile digunakan untuk membentuk image aplikasi. Docker base image dimulai dari Python 3.14, kemudian direktori kerja ditetapkan pada /app, seluruh kode proyek disalin ke image, dependensi dipasang, database diinisialisasi, port 5000 dibuka, dan Flask dijalankan sehingga dapat menerima koneksi dari luar container.

- Bangun image Docker.

<img src="images/docker.png" width="700">
<img src="images/docker1.png" width="700">

Pembahasan:

Docker daemon harus aktif sebelum proses build dimulai. Perintah docker build membaca Dockerfile dan menghasilkan image bernama flaskr dengan tag 1.0.0 berdasarkan kondisi proyek pada direktori saat ini.

- Image yang telah dibuat.

<img src="images/docker2.png" width="700">

Pembahasan:

Image yang berhasil dibentuk dapat diperiksa dengan perintah docker image ls. Image yang tidak lagi digunakan sebaiknya dihapus berdasarkan ID-nya agar penyimpanan pada host tidak terisi oleh image yang tidak diperlukan.

### 4. Menjalankan Image

<img src="images/docker3.png" width="700">
<img src="images/tes.png" width="700">

Pembahasan:

Container dijalankan dengan memetakan port 5000 pada container ke port 5001 pada host. Dengan pemetaan tersebut, aplikasi dapat diakses melalui http://localhost:5001 dan terbukti berhasil dijalankan sebagai Containerized App menggunakan Docker.

### 5. Membuat Aplikasi Menjadi CA dengan Podman

<img src="images/podman.png" width="700">
<img src="images/podman1.png" width="700">
<img src="images/podman3.png" width="700">

Pembahasan:

Podman dapat membangun aplikasi dari Dockerfile yang sama dan tidak memerlukan Docker daemon. Jika Docker aktif, Docker service perlu dihentikan terlebih dahulu pada distribusi yang menggunakan systemd atau dinit agar tidak terjadi konflik penggunaan runtime container.

- Image yang telah dibuat.

<img src="images/podmanimage.png" width="700">

Pembahasan:

Perintah podman build membangun image flaskr:1.0.0 melalui delapan tahapan Dockerfile. Setiap tahapan menghasilkan lapisan image dan hasil akhir ditandai sebagai image dengan ID serta nama localhost/flaskr:1.0.0.

- Jalankan image menggunakan Podman.

<img src="images/podmanrun.png" width="700">
<img src="images/tes.png" width="700">

Pembahasan:

Container Podman dijalankan dengan pemetaan port yang sama, yaitu port 5001 pada host menuju port 5000 pada container. Browser yang mengakses localhost:5001 dapat menampilkan aplikasi Flask, sehingga proses build dan menjalankan image menggunakan Podman dinyatakan berhasil.

## Tugas

1.  Contoh Vendor SaaS, PaaS, dan IaaS

    SaaS (Software as a Service): Google Workspace (sebelumnya G Suite)

    PaaS (Platform as a Service): Heroku (anak perusahaan Salesforce)

    IaaS (Infrastructure as a Service): Amazon Web Services (AWS) — khususnya layanan Amazon EC2

2. Uraian Layanan (Service) dari Masing-Masing Vendor

| Kategori XaaS | Contoh Vendor | Uraian Layanan (*Service*) yang Disediakan |
| :--- | :--- | :--- |
| **SaaS** (*Software as a Service*) | **Google Workspace** | Menyediakan perangkat lunak produktivitas dan kolaborasi berbasis cloud yang siap pakai langsung melalui peramban web atau aplikasi seluler. Layanannya mencakup surel bisnis (**Gmail**), penyimpanan awan (**Google Drive**), pengolah dokumen (**Docs, Sheets, Slides**), serta konferensi video (**Google Meet**). Pengguna tidak perlu mengurus instalasi, pemeliharaan server, maupun pembaruan perangkat lunak. |
| **PaaS** (*Platform as a Service*) | **Heroku** | Menyediakan lingkungan platform lengkap bagi pengembang (*developer*) untuk membangun, menjalankan, dan mengelola aplikasi tanpa harus memusingkan infrastruktur server di baliknya. Layanannya meliputi dukungan berbagai bahasa pemrograman (Node.js, Python, Ruby, Java), manajemen basis data terkelola (*Heroku Postgres*), integrasi CI/CD otomatis dari Git, serta penskalaan sumber daya aplikasi secara instan. |
| **IaaS** (*Infrastructure as a Service*) | **Amazon Web Services (AWS EC2)** | Menyediakan infrastruktur komputasi virtual dasar melalui internet dengan sistem bayar sesuai pemakaian (*pay-as-you-go*). Layanannya mencakup penyewaan mesin virtual (*Virtual Machines/Instances*), kapasitas penyimpanan blok dan objek (**EBS & S3**), konfigurasi jaringan virtual (**VPC**), penyeimbang beban (*Load Balancer*), serta firewall keamanan. Pengguna memiliki kendali penuh atas sistem operasi dan aplikasi yang diinstal di dalamnya. |

3. Visualisasi dan Penjelasan Arsitektur XaaS

    <img src="images/diagram.jpeg" width="700">

    1. On-Premises (Sebagai Pembanding): Seluruh 9 lapisan arsitektur—dari jaringan fisik hingga aplikasi—dikelola dan dibiayai sepenuhnya secara mandiri oleh pengguna di pusat data lokal.

    2. Arsitektur IaaS: Vendor mengambil alih pengelolaan infrastruktur fisik dan virtualisasi (Networking, Storage, Servers, Virtualization). Pengguna tetap mengelola lapisan sistem operasi (OS), middleware, runtime, data, hingga aplikasi di atasnya.

    3. Arsitektur PaaS: Vendor memperluas pengelolaannya hingga ke tingkat sistem operasi,      middleware, dan runtime. Arsitektur ini memungkinkan pengembang fokus hanya pada lapisan teratas, yaitu Data dan Applications yang mereka bangun.

    4. Arsitektur SaaS: Vendor mengelola seluruh tumpukan (full-stack) dari lapisan jaringan paling bawah hingga Applications dan Data di paling atas. Pengguna akhir cukup mengakses layanan melalui antarmuka klien (browser/aplikasi) dan menggunakan fiturnya secara langsung.

## Kesimpulan

Praktikum Modul 7 memberikan pemahaman bahwa Cloud Computing menyediakan layanan komputasi melalui model SaaS, PaaS, dan IaaS sesuai kebutuhan pengguna. Praktikum ini juga membuktikan bahwa aplikasi Flask dapat dikemas sebagai Containerized App menggunakan Dockerfile, dibangun menjadi image, dan dijalankan pada Docker maupun Podman. Pemetaan port memungkinkan aplikasi yang berjalan di dalam container tetap dapat diakses melalui browser pada mesin host. Docker dan Podman memberikan cara yang konsisten untuk membangun dan menjalankan aplikasi secara terisolasi, portabel, serta mudah dipindahkan antarlingkungan.