# -*- coding: utf-8 -*-
import socket
import time
import os
import psql.db
import datetime

from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = str(socket.gethostname())
PORT_NUMBER = 80


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        paths = {
            '/': {'status': 200},
            '/favicon.ico': {'status': 500}
        }

        if self.path in paths:
            self.respond(paths[self.path])
        else:
            self.respond({'status': 500})

    def handle_http(self, status_code, path):
        self.send_response(status_code)

        print("Writing to DB log message")

        time_now = datetime.datetime.now()
        date = time_now.strftime('%Y-%m-%d %H:%M:%S')
        
        
        if(db_session.writelogtodb(date,"Accessed " + str(path) + " via server " + str(HOST_NAME))):
            dbStatus="Success"
            dbStatusHTML="<font color=\"green\"><b>Success</b></font>"
        else:
            dbStatus="Fail"
            dbStatusHTML="<font color=\"red\"><b>Fail</b></font>"

        
        print("Writing to DB result: "+str(dbStatus))
        
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        content = '''
        <html><head><title>MyWebApp</title></head>
            <body>
                <h2>
                <p>Serving host %s</p>
                <p></p>
                <p>Time: %s</p>
                <p>Accessed path: %s</p>
                <p>Writing to DB status: %s</p></h2>
            </body>
        </html>
        ''' % (str(HOST_NAME), str(date), str(path), str(dbStatusHTML))

        return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['status'], self.path)
        self.wfile.write(response)

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'HTTP Server Starts')
    

    DBUSER = os.environ.get('DBUSER')
    DBPASS = os.environ.get('DBPASS')
    DBNAME = os.environ.get('DBNAME')
    DBHOST = os.environ.get('DBHOST')
    if not DBHOST:
        DBHOST="127.0.0.1"
    DBPORT = os.environ.get('DBPORT')
    if not DBPORT:
        DBPORT=str(5432)

    print("Initial connection to DB")
    db_session = psql.db.db(user=DBUSER, password=DBPASS,host=DBHOST,database=DBNAME)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    db_session.close_db()

    httpd.server_close()

    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))

    

    