#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'

print('{:b}{:b}{:b}{:b}{:b}{:b}'.format(int(MAC[0:2], 16),int(MAC[3:4], 16),int(MAC[6:7], 16),int(MAC[8:9], 16),int(MAC[11:12], 16),int(MAC[13:14], 16)))

