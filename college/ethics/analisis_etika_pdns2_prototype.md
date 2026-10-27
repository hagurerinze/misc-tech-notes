# Analisis Pelanggaran Etika dan Tanggung Jawab Profesional dalam Insiden Ransomware Pusat Data Nasional Sementara (PDNS) 2 Indonesia Tahun 2024

> **Status:** draf kerja untuk riset dan penyusunan tugas Etika IT.  
> **Tujuan:** menyimpan fakta yang dilaporkan, rantai sumber, batas bukti, hipotesis yang perlu diuji, dan kerangka analisis etika.  
> **Prinsip:** bedakan fakta, laporan pihak lain, klaim yang belum diverifikasi, dan interpretasi penulis.

## 1. Pertanyaan utama

Bagaimana insiden ransomware PDNS 2 pada Juni 2024 memperlihatkan persoalan etika dan tanggung jawab profesional dalam keamanan infrastruktur digital pemerintah, pengelolaan kredensial, kesiapan pemulihan, dan perlindungan data pribadi?

### Pertanyaan turunan

1. Apa yang diketahui dari kronologi resmi tentang upaya menonaktifkan Windows Defender dan aktivitas berbahaya?
2. Apa yang dapat dan tidak dapat disimpulkan dari pemberitaan mengenai kata sandi `Admin#1234`?
3. Apa pelajaran etika dari dokumentasi terpisah yang mengiklankan layanan *dump database sekolah*?
4. Bagaimana tanggung jawab dibahas secara proporsional antara pimpinan/institusi, operator teknis, dan pelaku serangan?
5. Rekomendasi apa yang masuk akal tanpa mengklaim lebih dari yang didukung bukti?

## 2. Batas ruang lingkup

Analisis ini memiliki tiga jalur yang berkaitan pada tingkat tema keamanan dan tata kelola data, tetapi **tidak diasumsikan sebagai satu insiden teknis**:

- **Jalur A — PDNS 2:** ransomware, kronologi yang dilaporkan, gangguan layanan publik, deteksi, respons, dan pemulihan.
- **Jalur B — Tata kelola kredensial:** pemberitaan mengenai `Admin#1234` dan pertanyaan tentang keamanan serta pengelolaan akses.
- **Jalur C — Penawaran database sekolah:** dokumentasi promosi/percakapan yang disediakan untuk analisis, terkait dugaan penawaran pengambilan atau perdagangan data pribadi.

Tidak ada dasar yang cukup dalam bahan yang dirujuk di sini untuk menyatakan bahwa `Admin#1234` merupakan jalur masuk ransomware PDNS 2, atau bahwa dokumentasi database sekolah berasal dari PDNS 2. Jika bukti forensik atau sumber resmi baru ditemukan, hubungan tersebut perlu dinilai ulang secara eksplisit, bukan diasumsikan.

## 3. Standar pencatatan bukti

Gunakan label berikut ketika menambahkan temuan:

- **[FAKTA RESMI DILAPORKAN]** — informasi dalam pernyataan atau laporan resmi; sebutkan siapa yang melaporkannya.
- **[LAPORAN MEDIA]** — informasi yang diberitakan media dan sebaiknya ditautkan ke sumber aslinya.
- **[DOKUMENTASI PENGAMAT]** — tangkapan layar atau materi yang disediakan untuk analisis; belum tentu diverifikasi independen.
- **[HIPOTESIS]** — penjelasan yang mungkin, tetapi belum dibuktikan.
- **[ANALISIS ETIKA]** — penilaian normatif berdasarkan fakta dan prinsip etika.
- **[BELUM DIKETAHUI]** — pertanyaan yang tidak bisa dijawab dengan bukti yang tersedia.

### Aturan analisis

1. Jangan menyamakan urutan waktu dengan hubungan sebab-akibat.
2. Jangan menyimpulkan akses awal penyerang hanya dari adanya kelemahan keamanan.
3. Jangan menyatakan backup tidak ada tanpa bukti; bedakan backup tidak tersedia, tidak lengkap, terdampak, atau gagal dipulihkan.
4. Jangan menyamakan penggunaan Windows atau konektivitas jaringan dengan kelalaian secara otomatis.
5. Jangan menyebut identitas individu atau menuduh pihak tertentu tanpa bukti yang memadai.
6. Jangan menampilkan data siswa, NIK, NISN, alamat, nomor telepon, atau identitas akun dalam versi publik.
7. Jelaskan keterbatasan dokumentasi dan sumber yang digunakan.

## 4. Jalur A — Insiden ransomware PDNS 2

### 4.1 Kronologi yang dilaporkan

Menurut keterangan BSSN yang dikutip dalam konferensi pers/pemberitaan pada akhir Juni 2024:

- Upaya menonaktifkan Windows Defender dilaporkan teridentifikasi mulai **17 Juni 2024 sekitar pukul 23.15 WIB**.
- Aktivitas berbahaya dilaporkan mulai **20 Juni 2024 sekitar pukul 00.54 WIB**.
- Laporan publik menyebut aktivitas seperti pemasangan berkas berbahaya, penghapusan berkas sistem penting, dan penonaktifan layanan.
- Windows Defender dilaporkan mengalami *crash* sekitar pukul 00.55 WIB.

Sumber awal untuk ditinjau:

- ANTARA News, “Menkominfo jelaskan kronologi serangan siber PDNS 2” (27 Juni 2024):  
  https://www.antaranews.com/berita/4171167/menkominfo-jelaskan-kronologi-serangan-siber-pdns-2.html
- Komdigi, siaran pers terkait pemulihan PDNS 2 (27 Juni 2024):  
  https://www.komdigi.go.id/berita/siaran-pers/detail/siaran-pers-np-tentang-percepat-pemulihan-kominfo-bssn-dan-telkom-operasikan-server-baru-pengganti

**Catatan verifikasi:** buka ulang tautan dan pastikan istilah serta waktu sesuai sumber. Bedakan laporan awal dari temuan forensik akhir.

### 4.2 Apa yang dapat disimpulkan?

Kronologi tersebut relevan untuk mengevaluasi:

- pemantauan terhadap perubahan status kontrol keamanan;
- kemampuan mendeteksi aktivitas yang tidak wajar;
- eskalasi dan respons ketika alat proteksi dinonaktifkan;
- pembatasan hak akses dan segmentasi sistem;
- pencadangan, pengujian pemulihan, dan kesinambungan layanan.

### 4.3 Apa yang belum dapat disimpulkan?

Berdasarkan sumber terbuka yang dicantumkan dalam draf ini, belum cukup dasar untuk memastikan:

- metode akses awal penyerang;
- apakah akses diperoleh melalui kredensial, kerentanan, konfigurasi, rekayasa sosial, atau metode lain;
- siapa yang melakukan setiap tindakan pada sistem;
- apakah satu kontrol keamanan yang gagal merupakan penyebab tunggal;
- apakah ada keterlibatan orang dalam (*insider*) dalam serangan.

Semua hal di atas perlu diperlakukan sebagai pertanyaan investigasi, bukan fakta.

### 4.4 Dampak layanan dan backup

Pemberitaan resmi pada masa pemulihan menyebut 239 instansi terdampak dan 43 instansi tidak terdampak karena data yang tersimpan di PDNS 2 merupakan data cadangan. Pernyataan ini tidak cukup untuk menjelaskan kondisi backup setiap instansi atau seluruh detail pemulihan.

Dalam analisis, bedakan kondisi berikut:

- backup tidak pernah dibuat;
- backup ada tetapi tidak lengkap atau sudah usang;
- backup tersimpan pada lingkungan yang ikut terdampak;
- backup tersedia tetapi proses pemulihan tidak berhasil atau belum diuji;
- backup berhasil dipulihkan dalam waktu yang dapat diterima.

Jangan memilih salah satu kondisi tanpa sumber yang mendukung.

## 5. Jalur B — Tata kelola kredensial dan isu `Admin#1234`

### 5.1 Mengapa isu ini penting?

Pada Juli 2024, media memberitakan beredarnya dokumen yang memuat informasi akses layanan pusat data dan kata sandi `Admin#1234` yang dikaitkan dengan salah satu pengguna layanan. Isu ini relevan sebagai pertanyaan tentang tata kelola kredensial, paparan informasi akses, pengelolaan akun berhak tinggi, dan tanggung jawab pihak yang membuat, menyimpan, membagikan, serta mengawasi kredensial.

Sumber awal:

- Katadata, pemberitaan mengenai kata sandi `Admin#1234` (6 Juli 2024):  
  https://katadata.co.id/digital/teknologi/6688d1d936c50/viral-pusat-data-dibobol-karena-password-admin1234-ini-kata-kominfo
- Katadata, pemberitaan tentang pengaturan ulang kata sandi pusat data (9 Juli 2024):  
  https://katadata.co.id/digital/teknologi/668d0061a0c7c/kominfo-atur-ulang-password-pusat-data-nasional-di-setiap-kementerian
- Katadata, “Belajar dari Pusat Data, Ini Daftar Password Gampang Ditebak Hacker” (9 Juli 2024):  
  https://katadata.co.id/digital/teknologi/668cc247182ab/belajar-dari-pusat-data-ini-daftar-password-gampang-ditebak-hacker

**Catatan penting:** sumber-sumber ini merupakan titik awal penelusuran media. Baca keseluruhan artikel dan cari pernyataan resmi yang dirujuk sebelum menjadikan detail tertentu sebagai fakta final.

### 5.2 Analisis keamanan

Kredensial yang mudah ditebak, dibagikan secara tidak aman, atau terekspos dapat meningkatkan risiko akses tidak sah. Risiko dapat menjadi lebih besar apabila:

- kredensial digunakan pada akun dengan hak akses tinggi;
- kata sandi digunakan ulang pada layanan lain;
- banyak orang menggunakan akun bersama sehingga aktivitas sulit diaudit;
- tidak ada autentikasi multifaktor ketika tersedia dan sesuai risiko;
- kredensial tidak dicabut atau dirotasi setelah paparan terdeteksi;
- log akses dan peninjauan hak akses tidak memadai.

Ini merupakan risiko umum dalam tata kelola akses, bukan bukti bahwa semua kondisi tersebut terjadi dalam insiden PDNS 2.

### 5.3 Hubungan dengan serangan PDNS 2

**Status: belum terbukti secara spesifik berdasarkan sumber dalam draf ini.**

Pemberitaan mengenai `Admin#1234` layak dianalisis sebagai isu keamanan kredensial yang serius. Namun, jangan menuliskan bahwa kata sandi tersebut adalah jalur masuk ransomware PDNS 2 tanpa bukti forensik atau pernyataan resmi yang secara jelas mengonfirmasi hubungan itu.

Formulasi yang aman secara akademik:

> Pemberitaan mengenai kredensial `Admin#1234` menimbulkan pertanyaan serius tentang tata kelola akses dan kerahasiaan informasi autentikasi. Akan tetapi, berdasarkan sumber yang dirujuk dalam analisis ini, belum dapat dipastikan bahwa kredensial tersebut digunakan untuk memperoleh akses awal dalam serangan ransomware PDNS 2.

### 5.4 Praktik yang direkomendasikan

- Terapkan kata sandi unik dan kuat serta pengelolaan rahasia yang aman.
- Batasi akun administrator dan gunakan hak akses minimum.
- Terapkan autentikasi multifaktor bila tersedia dan sesuai tingkat risiko.
- Hindari akun bersama; gunakan akun individual agar aktivitas dapat diaudit.
- Tinjau, rotasi, atau cabut kredensial yang diduga terekspos.
- Catat dan tinjau akses istimewa.
- Tetapkan prosedur respons untuk paparan kredensial.

## 6. Jalur C — Dokumentasi penawaran database sekolah

### 6.1 Apa yang terlihat dalam dokumentasi?

Tangkapan layar yang disediakan untuk tugas ini memperlihatkan:

- materi promosi yang mengklaim menawarkan layanan *dump database sekolah*;
- klaim mengenai jenis data yang bisa diperoleh, seperti nama, jenis kelamin, NIK, NISN, informasi orang tua, tanggal/tempat lahir, alamat, kelas, dan sekolah;
- percakapan yang tampak membahas transaksi dan contoh keluaran mirip data terstruktur;
- antarmuka yang mengklaim menyediakan fungsi untuk memulai proses *dump* menggunakan NPSN.

Materi tersebut merupakan **dokumentasi klaim yang terlihat pada tangkapan layar**. Dokumen ini tidak memverifikasi secara independen keaslian data, asal-usulnya, apakah prosesnya benar-benar berfungsi, cakupan sekolah yang dapat diakses, atau legalitas akses yang diklaim.

### 6.2 Batas penggunaan sebagai bukti

Tangkapan layar dapat membantu mendokumentasikan bahwa materi promosi atau klaim tersebut tampak beredar di kanal yang direkam. Namun, screenshot saja tidak membuktikan:

- data berasal dari sistem pemerintah tertentu;
- data tersebut masih aktual atau autentik;
- penjual benar-benar memiliki akses yang diklaim;
- data diperoleh dari PDNS 2;
- terjadi kebocoran baru, bukan penggunaan ulang data lama;
- seluruh sekolah atau siswa dalam klaim tersebut terdampak.

Jangan mengubah klaim penjual menjadi fakta yang sudah terverifikasi.

### 6.3 Relevansi etika dan privasi

Jika data siswa diperoleh, diperdagangkan, atau disebarkan tanpa dasar yang sah, risiko etisnya mencakup hilangnya kendali individu atas informasi pribadi, penipuan dan penyalahgunaan identitas, penargetan terhadap siswa atau keluarga, penyebaran informasi anak yang sulit ditarik kembali, dan menurunnya kepercayaan terhadap pengelolaan data pendidikan.

Penilaian atas tindakan pihak tertentu tetap memerlukan bukti yang memadai. Analisis dapat menilai risiko dan prinsip yang berlaku tanpa menuduh identitas yang belum terbukti.

### 6.4 Pemisahan dari insiden PDNS 2

Belum ada dasar dalam dokumentasi yang disediakan untuk menyatakan bahwa penawaran database sekolah tersebut berasal dari PDNS 2 atau berhubungan langsung dengan ransomware tahun 2024. Keduanya dapat dibahas dalam satu tugas sebagai isu keamanan dan tata kelola data, tetapi harus dipisahkan secara eksplisit dalam kronologi dan kesimpulan.

Sumber konteks yang perlu ditinjau:

- Komdigi, informasi mengenai investigasi penjualan data pribadi ilegal (2 Oktober 2026):  
  https://portal.komdigi.go.id/kanal-publik/berita-kini/10576
- Kemendikdasmen, keterangan mengenai penelusuran dugaan penyalahgunaan data Dapodik (5 Agustus 2026):  
  https://www.kemendikdasmen.go.id/siaran-pers/15940-kemendikdasmen-telusuri-dugaan-penyalahgunaan-dapodik-tegaskan-komitmen-lindungi-data-peserta-didik
- ANTARA, pernyataan pemerintah mengenai dugaan kebocoran data siswa (Februari 2026):  
  https://www.antaranews.com/berita/5407966/menko-pratikno-tegaskan-tidak-ada-kebocoran-data-siswa

**Catatan verifikasi waktu:** status penyelidikan dapat berubah. Buka ulang sumber dan pastikan tanggal, konteks, serta statusnya sebelum menggunakan sumber dalam PDF final.

### 6.5 Penanganan dokumentasi

Untuk versi publik:

- samarkan nama siswa, NIK, NISN, alamat, nomor telepon, dan data keluarga;
- samarkan identitas akun atau nomor kontak yang dapat mengidentifikasi individu;
- hindari mengunggah contoh data mentah atau JSON berisi data pribadi;
- gunakan hanya gambar yang diperlukan untuk argumen;
- simpan salinan asli secara privat bila diperlukan untuk dokumentasi, dan jangan menyebarkannya ulang.

## 7. Analisis etika: tanggung jawab berlapis

Analisis tanggung jawab tidak seharusnya menjadi peringkat kesalahan yang dibuat tanpa dasar. Nilai tindakan berdasarkan kewenangan, kewajiban, keputusan, akses terhadap informasi, sumber daya, dan bukti yang tersedia. Tanggung jawab etis, administratif, dan pidana juga merupakan kategori berbeda.

### 7.1 Pemerintah dan pimpinan institusi

Tanggung jawab pada tingkat tata kelola mencakup penetapan standar dan kebijakan keamanan, pengawasan terhadap penyedia serta operator, alokasi sumber daya dan pembagian kewenangan, penilaian risiko dan pengujian kesiapan pemulihan, transparansi yang bertanggung jawab kepada publik, serta evaluasi pascainsiden dan tindak lanjut terukur.

Keamanan tidak cukup diperlakukan sebagai persoalan teknis yang diserahkan seluruhnya kepada staf operasional. Namun, penilaian terhadap keputusan pimpinan tertentu memerlukan bukti tentang kewenangan, pengetahuan, keputusan, dan kondisi saat itu.

### 7.2 Operator dan pengelola teknis

Tanggung jawab profesional dapat meliputi konfigurasi dan pemeliharaan sistem sesuai prosedur, pengelolaan kredensial dan hak akses, pemantauan peringatan serta perubahan kontrol keamanan, eskalasi terhadap aktivitas mencurigakan, pencatatan dan dokumentasi insiden, serta pengujian backup dan proses pemulihan.

Penilaian harus mempertimbangkan lingkup kewenangan operator, prosedur yang tersedia, beban kerja, sumber daya, dan informasi yang dapat diaksesnya. Jangan mengalihkan seluruh tanggung jawab organisasi kepada individu teknis tanpa bukti yang mendukung.

### 7.3 Pelaku serangan

Pihak yang dengan sengaja menjalankan ransomware dan mengganggu sistem memikul tanggung jawab langsung atas tindakan serangan tersebut. Kelemahan pertahanan korban, jika terbukti ada, tidak membenarkan tindakan pelaku. Analisis kelemahan sistem bertujuan memahami risiko dan memperbaiki pertahanan, bukan mengurangi tanggung jawab pelaku.

### 7.4 Penjual, pembeli, dan penyebar data

Jika data pribadi diperoleh atau diperdagangkan tanpa dasar yang sah, tindakan itu menimbulkan persoalan serius mengenai kerahasiaan, privasi, persetujuan, dan potensi kerugian individu. Namun, dokumentasi yang tersedia belum cukup untuk menetapkan identitas, sumber data, atau seluruh peran pihak yang terlihat dalam screenshot.

### 7.5 Cara membuat penilaian yang adil

Untuk setiap pihak, tanyakan:

1. Apa kewajiban atau tanggung jawab yang relevan?
2. Apa kewenangan nyata pihak tersebut?
3. Apa tindakan atau kelalaian yang didukung bukti?
4. Apa yang masih belum diketahui?
5. Apakah ada faktor organisasi atau sistemik yang membatasi tindakan?
6. Rekomendasi apa yang sebanding dengan temuan?

## 8. Prinsip etika dan rekomendasi

### Prinsip etika

- **Kerahasiaan:** informasi hanya boleh diakses dan digunakan oleh pihak berwenang.
- **Integritas:** sistem dan data harus dilindungi dari perubahan atau penghapusan yang tidak sah.
- **Ketersediaan:** layanan publik perlu memiliki rencana pemulihan yang teruji.
- **Akuntabilitas:** tindakan istimewa harus dapat ditelusuri dan dipertanggungjawabkan.
- **Kompetensi profesional:** pihak yang bertanggung jawab harus menerapkan praktik keamanan yang sesuai risiko dan kewenangannya.
- **Proporsionalitas:** klaim dan penilaian harus sebanding dengan bukti.
- **Perlindungan privasi:** data pribadi, khususnya data anak, tidak boleh disebarluaskan hanya untuk membuktikan suatu dugaan.

### Rekomendasi teknis dan tata kelola

1. Terapkan pemantauan terpusat untuk perubahan pada antivirus, EDR, log, dan kontrol keamanan kritis.
2. Batasi hak akses administrator dan audit penggunaan akun istimewa.
3. Tinjau kebijakan kata sandi, autentikasi multifaktor, serta prosedur penanganan kredensial terekspos.
4. Segmentasikan lingkungan dan batasi jalur akses antarsistem sesuai kebutuhan.
5. Simpan backup yang terisolasi dari lingkungan utama dan lakukan uji pemulihan berkala.
6. Tetapkan prosedur eskalasi serta respons insiden yang jelas dan diuji.
7. Lakukan evaluasi pascainsiden yang mencatat temuan, ketidakpastian, pemilik tindak lanjut, dan tenggat perbaikan.
8. Terapkan pengendalian akses, pencatatan aktivitas, retensi yang wajar, dan prosedur respons terhadap dugaan penyalahgunaan data pribadi.
9. Publikasikan informasi kepada masyarakat secara akurat, termasuk hal yang sudah diketahui dan yang masih diselidiki.

Rekomendasi ini merupakan praktik yang patut dipertimbangkan; bukan pernyataan bahwa semua kontrol tersebut pasti tidak ada pada sistem yang dibahas.

## 9. Kesimpulan sementara

Insiden PDNS 2 menunjukkan bahwa keamanan infrastruktur digital pemerintah tidak hanya bergantung pada perangkat lunak proteksi, tetapi juga pada tata kelola akses, pemantauan, kesiapan pemulihan, dan akuntabilitas. Laporan mengenai upaya menonaktifkan Windows Defender menjadi alasan untuk menelaah deteksi dan respons keamanan. Pemberitaan `Admin#1234` menyoroti risiko pengelolaan kredensial, tetapi tidak boleh dianggap sebagai bukti jalur masuk ransomware tanpa konfirmasi yang jelas.

Dokumentasi penawaran database sekolah menimbulkan pertanyaan serius mengenai privasi dan perlindungan data siswa, tetapi keaslian serta asal-usul data belum diverifikasi independen. Tidak ada dasar yang cukup untuk menghubungkannya secara teknis dengan insiden PDNS 2.

Tanggung jawab sebaiknya dianalisis pada beberapa lapisan: pimpinan dan institusi untuk tata kelola, operator sesuai kewenangan profesional, serta pelaku atas tindakan serangan. Kesimpulan akhir harus berfokus pada bukti, batas pengetahuan, dan langkah perbaikan—bukan menetapkan satu pihak sebagai penyebab tunggal tanpa dukungan yang memadai.

## 10. Daftar sumber awal

1. ANTARA News. (27 Juni 2024). “Menkominfo jelaskan kronologi serangan siber PDNS 2.”  
   https://www.antaranews.com/berita/4171167/menkominfo-jelaskan-kronologi-serangan-siber-pdns-2.html
2. Kementerian Komunikasi dan Informatika/Komdigi. (27 Juni 2024). Siaran pers terkait percepatan pemulihan PDNS 2.  
   https://www.komdigi.go.id/berita/siaran-pers/detail/siaran-pers-np-tentang-percepat-pemulihan-kominfo-bssn-dan-telkom-operasikan-server-baru-pengganti
3. Katadata. (6 Juli 2024). Pemberitaan mengenai kata sandi `Admin#1234`.  
   https://katadata.co.id/digital/teknologi/6688d1d936c50/viral-pusat-data-dibobol-karena-password-admin1234-ini-kata-kominfo
4. Katadata. (9 Juli 2024). Pemberitaan mengenai pengaturan ulang kata sandi pusat data.  
   https://katadata.co.id/digital/teknologi/668d0061a0c7c/kominfo-atur-ulang-password-pusat-data-nasional-di-setiap-kementerian
5. Katadata. (9 Juli 2024). “Belajar dari Pusat Data, Ini Daftar Password Gampang Ditebak Hacker.”  
   https://katadata.co.id/digital/teknologi/668cc247182ab/belajar-dari-pusat-data-ini-daftar-password-gampang-ditebak-hacker
6. Kementerian Komunikasi dan Digital. (2 Oktober 2026). Pemberitaan mengenai investigasi penjualan data pribadi ilegal.  
   https://portal.komdigi.go.id/kanal-publik/berita-kini/10576
7. Kementerian Pendidikan Dasar dan Menengah. (5 Agustus 2026). “Kemendikdasmen Telusuri Dugaan Penyalahgunaan Dapodik, Tegaskan Komitmen Lindungi Data Peserta Didik.”  
   https://www.kemendikdasmen.go.id/siaran-pers/15940-kemendikdasmen-telusuri-dugaan-penyalahgunaan-dapodik-tegaskan-komitmen-lindungi-data-peserta-didik
8. ANTARA News. (Februari 2026). Pernyataan pemerintah mengenai dugaan kebocoran data siswa.  
   https://www.antaranews.com/berita/5407966/menko-pratikno-tegaskan-tidak-ada-kebocoran-data-siswa
9. Dokumentasi yang disediakan untuk tugas: tangkapan layar materi promosi dan percakapan terkait klaim *dump database sekolah*. Sumber, keaslian data, dan klaim akses belum diverifikasi secara independen.

## 11. Checklist sebelum PDF final

- [ ] Buka ulang semua tautan sumber dan pastikan judul, tanggal, serta isi sesuai.
- [ ] Tambahkan sumber primer atau pernyataan resmi bila tersedia.
- [ ] Pastikan kronologi dan angka dampak ditulis sesuai konteks sumber.
- [ ] Pastikan isu `Admin#1234` tidak dinyatakan sebagai penyebab langsung tanpa bukti.
- [ ] Pastikan dokumentasi sekolah tidak diklaim terkait dengan PDNS 2.
- [ ] Samarkan semua data pribadi dan identitas akun dalam screenshot.
- [ ] Tambahkan identitas tugas sesuai format dosen, jika diperlukan.
- [ ] Ringkas atau perluas bagian PDF berdasarkan kebutuhan tugas, bukan sekadar jumlah halaman.
- [ ] Cantumkan tanggal akses sumber web jika diwajibkan oleh format sitasi.
- [ ] Setelah PDF final selesai, tentukan apakah versi Markdown ini akan dipublikasikan ke GitHub dan apakah screenshot perlu dikecualikan dari repositori publik.
