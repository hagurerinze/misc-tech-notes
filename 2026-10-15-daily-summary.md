# Daily Summary - 15 October 2026

Short notes about what I worked on and learned today.

---

## 1. scrcpy over WiFi (wireless)

- I forgot how to use scrcpy wirelessly, so I asked for a tutorial.
- I was listening to a Zoom meeting on my phone with TWS earbuds. Then I ran scrcpy.
- My question: does the sound go to the laptop, or does it stay on the phone?
- What I saw: I did not notice any change in the sound while scrcpy was running.

**Result:** TODO (add the final steps that worked and the answer about the audio)

---

## 2. UiPath (first look)

I did not know UiPath before today. This is what I learned.

- UiPath is an **RPA** tool (Robotic Process Automation). A software robot copies human steps on a computer: click, type, copy data, fill forms.
- Main parts:
  - **Studio**: where you build the automation.
  - **Robot**: runs the automation.
  - **Orchestrator**: controls and schedules many robots.
  - **Automation Cloud**: the cloud version.
- **Studio (desktop) only runs on Windows** and uses .NET. On a low-spec Windows PC it can be slow. Linux cannot run it. Wine or a VM is not a good idea, because UI automation (click and type) often fails.
- **Studio Web** runs in the browser, so Linux can use it. But it has fewer features, and UI automation on a local machine usually needs a Windows robot.
- Free ways to learn: **Community Edition** and **UiPath Academy**.
- How I see it: the idea is close to a shell script, cron, or a systemd timer. It is "make repeated work run by itself", but with a visual tool.

---

## 3. OS assignment: DOS internal and external commands

- Task: find out about internal and external DOS commands.
- I made one `.md` file with tables: 10 internal commands and 10 external commands.
- I also added: what DOS is, and a short comparison of DOS, Command Prompt, PowerShell, terminal, and BSD.

Things I fixed after checking facts:

- `ls` means **list**, and `cd` means **change directory**.
- DOS accepts both short and long names: `MD` = `MKDIR`, `RD` = `RMDIR`.
- IBM PC DOS is the version of MS-DOS that IBM sold with its own PCs.
- Windows 95, 98, and ME were built on top of DOS. Windows based on NT (2000, XP, and later) do not use DOS as the core.
- `cmd` and PowerShell are shells with a DOS-like style. They are not real DOS.
- The closest living thing to DOS is **FreeDOS** (free, MS-DOS compatible).
- **OpenBSD** feels close in the minimal CLI way, but it is Unix-like, not part of the DOS family.

The full file is `dos-internal-eksternal.md`. It has a source list at the end.
