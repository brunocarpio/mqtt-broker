#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.core.engine.util import objectToBytes

PORT = 8000
group = PairingGroup('SS512')

def cpabe_setup():
    g, gp = group.random(G1), group.random(G2)
    alpha, beta = group.random(ZR), group.random(ZR)
    g.initPP(); gp.initPP()
    h = g ** beta; f = g ** ~beta
    e_gg_alpha = pair(g, gp ** alpha)
    pk = { 'g':g, 'g2':gp, 'h':h, 'f':f, 'e_gg_alpha':e_gg_alpha }
    mk = {'beta':beta, 'g2_alpha':gp ** alpha }
    return (pk, mk)

(pk, mk) = cpabe_setup()

def cpabe_keygen(pk, mk, S):
    r = group.random()
    g_r = (pk['g2'] ** r)
    D = (mk['g2_alpha'] * g_r) ** (1 / mk['beta'])
    D_j, D_j_pr = {}, {}
    for j in S:
        r_j = group.random()
        D_j[j] = g_r * (group.hash(j, G2) ** r_j)
        D_j_pr[j] = pk['g'] ** r_j
    return { 'D':D, 'Dj':D_j, 'Djp':D_j_pr, 'S':S }

class HandleRequests(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = parse.urlsplit(self.path)
        params = dict(parse.parse_qsl(parsed_url.query))
        print(params)
        if parsed_url.path == '/pk':
            self.send_response(200)
            self.send_header('Content-type', 'application/octet-stream')
            self.end_headers()
            self.wfile.write(objectToBytes(pk, group))
        if parsed_url.path == '/keygen':
            self.send_response(200)
            self.send_header('Content-type', 'application/octet-stream')
            self.end_headers()
            attributes = list(params.values())
            print(attributes)
            sk = cpabe_keygen(pk, mk, attributes)
            self.wfile.write(objectToBytes(sk, group))

def run(server_class=HTTPServer, handler_class=HandleRequests):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
