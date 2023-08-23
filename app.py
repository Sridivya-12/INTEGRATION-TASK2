from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/divya')
def home1():
    return render_template('index1.html')
@app.route('/Surya')
def home2():
    return render_template('index2.html')
@app.route('/krishna')
def home3():
    return render_template('index3.html')
@app.route('/abdul')
def home4():
    return render_template('index4.html')
@app.route('/divya1')
def home5():
    return render_template('index5.html')
@app.route('/divya2')
def home6():
    return render_template('index6.html')



if(__name__)=="__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)