#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки CONFIG список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'

vlans = []
for w in CONFIG.split():
    if ',' in w:
        for vlan in w.split(','):
            vlans.append(vlan)

print(vlans)

