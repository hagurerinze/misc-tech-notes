# Perintah Internal dan Eksternal DOS

> Acuan: MS-DOS (versi 5.0 - 6.22). Beberapa perintah bisa berbeda di versi lain.

## Beda Singkat

| Jenis | Lokasi perintah | Perlu file terpisah? |
|-------|-----------------|----------------------|
| **Internal** | Sudah ada di dalam `COMMAND.COM`, otomatis dimuat ke memori saat DOS menyala | Tidak |
| **Eksternal** | Berupa file program sendiri (`.EXE`, `.COM`, `.BAT`) di disk | Ya, file harus ada di disk/folder yang bisa dijangkau (misal lewat `PATH`) |

---

## 10 Perintah Internal

| No | Perintah | Fungsi | Contoh |
|----|----------|--------|--------|
| 1 | `DIR` | Menampilkan isi direktori | `DIR C:\GAMES` |
| 2 | `CD` | Pindah direktori | `CD \DOS` |
| 3 | `MD` | Membuat direktori baru | `MD TUGAS` |
| 4 | `RD` | Menghapus direktori kosong | `RD TUGAS` |
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
- Perintah eksternal tidak akan jalan kalau file programnya tidak ditemukan. Biasanya muncul pesan `Bad command or file name`.
