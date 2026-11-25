# Perintah Internal dan Eksternal DOS

> Acuan perintah: MS-DOS (versi 5.0 - 6.22). Beberapa perintah bisa berbeda di versi lain, apalagi ada perbedaan antara MS-DOS, IBM PC DOS, dan DOS versi lainnya.

---

## 1. Apa itu DOS?

**DOS** (*Disk Operating System*) adalah sistem operasi lama yang dipakai di PC sebelum tampilan grafis (GUI) jadi standar. Kalau digampangin: ini "nenek moyang" layar hitam penuh ketikan yang sekarang masih bisa lu lihat di `cmd`.

- **MS-DOS** buatan Microsoft. Versi yang dijual IBM untuk komputer mereka namanya **IBM PC DOS** (IBM melisensi MS-DOS dan merilisnya sebagai PC DOS 1.0 pada 1981). Keduanya mirip, tapi lama-lama berkembang sendiri-sendiri.
- DOS dipakai luas di era 1980-an sampai 1990-an dan terkenal **ringan**, jadi cocok untuk komputer yang spesifikasinya sangat terbatas.
- Windows lama (95, 98, ME) masih berdiri di atas DOS. Sejak Windows berbasis NT (2000, XP, dan seterusnya), Windows **tidak lagi** memakai DOS sebagai inti sistem.
- Kalau lu pernah buka **Command Prompt (cmd)** atau **Windows PowerShell** (muncul label x64 / x86 sesuai arsitektur yang dipakai), itu **bukan DOS asli**. Itu program shell di Windows modern, yang gaya perintahnya mirip DOS.

---

## 2. Perbandingan Singkat

Perbedaannya lumayan jauh kalau dibahas semua, jadi simpel aja:

| Nama | Apa itu | Catatan |
|------|---------|---------|
| **DOS** (MS-DOS, PC DOS, FreeDOS) | Sistem operasi lengkap berbasis teks | Tidak ada GUI bawaan |
| **Command Prompt (cmd)** | Shell di Windows modern | Gaya perintahnya mirip DOS, tapi bukan DOS |
| **PowerShell** | Shell Windows yang lebih modern dan kuat | Banyak perintah lama (dan perintah ala Unix) tersedia sebagai alias |
| **Terminal** (Linux, dll) | Jendela untuk menjalankan shell (bash, dll) | Terminal bukan OS |
| **BSD** (FreeBSD, OpenBSD) | Sistem operasi Unix-like | Perintahnya ala Unix, mirip Linux |

Contoh paling gampang buat ngebedain DOS dan Linux/BSD:

| Fungsi | DOS | Linux / BSD |
|--------|-----|-------------|
| Lihat isi folder | `dir` | `ls` |
| Pindah folder | `cd` | `cd` |
| Buat folder | `md` atau `mkdir` | `mkdir` |
| Hapus folder kosong | `rd` atau `rmdir` | `rmdir` |

Simpel kan? Cara ngenalinnya: baca singkatannya.

- `dir` = *directory*
- `ls` = *list*
- `cd` = *change directory*
- `md` = *make directory*, `mkdir` = *make directory* juga tapi lebih mudah dikenali karena lebih panjang dikit
- `rd` = *remove directory*, `rmdir` = *remove directory* juga, sama polanya

Catatan: DOS menerima versi pendek **dan** panjangnya (`MD` = `MKDIR`, `RD` = `RMDIR`, `CD` = `CHDIR`). Linux/BSD hanya pakai versi panjang untuk buat dan hapus folder.

---

## 3. Beda Internal dan Eksternal

| Jenis | Lokasi perintah | Perlu file terpisah? |
|-------|-----------------|----------------------|
| **Internal** | Sudah ada di dalam `COMMAND.COM`, otomatis dimuat ke memori saat DOS menyala. Dengan kata lain yang simpel: dia udah ada tanpa lu bawa dari luar, sesuai namanya | Tidak |
| **Eksternal** | Berupa file program sendiri (`.EXE`, `.COM`, `.BAT`) di disk. Mau contoh gampang? Lu manggil game lu kayak `valorant.exe` lewat path | Ya, file harus ada di disk/folder yang bisa dijangkau (misal lewat `PATH`) |

---

## 10 Perintah Internal

| No | Perintah | Fungsi | Contoh |
|----|----------|--------|--------|
| 1 | `DIR` | Menampilkan isi direktori | `DIR C:\GAMES` |
| 2 | `CD` | Pindah direktori | `CD \DOS` |
| 3 | `MD` (`MKDIR`) | Membuat direktori baru | `MD TUGAS` |
| 4 | `RD` (`RMDIR`) | Menghapus direktori kosong | `RD TUGAS` |
| 5 | `COPY` | Menyalin file | `COPY A.TXT B.TXT` |
| 6 | `DEL` | Menghapus file | `DEL A.TXT` |
| 7 | `REN` | Mengganti nama file | `REN A.TXT BARU.TXT` |
| 8 | `TYPE` | Menampilkan isi file teks | `TYPE A.TXT` |
| 9 | `CLS` | Membersihkan layar | `CLS` |
| 10 | `VER` | Menampilkan versi DOS | `VER` |

---

## 10 Perintah Eksternal

| No | Perintah | Fungsi | Contoh |
|----|----------|--------|--------|
| 1 | `FORMAT` | Memformat disk | `FORMAT A:` |
| 2 | `FDISK` | Mengatur partisi hard disk | `FDISK` |
| 3 | `CHKDSK` | Memeriksa kondisi disk dan memori | `CHKDSK C:` |
| 4 | `XCOPY` | Menyalin file beserta subdirektori | `XCOPY C:\DATA D:\ /S` |
| 5 | `DELTREE` | Menghapus direktori beserta isinya | `DELTREE C:\TEMP` |
| 6 | `ATTRIB` | Melihat/mengubah atribut file (read-only, hidden, dll) | `ATTRIB +R A.TXT` |
| 7 | `EDIT` | Editor teks bawaan DOS | `EDIT CATATAN.TXT` |
| 8 | `MEM` | Menampilkan penggunaan memori | `MEM` |
| 9 | `TREE` | Menampilkan struktur folder berbentuk pohon | `TREE C:\` |
| 10 | `FIND` | Mencari teks di dalam file | `FIND "halo" A.TXT` |

---

## Catatan

- `DELTREE` hanya ada di MS-DOS 6.x, tidak ada di semua versi.
- Perintah eksternal tidak akan jalan kalau file programnya tidak ditemukan. Biasanya muncul pesan `Bad command or file name`. Penyebab utamanya: beda path dan nama yang typo.

---

## Fun Fact

- Kelen ngerasa ga memakainya kan? Padahal laptop, HP, dan PC yang kalian pakai masih memakai **konsep** yang mirip: perintah teks (CLI). Windows modern memang bukan berbasis DOS lagi, tapi `cmd` dan PowerShell masih ada. Yang membedakan di masa modern ini adalah **GUI** yang bikin kita gak perlu ketik-ketik lagi. Tapi bukan berarti CLI hilang. Bagi developer, GUI dan CLI dikombinasikan, terutama di Windows dan Mac yang dikira full GUI padahal engga. Jadi ada UI bukan berarti full GUI.
- Fakta kedua: Linux yang dikira CLI only oleh banyak orang justru terkenal sangat fleksibel untuk dikustom tampilannya. Banyak pilihan DE dan WM, dan yang cantik-cantik sering muncul di rilis distro populer. GUI + CLI dua-duanya dominan.
- Yang masih hidup dan **paling dekat dengan DOS** saat ini adalah **FreeDOS**: sistem operasi gratis (GPL) yang dibuat kompatibel dengan MS-DOS. Proyeknya mulai 29 Juni 1994, setelah Microsoft mengumumkan tidak akan menjual/mendukung MS-DOS lagi.
- **OpenBSD** juga jadi salah satu alternatif yang terasa dekat dari sisi pengalaman CLI yang minimalis, walau dia Unix-like (bukan keluarga DOS). OpenBSD bisa dipakai tanpa GUI (teks saja) atau dengan GUI (X11), tergantung dipasang atau tidak. Ada candaan di Reddit bahwa pengguna OpenBSD tidak mau pakai desktop, dan kalau OpenBSD tampil GUI mereka mau lempar device sendiri. Itu candaan komunitas, bukan fakta resmi.

---

## Sumber

1. MS-DOS dan IBM PC DOS (sejarah, lisensi ke IBM): https://en.wikipedia.org/wiki/MS-DOS
2. FreeDOS (kompatibel MS-DOS, lisensi GPL, mulai 1994, Windows NT tidak memakai DOS): https://en.wikipedia.org/wiki/FreeDOS
3. OpenBSD (Unix-like, berbasis BSD, X11): https://en.wikipedia.org/wiki/OpenBSD
4. OpenBSD Handbook, X Window System (GUI di OpenBSD): https://www.openbsdhandbook.com/x11/
5. Internal vs eksternal di MS-DOS 6.22 (COMMAND.COM, contoh COPY dan FORMAT): https://informit.com/articles/article.aspx?p=131120
6. Daftar perintah internal (CD, DIR, MD/MKDIR, RD/RMDIR, dll): https://www.computerhope.com/jargon/i/intecomm.htm
