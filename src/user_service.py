import csv, sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib

DATA_CACHE = None

def load_data():
    global DATA_CACHE
    if DATA_CACHE is None:
        DATA_CACHE = []
        with open('data/users.csv') as f:
            r = csv.reader(f)
            header = next(r, None)  # Skip the header row if present
            for row in r:
                # Expecting these fields:
                # user_id,name,email,signup_date,age,height_cm,weight_kg,activity_level,health_goals
                if len(row) < 9:
                    continue
                DATA_CACHE.append({
                    "user_id": row[0],
                    "name": row[1],
                    "email": row[2],
                    "signup_date": row[3],
                    "age": row[4],
                    "height_cm": row[5],
                    "weight_kg": row[6],
                    "activity_level": row[7],
                    "health_goals": row[8],
                })
    return DATA_CACHE

def find_user_by_id(uid):
    d = load_data()
    for u in d:
        if u['user_id'] == uid:
            return u
    return None

def find_users_by_name(n):
    d = load_data()
    results = []
    for u in d:
        if n.lower() in u['name'].lower():
            results.append(u)
    return results

def handle_cli(args):
    if len(args) < 2:
        print("Usage: python user_service.py [--id USER_ID | --name USER_NAME]")
        sys.exit(1)
    if args[1] == '--id':
        user = find_user_by_id(args[2])
        if user:
            print("Found user:", user)
        else:
            print("User not found.")
    elif args[1] == '--name':
        users = find_users_by_name(args[2])
        if users:
            for u in users:
                print("Found user:", u)
        else:
            print("No users found.")
    else:
        print("Unknown option.")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # example endpoint: /user?id=123 or /user?name=alice
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if 'id' in params:
            uid = params['id'][0]
            user = find_user_by_id(uid)
            if user:
                self.wfile.write(str(user).encode('utf-8'))
            else:
                self.wfile.write(b'{}')
        elif 'name' in params:
            name = params['name'][0]
            users = find_users_by_name(name)
            self.wfile.write(str(users).encode('utf-8'))
        else:
            self.wfile.write(b'{}')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].startswith('--'):
        handle_cli(sys.argv)
    else:
        print("Starting HTTP server on 0.0.0.0:8080")
        httpd = HTTPServer(('0.0.0.0', 8080), Handler)
        httpd.serve_forever()
