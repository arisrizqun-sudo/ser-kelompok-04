"""Servo virtual untuk Jobsheet 07 (OPSIONAL, file ini tidak perlu diketik).

Cara pakai: taruh file ini di folder p07, lalu tambahkan SATU baris
    import servo_layar
di bawah "import pin_tiruan" pada program yang memakai class Servo
(coba_servo_kelas.py, animasi_uji.py, rekam_gerak.py).

Setiap kali Servo.gerak_ke() dipanggil, sebuah halaman di peramban akan
menggerakkan lengan servo ke sudut yang sama. Halaman hanya berjalan di
komputer Anda sendiri (127.0.0.1) dan tidak membutuhkan paket tambahan.
Hapus baris import tersebut di Raspberry Pi, servo sungguhan akan bergerak.
"""
import atexit
import json
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import komponen

JEDA = 0.5          # jarak minimum antar gerakan (detik) agar gerakan terlihat
_keadaan = {}       # nama servo -> data yang ditampilkan
_kunci = threading.Lock()
_terhubung = threading.Event()
_server = None
_terakhir = 0.0

HALAMAN = """<!doctype html>
<html lang="id"><head><meta charset="utf-8"><title>Servo virtual</title>
<style>
body{font-family:'Segoe UI',Arial,sans-serif;margin:0;background:#f2f2f2;color:#262626}
header{padding:12px 20px;background:#1E2761;color:#fff}
header h1{font-size:18px;margin:0 0 4px 0}
#status{font-size:13px;opacity:.9}
#kumpulan{display:flex;flex-wrap:wrap;gap:16px;padding:16px;justify-content:center}
.kartu{background:#fff;border:1px solid #c8c8c8;border-radius:10px;padding:6px 14px 10px;width:460px}
.kartu h2{font-size:16px;margin:8px 0 0 0}
.lengan{transition:transform .35s ease-in-out;transform-origin:230px 250px}
.angka{font-size:15px;margin-top:2px}
.pesan{color:#A31515;font-weight:600;min-height:1.5em;font-size:14px}
</style></head><body>
<header><h1>Servo virtual</h1><div id="status">Menghubungkan ke program Python...</div></header>
<div id="kumpulan"></div>
<script>
var NS = 'http://www.w3.org/2000/svg';
var kartu = {};
function el(nama, atribut, induk){
  var e = document.createElementNS(NS, nama);
  for (var k in atribut) e.setAttribute(k, atribut[k]);
  if (induk) induk.appendChild(e);
  return e;
}
function titik(sudut, jari){
  var r = sudut * Math.PI / 180;
  return [230 - jari * Math.cos(r), 250 - jari * Math.sin(r)];
}
function buatKartu(nama){
  var d = document.createElement('div'); d.className = 'kartu';
  var h = document.createElement('h2'); h.textContent = nama; d.appendChild(h);
  var svg = el('svg', {viewBox: '0 0 460 290', width: '440'}, d);
  el('path', {d: 'M 60 250 A 170 170 0 0 1 400 250', fill: 'none', stroke: '#9a9a9a', 'stroke-width': 3}, svg);
  [0, 45, 90, 135, 180].forEach(function(a){
    var p = titik(a, 158), q = titik(a, 178), t = titik(a, 200);
    el('line', {x1: p[0], y1: p[1], x2: q[0], y2: q[1], stroke: '#9a9a9a', 'stroke-width': 3}, svg);
    var tk = el('text', {x: t[0], y: t[1] + 5, 'text-anchor': 'middle', 'font-size': 15, fill: '#555'}, svg);
    tk.textContent = a + '\\u00b0';
  });
  el('rect', {x: 165, y: 250, width: 130, height: 34, rx: 6, fill: '#1E2761'}, svg);
  var g = el('g', {'class': 'lengan'}, svg);
  el('line', {x1: 230, y1: 250, x2: 230, y2: 92, stroke: '#F2A104', 'stroke-width': 12, 'stroke-linecap': 'round'}, g);
  el('circle', {cx: 230, cy: 250, r: 16, fill: '#1E2761'}, svg);
  var angka = document.createElement('div'); angka.className = 'angka'; d.appendChild(angka);
  var pesan = document.createElement('div'); pesan.className = 'pesan'; d.appendChild(pesan);
  document.getElementById('kumpulan').appendChild(d);
  return {lengan: g, angka: angka, pesan: pesan};
}
function perbarui(s){
  if (!kartu[s.nama]) kartu[s.nama] = buatKartu(s.nama);
  var k = kartu[s.nama];
  k.lengan.style.transform = 'rotate(' + (s.sudut - 90) + 'deg)';
  k.angka.textContent = 'Sudut ' + s.sudut + '\\u00b0 | lebar pulsa ' + s.lebar + ' ms';
  k.pesan.textContent = s.pesan;
}
function ambil(){
  fetch('/status', {cache: 'no-store'}).then(function(r){ return r.json(); }).then(function(j){
    document.getElementById('status').textContent = 'Terhubung ke program Python';
    j.servo.forEach(perbarui);
  }).catch(function(){
    document.getElementById('status').textContent = 'Program Python sudah berhenti. Halaman ini boleh ditutup.';
  });
}
setInterval(ambil, 100);
ambil();
</script></body></html>
"""


class _Penangan(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/status":
            _terhubung.set()
            with _kunci:
                isi = json.dumps({"servo": list(_keadaan.values())})
            self._kirim(isi.encode("utf-8"), "application/json")
        elif self.path in ("/", "/index.html"):
            self._kirim(HALAMAN.encode("utf-8"), "text/html; charset=utf-8")
        else:
            self.send_error(404)

    def _kirim(self, data, jenis):
        self.send_response(200)
        self.send_header("Content-Type", jenis)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


def _mulai():
    global _server
    if _server is not None:
        return
    _server = ThreadingHTTPServer(("127.0.0.1", 0), _Penangan)
    _server.daemon_threads = True
    threading.Thread(target=_server.serve_forever, daemon=True).start()
    alamat = "http://127.0.0.1:%d" % _server.server_address[1]
    print("Servo virtual: bila peramban tidak terbuka sendiri, buka", alamat)
    webbrowser.open(alamat)
    if not _terhubung.wait(10):
        print("Peramban belum terhubung, program dilanjutkan tanpa tampilan")


def _simpan(servo, pesan=""):
    sudut = float(servo.nilai)
    lebar = servo.lebar_pulsa()
    if lebar is None:
        lebar = round(1 + sudut / 180, 3)
    with _kunci:
        _keadaan[servo.nama] = {"nama": servo.nama, "sudut": sudut,
                                "lebar": lebar, "pesan": pesan}


_gerak_ke_asli = komponen.Servo.gerak_ke


def _gerak_ke(self, sudut):
    global _terakhir
    if self.nama not in _keadaan:
        _simpan(self)
    _mulai()
    sisa = JEDA - (time.time() - _terakhir)
    if sisa > 0:
        time.sleep(sisa)
    try:
        _gerak_ke_asli(self, sudut)
    except ValueError as e:
        _simpan(self, "ditolak: " + str(e))
        _terakhir = time.time()
        raise
    _simpan(self)
    _terakhir = time.time()


def _tunggu_akhir():
    if _server is not None:
        time.sleep(0.8)


komponen.Servo.gerak_ke = _gerak_ke
atexit.register(_tunggu_akhir)