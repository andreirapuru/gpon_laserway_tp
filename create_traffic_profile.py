#Author: Andre Ortega, brainwork.com.br, https://github.com/andreirapuru/gpon_laserway_tp

import sys

print('\n********************************** Script Started **********************************')
print('\n')

vlan_list = []
qtd_vlans = 0
i = count = 0

def swap_vlans(lst, p1, p2):
    lst[p1], lst[p2] = lst[p2], lst[p1]
    return lst

flag = True
while flag:
	try:
		qtd_vlans = abs(int(input('VLANs: ')))
		flag = False
	except:
		print("Number of VLANs must be a positive integer")

while (i < qtd_vlans):
	vlans_id = input('VLAN ID ' + str(i+1) +': ')
	if vlans_id.isdigit() and int(vlans_id) in range(1,4094):
		vlan_list.append(vlans_id)
		i+=1
	else:
		print(vlans_id, "is not a valide VLAN ID")

vlan_list = list(dict.fromkeys(vlan_list))
qtd_vlans = len(vlan_list)
print("\nVLANs:")
print(" ".join(vlan_list))
input("\nPress Enter to generate config for DBA Profile, VLAN Tagging Operation, Traffic and ONU Profile")

i=0
original_stdout = sys.stdout
with open('gpon_config.txt', 'w') as f:
	sys.stdout = f
	print("\nVLANs:")
	print(" ".join(vlan_list))
	print("\n!----------------------------- BRIDGE MODE (8 ports PON)-----------------------------!")
	print("bridge")
	print(" vlan pvid 1-24 1")
	print(" port port-bridge enable 1-8")
	print(" storm-control broadcast 1000 1-8")
	print(" spanning-tree")
	print(" spanning-tree mode rapid-pvst")
	print(" spanning-tree vlan 1")
	print(" loop-detect enable")
	print(" loop-detect 1-8")
	print(" loop-detect 1-8 period 1")
	print(" loop-detect 1-8 timer 5")
	print(" vlan add default 1-8 tagged")
	for i in range (len(vlan_list)):
		if vlan_list[i] == "1":
			print("")
		else:
			print(" vlan create {}".format(vlan_list[i]))
			print("	vlan add {} 1-8 tagged".format(vlan_list[i]))
			print("	spanning-tree vlan {}".format(vlan_list[i]))
	
	print("\n!------------------------------------- GPON MODE ------------------------------------!")
	print("\n!----------------------------- MULTICAST AND DBA PROFILE ----------------------------!")
	print("gpon")
	print(" olt multicast-gem 4094")
	print(" olt interwork igmp-snooping enable")
	print(" !")
	print(" dba-profile DBAPADRAO create")
	print("  mode sr")
	print("  sla fixed 256")
	print("  sla maximum 1031616")
	print("  apply")
	print(" !")
	print("\n!------------------------------ VLAN TAGGING OPERATION ------------------------------!")
	for i in range (len(vlan_list)):
		print(" extended-vlan-tagging-operation ACESSO_VLAN{} create".format(vlan_list[i]))
		print("  downstream-mode enable")
		print("  untagged-frame 1")
		print("   treat inner vid {} cos 0 tpid 0x8100".format(vlan_list[i]))
		print("  apply")
		print(" !")

	print()
	print("!----------------------------- TRAFFIC AND ONU PROFILES -----------------------------!")
	i=0
	while (i < qtd_vlans):
		for count in range(qtd_vlans):
			if count == 0:
				#4 port vlanX
				print(" traffic-profile TP_4P_V{} create".format(vlan_list[count]))
				print("  tcont 1")
				print("   gemport 1/1")
				print("   dba-profile DBAPADRAO")
				print("  mapper 1")
				print("   gemport count 1")
				print("  bridge 1")
				print("   ani mapper 1")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[count]))
				print("   uni eth 1")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[count]))
				print("    extended-vlan-tagging-operation ACESSO_VLAN{}".format(vlan_list[count]))
				print("   uni eth 2")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[count]))
				print("    extended-vlan-tagging-operation ACESSO_VLAN{}".format(vlan_list[count]))
				print("   uni eth 3")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[count]))
				print("    extended-vlan-tagging-operation ACESSO_VLAN{}".format(vlan_list[count]))
				print("   uni eth 4")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[count]))
				print("    extended-vlan-tagging-operation ACESSO_VLAN{}".format(vlan_list[count]))
				print("  apply")
				print(" !")
				print(" onu-profile ONU_4P_V{} create".format(vlan_list[count]))
				print("  traffic-profile TP_4P_{}".format(vlan_list[count]))
				print("  loop-detect enable")
				print("  apply")
				print(" !")
			else:
				#3 port vlanX + 1 porta vlanY
				print(" traffic-profile TP_3P_V{}_1P_V{} create".format(vlan_list[0],vlan_list[count]))
				print("  tcont 1")
				print("   gemport 1/1")
				print("   dba-profile DBAPADRAO")
				print("  tcont 2")
				print("   gemport 2/1")
				print("   dba-profile DBAPADRAO")
				print("  mapper 1")
				print("   gemport count 1")
				print("  mapper 2")
				print("   gemport count 1")
				print("  bridge 1")
				print("   ani mapper 1")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[0]))
				print("   uni eth 1")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[0]))
				print("    extended-vlan-tagging-operation ACESSO_VLAN{}".format(vlan_list[0]))
				print("   uni eth 2")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[0]))
				print("    extended-vlan-tagging-operation ACESSO_VLAN{}".format(vlan_list[0]))
				print("   uni eth 3")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[0]))
				print("    extended-vlan-tagging-operation ACESSO_VLAN{}".format(vlan_list[0]))
				print("  bridge 2")
				print("   ani mapper 2")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[count]))
				print("   uni eth 4")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[count]))
				print("    extended-vlan-tagging-operation ACESSO_VLAN{}".format(vlan_list[count]))
				print("  apply")
				print(" !")
				print(" onu-profile ONU_3P_V{}_1P_V{} create".format(vlan_list[0],vlan_list[count]))
				print("  traffic-profile TP_3P_V{}_1P_V{} create".format(vlan_list[0],vlan_list[count]))
				print("  loop-detect enable")
				print("  apply")
				print(" !")
				#2 port vlanX + 2 porta vlanY
				print(" traffic-profile TP_2P_V{}_2P_V{} create".format(vlan_list[0],vlan_list[count]))
				print("  tcont 1")
				print("   gemport 1/1")
				print("   dba-profile DBAPADRAO")
				print("  tcont 2")
				print("   gemport 2/1")
				print("   dba-profile DBAPADRAO")
				print("  mapper 1")
				print("   gemport count 1")
				print("  mapper 2")
				print("   gemport count 1")
				print("  bridge 1")
				print("   ani mapper 1")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[0]))
				print("   uni eth 1")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[0]))
				print("    extended-vlan-tagging-operation ACESSO_VLAN{}".format(vlan_list[0]))
				print("   uni eth 2")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[0]))
				print("    extended-vlan-tagging-operation ACESSO_VLAN{}".format(vlan_list[0]))
				print("  bridge 2")
				print("   ani mapper 2")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[count]))
				print("   uni eth 3")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[count]))
				print("    extended-vlan-tagging-operation ACESSO_VLAN{}".format(vlan_list[count]))
				print("   uni eth 4")
				print("    vlan-filter vid {} untagged allow".format(vlan_list[count]))
				print("    extended-vlan-tagging-operation ACESSO_VLAN{}".format(vlan_list[count]))
				print("  apply")
				print(" !")
				print(" onu-profile ONU_2P_V{}_2P_V{} create".format(vlan_list[0],vlan_list[count]))
				print("  traffic-profile TP_2P_V{}_2P_V{} create".format(vlan_list[0],vlan_list[count]))
				print("  loop-detect enable")
				print("  apply")
				print(" !")
		i+=1
		try:
			swap_vlans(vlan_list, 0, i)
		except:
			print('\n')

sys.stdout = original_stdout
print('\n*********************** Config save to file gpon_config.txt ************************')