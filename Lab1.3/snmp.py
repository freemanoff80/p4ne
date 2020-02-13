from pysnmp.hlapi import * # Импортировать только High-level API

#snmp_object = ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
#snmp_object2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result = getCmd(SnmpEngine(),
	CommunityData("public", mpModel=0),
	UdpTransportTarget(("10.31.70.107", 161)),
	ContextData(),
	ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))


result2 = nextCmd(SnmpEngine(),
	CommunityData("public", mpModel=0),
	UdpTransportTarget(("10.31.70.107", 161)),
	ContextData(),
	ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
    lexicographicMode=False)

res = list(result)
print(res)

print('\n')

for i in res:
   for j in i[3]:
       print(j)

print('\n')

for i in result2:
   for j in i[3]:
       print(j)


tup_test = ((((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4)),
             ((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4)),
             ((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4)),
             ((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4))),
            (((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4)),
             ((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4)),
             ((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4)),
             ((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4))),
            (((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4)),
             ((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4)),
             ((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4)),
             ((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4))),
            (((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4)),
             ((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4)),
             ((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4)),
             ((1,2,3,4),(1,2,3,4),(1,2,3,4),(1,2,3,4))))

for i in tup_test:
    for j in i[3]:
        print(j)