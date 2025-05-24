from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from urllib.parse import urlparse, unquote

class MarkdownHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL
        parsed_path = urlparse(self.path)
        path = unquote(parsed_path.path)
        
        # If it's a markdown file
        if path.endswith('.md'):
            try:
                # Read the markdown file
                with open('.' + path, 'r') as f:
                    content = f.read()
                
                # Read the template
                with open('pages/key_value_store/template.html', 'r') as f:
                    template = f.read()
                
                # Replace the content placeholder with the markdown content
                html_content = template.replace('<!-- Content will be loaded here -->', 
                    f'<div class="markdown-content">{content}</div>')
                
                # Send the response
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html_content.encode())
                return
            except Exception as e:
                print(f"Error serving {path}: {e}")
        
        # For all other files, use the default handler
        return SimpleHTTPRequestHandler.do_GET(self)

def run(server_class=HTTPServer, handler_class=MarkdownHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run() 