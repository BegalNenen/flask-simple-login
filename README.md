Ini adalah aplikasi Flask Login tanpa Database dengan logika validasi sederhana. Menyamakan hasil input dengan data yang ada pada perintah validasi, lalu memperbarui halaman berdasarkan hasil input tadi. Jika string yang dimasukan sama dengan string yang ada pada fitur validasi, maka login sukses dan sebaliknya.

Saat user berhasil login, halaman akan diperbarui tanpa pengalihan url ke halaman baru. Jika saya mengalihkannya ke halaman baru, maka saya harus membuat rute khusus untuk halaman itu. Rasanya fitur login ini terasa sia sia karena jika rute baru (sebut saja: Dashboard) dibuat, saya tidak perlu melakukan login terlebih dahulu, cukup menambahkan `/dashboard` pada url.
