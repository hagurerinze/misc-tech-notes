# Organizing My Videos Folder

Date: 22 October 2026

## Goal

My videos folder was sorted by month only (`2022-04` to `2026-03`). The month `2025-12` was split into `part1`, `part2` and `part3`. I wanted a cleaner layout.

My rules:

- Group by file type first (Mp4, Mkv, Webm, 3gp, ...).
- Then Year, Month, Day.
- If one day folder has more than 500 files, split it into `YYYY-MM-DD-Part1`, `Part2`, and so on.
- If two files have the same name, add a suffix. No file is lost or overwritten.

## Result layout

```
Videos/
├── Mp4/2025/12/2025-12-24-Part1/...
├── Mkv/2025/10/2025-10-12/...
├── Webm/...
├── 3gp/...
└── videos.txt        (stays in the root folder)
```

## The script: `organize_videos.py`

- Default mode is **dry-run**. It only shows the plan and moves nothing.
- `--apply` runs the move. You must type `ya` (yes) to confirm.
- `--undo LOG` moves files back using a log file.
- Same names get `_1`, `_2` before the extension, for example `Unnamed (1)_1.mp4`.
- A folder with more than 500 files is split evenly. 501 files become 251 + 250.
- Every move is saved in `_organize_log_*.tsv`. The full plan is saved in `_organize_plan.tsv`.
- The script skips itself and `.py`, `.txt`, `.md`, `.tsv`, `.sh`, `.log` files.

### How the date is chosen

1. If the file name has a date (`VID-20260125-WA...`, `VID_20251127_...`), use it.
2. If not, use the **modified time (mtime)**.

The date in the name is used first because it is the real record or send date. The modified time can change when a file is copied.

## Dry-run result

- 1105 files in total. This included 1 `.py` and 1 `.txt` file, which the fixed script now skips.
- Date from file name: 37. Date from mtime: 1068.
- Same names: 0.
- Split: **Mp4 on 2025-12-24 had 964 files, so it became 2 parts (482 + 482)**.

## Modified time vs created time

I checked with `stat`:

| File | Modify | Birth (created) |
|---|---|---|
| `Unnamed (1).3GP` | 2025-12-24 01:49:54 | 2026-02-22 03:25:24 |
| 500 files in `2025-12_part1` | 488 on 2025-12-24, the rest in December | all on 2026-02-22 |

What I learned:

- **Created time is not useful.** It is only the day the files were copied to this disk.
- **Modified time is better.** It stays from the original source, and the month matches my old folder name (2025-12).
- Many files are on one day (2025-12-24), so that day got `Part1` and `Part2`.
- File permission is `0755`. It probably comes from exFAT or NTFS. It is not dangerous. To fix it: `find . -type f -exec chmod 644 {} +`.

## Check before `--apply`

This shows files whose month would change compared to the old folder. It should be empty:

```bash
cd ~/Public/Organized/Videos
awk -F'\t' '{split($1,a,"/"); split($2,b,"/"); if (substr(a[1],1,7) != b[2]"-"b[3]) print $1 "  ->  " $2}' _organize_plan.tsv | head -20
```

## Commands

```bash
python3 organize_videos.py ~/Public/Organized/Videos              # dry-run
python3 organize_videos.py ~/Public/Organized/Videos --apply      # run it
python3 organize_videos.py ~/Public/Organized/Videos --undo ~/Public/Organized/Videos/_organize_log_XXXX.tsv
```

## What I saved as backup

- The tree before I ran the script (the old layout).
- The old `organize_videos.py` (before the edit).
- The new `organize_videos.py` (after the edit).
- The log after `--apply`.
- The plan log.

## Important notes

- The log saves the **file name at the time of the move**. After my own rename, `--undo` can only restore files that still have the same name. Renamed files are skipped. The rename was my own choice.
- Lesson: **save the tree and the log before you reorganize a folder**, so the old layout is never forgotten again.
