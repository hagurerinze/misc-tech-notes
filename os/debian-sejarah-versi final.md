# Debian: Sejarah, Versi, dan Codename

## Apa itu Debian?

> Debian adalah salah satu distro Linux tertua yang masih hidup sampai sekarang dan jadi "induk" dari ratusan distro lain, termasuk Ubuntu (dan lewat Ubuntu, Linux Mint), Kali, dan Proxmox. Filosofinya beda sama distro lain: Debian gak ngejar fitur terbaru, tapi ngejar stabil dan bebas. Paket di repo utama Debian Stable harus lewat proses testing berbulan-bulan dan sesuai Debian Free Software Guidelines (DFSG). Karena itu Debian sering dipakai buat server, laptop kentang, dan basis belajar sysadmin. Slogannya: "The Universal Operating System".

Debian sering muncul di top search, tapi bukan yang paling hype. Bahkan beberapa live mode kayak GParted Live (buat partisi) juga berbasis Debian.

Debian pakai APT sebagai package manager dan filosofinya stabil + minimal. Untuk urusan minimal, dia agak mirip Arch. Bedanya, Arch pakai pacman (`pacman -Syu`) dan konsepnya rolling release, sedangkan Debian rilisnya per versi (sekitar 2 tahun sekali) dan stabil.

Debian juga dikenal punya fokus kuat di keamanan lewat Debian Security Team dan update patch yang rutin di rilis stable. Untuk keamanan berbasis isolasi ada Qubes OS (yang sendiri sering memakai Debian sebagai template), dan untuk rollback/reproducibility ada NixOS. Tapi Debian sudah cukup aman untuk pemakaian harian dan sering jadi basis distro yang fokus ke keamanan dan privasi, seperti **Tails** dan **Whonix**.

- **Tails** adalah OS live yang dijalankan dari flashdisk dan mengarahkan semua koneksi lewat jaringan Tor. Tails bersifat **amnesic**: setelah dimatikan, datanya hilang dan tidak meninggalkan jejak, kecuali kita mengaktifkan fitur Persistent Storage.
- **Whonix** bekerja lewat dua VM, satu sebagai gateway Tor dan satu sebagai workstation, dan sering dipakai di dalam Qubes.

Fun fact: Kali Linux juga berbasis Debian.

Jadi Debian itu OS yang "underrated", ketutup sama populernya distro yang udah dipoles cantik kayak CachyOS, Bazzite, Zorin, dan lainnya. Ada yang nanya, "Debian bisa nggak jadi secantik itu?" Jawaban simpelnya: bisa, tinggal "colong-colong" konsep tema dan tampilan mereka aja.

---

## Sejarah Singkat

- **16 Agustus 1993**: Ian Murdock mengumumkan proyek Debian. Namanya gabungan dari nama pacarnya saat itu, **Deb**ra, dan namanya sendiri, **Ian**.
- **1993-1995**: Debian sempat disponsori Free Software Foundation (FSF), lalu berhenti karena perbedaan pandangan.
- **1996**: Rilis stabil pertama dengan nomor versi 1.x (Buzz). Versi 1.0 sendiri tidak pernah dirilis resmi karena ada vendor CD yang keliru menjual build yang belum jadi, jadi nomornya dilewati.
- **1997**: Proyek berjalan mandiri di bawah **Software in the Public Interest (SPI)**, organisasi nirlaba untuk menaungi aset dan merek Debian.
- **2004**: Ubuntu, turunan Debian yang paling populer, rilis pertama kali. Linux Mint dan banyak distro lain menyusul.

## Asal Nama Codename

Codename rilis Debian diambil dari nama karakter film **Toy Story**. Ini dimulai sejak Debian 1.1 karena Bruce Perens (Project Leader saat itu) bekerja di Pixar.

- **Sid** (unstable) = anak tetangga yang suka merusak mainan. Kebetulan juga bisa dibaca "Still In Development".
- **Testing** = calon stable berikutnya.
- **Experimental** = rc-buggy (mobil mainan Andy).

## Tabel Rilis

| Versi | Codename | Karakter Toy Story | Tanggal rilis |
|---|---|---|---|
| 1.1 | Buzz | Buzz Lightyear | 17 Jun 1996 |
| 1.2 | Rex | Rex (dinosaurus) | 12 Des 1996 |
| 1.3 | Bo | Bo Peep | 5 Jun 1997 |
| 2.0 | Hamm | Hamm (celengan babi) | 24 Jul 1998 |
| 2.1 | Slink | Slinky Dog | 9 Mar 1999 |
| 2.2 | Potato | Mr. Potato Head | 15 Agu 2000 |
| 3.0 | Woody | Woody | 19 Jul 2002 |
| 3.1 | Sarge | Sarge (tentara mainan) | 6 Jun 2005 |
| 4.0 | Etch | Etch A Sketch | 8 Apr 2007 |
| 5.0 | Lenny | Lenny (teropong mainan) | 14 Feb 2009 |
| 6.0 | Squeeze | Squeeze Toy Aliens | 6 Feb 2011 |
| 7 | Wheezy | Wheezy (penguin) | 4 Mei 2013 |
| 8 | Jessie | Jessie | 25 Apr 2015 |
| 9 | Stretch | Stretch (gurita) | 17 Jun 2017 |
| 10 | Buster | Buster (anjing Andy) | 6 Jul 2019 |
| 11 | Bullseye | Bullseye (kuda Woody) | 14 Agu 2021 |
| 12 | Bookworm | Bookworm (cacing buku) | 10 Jun 2023 |
| 13 | Trixie | Trixie (triceratops) | 9 Agu 2025 |
| 14 | Forky | Forky | Belum rilis (masih testing) |

## Kondisi Sekarang (per 29 September 2026)

- **Stable**: Debian 13 "Trixie", rilis awal 9 Agustus 2025. Update terbaru saat ini **13.7** (12 September 2026).
- **Testing**: "Forky" (calon Debian 14).
- **Unstable**: "Sid", selalu bernama Sid dan tidak pernah punya nomor versi.
- Siklus dukungan: 3 tahun dukungan penuh + 2 tahun Long Term Support (LTS), total sekitar 5 tahun per rilis.

## Tiga Cabang Debian

| Cabang | Fungsi |
|---|---|
| Stable | Rilis resmi, dipakai untuk produksi/harian |
| Testing | Paket yang sedang "antri" jadi stable berikutnya |
| Unstable (Sid) | Tempat pengembangan aktif, paling baru tapi paling rawan rusak |

## Sumber

- debian.org/releases
- debian.org/News (pengumuman point release)
- Wikipedia: Debian release version history

---

Bagi yang tertarik soal OS atau lagi exploring, boleh keliling ke GitHub gw: [github.com/hagurerinze](https://github.com/hagurerinze)
