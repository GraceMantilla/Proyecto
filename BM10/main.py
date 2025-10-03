from flask import Flask, render_template

app = Flask(__name__)

def result_calculate(size, light, device):
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + light * light_coef + device * devices_coef 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/size')
def size():
    return render_template('size.html')

@app.route('/<size>')
def light(size):
    return render_template(
                            'light.html', 
                            size=size
                           )

@app.route('/<size>/<light>')
def electronic(size, light):
    return render_template(
                            'electronic.html',
                            size = size, 
                            light = light                       
                           )

@app.route('/<size>/<light>/<device>')
def end(size, light, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(light), 
                                                    int(device)
                                                    )
                        )

app.run(debug=True)