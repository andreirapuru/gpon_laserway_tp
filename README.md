# Gpon Laserway Traffic and Onu Profile
GPON - Furukawa Laserway Traffic and Profile
Script to generate bridge config (VLANs create) and GPON (VLAN Tagging Operation, Traffic and ONU profiles), for Furukawa GPON OLT.
Config generated is saved in a .txt.
The script also has a static DBA Profile.

# Requires
Python

# Supports
OLT Furukawa Laserway

# Limitations
Script will generated:
1 Traffic Profile with 4 Ports in VLAN X
1 Traffic Profile with 3 Ports in VLAN X and 1 Port in VLAN Y
1 Traffic Profile with 2 Port in VLAN X and 2 Ports in VLAN Y
1 ONU Profile for each Traffic Profile

# Usage
Install Python
Download this repository or copy file create_traffic_profile.py.
Run pynton create_traffic_profile.py
Inform quantity of VLANs you need and each VLAN ID.

# Use case
To create VLAN Tagging Operation, Traffic and ONU Profiles for Furukawa Laserway OLT.

# Getting Help
If you are having trouble or need help, create an issue here

# Credits and references
Andre Ortega, 
