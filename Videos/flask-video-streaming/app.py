#!/usr/bin/env python
from flask import Flask, render_template, Response, url_for, redirect
from flask import send_from_directory
# emulated camera
from camera import Camera
import os
import socket
import fcntl
import struct
import thread
import time

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)

@app.route('/leave')
def leave():
    thread.start_new_thread(flow,())
    return ''

@app.route('/')
def index():
    #"""Video streaming home page."""
    #os.system('./try.py 10.0.0.1 2')
    return redirect(url_for('video'))
    #return render_template('index.html')

@app.route('/video')
def video():
    """Video streaming home page."""
    ip = get_ip()
    print ip
    if(ip == '1'):
        web_name = 'Web2'
    else:
        web_name = 'Web1'
    return render_template('index.html',
                           name = web_name)

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def get_ip():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        inet = fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s','h5-eth0'[:15]))
        ret = '0'
    except Exception as e:
        ret = '1'
    return ret

def flow():
    ip = get_ip()
    #time.sleep(10)
    print "start"
    os.system('./try.py 10.0.0.1 2 '+ip)
    os.system('./try.py 10.0.0.2 2 '+ip)
    os.system('./try.py 10.0.0.3 2 '+ip)
    print "stop"
    thread.exit_thread()

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/<filename>')
def get_file(filename):
    return send_from_directory('./',filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=5000)
