# Windows 10 WSL Debian Ghost Cleanup

## Device / situation

This was the Dell laptop that had previously been used to test WSL
installation.

The WSL installation attempt failed because the Windows installation was
Ghost Spectre.

The goal was to undo the failed WSL/Debian installation and remove all
remaining leftovers, especially a Debian entry that still appeared in
the normal Windows 10 Start Menu and Search.

Windows version checked:

```powershell
Get-ComputerInfo | Select-Object WindowsProductName,WindowsVersion,OsBuildNumber
```

Output:

```text
WindowsProductName WindowsVersion OsBuildNumber
------------------ -------------- -------------
Windows 10 Pro     2009           19045
```

## Initial WSL state

The following commands showed that WSL itself was not active:

```powershell
wsl --status
wsl --version
wsl --list --verbose
wsl --list --all --verbose
```

`wsl.exe` existed:

```text
C:\Windows\system32\wsl.exe
```

The WSL optional features were checked:

```powershell
@("Microsoft-Windows-Subsystem-Linux","VirtualMachinePlatform") | ForEach-Object { Get-WindowsOptionalFeature -Online -FeatureName $_ | Select FeatureName,State }
```

Result:

```text
Microsoft-Windows-Subsystem-Linux Disabled
VirtualMachinePlatform Disabled
```

So both relevant Windows optional features were already disabled.

## Debian AppX check

The AppX package check returned no Debian package:

```powershell
Get-AppxPackage -AllUsers | Where-Object Name -match 'WindowsSubsystemForLinux|TheDebianProject.Debian' | Select Name,Version,PackageFullName
```

No output.

The WSL registry location was also empty:

```powershell
Get-ChildItem "HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss" -ErrorAction SilentlyContinue | Select PSChildName
```

No output.

## Debian leftover folders

A search found these folders under the user package directory:

```text
C:\Users\Administrator\AppData\Local\Packages\MicrosoftCorporationII.WindowsSubsystemForLinux_8wekyb3d8bbwe

C:\Users\Administrator\AppData\Local\Packages\TheDebianProject.DebianGNULinux_76v4gfsz19hv4
```

The Debian package directory was only about 0.01 MB and contained only
the normal package directory structure:

```text
AC
AppData
LocalCache
LocalState
RoamingState
Settings
SystemAppData
TempState
```

The Debian leftover was removed:

```powershell
Remove-Item "$env:LOCALAPPDATA\Packages\TheDebianProject.DebianGNULinux_76v4gfsz19hv4" -Recurse -Force
```

Afterward only the WSL package directory remained:

```text
MicrosoftCorporationII.WindowsSubsystemForLinux_8wekyb3d8bbwe
```

That WSL directory was also only about 0.01 MB.

## Start Menu investigation

The Debian entry was still visible in the normal Windows Start Menu.

Important observation:

-   Debian appeared in the normal Windows Start Menu and Search.
-   Debian did not appear in the StartIsBack search.
-   Normal clicking the Debian entry did nothing.
-   `Uninstall` / `App settings` also did not actually remove it.
-   File Manager search for Debian returned zero results.
-   Start Menu shortcut searches returned zero results.

Start Menu shortcut locations were checked:

```powershell
Get-ChildItem "$env:APPDATA\Microsoft\Windows\Start Menu\Programs","$env:ProgramData\Microsoft\Windows\Start Menu\Programs" -Recurse -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -match 'Debian|WSL' } | Select FullName
```

No output.

Explorer was restarted:

```powershell
Stop-Process -Name explorer -Force
Start-Process explorer.exe
```

The Debian entry remained.

## StartIsBack check

Because StartIsBack was installed, its cache was checked:

```powershell
$p="$env:LOCALAPPDATA\StartIsBack\Cache"
Get-ChildItem $p -Force -ErrorAction SilentlyContinue | Select Name,Length,LastWriteTime
```

Cache files included:

```text
appsfolder.dat
pcsettingspages.dat
pcsettingssearch.dat
```

The `appsfolder.dat` file was checked for Debian:

```powershell
$p="$env:LOCALAPPDATA\StartIsBack\Cache\appsfolder.dat"
if (Test-Path $p) {
    $b=[IO.File]::ReadAllBytes($p)
    $s=[Text.Encoding]::Unicode.GetString($b)
    if ($s -match 'Debian|TheDebianProject') {
        "Debian found in StartIsBack cache"
    } else {
        "Debian not found in cache"
    }
}
```

Result:

```text
Debian not found in cache
```

The StartIsBack cache was cleared, but the Debian ghost remained.

This helped establish that StartIsBack was not the source of the ghost
entry.

## System-wide vs per-user test

A temporary Windows user was created:

```powershell
net user WSLTestTemp "TempTest123!" /add
```

Adding it to `Users` returned:

```text
System error 1378 has occurred.

The specified account name is already a member of the group.
```

This was not a problem; it simply meant the account was already in the
group.

The temporary user was used to test the Start Menu.

Result:

```text
WSLTestTemp: Debian did NOT appear
Administrator: Debian DID appear
```

This was the key result.

It proved that the ghost entry was specific to the `Administrator` user
profile and was not a system-wide Debian installation.

The temporary account was later deleted:

```powershell
net user WSLTestTemp /delete
```

Result:

```text
The command completed successfully.
```

## Registry checks

Several possible locations were checked and all returned zero matches.

AppX repository:

```powershell
reg query "HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppModel\Repository\Packages" /s /f "TheDebianProject" 2>$null
reg query "HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppModel\Repository\Packages" /s /f "DebianGNULinux" 2>$null
reg query "HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppModel\Repository\Packages" /s /f "Debian" 2>$null
```

All:

```text
End of search: 0 match(es) found.
```

Other registry locations:

```powershell
reg query "HKCU\Software\Classes\Applications" /s /f "Debian" 2>$null
reg query "HKCU\Software\Classes\ActivatableClasses" /s /f "Debian" 2>$null
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist" /s /f "Debian" 2>$null
```

All:

```text
End of search: 0 match(es) found.
```

`Get-StartApps` was also checked:

```powershell
Get-StartApps | Where-Object {$_.Name -like '*Debian*'}
```

No output.

AppX checks also returned no Debian:

```powershell
Get-AppxPackage -Name '*Debian*' -ErrorAction SilentlyContinue
Get-AppxPackage -AllUsers -Name '*Debian*' -ErrorAction SilentlyContinue
```

No output.

## Shell and CloudStore investigation

The following per-user Windows folders existed:

```text
CloudStore
PowerShell
Shell
```

CloudStore was searched for Debian-related strings, with no output.

The Shell folder contained only:

```text
DefaultLayouts.xml
LayoutModification.json
LayoutModification.xml
```

A backup was made before further investigation:

```powershell
$stamp=Get-Date -Format yyyyMMdd-HHmmss
$b="$env:USERPROFILE\Desktop\ShellBackup-$stamp"
New-Item $b -ItemType Directory -Force | Out-Null
Copy-Item "$env:LOCALAPPDATA\Microsoft\Windows\Shell" "$b\Shell" -Recurse -Force -ErrorAction SilentlyContinue
Copy-Item "$env:LOCALAPPDATA\Microsoft\Windows\CloudStore" "$b\CloudStore" -Recurse -Force -ErrorAction SilentlyContinue
```

Backup created:

```text
C:\Users\Administrator\Desktop\ShellBackup-20260903-051629
```

No Shell or CloudStore files were deleted.

## Start Menu package investigation

The following per-user packages were found:

```text
Microsoft.Windows.Search_cw5n1h2txyewy
Microsoft.Windows.ShellExperienceHost_cw5n1h2txyewy
Microsoft.Windows.StartMenuExperienceHost_cw5n1h2txyewy
```

A recursive listing showed that `StartMenuExperienceHost` had a
`TempState` directory with a timestamp around the time of the old Debian
installation.

The directory contents were:

```text
StartUnifiedTileModelCache.dat
TileCache_100_3_PNGEncoded_Data.bin
TileCache_100_3_PNGEncoded_Header.bin
```

Important timestamps:

```text
StartUnifiedTileModelCache.dat
8/3/2026 3:58:25 PM
```

The TileCache files had older timestamps:

```text
5/5/2026 4:38:37 PM
```

The timestamp of `StartUnifiedTileModelCache.dat` closely matched the
timestamp of the old Debian leftover package state.

## Final fix

Only the stale Start Menu model cache was removed.

First the Start Menu process was stopped, then the cache file was
deleted:

```powershell
Stop-Process -Name StartMenuExperienceHost -Force -ErrorAction SilentlyContinue
Remove-Item "$env:LOCALAPPDATA\Packages\Microsoft.Windows.StartMenuExperienceHost_cw5n1h2txyewy\TempState\StartUnifiedTileModelCache.dat" -Force
Start-Process explorer.exe
```

There was an earlier accidental double-paste that produced an invalid
command such as:

```text
Start-Process explorer.exeStop-Process -Name ...
```

PowerShell rejected it with a parsing/parameter error. It did not
perform an unintended destructive operation.

The correct command was then run successfully.

## Result

After deleting:

```text
StartUnifiedTileModelCache.dat
```

the ghost Debian entry disappeared from the Start Menu.

Therefore the final diagnosis was:

```text
WSL installation              -> already disabled/removed
Debian AppX                   -> removed
Debian filesystem             -> removed
Debian shortcuts              -> none
WSL registry                  -> none
AppX repository               -> none
StartIsBack cache             -> not the source
CloudStore                    -> not the source
Get-StartApps                 -> no Debian
Temporary clean user          -> no Debian
StartMenuExperienceHost cache -> stale Debian ghost
```

The remaining Debian entry was a stale Windows 10 Start Menu cache entry
in:

```text
%LOCALAPPDATA%\Packages\Microsoft.Windows.StartMenuExperienceHost_cw5n1h2txyewy\TempState\StartUnifiedTileModelCache.dat
```

Deleting that cache file caused Windows to regenerate the Start Menu
state and removed the ghost.

## Final state

The WSL/Debian test installation was successfully undone.

The Debian ghost entry was successfully removed.

No broad Start Menu database reset or registry deletion was necessary.

The `Shell`/`CloudStore` backup remains at:

```text
C:\Users\Administrator\Desktop\ShellBackup-20260903-051629
```
