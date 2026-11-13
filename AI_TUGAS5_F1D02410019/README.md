# Tugas 5 - Sistem Pakar Sederhana: Rekomendasi Kopi

- **Nama:** Naylarifa Maulida Asri
- **NIM:** F1D02410019
- **Mata kuliah:** Kecerdasan Buatan

## 1. Topik dan cara menjalankan

Topik: **rekomendasi kopi** (bukan kesehatan manusia). Program menanyakan selera rasa dan alat seduh yang dimiliki, lalu menyimpulkan **jenis biji, tingkat sangrai, dan cara seduh** yang cocok beserta alasannya. Program juga bisa memberi saran perbaikan bila seduhan terasa pahit, asam, atau hambar.

- Bahasa: Python 3 (diuji pada Python 3.12; versi 3.8 ke atas cukup), tanpa library tambahan.
- Mesin forward chaining ditulis sendiri di `main.py`. Aturan ada di `kb_kopi.json`.

Jalankan dari dalam folder ini:

```
python main.py   # jalankan program
python test.py   # uji otomatis 6 kasus
```

Di Windows, jika `python` tidak dikenali, coba `py main.py`.

**Cara mengisi jawaban:** program menampilkan 12 pertanyaan bernomor, misalnya `1. Apakah Anda suka kopi yang rasanya asam segar (seperti buah)? (y/t) >`. Ketik `y` untuk ya atau `t` untuk tidak, lalu Enter. Setelah semua dijawab, program menampilkan siklus, kesimpulan, alasan, dan catatan batas keberlakuan. Di akhir, program bertanya `Rekomendasi lagi? (y/t)`.

File: `kb_kopi.json` (aturan dan sumber), `main.py` (program), `test.py` (uji), `hasil/` (keluaran teks), `screenshot/` (tangkapan layar).

## 2. Latar belakang: apa yang dikatakan sumber

Rasa kopi tidak ditentukan satu hal saja. Sumber-sumber yang saya pakai menunjukkan tiga penentu utama yang bisa dipilih peminum kopi sendiri: **jenis biji**, **tingkat sangrai**, dan **cara seduh (termasuk ukuran gilingan)**. Bagian ini merangkum isi sumber dengan kata-kata saya sendiri; aturan di Bagian 4 disusun dari ringkasan ini.

**Jenis biji (S1).** Penelitian Universitas Diponegoro membandingkan kopi arabika dan robusta. Kopi arabika dilaporkan berasa lebih asam, bertekstur lebih lembut, dan beraroma harum. Hasil ukurnya konsisten dengan itu: total asam arabika lebih tinggi daripada robusta (sekitar 1,06% dibanding 0,76%), begitu pula total padatan terlarut (sekitar 9,60% dibanding 8,82%), dan panelis menilai arabika lebih manis. Robusta digambarkan beraroma kuat, tidak seasam arabika, bertekstur lebih kasar, dan berkadar kafein lebih tinggi. Karena kafein menyumbang rasa pahit, arabika yang kafeinnya lebih rendah dinilai cenderung lebih asam daripada pahit.

**Tingkat sangrai (S2).** Prosiding Politeknik Negeri Jember menjelaskan bahwa penyangraian ikut menentukan rasa dan, menurut kajian yang dikutipnya, porsinya sekitar 30% dari cita rasa akhir (jenis kopi sekitar 60%, penyajian sekitar 10%). Sangrai terang (light) memberi keasaman paling menonjol pada arabika, sangrai sedang (medium) memberi rasa seimbang, dan sangrai gelap (dark) memberi rasa tebal yang hampir pahit karena senyawa asam terurai makin banyak saat sangrai makin lama. Pada uji kesukaan 30 panelis, dark roast paling banyak disukai, tetapi perbedaan rasanya tidak signifikan secara statistik. Jadi tingkat sangrai pada sistem ini adalah kecenderungan, bukan kepastian.

**Cara seduh dan gilingan (S3).** National Coffee Association USA menyebut aturan umum: makin lama kopi bersentuhan dengan air, makin kasar gilingannya. Maka espresso (seduh dalam hitungan detik) memakai gilingan halus, drip dan pour-over gilingan sedang, serta French press dan cold brew gilingan kasar. French press dikenal berasa bold dan berbody penuh, cocok untuk sangrai sedang sampai gelap, dengan air sekitar 93 +/- 3 derajat Celsius, kontak sekitar 4 menit, dan rasio kopi:air 1:10 sampai 1:16. Panduan itu juga memberi cara memperbaiki rasa: seduhan yang pahit atau asam mungkin digiling terlalu halus (terlalu banyak terekstraksi), sedangkan seduhan hambar atau encer mungkin digiling terlalu kasar.

## 3. Sumber

| Kode | Judul | Penerbit | Tahun | URL | Diakses |
| ---- | ----- | -------- | ----- | --- | ------- |
| S1 | Perbedaan Sifat Fisikokimia dan Organoleptik Produk Kopi Rempah dari Kopi Arabika dan Kopi Robusta (Priyanto, Hintono, Dwiloka; Jurnal Aplikasi Teknologi Pangan 11(4), hlm. 179-184; DOI 10.17728/jatp.13827) | Universitas Diponegoro (Indonesian Food Technologists) | 2022 | [link](https://ejournal2.undip.ac.id/index.php/jatp/article/download/13827/10234) | 13 Nov 2026 |
| S2 | Pengaruh Teknik Penyangraian Terhadap Tingkat Kesukaan Konsumen Kopi Arabika Varietas Lini-S 795 (Hartatie & Nisa; Prosiding Agropross, hlm. 691-697; E-ISSN 2964-0172) | Politeknik Negeri Jember | 2024 | [link](https://proceedings.polije.ac.id/index.php/agropross/article/download/789/673/1095) | 13 Nov 2026 |
| S3 | French press coffee (panduan seduh dan ukuran gilingan) | National Coffee Association USA (aboutcoffee.org) | diperbarui 6 Feb 2025 | [link](https://www.aboutcoffee.org/brewing/french-press-coffee/) | 13 Nov 2026 |

Aturan adalah parafrasa, bukan kutipan. Isi yang diambil dari sumber:

- S1 hlm. 180 dan 182-183: arabika lebih asam, lebih lembut, kafein lebih rendah; robusta beraroma kuat, kafein lebih tinggi, tidak seasam arabika; total asam dan padatan terlarut arabika lebih tinggi, arabika dinilai lebih manis.
- S2 hlm. 692 dan 694-695: light roast menonjolkan keasaman, medium roast seimbang, dark roast tebal dan hampir pahit; asam menjadi pahit seiring sangrai makin lama.
- S3: tabel ukuran gilingan per metode, angka seduh French press (suhu, waktu, rasio), French press cocok untuk sangrai sedang sampai gelap, dan petunjuk perbaikan rasa dari ukuran gilingan.

Yang merupakan rumusan saya sendiri: mengelompokkan selera menjadi tiga "profil" (cerah, seimbang, pekat); R7 (campuran arabika-robusta bagi yang menyukai profil seimbang sekaligus pekat); dan R12 (menggabungkan S2 dan S3 untuk saran French press pada profil cerah). S3 berasal dari asosiasi industri, bukan lembaga pemerintah atau universitas; bagian yang memakainya hanya soal cara seduh.

## 4. Tabel aturan (14 aturan, 11 kesimpulan akhir)

Hasil antara (miring) dipakai aturan lain. Kesimpulan akhir ditulis tebal.

| Aturan | IF | THEN | Sumber |
| ------ | -- | ---- | ------ |
| R1 | suka rasa asam segar | *profil cerah* | S1, S2 |
| R2 | ingin rasa seimbang ATAU suka rasa manis lembut | *profil seimbang* | S1, S2 |
| R3 | suka rasa pahit pekat ATAU ingin body tebal | *profil pekat* | S1, S2, S3 |
| R4 | *profil cerah* | **BIJI: arabika sangrai terang** | S1, S2 |
| R5 | *profil seimbang* | **BIJI: arabika sangrai sedang** | S1, S2 |
| R6 | *profil pekat* | **BIJI: robusta atau sangrai gelap** | S1, S2 |
| R7 | *profil seimbang* DAN *profil pekat* | **BIJI: campuran arabika-robusta, sangrai sedang sampai gelap** | S1, S2 |
| R8 | punya mesin espresso | **SEDUH: espresso, gilingan halus** | S3 |
| R9 | punya French press | **SEDUH: French press, gilingan kasar, 93 +/- 3 C, 4 menit, 1:10-1:16** | S3 |
| R10 | punya dripper atau mesin drip | **SEDUH: drip/pour-over, gilingan sedang** | S3 |
| R11 | ingin kopi dingin DAN bersedia merendam beberapa jam | **SEDUH: cold brew, gilingan kasar** | S3 |
| R12 | punya French press DAN *profil cerah* | **SARAN: French press cocok untuk sangrai sedang-gelap; untuk sangrai terang pertimbangkan pour-over** | S2, S3 |
| R13 | kopi terasa terlalu pahit atau asam | **PERBAIKAN: gilingan lebih kasar** | S3 |
| R14 | kopi terasa hambar atau encer | **PERBAIKAN: gilingan lebih halus** | S3 |

Rantai aturan: R1 -> R4 dan R12; R2 -> R5 dan R7; R3 -> R6 dan R7 (tiga profil adalah hasil antara yang dipakai aturan lain). Fakta yang ditanyakan ke user adalah fakta yang tidak pernah menjadi hasil aturan (12 pertanyaan).

## 5. Metode: Forward Chaining

Dipilih karena user sudah tahu faktanya (selera dan alat yang dimiliki), dan kesimpulan muncul dari rantai aturan: selera menjadi profil, profil menjadi rekomendasi biji. Langkahnya:

```
memori <- fakta yang dijawab "ya"
ULANGI:
    cocok <- aturan yang syaratnya terpenuhi DAN hasilnya belum ada di memori
    JIKA cocok kosong: BERHENTI
    r <- aturan pertama di cocok
    tambahkan r.maka ke memori dan catat bahwa r.maka berasal dari r
```

Mode `dan` = semua syarat harus ada di memori. Mode `atau` = cukup satu syarat. Aturan yang hasilnya sudah ada tidak dijalankan lagi supaya program berhenti. Kesimpulan akhir adalah hasil yang tidak dipakai sebagai syarat oleh aturan lain. Alasan ditampilkan dengan menelusuri balik dari kesimpulan ke aturan yang menghasilkannya, sampai ke jawaban user, lengkap dengan kode sumber tiap aturan.

## 6. Kasus uji

| # | Jawaban "ya" | Kesimpulan | Keluaran |
| - | ------------ | ---------- | -------- |
| 1 | suka rasa asam segar, punya dripper | arabika sangrai terang; seduh drip/pour-over gilingan sedang | `hasil/kasus1.txt` |
| 2 (negatif) | ingin kopi dingin saja (tidak bersedia merendam) | tidak ada | `hasil/kasus2.txt` |
| 3 | suka pahit pekat, body tebal, punya French press dan mesin espresso | robusta atau sangrai gelap; espresso gilingan halus; French press gilingan kasar | `hasil/kasus3.txt` |

`test.py` juga menguji 3 kasus lain (manis lembut + pahit pekat menghasilkan campuran; suka asam + French press memicu saran R12; cold brew + seduhan terlalu pahit). Kasus 2 tidak menghasilkan kesimpulan karena cold brew (R11) butuh dua syarat sekaligus: ingin kopi dingin DAN bersedia merendam beberapa jam.

![Kasus 1](screenshot/kasus1.png)
![Kasus 2 (tidak ada kesimpulan)](screenshot/kasus2.png)
![Kasus 3](screenshot/kasus3.png)

## 7. Batas keberlakuan

Pengetahuan dalam program ini berasal dari tiga sumber: jurnal Universitas Diponegoro (2022), prosiding Politeknik Negeri Jember (2024), dan panduan National Coffee Association USA (2025). Aturannya hanya untuk memilih jenis biji, tingkat sangrai, dan cara seduh rumahan berdasarkan selera, bukan untuk menilai mutu kopi atau memberi saran kesehatan. Selera rasa itu subjektif; perbedaan rasa antartingkat sangrai pada S2 tidak signifikan secara statistik, dan S1 membandingkan hanya satu sampel arabika dan satu sampel robusta, dan sampelnya berupa kopi rempah (ditambah kayu manis dan gula aren), sehingga hubungan "arabika = asam, robusta = pahit" adalah kecenderungan umum, bukan hukum. Hasilnya adalah saran awal, bukan keputusan akhir; coba beberapa kombinasi dan sesuaikan dengan lidah Anda. Catatan ini juga ditampilkan di akhir keluaran program.

## 8. Penggunaan alat bantu AI

Saya menggunakan Claude (AI) sebagai alat bantu untuk mencari sumber, menyusun draf aturan dari sumber, dan menulis kode awal program serta draf README. Sumber, aturan, dan kode tersebut saya periksa sendiri, dan saya memahami cara kerjanya.
