#!/usr/bin/env python
# import gtk.gdk
# from gi.repository import Gtk
import threading
import pyscreenshot as ImageGrab
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
from models.dwave import Dwave
from ctypes import c_float
from random import randint

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None
f = Dwave()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None


# def background_thread():
#     """Example of how to send server generated events to clients."""
#     count = 0
#     while True:
#         socketio.sleep(10)
#         count += 1
#         socketio.emit('my_response',
#                       {'data': 'Server generated event', 'count': count},
#                       namespace='/test')


@app.route('/')
def index():
    return render_template('index0.html', async_mode=socketio.async_mode)


@socketio.on('my_event', namespace='/test')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})


@socketio.on('my_broadcast_event')
def test_broadcast_message(json):
    # x = json['data']['x']
    # y = json['data']['y']
    # z = json['data']['z']
    # angle = json['data']['angle']
    px = json['data']['position']['x']
    py = json['data']['position']['y']
    pz = json['data']['position']['z']
    ux = json['data']['up']['x']
    uy = json['data']['up']['y']
    uz = json['data']['up']['z']
    # f.set_quat(c_float(x), c_float(y), c_float(z), c_float(angle))
    f.set_quat(c_float(px), c_float(py), c_float(pz), c_float(ux), c_float(uy), c_float(uz))
    print(json['data']['position']['x'])
    # f.run()
    dw = threading.Thread(target = f.run)
    dw.start()
    dw.join()
    # try:
    #     thread.start_new_thread(f.run(), ())
    # except:
    #     print("Error: unable to start DWAVE")

    # img = ImageGrab.grab()
    # img.save('static/screenshot.png','png')

    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': str(json), 'id': randint(0, 1000)},
         broadcast=True)

# @socketio.on('my_broadcast_event')
# def test_broadcast_message(json):
#     session['receive_count'] = session.get('receive_count', 0) + 1
#     emit('my_response',
#          {'data': str(json), 'count': session['receive_count']},
#          broadcast=True)


@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
    disconnect()


@socketio.on('my_ping', namespace='/test')
def ping_pong():
    emit('my_pong')


@socketio.on('connect', namespace='/test')
def test_connect():
    # global thread
    # if thread is None:
    #     thread = socketio.start_background_task(target=background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app, debug=True)

# # from flask import Flask, render_template
# # app = Flask(__name__)
# #
# # @app.route('/')
# # def index():
# #     return render_template('test.html')
#
# # -*- coding: utf-8 -*-
# """
#     jQuery Example
#     ~~~~~~~~~~~~~~
#     A simple application that shows how Flask and jQuery get along.
#     :copyright: (c) 2015 by Armin Ronacher.
#     :license: BSD, see LICENSE for more details.
# """
# from flask import Flask, jsonify, render_template, request
# import gtk.gdk
# app = Flask(__name__)
#
#
# @app.route('/_add_numbers')
# def add_numbers():
#     # a = request.args.get('a', 0, type=int)
#     # b = request.args.get('b', 0, type=int)
#     # return jsonify(result=a + b)
#     w = gtk.gdk.get_default_root_window()
#     sz = w.get_size()
#     print "The size of the window is %d x %d" % sz
#     pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
#     pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
#     if (pb != None):
#         pb.save("screenshot.png","png")
#         print "Screenshot saved to screenshot.png."
#     else:
#         print "Unable to get the screenshot."
#
#
#
# @app.route('/')
# def index():
#     return render_template('index2.html')
#
# if __name__ == '__main__':
#     app.run()
