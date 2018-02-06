#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'


template = ('Protocol:              {proto} \n'
'Prefix:                {prefix} \n'
'AD/Metric:             {metric} \n'
'Next-Hop:              {nHop} \n'
'Last update:           {lUpd}\n'
'Outbound Interface     {outIf}\n')


ospf_route = ospf_route.replace(',','')

lor = ospf_route.split()

proto =''
if lor[0] == 'O': 
    proto = 'OSPF'

prefix = lor[1]
metric = lor[2][1:-1]
lUpd = lor[5]
nHop = lor[4]
outIf = lor[6]

print(template.format(proto = proto, prefix = prefix, metric = metric, nHop = nHop, lUpd = lUpd, outIf = outIf))
