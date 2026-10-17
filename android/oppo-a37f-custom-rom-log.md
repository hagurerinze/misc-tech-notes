# Oppo A37f Custom ROM Project — Checkpoint Log

> ⚠️ **Don't try this on your main phone if you don't have another device yet.**
> This process involves unlocking the bootloader, editing raw partitions over EDL, flashing an unofficial recovery, and flashing an unofficial ROM. Every step carries real risk of a bricked or unusable phone. Have a backup phone before attempting this on a device you depend on.

## Device info
- **Phone:** Oppo A37f
- **Chipset:** Qualcomm MSM8916 (Snapdragon 410), 32-bit software stack
- **Stock firmware at start:** A37fEX_11_190711 (A.38, July 2019) — newer than most guides assume, which likely explains earlier failed EDL attempts before this log begins
- **RAM:** low-spec (2GB class device)
- **Hardware quirk:** no working physical volume buttons; power button works but only with a hard press. This absence of buttons became the single biggest source of trouble throughout the project.

## Goal
Move off stock Android 5.1.1 onto a custom ROM (LineageOS, targeting Android 10 as the "sweet spot" for this hardware) via EDL + TWRP, while keeping the IMEI intact.

## Tools used
- **bkerler's `edl` tool**, installed on a Debian 13 (trixie) laptop in a Python venv (`~/edlenv`)
- ModemManager removed, udev rules installed for the device
- Working directories: `~/a37` (ROM/TWRP files), `~/a37/backup` (partition dumps)

---

## Step 1 — Full partition backup (before touching anything)

With the phone in EDL mode, dumped every partition except `system`, `userdata`, and `cache` (skipped because backing those up wasn't needed and would have taken much longer):

```
edl printgpt
edl rl . --skip=system,userdata,cache --genxml
```

This produced backups including `modemst1.bin`, `modemst2.bin`, `fsg.bin`, `fsc.bin`, `persist.bin`, `devinfo.bin`, `boot.bin`, `recovery.bin`, `misc.bin`, `oppodycnvbk.bin`, `oppostanvbk.bin`, and a `rawprogram0.xml`. Verified every file size against the partition table and checksummed the folder. This backup turned out to be essential later.

**IMEI was also written down and photographed beforehand as an extra reference point** (though the real safety net was the modemst1/modemst2 backup, not the photo).

## Step 2 — Bootloader unlock via devinfo patch

The phone reported itself as MSM8916, "possibly unfused," meaning any EDL loader works without needing a device-specific firehose file — this simplified things a lot compared to what older guides assumed.

Patched `devinfo.bin` by setting the bytes at offsets `0x10` and `0x18` to `0xFF` (this is the known unlock flag pattern for this chip generation), verified the patch with `cmp -l`, then wrote it back:

```
edl w devinfo devinfo_patched.bin
edl r devinfo devinfo_check.bin
cmp devinfo_patched.bin devinfo_check.bin && echo MATCH
edl reset
```

Phone booted back into stock Android 5.1.1 normally. No visible confirmation the bootloader was unlocked at this point — the real test was whether TWRP would boot later.

**Note on entering EDL:** the phone has no working volume buttons, so the standard "power off + hold vol up+down + plug in USB" method couldn't be used after this point (it *was* used once, successfully, for the very first backup, before this was fully realized). From here on, `adb reboot edl` became the primary way into EDL — but only works while adb has a live connection, i.e., while booted into TWRP or a working Android with debugging on.

## Step 3 — Flashing TWRP

Downloaded Meghthedev's TWRP 3.7.0_9-0 build for the A37f (`twrp_A37_3.7.img`, ~25MB, fits the 32MB recovery partition). Verified it was a valid Android bootimg before flashing.

**The "boot straight to recovery" problem:** since the phone has no buttons, there's no way to interrupt a normal boot to jump into recovery. The fix used was patching the **misc** partition with the Android bootloader control block (BCB) flag `boot-recovery`, so the phone would go straight to TWRP on the next boot instead of booting Android (which might have overwritten TWRP with stock recovery).

```
# recovery + misc flag written and verified in one gated command:
edl w recovery ../twrp_A37_3.7.img && \
edl r recovery recovery_check.bin && \
cmp -n 25214976 ../twrp_A37_3.7.img recovery_check.bin && \
edl w misc misc_bcb.bin && \
edl r misc misc_check.bin && \
cmp misc_bcb.bin misc_check.bin && \
echo BOTH_MATCH && edl reset
```

This worked — phone booted straight into TWRP, confirming **the bootloader unlock had succeeded.**

**adb showed the phone as `recovery`**, and the misc flag was automatically cleared by TWRP on boot (verified as all-zero afterward), meaning a normal reboot from here would go to system, not loop back to TWRP.

## ⚠️ Mistake #1 — `adb reboot edl` used from inside TWRP

While trying to make a stock system partition backup for extra safety, `adb reboot edl` was run **from within TWRP**, under the wrong assumption that TWRP supported this. It didn't — the phone just rebooted normally into stock Android, **which overwrote the custom TWRP recovery with the stock one** (confirmed via a failed `cmp` check afterward, byte mismatch at byte 9).

**Lesson:** `adb reboot edl` is an Android/TWRP-userspace command that depends on what's booted; it is *not* a hardware-level trigger. Don't assume it works from every context.

## ⚠️ Mistake #2 — a gated command chain wasn't actually gated

The recovery command that follows immediately after this failure was written as separate lines instead of one `&&`-chained command, so `edl reset` executed even though the `cmp` check for TWRP had already failed. This meant a reset was triggered on the wrong recovery image without the intended safety gate stopping it.

**Lesson:** when chaining verify-then-act steps, use `&&` throughout, not just visually group commands — a partial paste/partial failure can still let the final destructive step run.

**Recovery from these two mistakes:** TWRP + the misc flag were rewritten with a fully gated `&&` chain, and this time it worked, landing back in TWRP successfully with `BOTH_MATCH` confirmed for both the recovery and misc writes.

## Step 4 — First ROM flash: Tipz build (LineageOS 17.1, 20210810)

Downloaded `lineage-17.1-20210810-UNOFFICIAL-A37.zip` (~438MB) from SourceForge (Tipz builds). Verified:
- SHA1/MD5 matched SourceForge's listed checksums
- `unzip -t` showed no archive errors
- `updater-script` asserted device names A37/A37f/A37fw/A37fs — phone reported as `A37f`, a match
- `updater-script` also asserted a specific trustzone version (`TZ.BF.3.0.C3.1-00006`) — checked against the backed-up `tz.bin`/`tzbak.bin` partitions and it matched, so the flash wasn't blocked

Did a Factory Reset in TWRP (not Format Data), pushed the zip via `adb push`, verified size and SHA1 on-device, and installed. **Install completed successfully with no errors.**

### Problems after boot
- A "Bluetooth keeps stopping" crash loop appeared repeatedly
- The **launcher was badly broken**: no working Home/Recents button function (physical presses gave vibration feedback but did nothing), no lock screen by default, notification shade wouldn't pull down
- These symptoms together pointed to Android's first-time setup wizard never completing, which blocks the status bar/quick settings until done — though this was never confirmed for certain

### ⚠️ Mistake #3 — assuming `adb reboot edl` / a black screen meant something it didn't
When troubleshooting, `adb reboot edl` was tried again from what was actually a booted (broken) Android session, wrongly assumed to be harmless ("nothing changes"). This was another instance of not accounting for context-dependent commands. It also cost time diagnosing what was actually a UI/launcher crash as if it were a full black-screen/bootloop issue, before the real symptoms (physical buttons vibrating with no action, no lock screen, no notification shade) were fully described.

**Lesson:** describe *all* observed symptoms up front (especially anything involving physical buttons or vibration feedback) — partial descriptions led to several rounds of wrong hypotheses.

### The real blocker: no way back in
This ROM turned out to have a **broken USB driver while booted** — the phone could only charge while powered off, never while the OS was running, and `adb devices` never showed the phone at all while booted into this ROM, no matter what was tried:
- Settings → Developer options → Build number tap: **the button did nothing, no toast, even after 7+ taps** (confirmed broken, not just hidden)
- Direct activity launching via a sideloaded **Activity Launcher** app: failed with "unable to find activity" — the ROM blocks direct activity launches for restricted screens
- **Termux** shell commands (`settings put global adb_enabled 1`, `input tap`, even direct binary paths like `/system/bin/input`): all failed with permission denied — a regular app without shell/system privileges can't do this even from on-device
- A USB OTG mouse *did* work for navigation (confirming touch/USB-peripheral input worked even though data/adb over the PC-facing USB port did not) and got as far as installing Lawnchair as a working launcher, but couldn't get any further since Settings itself was too broken

**Conclusion:** this specific ROM build had USB broken at the kernel/driver level while booted — a problem no on-device software workaround could fix, since every workaround (Settings toggle, Activity Launcher, Termux) ultimately depends on either a working USB/adb link or elevated permissions the phone was withholding.

## Current status / next step: the EDL "deep-flash" cable

Since the phone has:
- No working volume buttons
- A power-button menu with only Power off / Restart / Emergency (no recovery/download mode option)
- A broken USB driver while booted (so `adb reboot edl` has nothing to talk to)

...the only remaining way back into EDL is a **hardware-level trigger that doesn't depend on Android at all**: shorting the D+ (green) and GND (black) wires on a USB cable while the phone is fully powered off. This works because it's read by the Qualcomm chip's bootrom before any software (including a broken ROM) ever loads.

### Cable prep instructions (for the next session)
1. Cut a spare micro-USB cable ~1–2 inches from the micro-USB end.
2. Strip the outer jacket to expose the 4 inner wires (red/VCC, white/D-, green/D+, black/GND).
3. Strip a small bit of insulation off just the green and black wires.
4. Twist green and black together (one single joint — not two connections), tape it so it can't touch red or white.
5. Leave red and white completely disconnected from everything.
6. Power the phone off completely, plug the modified end into the phone, the normal end into the laptop.
7. Run `lsusb | grep -i qualcomm` — look for the `05c6:9008` device.
8. If it appears, from `~/a37/backup`:
   ```
   edl w recovery ../twrp_A37_3.7.img && \
   edl r recovery recovery_check.bin && \
   cmp -n 25214976 ../twrp_A37_3.7.img recovery_check.bin && \
   edl w misc misc_bcb.bin && \
   edl r misc misc_check.bin && \
   cmp misc_bcb.bin misc_check.bin && \
   echo BOTH_MATCH && edl reset
   ```
   (Note the `&&` chaining this time — learned from Mistake #2.)

### Planned next ROM attempt
Instead of the Tipz build, try **DeepakChaurasia's LineageOS 17.1 (20220328, `_gms_go` build)**, whose own bring-up thread lists calling, Wi-Fi, camera, Bluetooth, audio, and VoLTE as confirmed working — the only build found so far with a stated "what works" list rather than silence or a bug list. It also bundles GApps Go, which is a bonus rather than a requirement.

Link (unverified beyond checksums to be run when downloaded):
`https://yassu.supersaiyan.workers.dev/0:/download/lineage-17.1-20220328-UNOFFICIAL-A37_gms_go.zip`

Before flashing it, repeat the same verification steps as before: size, checksum, `unzip -t`, and read the `updater-script` for device-name and trustzone asserts.

## Standing facts to remember
- **IMEI has been confirmed intact** after the bootloader unlock and after the first ROM flash — the modemst1/modemst2/fsg/persist backup strategy has worked as intended.
- **Full raw backup lives in `~/a37/backup`** on the Debian laptop — includes everything needed to restore stock partitions (except `system`/`userdata`/`cache`, which weren't backed up).
- **TWRP write + misc flag write must always be done as one `&&`-chained command**, never as separate/sequential commands, to avoid Mistake #2 happening again.
- **Never assume `adb reboot edl` works** — it only works if adb already has a live, authorized connection to a booted (working) system.
- **This specific hardware (no buttons) removes the two easiest recovery paths** (button combo, power-menu recovery option) that most guides assume are available — every step of this project had to route around that.
