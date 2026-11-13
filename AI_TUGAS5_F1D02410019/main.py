import json
import os

BERKAS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kb_kopi.json')


def muat(path=BERKAS):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def terpenuhi(aturan, memori):
    """mode 'dan' = semua syarat ada di memori; 'atau' = salah satu cukup."""
    ada = [s in memori for s in aturan['jika']]
    return all(ada) if aturan['mode'] == 'dan' else any(ada)


def maju(kb, fakta_awal):
    """Forward chaining. Mengembalikan (memori, urutan, asal)."""
    memori = set(fakta_awal)
    urutan = []            # [(nomor siklus, id aturan, hasil)]
    asal = {}              # hasil -> aturan penghasilnya
    siklus = 0
    while True:
        cocok = [a for a in kb['aturan'] if terpenuhi(a, memori) and a['maka'] not in memori]
        if not cocok:
            return memori, urutan, asal
        r = cocok[0]
        siklus += 1
        memori.add(r['maka'])
        asal[r['maka']] = r
        urutan.append((siklus, r['id'], r['maka']))


def fakta_dasar(kb):
    """Fakta yang tidak pernah menjadi hasil aturan: ditanyakan ke user."""
    hasil = {a['maka'] for a in kb['aturan']}
    dasar = []
    for a in kb['aturan']:
        for s in a['jika']:
            if s not in hasil and s not in dasar:
                dasar.append(s)
    return dasar


def kesimpulan_akhir(kb, asal):
    """Hasil yang tidak dipakai sebagai syarat oleh aturan lain."""
    dipakai = {s for a in kb['aturan'] for s in a['jika']}
    return [h for h in asal if h not in dipakai]


def cetak_alasan(r, memori, asal, tingkat=0):
    pad = '  ' * tingkat
    ada = [s for s in r['jika'] if s in memori]
    print(f"{pad}{r['maka']}  <- {r['id']} ({', '.join(ada)})  [sumber: {', '.join(r['sumber'])}]")
    for s in ada:
        if s in asal:
            cetak_alasan(asal[s], memori, asal, tingkat + 1)


def sesi(kb, jawab):
    """Satu sesi tanya-jawab. jawab(nomor, fakta, pertanyaan) -> True/False."""
    print(kb['judul'])
    print('Jawab y/t.')
    ya = []
    for i, f in enumerate(fakta_dasar(kb), 1):
        if jawab(i, f, kb['pertanyaan'].get(f, f'Apakah {f}?')):
            ya.append(f)
    print()
    print('Fakta awal:', ', '.join(ya) if ya else '(tidak ada)')
    print()
    memori, urutan, asal = maju(kb, ya)
    for n, rid, hasil in urutan:
        print(f'Siklus {n}: {rid} -> {hasil}')
    print(f'Siklus {len(urutan) + 1}: tidak ada aturan baru, berhenti')
    print()
    akhir = kesimpulan_akhir(kb, asal)
    if akhir:
        print('Kesimpulan:')
        for h in akhir:
            print(f'  - {h}')
        print('Alasan:')
        for h in akhir:
            cetak_alasan(asal[h], memori, asal, 1)
    else:
        print('Kesimpulan: tidak ada (fakta yang diberikan belum cukup untuk menarik kesimpulan)')
    print()
    print('Catatan:', kb['batas'])
    return akhir


def jawab_keyboard(nomor, fakta, pertanyaan):
    while True:
        j = input(f'{nomor}. {pertanyaan} (y/t) > ').strip().lower()
        if j in ('y', 't'):
            return j == 'y'
        print('   Ketik y atau t.')


if __name__ == '__main__':
    kb = muat()
    while True:
        sesi(kb, jawab_keyboard)
        print()
        if input('Rekomendasi lagi? (y/t) > ').strip().lower() != 'y':
            break
        print()
