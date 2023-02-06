# Gpon Laserway Traffic and Onu Profile
- Script to generate bridge config (VLANs create) and GPON config (VLAN Tagging Operation, Traffic and ONU profiles), for Furukawa GPON OLT.
- Config generated is saved in a .txt.
- The script also has a static DBA Profile, for sample.

# Requires
- Python

# Supports
- OLT Furukawa Laserway

# Limitations
- Config VLANs (bridge mode) only for Pon Ports (for uplink ports you will need to configure manually).
- Config only 3 Traffic Profiles, for each combination of VLANs.
- 1 Traffic Profile with 4 Ports in VLAN X
- 1 Traffic Profile with 3 Ports in VLAN X and 1 Port in VLAN Y
- 1 Traffic Profile with 2 Ports in VLAN X and 2 Ports in VLAN Y
- 1 ONU Profile for each Traffic Profile

# Usage
1) Install Python
2) Download this repository or copy file create_traffic_profile.py.
3) Run pynton create_traffic_profile.py
4) Inform quantity of VLANs you need and each VLAN ID.

# Use case
To create VLAN Tagging Operation, Traffic and ONU Profiles for Furukawa Laserway OLT.

# Getting Help
If you are having trouble or need help, create an issue here

# Credits and references
Andre Ortega, brainwork.com.br
