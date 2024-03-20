from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import subprocess

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        out = ""

        p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            out+=line,
        retval = p.wait()
        self.wfile.write("->"+out)

        return
if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('', 8000), GetHandler)
    server.serve_forever()
