#/usr/local/bin/python3
# -*- coding: utf-8 -*-
import socket
import time
import os
import psql.db
import datetime

from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = str(socket.gethostname())
PORT_NUMBER = 80

def connect_to_db():
    connection_status=False

    DBUSER = os.environ.get('DBUSER')
    DBPASS = os.environ.get('DBPASS')
    DBNAME = os.environ.get('DBNAME')
    DBHOST = os.environ.get('DBHOST')

    if not DBHOST:
        DBHOST="127.0.0.1"
    DBPORT = os.environ.get('DBPORT')
    if not DBPORT:
        DBPORT=str(5432)

    print(time.asctime(),"webapp: Initiating connection to DB")
    
    # Exception if connection failed
    db_session = psql.db.db(user=DBUSER, password=DBPASS,host=DBHOST,database=DBNAME)
    return db_session

def write_log_to_db(logmessage):
    try:
        db_session=connect_to_db()
        db_session.writelogtodb(time.asctime(), logmessage)
        db_session.close_db()
    except:
        return False
    return True


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    
    def do_GET(self):
        paths = {
            '/': {'status': 200},
            '/load': {'status': 200}
        }

        if self.path in paths:
            self.respond(paths[self.path])
        else:
            self.respond({'status': 500})

    def handle_http(self, status_code, path):
        self.send_response(status_code)

        dbStatus=""

        if(write_log_to_db("Accessed path \"" + str(path) + "\" via server name \"" + str(HOST_NAME) + "\"")):
            dbStatus="Success"
            dbStatusHTML="<font color=\"green\"><b>Success</b></font>"
        else:
            dbStatus="Fail"
            dbStatusHTML="<font color=\"red\"><b>Fail</b></font>"  

        print(time.asctime(),"webapp: Writing access fact to DB: " + str(dbStatus))      
        
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        load_str=""
        if "load" in path.lower():
            load_str="stress --vm 1 --vm-bytes 128M --timeout 10s"
            os.system(load_str)

        content = '''
        <html><head><title>MyWebApp</title></head>
            <body>
                <h2>
                <p>Serving host %s</p>
                <p></p>
                <p>Time: %s</p>
                <p>Accessed path: %s</p>
                <p>Writing to DB status: %s</p></h2>
                <hr>

                <h3><p><a href="/load">Click to add some load</a></p></h3>
        ''' % (str(HOST_NAME), str(time.asctime()), str(path), str(dbStatusHTML))
        if load_str:
            content += "<h3><p>Temp additional load was added: %s</p></h3>" % (str(load_str))
        content += '''
            </body>
        </html>
        '''

        return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['status'], self.path)
        self.wfile.write(response)

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print(time.asctime(), 'webapp: HTTP Server Starts')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))
