# PDNS 2, Keamanan Data, dan Tanggung Jawab Profesional

> Catatan analisis pribadi. Dokumen ini memisahkan data, fakta yang
> dilaporkan, bukti yang tersedia, dan asumsi. Isinya dapat berubah
> ketika sumber baru ditemukan atau informasi berhasil diverifikasi.

## Fokus

Tiga jalur dibahas dalam catatan ini:

-   **Ransomware PDNS 2 (2024):** kronologi yang dilaporkan, gangguan
    layanan, keamanan sistem, dan tanggung jawab profesional.
-   **Kredensial `Admin#1234`:** persoalan pengelolaan akses dan
    keamanan kata sandi yang diberitakan dalam konteks PDNS.
-   **Dugaan penawaran dump database sekolah:** dokumentasi promosi dan
    percakapan yang memunculkan pertanyaan tentang akses serta
    perdagangan data pribadi.

Ketiganya relevan pada tingkat tema keamanan dan tata kelola data.
Namun, relevansi tema tidak membuktikan bahwa ketiganya merupakan satu
rangkaian kejadian atau memiliki hubungan teknis langsung.

## 1. PDNS 2

Pada Juni 2024, serangan ransomware terhadap PDNS 2 mengganggu layanan
sejumlah instansi pemerintah.

Dalam keterangan yang dikutip media pada akhir Juni 2024, BSSN
melaporkan adanya upaya menonaktifkan Windows Defender mulai 17 Juni
2024 sekitar pukul 23.15 WIB. Aktivitas berbahaya kemudian dilaporkan
terdeteksi pada 20 Juni 2024 sekitar pukul 00.54 WIB.

Kronologi ini menjadi dasar untuk membahas pemantauan keamanan, respons
terhadap perubahan kontrol keamanan, pembatasan akses, kesiapan backup,
dan pemulihan layanan.

**Batas kesimpulan:** kronologi tersebut tidak dengan sendirinya
menjelaskan bagaimana penyerang memperoleh akses awal. Metode akses,
pelaku setiap tindakan, dan kemungkinan hubungan dengan kelemahan
tertentu harus mengikuti bukti yang tersedia, bukan dugaan.

### Hal yang perlu dibedakan

-   Backup tidak tersedia.
-   Backup tersedia tetapi tidak lengkap atau sudah usang.
-   Backup ikut terdampak.
-   Backup tersedia tetapi belum dapat dipulihkan.
-   Backup berhasil dipulihkan dalam waktu yang dapat diterima.

Kondisi-kondisi tersebut berbeda. Jangan menyatakan salah satunya
terjadi tanpa sumber yang mendukung.

## 2. Isu kredensial `Admin#1234`

Pada Juli 2024, media memberitakan dokumen yang memuat informasi akses
pusat data dan kata sandi `Admin#1234` yang dikaitkan dengan salah satu
pengguna layanan. Isu ini penting untuk membahas keamanan kredensial,
pengawasan akses, dan tanggung jawab dalam menjaga informasi
autentikasi.

Kredensial yang mudah ditebak atau terekspos dapat meningkatkan risiko
akses tidak sah. Risikonya bergantung antara lain pada hak akses akun,
penggunaan ulang kata sandi, siapa yang dapat mengakses kredensial,
pemantauan log, dan seberapa cepat kredensial yang terpapar ditangani.

Pemberitaan mengenai isu ini perlu dibaca dengan cermat, termasuk
pernyataan pejabat yang dikutip media. Jangan mengecilkan arti persoalan
kredensial; tetapi jangan pula menyatakan bahwa kata sandi tersebut
merupakan jalur masuk ransomware tanpa bukti yang secara jelas mendukung
hubungan itu.

### Pertanyaan analisis

-   Siapa yang berwenang membuat, menyimpan, menggunakan, dan mengawasi
    kredensial?
-   Apakah akses istimewa dibatasi dan dapat diaudit?
-   Apa yang semestinya dilakukan jika kredensial diketahui telah
    terekspos?
-   Mana yang merupakan pernyataan resmi, laporan media, dan kesimpulan
    analisis?

## 3. Dugaan penawaran dump database sekolah

Dokumentasi yang tersedia memperlihatkan materi promosi yang mengklaim
menawarkan layanan *dump database sekolah*, klaim mengenai jenis data
yang dapat diperoleh, serta percakapan yang tampak membahas transaksi
dan contoh keluaran data.

Informasi yang disebut dalam materi promosi mencakup data pribadi siswa
dan keluarga. Jika data seperti itu diperoleh atau diperdagangkan tanpa
dasar yang sah, persoalannya menyangkut privasi, potensi penyalahgunaan
identitas, keamanan anak, dan tanggung jawab pihak yang mengakses atau
menyebarkan data.

Namun, screenshot hanya menunjukkan materi dan klaim yang tampak di
dalamnya. Screenshot tersebut tidak secara mandiri membuktikan keaslian
data, asal-usul data, cakupan akses, apakah layanan benar-benar
berfungsi, atau apakah data berasal dari sistem tertentu.

### Status dokumentasi dan analisis

Terdapat beberapa screenshot yang mendokumentasikan materi promosi dan
percakapan terkait dugaan transaksi dump database sekolah. Screenshot
tersebut **tidak ditautkan satu per satu dalam dokumen ini**.
Dokumentasinya masih dianalisis untuk memisahkan informasi yang dapat
diverifikasi dari klaim yang belum teruji. Tujuannya adalah mengumpulkan
fakta sebelum mengambil kesimpulan atau bertindak gegabah.

Pembaca dapat membentuk asumsi sendiri, tetapi asumsi bukan bukti.
**Sebelum membuat atau menyebarkan klaim tentang pelaku, sumber data,
korban, maupun hubungan dengan insiden lain, pikirkan kembali apakah
bukti yang tersedia benar-benar mendukung klaim tersebut.** Kesimpulan
terlalu cepat dapat menyesatkan, merugikan pihak yang tidak terkait, dan
mengaburkan fakta yang sebenarnya perlu dicari.

Dokumentasi ini tidak cukup untuk menyatakan bahwa data tersebut berasal
dari PDNS 2 atau bahwa penawaran itu memiliki hubungan teknis langsung
dengan ransomware tahun 2024. Kedua topik dapat dibahas bersama sebagai
persoalan keamanan dan tata kelola data, tetapi hubungan langsungnya
belum terbukti dalam catatan ini.

## 4. Tanggung jawab dan etika

Tanggung jawab tidak perlu dipaksa menjadi peringkat kesalahan mutlak.
Penilaian perlu mempertimbangkan kewenangan, kewajiban, tindakan, sumber
daya, dan bukti.

-   **Pemerintah dan pimpinan institusi:** tata kelola risiko,
    pengawasan, standar keamanan, sumber daya, kesinambungan layanan,
    dan akuntabilitas kepada publik.
-   **Operator dan pengelola teknis:** konfigurasi, pengelolaan
    kredensial, pemantauan, eskalasi aktivitas mencurigakan, dokumentasi
    insiden, dan pengujian pemulihan sesuai kewenangannya.
-   **Pelaku serangan:** tanggung jawab langsung atas tindakan
    ransomware yang disengaja.
-   **Pihak yang memperoleh atau memperdagangkan data tanpa hak:**
    persoalan etika dan hukum terkait privasi serta penyalahgunaan data,
    apabila tindakan dan keterlibatannya dapat dibuktikan.

Kelemahan sistem, bila terbukti, dapat membantu menjelaskan bagaimana
serangan mungkin terjadi. Kelemahan itu tidak membenarkan tindakan
penyerang. Pada saat yang sama, tanggung jawab organisasi tidak
seharusnya otomatis dibebankan seluruhnya kepada satu operator tanpa
memeriksa kewenangan dan kondisi kerjanya.

## 5. Prinsip yang digunakan

-   **Data tetap data:** tuliskan apa yang benar-benar tercatat atau
    ditunjukkan sumber.
-   **Fakta lapangan tetap fakta lapangan:** jelaskan siapa yang
    mengamati atau melaporkannya dan dalam konteks apa.
-   **Bukti tetap bukti:** jelaskan apa yang dapat dan tidak dapat
    dibuktikan olehnya.
-   **Asumsi tetap asumsi:** beri label dan jangan menaikkannya menjadi
    fakta hanya karena terlihat masuk akal.
-   **Korelasi bukan sebab-akibat:** dua hal yang muncul dalam konteks
    serupa belum tentu memiliki hubungan teknis.
-   **Kritik harus proporsional:** kritik kebijakan, tindakan, atau tata
    kelola berdasarkan bukti; hindari tuduhan terhadap individu tanpa
    dasar cukup.
-   **Lindungi data pribadi:** jangan memublikasikan ulang nama siswa,
    NIK, NISN, alamat, nomor telepon, data keluarga, atau identitas akun
    yang tidak perlu.

## 6. Kesimpulan sementara

Insiden PDNS 2 menunjukkan pentingnya keamanan berlapis, pemantauan,
pengelolaan akses, kesiapan pemulihan, dan akuntabilitas. Isu
`Admin#1234` merupakan bahan penting untuk menilai tata kelola
kredensial, tetapi klaim mengenai perannya dalam jalur masuk ransomware
harus mengikuti bukti yang benar-benar tersedia.

Dokumentasi dugaan penawaran dump database sekolah menimbulkan
pertanyaan serius mengenai perlindungan data pribadi. Namun, sumber,
keaslian, dan cakupan data belum diverifikasi secara independen. Tidak
ada dasar yang cukup dalam catatan ini untuk menghubungkannya secara
teknis dengan serangan PDNS 2.

Analisis ini terbuka untuk koreksi. Jika bukti baru ditemukan,
kesimpulan perlu diperbarui; jika bukti tidak mendukung suatu klaim,
klaim tersebut harus dibatasi atau ditarik.

## Sumber

1.  ANTARA News. (27 Juni 2024). "Menkominfo jelaskan kronologi serangan
    siber PDNS 2."\
    https://www.antaranews.com/berita/4171167/menkominfo-jelaskan-kronologi-serangan-siber-pdns-2.html
2.  Komdigi. (27 Juni 2024). Siaran pers terkait percepatan pemulihan
    PDNS 2.\
    https://www.komdigi.go.id/berita/siaran-pers/detail/siaran-pers-np-tentang-percepat-pemulihan-kominfo-bssn-dan-telkom-operasikan-server-baru-pengganti
3.  Katadata. (6 Juli 2024). Pemberitaan mengenai kata sandi
    `Admin#1234`.\
    https://katadata.co.id/digital/teknologi/6688d1d936c50/viral-pusat-data-dibobol-karena-password-admin1234-ini-kata-kominfo
4.  Katadata. (9 Juli 2024). Pemberitaan mengenai pengaturan ulang kata
    sandi pusat data.\
    https://katadata.co.id/digital/teknologi/668d0061a0c7c/kominfo-atur-ulang-password-pusat-data-nasional-di-setiap-kementerian
5.  Katadata. (9 Juli 2024). "Belajar dari Pusat Data, Ini Daftar
    Password Gampang Ditebak Hacker."\
    https://katadata.co.id/digital/teknologi/668cc247182ab/belajar-dari-pusat-data-ini-daftar-password-gampang-ditebak-hacker
6.  Komdigi. (2 Oktober 2026). Informasi mengenai investigasi penjualan
    data pribadi ilegal.\
    https://portal.komdigi.go.id/kanal-publik/berita-kini/10576
7.  Kemendikdasmen. (5 Agustus 2026). "Kemendikdasmen Telusuri Dugaan
    Penyalahgunaan Dapodik, Tegaskan Komitmen Lindungi Data Peserta
    Didik."\
    https://www.kemendikdasmen.go.id/siaran-pers/15940-kemendikdasmen-telusuri-dugaan-penyalahgunaan-dapodik-tegaskan-komitmen-lindungi-data-peserta-didik
8.  ANTARA News. (Februari 2026). Pernyataan pemerintah mengenai dugaan
    kebocoran data siswa.\
    https://www.antaranews.com/berita/5407966/menko-pratikno-tegaskan-tidak-ada-kebocoran-data-siswa
9.  Dokumentasi yang disediakan untuk analisis: screenshot materi
    promosi dan percakapan terkait klaim *dump database sekolah*.
    Sumber, keaslian data, dan klaim akses belum diverifikasi secara
    independen.
