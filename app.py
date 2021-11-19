from flask import Flask, render_template, request
import os

app = Flask(__name__)



def parser(file_name):
    f = open(".//server_logs//"+file_name, 'r')
    text = f.read()
    f.close()
    
    hrs = 0
    mins = 0
    i = text.index('Time Log:')
    text = text[i::]
    text = text.splitlines()
    
    for l in text:
    
        if 'am' in l or 'pm' in l:
            loop = 0
            for i in range(len(l)):
                if loop > 2:
                    break
                if loop == 0 and (l[i:i+2]=='am' or l[i:i+2] == 'pm'):
                    start = l[i-5:i]
                    loop += 1
                elif loop == 1 and (l[i:i+2]=='am' or l[i:i+2] == 'pm'):
                    stop = l[i-5:i]
                    loop += 1
                elif loop == 2:
                    strtm = int(start[-2:])
                    enm = int(stop[-2:])
                    strth = int(start[:2].strip())
                    enhr = int(stop[:2].strip())
                    
                    mi = 0
                    hr = 0
                    
                    if strtm > enm:
                        mi = 60 - (strtm-enm)
                        hr -= 1
                    else:
                        mi = enm - strtm

                    if strth > enhr:
                        hr = hr + (12 - (strth - enhr))
                    else:
                        hr = hr + enhr - strth
                    
                    hrs += hr
                    mins += mi
                    
                    loop = 0
                    break
        else:
            pass
            
    hrs += (mins//60)
    mins = (mins%60)
    return str(str(hrs)+' hours '+ str(mins)+' minutes')
    

@app.route('/')
def home():
    fl = os.listdir(".//server_logs")
    return render_template("homepage.html", filelist =fl)

@app.route('/submit', methods=['POST'])
def submit():
    fname = request.form.get("selectedf")
    t = parser(fname)
    fl = os.listdir(".//server_logs")
    return render_template("time.html", time = t, fname = fname)

if __name__=='__main__':
    app.run(debug=True)