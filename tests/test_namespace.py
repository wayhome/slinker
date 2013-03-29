#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slinker import Namespace

links = Namespace()

link1 = links.link('first')
link1_dup = links.link('first')

print link1 == link1_dup
