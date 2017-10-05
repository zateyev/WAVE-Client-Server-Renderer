#!/usr/bin/env python
# import gtk.gdk
# from gi.repository import Gtk
import threading
import pyscreenshot as ImageGrab
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
from models.dwave import Dwave
from ctypes import c_float, c_int
from random import randint
import time

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

f = Dwave()

dw = threading.Thread(target = f.run)
# f.set_scene_size(c_int(int(round(1024))), c_int(int(round(681))))
# dw.start()

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
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('first_connection')
def test_message(json):
    width = json['data']['width']
    height = json['data']['height']
    f.set_scene_size(c_int(int(round(width))), c_int(int(round(height))))
    dw.start()
    print("socket connection established")
    # session['receive_count'] = session.get('receive_count', 0) + 1
    emit('server_response', {'data': json['data']})


@socketio.on('query_img')
def test_broadcast_message(json):
    px = json['data']['position']['x']
    py = json['data']['position']['y']
    pz = json['data']['position']['z']
    ux = json['data']['up']['x']
    uy = json['data']['up']['y']
    uz = json['data']['up']['z']

    xmin = json['data']['geometry']['xmin']
    xmax = json['data']['geometry']['xmax']
    ymin = json['data']['geometry']['ymin']
    ymax = json['data']['geometry']['ymax']
    zmin = json['data']['geometry']['zmin']
    zmax = json['data']['geometry']['zmax']

    width = json['data']['size']['width']
    height = json['data']['size']['height']
    # print(json['data']['position']['x'])
    # print(json['data']['position']['y'])
    # print(json['data']['position']['z'])

    # ds = threading.Thread(target = f.set_cam_settings,
    #                   args = (c_float(px), c_float(py), c_float(pz),
    #                           c_float(ux), c_float(uy), c_float(uz)))
    # ds.start()
    # ds.join()

    f.reset()
    f.set_cam_settings(c_float(px), c_float(py), c_float(pz), c_float(ux), c_float(uy), c_float(uz))
    # f.set_scene_size(c_int(int(round(width))), c_int(int(round(height))))
    f.set_geometry(c_float(xmin), c_float(xmax), c_float(ymin), c_float(ymax), c_float(zmin), c_float(zmax))

    # if not dw.isAlive():
    #     dw.start()

    # print(not dw.isAlive())

    # print(width)
    # print(height)

    # f.run()

    # dw = threading.Thread(target = f.run)
    # dw.start()
    # dw.join()

    # uid = json['data']['uid']

    # session['receive_count'] = session.get('receive_count', 0) + 1

    while not f.is_image_ready():
        pass

    emit('receive_img',# + str(uid),
    {'data': json['data']['position']['x'], 'id': randint(0, 100000)})
    #  {'data': str(json), 'id': randint(0, 1000)})


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


@socketio.on('disconnect') #, namespace='/test')
def test_disconnect():
    dw.stop()
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
