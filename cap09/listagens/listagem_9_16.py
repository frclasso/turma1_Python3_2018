#!/usr/bin/env python3
# -*-coding:utf-8 -*-

""" Alteração do nome de arquivos e diretórios
"""
import os
os.makedirs("avo/pai/filho/neto")
os.makedirs("avo/mãe/filha/neta")
os.rename("avo/pai/filho/neto","avo/pai/filho/netos")
