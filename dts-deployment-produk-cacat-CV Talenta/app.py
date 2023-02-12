from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('modelprodukcacatcvtalenta.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    Produk, BeratProduk, BentukProduk, Pengukuran, UkuranCacat, Posisi, Area = [x for x in request.form.values()]

    data = []

    data.append(int(Produk))

    if BeratProduk == 'kecil':
        data.extend([0, 1])
    elif BeratProduk == 'sedang':
        data.extend([1, 0])
    else:
        data.extend([1, 1])

    if BentukProduk == 'besar':
        data.extend([0, 1])
    else:
        data.extend([1, 0])

    if Pengukuran == 'ada':
        data.extend([0, 1])
    else:
        data.extend([1, 0])

    if UkuranCacat == 'besar':
        data.extend([0, 1])
    elif UkuranCacat == 'kecil':
        data.extend([1, 0])
    else:
        data.extend([1, 1])

    if Posisi == 'luar':
        data.extend([0, 1])
    else:
        data.extend([1, 0])

    if Area == 'Lock':
        data.extend([0, 1])
    elif Area == 'NoLock':
        data.extend([1, 0])
    else:
        data.extend([1, 0])

    prediction = model.predict([data])
    output = round(prediction[0], 6)

    return render_template('index.html', Produk=Produk, BeratProduk=BeratProduk, BentukProduk=BentukProduk, Pengukuran=Pengukuran, UkuranCacat=UkuranCacat, Posisi=Posisi, Area=Area, Hasil=output)


if __name__ == '__main__':
    app.run(debug=True)
