#!/usr/bin/env python3
"""
Rapihin folder Videos:

    <root>/<Tipe>/<YYYY>/<MM>/<YYYY-MM-DD>[-PartN]/<file>

- Tipe   = ekstensi file (Mp4, Mkv, Webm, 3gp, ...)
- Tanggal diambil dari nama file (VID-20260125-..., VID_20251127_...),
  kalau tidak ada, dari waktu modifikasi file (mtime).
- Kalau 1 folder tanggal isinya > --chunk (default 500) file,
  dipecah jadi YYYY-MM-DD-Part1, -Part2, ...
- Nama file yang sama di tujuan yang sama TIDAK menimpa: diberi
  suffix _1, _2, ... sebelum ekstensi.

Default = DRY-RUN (cuma tampilkan rencana, tidak memindah apa pun).

Pemakaian:
    python3 rapihin_videos.py ~/Videos                 # dry-run
    python3 rapihin_videos.py ~/Videos --apply         # jalankan
    python3 rapihin_videos.py ~/Videos --undo ~/Videos/_organize_log_XXXX.tsv
"""
import argparse
import csv
import datetime as dt
import math
import os
import re
import shutil
import sys
from collections import Counter, defaultdict

LOG_PREFIX = "_organize_"
SKIP_ROOT_FILES = {"videos.txt"}
SKIP_EXT = {".py", ".txt", ".md", ".tsv", ".sh", ".log"}
NAME_DATE = re.compile(r"(?<!\d)(20\d{2})(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])")


def file_date(path, name):
    m = NAME_DATE.search(name)
    if m:
        try:
            return dt.date(*map(int, m.groups())), "nama"
        except ValueError:
            pass
    return dt.date.fromtimestamp(os.stat(path).st_mtime), "mtime"


def scan(root):
    items = []
    for d, dirs, files in os.walk(root):
        dirs.sort()
        for f in sorted(files):
            p = os.path.join(d, f)
            if os.path.islink(p):
                continue
            if os.path.abspath(p) == os.path.abspath(__file__):
                continue
            if os.path.splitext(f)[1].lower() in SKIP_EXT:
                continue
            if d == root and (f in SKIP_ROOT_FILES or f.startswith(LOG_PREFIX)):
                continue
            ext = os.path.splitext(f)[1].lstrip(".").lower() or "other"
            date, src = file_date(p, f)
            items.append((p, f, ext, date, src))
    return items


def make_plan(root, chunk):
    groups = defaultdict(list)
    for it in scan(root):
        groups[(it[2], it[3])].append(it)

    plan, taken = [], set()
    renamed = 0
    split_info = []
    src_count = Counter()

    for (ext, date), lst in sorted(groups.items()):
        lst.sort(key=lambda x: x[1].lower())
        n = len(lst)
        parts = math.ceil(n / chunk) if n > chunk else 1
        per = math.ceil(n / parts)
        if parts > 1:
            split_info.append((ext, date.isoformat(), n, parts))

        for i, (p, name, _, _, src) in enumerate(lst):
            src_count[src] += 1
            day = date.isoformat()
            folder = day if parts == 1 else f"{day}-Part{i // per + 1}"
            dest_dir = os.path.join(
                root, ext.capitalize(), f"{date.year:04d}", f"{date.month:02d}", folder
            )
            dest = os.path.join(dest_dir, name)
            stem, e = os.path.splitext(name)
            k = 0
            while True:
                same = os.path.abspath(dest) == os.path.abspath(p)
                if same or (dest.lower() not in taken and not os.path.exists(dest)):
                    break
                k += 1
                dest = os.path.join(dest_dir, f"{stem}_{k}{e}")
            if k:
                renamed += 1
            taken.add(dest.lower())
            plan.append((p, dest, src))
    return plan, renamed, split_info, src_count


def prune(root):
    for d, _, _ in os.walk(root, topdown=False):
        if d != root and not os.listdir(d):
            os.rmdir(d)


def do_apply(root, plan):
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    logpath = os.path.join(root, f"{LOG_PREFIX}log_{stamp}.tsv")
    moved = 0
    with open(logpath, "w", newline="", encoding="utf-8", errors="surrogateescape") as lf:
        w = csv.writer(lf, delimiter="\t")
        for old, new, _ in plan:
            if os.path.abspath(old) == os.path.abspath(new):
                continue
            if os.path.exists(new):
                print("LEWAT (tujuan sudah ada):", new)
                continue
            os.makedirs(os.path.dirname(new), exist_ok=True)
            shutil.move(old, new)
            w.writerow([os.path.relpath(old, root), os.path.relpath(new, root)])
            lf.flush()
            moved += 1
    prune(root)
    print(f"\nSelesai: {moved} file dipindah.")
    print(f"Log (untuk undo): {logpath}")
    print(f"Undo: python3 {sys.argv[0]} {root} --undo {logpath}")


def do_undo(root, logfile):
    with open(logfile, newline="", encoding="utf-8", errors="surrogateescape") as f:
        rows = list(csv.reader(f, delimiter="\t"))
    back = 0
    for old, new in reversed(rows):
        o, n = os.path.join(root, old), os.path.join(root, new)
        if not os.path.exists(n):
            print("LEWAT (tidak ditemukan):", new)
            continue
        if os.path.exists(o):
            print("LEWAT (lokasi lama sudah terisi):", old)
            continue
        os.makedirs(os.path.dirname(o), exist_ok=True)
        shutil.move(n, o)
        back += 1
    prune(root)
    print(f"Undo selesai: {back} file dikembalikan.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root", help="folder Videos yang mau dirapikan")
    ap.add_argument("--apply", action="store_true", help="benar-benar memindah file")
    ap.add_argument("--undo", metavar="LOG", help="kembalikan dari file log .tsv")
    ap.add_argument("--chunk", type=int, default=500, help="batas file per folder tanggal (default 500)")
    a = ap.parse_args()

    root = os.path.abspath(os.path.expanduser(a.root))
    if not os.path.isdir(root):
        sys.exit(f"Folder tidak ada: {root}")

    if a.undo:
        do_undo(root, os.path.abspath(os.path.expanduser(a.undo)))
        return

    plan, renamed, split_info, src_count = make_plan(root, a.chunk)
    if not plan:
        sys.exit("Tidak ada file.")

    to_move = [p for p in plan if os.path.abspath(p[0]) != os.path.abspath(p[1])]
    by_ext = Counter(os.path.relpath(p[1], root).split(os.sep)[0] for p in plan)
    by_day = Counter(os.path.dirname(os.path.relpath(p[1], root)) for p in plan)

    print(f"Folder      : {root}")
    print(f"Total file  : {len(plan)} (perlu dipindah: {len(to_move)})")
    print(f"Sumber tgl  : dari nama file={src_count['nama']}, dari mtime={src_count['mtime']}")
    print(f"Nama kembar : {renamed} file diberi suffix _N")
    print("\nPer tipe:")
    for k, v in sorted(by_ext.items()):
        print(f"  {k:8} {v}")
    if split_info:
        print(f"\nDipecah (> {a.chunk} file):")
        for ext, day, n, parts in split_info:
            print(f"  {ext.capitalize()} {day}: {n} file -> {parts} part")
    print("\n10 folder tanggal terbesar:")
    for k, v in by_day.most_common(10):
        print(f"  {v:5}  {k}")
    print("\nContoh pemindahan:")
    for old, new, src in to_move[:8]:
        print(f"  {os.path.relpath(old, root)}\n    -> {os.path.relpath(new, root)}  [tgl dari {src}]")

    planfile = os.path.join(root, f"{LOG_PREFIX}plan.tsv")
    with open(planfile, "w", newline="", encoding="utf-8", errors="surrogateescape") as f:
        w = csv.writer(f, delimiter="\t")
        for old, new, _ in plan:
            w.writerow([os.path.relpath(old, root), os.path.relpath(new, root)])
    print(f"\nRencana lengkap: {planfile}")

    if not a.apply:
        print("\nDRY-RUN: belum ada file yang dipindah. Tambah --apply untuk menjalankan.")
        return

    if input("\nKetik 'ya' untuk menjalankan: ").strip().lower() != "ya":
        sys.exit("Dibatalkan.")
    do_apply(root, plan)


if __name__ == "__main__":
    main()
