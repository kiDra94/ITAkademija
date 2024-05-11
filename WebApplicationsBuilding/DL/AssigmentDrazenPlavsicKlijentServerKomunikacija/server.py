from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

students_dict = {
    '123': {'name': 'Marko', 'surname': 'Marković', 'average_grade': 8.5},
    '456': {'name': 'Ana', 'surname': 'Anić', 'average_grade': 7.9},
    '789': {'name': 'Ivan', 'surname': 'Ivanović', 'average_grade': 9.2},
    '101': {'name': 'Elena', 'surname': 'Elezović', 'average_grade': 6.8}
}


class StudentRequestHandler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-type')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()


    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        parsed_path = urlparse(self.path)
        if parsed_path.path == '/student':
            query_params = parse_qs(parsed_path.query)
            index = query_params.get('index', [None])[0]
            if index is None:
                self.wfile.write(json.dumps({'error': 'Index not provided'}).encode())
                return
            student_info = students_dict.get(index)
            if student_info:
                self.wfile.write(json.dumps(student_info).encode())
            else:
                self.wfile.write(json.dumps({'error': 'Student not found'}).encode())
        else:
            self.wfile.write(json.dumps({'error': 'Invalid path'}).encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode('utf-8'))
        except json.decoder.JSONDecodeError as e:
            self.wfile.write(json.dumps({'error': 'Invalid JSON data', 'details': str(e)}).encode())
            return
        
        index = data.get('index')
        if index is None:
            self.wfile.write(json.dumps({'error': 'Index not provided'}).encode())
            return
        
        students_dict[index] = {
            'name': data.get('name'),
            'surname': data.get('surname'),
            'average_grade': data.get('average_grade')
        }
        
        self.wfile.write(json.dumps({'message': 'Student added successfully'}).encode())

def run(server_class=HTTPServer, handler_class=StudentRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
