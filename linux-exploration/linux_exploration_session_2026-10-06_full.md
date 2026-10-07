# Linux / System Exploration Session — Topics #1–#12

**Date:** 2026-10-06  
**Status:** Exploration / Draft Log

> This document consolidates the exploration topics discussed in the recent session.  
> Statuses distinguish between ideas that were selected as drafts, ideas already tested, and topics explicitly skipped.

---

# 1. Ext4 `commit=` and Sudden Power Loss

## Question

The user checked the filesystem mount options on Laptop 1 to see whether an explicit ext4 `commit=` value was configured.

Commands used:

```bash
findmnt -no SOURCE,FSTYPE,OPTIONS /
findmnt -no SOURCE,FSTYPE,OPTIONS /home
findmnt -t ext4 -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Relevant result:

```text
/dev/sda3 ext4 rw,noatime
/dev/sda4 ext4 rw,noatime
```

No explicit `commit=` option was present.

## Explanation

For ext4, the normal default journal commit interval is approximately **5 seconds**.

`commit=` controls how frequently filesystem journal transactions are committed.

Conceptually:

```text
commit lower
→ commits more frequently
→ potentially more write activity
→ smaller journal commit window

commit higher
→ commits less frequently
→ potentially less frequent journal activity
→ larger window of data that may not yet be committed
```

Important clarification:

`commit=5` does **not** mean that every file modification is physically written to disk exactly every five seconds. Linux page cache, writeback, application behavior, and `fsync()` semantics also matter.

## AC-only / Dead Battery Context

Laptop 1 has a dead battery, so sudden power loss is more relevant than on a laptop with a healthy battery.

A battery normally functions as a small UPS:

```text
AC power
   ↓
Laptop battery
   ↓
System
```

With a dead battery:

```text
AC power
   ↓
System
```

A sudden outage therefore removes the protection normally provided by the battery.

A UPS or battery replacement can reduce this risk.

## Decision

No need to change `commit=` merely because the laptop is AC-only.

Current:

```text
rw,noatime
```

is reasonable.

**Status: Information / no configuration change.**

---

# 2. XZ Archive / Security Research

## Question

The user considered learning how to “crack” or analyze an XZ archive.

The topic was reframed as a learning path rather than immediately attempting exploitation.

## Proposed Learning Stages

### Stage 1 — XZ Basics

- `xz`
- `unxz`
- `.xz`
- `.tar.xz`
- compression stream
- checksum
- archive structure

### Stage 2 — Binary Inspection

- magic bytes
- hex dump
- metadata
- deliberate corruption
- observing binary changes

### Stage 3 — Internals

- xz-utils
- liblzma
- source code
- tracing

### Stage 4 — Reverse Engineering

- ELF basics
- GDB
- symbols
- call stack
- memory

### Stage 5 — Security Research

- fuzzing
- crash reproduction
- ASan
- UBSan
- vulnerability analysis

### Stage 6 — XZ Utils Incident

Study the 2024 XZ Utils backdoor incident, including:

- CVE-2024-3094
- supply-chain attack
- build-time injection
- liblzma interaction with SSH
- public technical analyses

The goal does not have to reach exploitation. Understanding the mechanism is already a valid learning result.

## Decision

The user considered the topic too intimidating for now.

**Status: Draft / not started.**

---

# 3. WhatsApp AI Bot on Laptop 1

## Idea

Create a WhatsApp bot running locally on Debian Laptop 1.

Potential architecture:

```text
WhatsApp
   ↓
Baileys
   ↓
Node.js bot
   ├── commands
   ├── SQLite memory
   ├── Linux system information
   ├── media handling
   └── Gemini API
          ↓
       AI response
```

## Possible Features

- `!ping`
- `!help`
- `!uptime`
- `!sysinfo`
- AI chat
- per-chat memory
- SQLite storage
- media handling
- owner-only commands
- Linux system information
- systemd service

## Technology Considerations

Potential WhatsApp Web automation libraries include:

- Baileys
- whatsapp-web.js
- other WhatsApp Web automation projects

Baileys is attractive for the low-spec laptop because it does not require running a full Chromium browser like Puppeteer-based solutions.

The official WhatsApp Business Cloud API is a separate approach and is API/backend oriented rather than a local WhatsApp Web bot.

## Risk

Unofficial WhatsApp Web automation can carry account restriction risk. Spam/bulk messaging should be avoided.

## Decision

User explicitly marked this idea as interesting and wanted it locked for future development.

**Status: LOCKED DRAFT.**

No installation has been performed.

---

# 4. Inkscape

## Question

The user asked about “inkspace”, referring to **Inkscape**.

## Explanation

Inkscape is an open-source **vector graphics editor**.

Useful for:

- SVG
- logos
- icons
- diagrams
- QRIS layouts
- UI assets
- scalable graphics

Comparison:

```text
Inkscape
→ vector

GIMP
→ raster
```

Inkscape is therefore useful when the artwork needs to remain scalable without losing quality.

## Decision

User confirmed understanding.

**Status: Tool identified / no active project.**

---

# 5. Kuyhaa

## Question

The user asked about `kuyhaa.me`.

## Explanation

It is a third-party software/game download site associated with “full version”, repack, cracked software, activator, and similar unofficial distribution.

It is not an official software distributor.

## Decision

The site was identified as a third-party/cracked-software source.

**Status: Information only.**

---

# 6. Barrier / Synergy / Input Leap — Keyboard & Mouse Sharing

## Initial Question

The user encountered **Barrier** in a package/software manager and asked what it was.

## Core Concept

Barrier allows one physical keyboard and mouse to control multiple computers over a local network.

Example:

```text
Laptop 1
Keyboard + Mouse
      ↓
   Barrier Server
      ↓
     Wi-Fi/LAN
      ↓
Barrier Client
      ↓
Laptop 2
```

The target laptop does not need its own physical keyboard/mouse for normal operation.

## What Barrier Is Not

It is not a remote desktop solution.

It does not transmit the target computer's display.

It is software KVM-like functionality for:

```text
keyboard
mouse
```

not video switching.

## Hardware KVM Comparison

Physical KVM:

```text
Keyboard
Mouse
Monitor
   ↓
 KVM hardware
 ↙     ↓
PC 1   PC 2
```

Barrier:

```text
Keyboard
Mouse
   ↓
Laptop 1
   ↓
Network
   ↓
Laptop 2
```

Barrier therefore removes the need for dedicated KVM hardware for keyboard/mouse sharing, but it does not replace a video KVM.

## Network

The machines only need to communicate on the same LAN.

Internet is not required.

A laptop hotspot can potentially be used as the local network.

## Synergy

Historical relationship:

```text
Synergy 1.x
     ↓
 Barrier fork
```

Synergy is the older project/technology from which Barrier originated.

## Android / Termux

Android is more complicated because Android has strong input and sandbox restrictions.

Running Barrier inside Debian under Termux/proot does **not automatically give it access to Android's system-wide keyboard/mouse input**.

Therefore Android support was not assumed.

## Input Leap

Input Leap was discussed as another continuation/fork in the same general category.

Its core purpose is still:

> Share one keyboard and mouse across multiple computers.

Potential target systems include:

- Debian/Linux
- Windows
- BSD systems

Android remained uncertain.

## Decision

User explicitly wanted this idea locked as a draft.

**Status: LOCKED DRAFT.**

Potential future exploration:

```text
Laptop 1
Debian
   ↓
keyboard + mouse
   ↓
Wi-Fi
   ↓
Debian / FreeBSD / Windows
```

No installation performed.

---

# 7. Game Assets → Custom Cursor

## Clarification

The user initially mentioned “mouse osu dan holocure”, referring to **mouse/cursor assets**, not physical mouse hardware.

## Relevant Formats

```text
.cur
→ Windows static cursor

.ani
→ Windows animated cursor

.ico
→ icon, not directly a cursor

.png / .svg
→ source artwork that can be converted into cursor assets
```

Linux/X11 uses the **Xcursor** format and cursor themes.

## Possible Workflow

```text
Game asset
   ↓
Clean background
   ↓
Resize
   ↓
Choose hotspot
   ↓
Windows .cur
   ↓
Windows .ani (optional)
   ↓
Linux Xcursor
   ↓
Cursor theme
   ↓
XFCE test
```

The **hotspot** is particularly important because it determines the actual click point of the cursor.

## Decision

User understood the concept.

**Status: Draft idea / not executed.**

---

# 8. XFCE Wayland Session vs Actual Xorg Usage

## Question

Could enabling/creating an XFCE Wayland session increase RAM on the next boot even if the user continues to boot into Xorg?

## Explanation

Simply having a Wayland session installed does not mean Wayland is running.

If the login session remains:

```text
LightDM
  ↓
Xorg
  ↓
XFCE
```

then a separate Wayland session should not consume RAM merely because its files/session entry exist.

RAM usage matters when actual processes/services are launched.

Potential checks:

```bash
free -h
```

```bash
ps -eo rss,comm --sort=-rss | head -20
```

```bash
systemd-analyze --no-pager
```

## Decision

The laptop was not available at the time, so no changes were performed.

The topic was kept as a draft/check for later.

**Status: Draft / no configuration change.**

---

# 9. `swww` / Static Wallpaper Fade Transition on X11

## Question

Could `swww` provide a wallpaper fade-in/fade-out effect similar to Windows?

## Explanation

Yes, conceptually, but `swww` is a **Wayland wallpaper daemon**.

It is useful for:

- static wallpapers
- wallpaper transitions
- fade effects
- Wayland-native wallpaper management

It is not a direct X11 solution.

## Current Laptop 1 Setup

```text
X11
 └── xwinwrap
      └── mpv
           └── VA-API
```

This existing stack is better suited to video/live wallpaper.

## User's Actual Goal

The user wants:

```text
Wallpaper A
    ↓
 fade out
    ↓
 transition
    ↓
 fade in
    ↓
Wallpaper B
```

while both wallpapers remain static images.

The interesting experiment is therefore not necessarily installing `swww`, but finding a way to achieve a similar effect on X11.

Potential direction:

- use `mpv`
- possibly retain `xwinwrap`
- transition between static images
- measure CPU/RAM

## Decision

**Selected as Draft #9.**

`swww` itself is not the current X11 solution.

---

# 10. antiX and Lightweight Ricing

## Question

Why can antiX look similar to XFCE while using significantly less RAM?

## Core Explanation

Visual appearance does not reveal the entire desktop architecture.

antiX commonly uses lightweight components such as **IceWM** rather than a complete XFCE desktop stack.

Conceptually:

```text
XFCE
├── xfwm4
├── xfce4-panel
├── xfdesktop
├── xfsettingsd
├── xfce4-session
├── Thunar
└── other integration
```

A lightweight antiX environment may instead use:

```text
IceWM
+ lightweight panel
+ menu
+ utilities
+ required daemons
```

Themes, icons, panels, menus, and window decorations can make the final UI look similar.

Therefore:

> Similar appearance does not imply similar resource usage.

## Init System

antiX uses **sysVinit by default**, rather than systemd.

This is part of its lightweight/minimal design, but it is incorrect to say that the low RAM usage comes only from not using systemd.

The overall desktop architecture matters more.

## Trade-offs

Advantages:

- very low RAM usage
- good for weak hardware
- low background overhead
- highly customizable

Trade-offs:

- less desktop integration
- more manual configuration
- fewer modern GUI conveniences
- less focus on Wayland
- some software/tutorials assume systemd
- installing many modern desktop components can eliminate some of the resource advantage

## Ricing

User became interested in the possibility of ricing antiX.

Potential stack:

```text
antiX
├── IceWM
│   └── custom theme
├── GTK theme
├── icon theme
├── cursor theme
├── panel
├── Conky
└── wallpaper
```

This could produce a heavily customized desktop while retaining a lightweight base.

## Decision

**Selected as Draft #10.**

No installation yet.

Reason for postponement:

- Laptop 3 is currently at home/unavailable.
- User does not currently have an external HDD for safe experimentation.

---

# 11. Foot vs Alacritty vs XFCE Terminal

## Question

What are Foot and Alacritty?

Both are **terminal emulators**.

They are not shells.

Architecture:

```text
Terminal emulator
       ↓
      Shell
       ↓
    Commands
```

For example:

```text
Alacritty
   └── bash
        ├── ls
        ├── sudo
        └── apt
```

## Foot

Foot is a lightweight terminal emulator focused primarily on **Wayland**.

Characteristics:

- lightweight
- fast
- native Wayland
- simple configuration
- suited to minimal Wayland environments

## Alacritty

Alacritty is a performance-oriented terminal emulator with GPU rendering.

Characteristics:

- fast rendering
- responsive input/output
- GPU acceleration
- cross-platform
- works on X11 and Wayland

## Direct XFCE Test

Because the user was currently using XFCE, Alacritty was tested directly without changing desktop/session.

RAM/CPU check:

```bash
ps -C alacritty -o pid,%cpu,%mem,rss,cmd
```

Result:

```text
PID    %CPU   %MEM   RSS       CMD
14779  2.5    5.5    102920    alacritty
```

XFCE Terminal:

```bash
ps -C xfce4-terminal -o pid,%cpu,%mem,rss,cmd
```

Result:

```text
PID    %CPU   %MEM   RSS       CMD
14454  0.8    1.9    36516     xfce4-terminal
```

Approximate RSS:

```text
Alacritty       ≈ 100.5 MiB
XFCE Terminal   ≈ 35.7 MiB
```

## Performance Test

The user also directly tested terminal responsiveness/speed.

Result:

> Alacritty felt faster.

This exposed a useful trade-off:

```text
XFCE Terminal
→ lower RAM in this test
→ slower-feeling performance

Alacritty
→ higher RAM in this test
→ faster-feeling performance
```

Therefore:

> Faster does not automatically mean lighter.

and:

> Lower RAM usage does not automatically mean faster.

## Shortcut / UX

The user noticed that:

```text
Ctrl + Shift + A
```

did not behave as expected for select-all.

This illustrates that terminal emulators can have different shortcut/selection behavior.

## Decision

Alacritty was **successfully tested**, but it was not selected as a permanent replacement for XFCE Terminal.

**Status: Experiment completed / no permanent switch.**

### Draft #11

Continue to compare:

- RAM
- CPU
- startup
- responsiveness
- rendering
- usability
- number of simultaneously open terminals

---

# 12. LeetCode

## Question

What is LeetCode?

LeetCode is a programming problem-solving platform focused heavily on algorithms and data structures.

Typical topics:

- arrays
- strings
- hash tables
- stacks
- queues
- linked lists
- trees
- graphs
- sorting
- binary search
- dynamic programming
- greedy algorithms

Typical progression:

```text
Easy
Medium
Hard
```

## User Direction

The user clarified that they are **not aiming toward competitive programming**.

Therefore LeetCode is not a priority.

The user's more relevant direction is practical technical work:

```text
Linux
├── Debian
├── system administration
├── troubleshooting
├── networking
├── Bash / scripting
├── Git / GitHub
├── Linux internals
├── services
├── BSD
└── practical projects
```

LeetCode may still be useful occasionally for programming logic, but it does not need to become a major roadmap item.

## Decision

**SKIP.**

No active draft.

---

# Final Decision Table

| # | Topic | Decision | Status |
|---|---|---|---|
| 1 | Ext4 `commit=` / sudden power loss | Understand, no change | Information |
| 2 | XZ archive/security research | Interesting but intimidating for now | Draft |
| 3 | WhatsApp AI bot | Explicitly selected | **Locked Draft** |
| 4 | Inkscape | Tool identified | Information |
| 5 | Kuyhaa | Identified as third-party/cracked distribution | Information |
| 6 | Barrier / Input Leap | Explicitly selected | **Locked Draft** |
| 7 | Game asset → custom cursor | Interesting | Draft |
| 8 | XFCE Wayland session / RAM | Deferred until laptop available | Draft |
| 9 | Static wallpaper fade on X11 | Selected | Draft |
| 10 | antiX + lightweight ricing | Selected, postponed | Draft |
| 11 | Foot / Alacritty | Alacritty tested | Experiment completed |
| 12 | LeetCode | Not aligned with current direction | **Skip** |

---

# Locked Drafts

These were explicitly requested to be saved as future ideas.

## Locked Draft A — WhatsApp AI Bot

```text
Debian Laptop 1
    ↓
Baileys / Node.js
    ↓
WhatsApp bot
    ├── commands
    ├── Gemini API
    ├── SQLite
    ├── Linux system info
    ├── media
    └── systemd
```

Status: **Locked / future project**

## Locked Draft B — Multi-Computer Keyboard & Mouse Sharing

Potential tools:

- Barrier
- Input Leap
- related KVM-over-LAN software

Potential environment:

```text
Debian
FreeBSD
Windows
```

Network:

```text
Wi-Fi / LAN
```

Goal:

> One keyboard and mouse controlling multiple computers without physical KVM hardware.

Android/Termux support remains uncertain and is not assumed.

Status: **Locked / future exploration**

---

# Overall Conclusions From the Session

## 1. Lightweight does not mean one-dimensional

A system can be:

```text
low RAM
```

without necessarily being:

```text
fastest
most convenient
most feature-rich
```

antiX and Alacritty provided two different examples of this principle.

## 2. Appearance can hide architecture

antiX can be made to look similar to XFCE while using a different and much smaller desktop stack.

Therefore:

```text
What the user sees
        ≠
What the system is running
```

## 3. Measure the specific resource you care about

Alacritty showed:

```text
Performance ↑
RAM ↑
```

while XFCE Terminal showed:

```text
RAM ↓
Performance ↓ (subjectively in the user's test)
```

Therefore, “lightweight” should be evaluated using multiple dimensions.

## 4. Drafting before installation is intentional

Several ideas remain drafts because immediate experimentation is unnecessary or unsafe without the appropriate hardware/storage.

Especially:

```text
antiX
```

will wait until Laptop 3 is available and safe experimentation is practical.

## 5. Practical Linux work remains the main direction

LeetCode was skipped because the user's current direction is not competitive programming.

The more relevant path remains:

```text
Linux
System Administration
Troubleshooting
Networking
Scripting
Git/GitHub
Linux Internals
BSD
Practical Projects
```

---

# Current State After This Session

```text
INFORMATION / UNDERSTOOD
├── ext4 commit=
├── Inkscape
└── Kuyhaa

DRAFT
├── XZ security research
├── Game asset → custom cursor
├── XFCE Wayland session investigation
├── Static wallpaper fade on X11
└── antiX lightweight ricing

LOCKED DRAFT
├── WhatsApp AI bot
└── Barrier / Input Leap multi-computer control

TESTED
└── Alacritty vs XFCE Terminal

SKIPPED
└── LeetCode
```

No major system configuration was changed as a result of this exploration session.
