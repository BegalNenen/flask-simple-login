from flask import Flask,render_template,request

app = Flask(__name__, template_folder="html")

# Membuat halaman login dan memeriksa hasil input    
@app.route('/admin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Mengambil string dari form login
        username = request.form['username']
        password = request.form['password']        
        # Cek data username dan password
        if username == 'admin' and password == 'pw@admin':
        	    # Jika input benar, maka akan dialihkan ke halaman admin
        	    return render_template('login_berhasil.html')
        # Jika input salah, akan dialihkan ke halaman login (lagi)
        return render_template('login_gagal.html')
    # Ini halaman login utama
    return render_template('login.html')
if __name__ == '__main__':
	app.run(debug = True)
