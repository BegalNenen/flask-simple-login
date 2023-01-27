### Simple Flask Login  
Ini adalah aplikasi Flask Login tanpa Database dengan logika validasi sederhana. 
  
### Cara Kerja  
Menyamakan hasil input dengan data string yang ada pada perintah validasi, lalu memperbarui halaman berdasarkan hasil input tadi. Jika string yang dimasukan sama dengan string yang ada pada fitur validasi, maka login sukses dan sebaliknya.

Saat user berhasil login, halaman akan diperbarui tanpa pengalihan url ke halaman baru.

### Catatan
#### Redirect  
Jika saya mengalihkannya ke halaman baru, maka saya harus membuat rute khusus untuk halaman tersebut. Rasanya fitur login ini terasa sia sia karena jika rute baru dibuat, saya tidak perlu melakukan login terlebih dahulu, cukup menambahkan `/dashboard` (jika halaman baru dinamakan dashboard) pada url.

#### Block
Saya sedikit kesulitan saat membuat block pada Flask, saya tidak mengerti kenapa block yang tidak muncul saat user gagal login. Jadi untuk sementara saya gunakan file `login_gagal.html` untuk menampilkan pemberitahuan bahwa username atau password yang dimasukan salah.

#### Deploy
Saya menambahkan file `vercel.json` agar Anda dapat langsung mencobanya di <a href="https://vercel.app">Vercel</a>
