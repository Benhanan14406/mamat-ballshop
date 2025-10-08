# **TUGAS INDIVIDU 2**
#

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Saya melihat atribut-atribut apa saja di checklist lalu mengimplementasikannya di model Bola dengan parameter-parameter yang sesuai untuk atribut-atribut tersebut. Setelah itu, saya mengolah data-data tersebut di function-function untuk halaman-halaman website saya di fiel views.py dan menghubungkan function-function tersebut ke link-link khusus di file urls.py.


### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Flowchart](flowchart.jpeg)


### Jelaskan peran settings.py dalam proyek Django!

File settings.py adalah control center proyek Django di mana file tersebut mengendalikan bagaimana proyek bekerja dalam environment.


### Bagaimana cara kerja migrasi database di Django?

Di Django, migrasi akan melihat perubahan-perubahan di file models.py lalu, jika terdeteksi adanya perubahan, perubahan-perubahan tersebut akan diaplikasikan ke database (penambahan/penghapusan model, perubahan atribut, dll). 


### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena Django menggunakan bahasa pemrograman Python, bahasa pemrograman yang relatif mudah untuk dipahami, dan karena Django memiliki struktur yang mudah dipahami.


### Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Tidak ada, informasi untuk tutorial 1 sudah sangat baik dan jelas.

#
#
#
# **TUGAS INDIVIDU 3**
#

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery diperlukan dalam pengimplementasian sebuah platform karena data delivery memungkinkan terjadinya komunikasi antara pengguna dan perangkat dengan transfer data yang cepat dan dalam bentuk yang dipahami berbagai perangkat.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, JSON lebih baik dan lebih populer dibandingkan XML karena JSON memiliki format yang lebih mudah dipahami dan mendapat native support di JavaScript.

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() pada form Django berfungsi untuk memvalidasi input dari user dan memberi error jika input tidak sesuai. Dengan begitu, method is_valid() dapat membantu menjaga keamanan aplikasi dan konsistensi data.  

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django?

csrf_token dibutuhkan saat membuat form di Django untuk menjaga aplikasi dari serangan CSRF sehingga data dalam aplikasi terjaga dengan aman. Tanpa adanya csrf_token, aplikasi kita akan lebih rentan terhadap serangan siber.

### Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Tanpa adanya CSRF token, penyerang dapat membuat request palsu dan/atau melakukan manipulasi data.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Cek ketentuan tugas.
2. Buat form XML dan JSON untuk seluruh Product.
3. Buat form XML dan JSON untuk Product tertentu dengan id.
4. Buat form ProductCreationForm untuk membuat Product baru.
5. Buat method-method validasi untuk seluruh data yang diterima ProductCreationForm.
6. Pastikan method-method validasi tersebut sudah sesuai dengan data yang divalidasi dan memberi error message yang sesuai.
7. Lakukan modifikasi terhadap code untuk mempersingkat dan memperjelas code.

### Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Tidak ada, informasi untuk tutorial 1 sudah sangat baik dan jelas.

## Screenshot Postman Untuk Access URL XML dan JSON Data Delivery

![Flowchart](xml_all.png)
![Flowchart](json_all.png)
![Flowchart](xml_byid.png)
![Flowchart](json_byid.png)

#
#
#
# **TUGAS INDIVIDU 4**
#

### Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

Django AuthenticationForm adalah form bawaan Django yang membantu implementasi fungsionalitas autentikasi dengan memverifikasi data User. Django AuthenticationForm, sebagai fitur bawaan, memiliki keamanan, kemudahan integrasi, dan kompatibilitas dengan Django secara langsung. Akan tetapi, Django AuthenticationForm hanya mampu memverifikasi model User bawaan Django dan bergantung pada session-based auth. 

### Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Autentikasi adalah proses verifikasi identitas pengguna, sedangkan otorisasi adakah proses pemberian hak akses pada pengguna. Django memfasilitasi autentikasi dengan form AuthenticationForm dan otorisasi dengan decorator dan class-based view.

### Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Session memiliki tingkat keamanan yang tinggi dan kapasitas yang besar, tetapi hal tersebut membuat session memiliki performance yang buruk, sedangkan cookie memiliki performance dan scalability yang baik akibat penyimpanan data di client, tetapi hal tersebut membuat cookie lebih rentan terhadap serangan siber dan kapasitas yang kecil.

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Secara default, penggunaan cookies dalam pengembangan web dapat membuat web rentan terhadap serangan XSS, CSRF,  dan session hijacking. Untuk menangani hal tersebut, Django memiliki fungsionalitas validasi dan built-in security middleware untuk menangani serangan XSS, CSRF token untuk menangani serangan CSRF, dan session cookie security settings default untuk menangani session hijacking.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Cek ketentuan tugas.
2. Buat function register, login, dan logout untuk autentikasi pengguna.
3. Modifikasi kode agar sesuai dengan program secara keseluruhan.
4. Hubungkan model Product dengan User.
5. Implementasi otorisasi di views.py.
6. Buat halaman HTML dan link URL yang sesuai.

#
#
#
# **TUGAS INDIVIDU 5**
#

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

1. Inline style (CSS yang ditulis langsung dalam elemen)
2. ID selector (CSS untuk id tertentu)
3. Class selector (CSS untuk class tertentu)
4. Element selector (CSS untuk elemen tertentu)

###  Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Responsive design menjadi konsep yang penting dalam pengembangan aplikasi web karena responsive design memungkinkan aplikasi masih memiliki tampilan yang compatible untuk berbagai device dan meningkatkan user experience. 

Contoh aplikasi yang sudah menerapkan responsive design: **Tokopedia**
Alasan: Untuk memungkinkan penggunaan Tokopedia di berbagai device sehingga memudahkan para pelanggan untuk membeli barang dan memberi untung bagi pihak Tokopedia.

Contoh aplikasi yang belum menerapkan responsive design: **Aplikasi Lama Dengan Ukuran Screen Fixed**
Alasan: Para pengguna pada masanya masih sering menggunakan hanya satu tipe device sehingga belum ada keperluan untuk membuat design yang responsive.

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

**Margin**: Space antara border suatu elemen dengan elemen external lainnya.
**Border**: Garis tepi dari elemen.
**Padding**: Space antara isi suatu elemen dengan bordernya.

Ketiga hal tersebut dapat diimplementasikan dengan CSS.

###  Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flex box digunakan untuk mengatur posisi elemen-elemen dalam satu dimensi sedangkan grid layout digunakan untuk mengatur posisi elemen-elemen dalam dua dimensi. 

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

1. Cek ketentuan tugas.
2. Rencanakan design yang akan diimplementasi
3. Eksperimentasi untuk membuat tampilan yang ideal.
4. Membuat method edit dan delete untuk Product.

#
#
#
# **TUGAS INDIVIDU 6**
#

### Apa perbedaan antara synchronous request dan asynchronous request?

Pada synchronous request, web akan menunggu sampai response diperoleh dari server, sedangkan pada asynchronous request, web tetap responsive selama menunggu response.

### Bagaimana AJAX bekerja di Django (alur request–response)?

Event di client -> JS mengirim request AJAX ke Django -> Request diproses Django -> Server memberi response -> JS di client memproses response

### Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?

AJAX memungkinkan web yang lebih responsive dan mulus dibandingkan render biasa.

### Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?

1. Menggunakan CSRF token.
2. Menggunakan HTTPS.
3. Validasi data.

### Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

AJAX membuat web lebih responsive dan mulus sehingga user lebih nyaman dan tidak perlu menunggu lama saat menggunakan qeb.