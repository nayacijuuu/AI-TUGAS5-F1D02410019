import contextlib
import io
import os

import main

KB = main.muat()
HERE = os.path.dirname(os.path.abspath(__file__))

KASUS = [
    ('Kasus 1: suka asam, punya dripper',
     {'suka rasa asam segar', 'punya dripper atau mesin drip'},
     ['BIJI: arabika dengan sangrai terang (light roast)',
      'SEDUH: drip atau pour-over, gilingan sedang (seperti garam dapur)'],
     ['BIJI: robusta atau sangrai gelap (dark roast)']),

    ('Kasus 2 (negatif): ingin kopi dingin saja, tidak mau merendam lama',
     {'ingin kopi dingin'},
     [], ['SEDUH: cold brew, gilingan kasar, rendam beberapa jam']),

    ('Kasus 3: suka pahit pekat, body tebal, punya French press dan mesin espresso',
     {'suka rasa pahit pekat', 'ingin body tebal', 'punya french press', 'punya mesin espresso'},
     ['BIJI: robusta atau sangrai gelap (dark roast)',
      'SEDUH: espresso, gilingan halus (seperti garam meja)'],
     ['BIJI: arabika dengan sangrai terang (light roast)']),

    ('Kasus 4: suka manis lembut dan suka pahit pekat (dua profil)',
     {'suka rasa manis lembut', 'suka rasa pahit pekat'},
     ['BIJI: campuran arabika-robusta dengan sangrai sedang sampai gelap'], []),

    ('Kasus 5: suka asam, punya French press (aturan AND dua rantai)',
     {'suka rasa asam segar', 'punya french press'},
     ['SARAN: French press paling cocok untuk sangrai sedang sampai gelap; untuk sangrai terang pertimbangkan pour-over'], []),
     
    ('Kasus 6: ingin kopi dingin dan bersedia merendam; seduhan terlalu pahit',
     {'ingin kopi dingin', 'bersedia merendam beberapa jam', 'kopi terasa terlalu pahit atau asam'},
     ['SEDUH: cold brew, gilingan kasar, rendam beberapa jam',
      'PERBAIKAN: gilingan terlalu halus, coba lebih kasar'], []),
]


def jalankan(ya):
    def jawab(nomor, fakta, pertanyaan):
        j = fakta in ya
        print(f'{nomor}. {pertanyaan} (y/t) > {"y" if j else "t"}')
        return j
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        akhir = main.sesi(KB, jawab)
    return buf.getvalue(), akhir


if __name__ == '__main__':
    gagal = 0
    for i, (nama, ya, harus, tidak) in enumerate(KASUS, 1):
        teks, akhir = jalankan(ya)
        ok = all(h in akhir for h in harus) and not any(t in akhir for t in tidak)
        if not harus:
            ok = ok and akhir == []
        print(('LULUS ' if ok else 'GAGAL ') + nama)
        gagal += not ok
        if i <= 3:
            with open(os.path.join(HERE, 'hasil', f'kasus{i}.txt'), 'w', encoding='utf-8') as f:
                f.write(teks)
    print()
    print('Semua lulus.' if gagal == 0 else f'{gagal} kasus gagal.')
    raise SystemExit(1 if gagal else 0)
