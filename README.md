# gpon_laserway_tp
GPON - Furukawa Laserway Traffic Profile
Script to generate bridge config (VLANs create) and GPON (VLAN Tagging Operation, Traffic and ONU profiles), for Furukawa GPON OLT.
Config generated is saved in a .txt.
The script also has a static DBA Profile.

Requires
None

Supports
OLT Furukawa Laserway

Limitations
Script will generated:
1 Traffic Profile with 4 Ports in VLAN X
1 Traffic Profile with 3 Ports in VLAN X and 1 Port in VLAN Y
1 Traffic Profile with 2 Port in VLAN X and 2 Ports in VLAN Y
1 ONU Profile for each Traffic Profile

Usage
Install Python
Download this repository or copy file create_traffic_profile.py.
Run pynton create_traffic_profile.py
Inform quantity of VLANs you need and each VLAN ID.

Use case
To perform backup, to enables logging, to collects information, to creates username, shut/no shut interfaces, to removes config, any other config/command that can be repeated over different devices

Getting Help
If you are having trouble or need help, create an issue here

Credits and references
Andre Ortega, 
