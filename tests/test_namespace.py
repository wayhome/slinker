#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slinker import Namespace


def test_namespace():
    links = Namespace()
    link1 = links.link('first')
    link1_dup = links.link('first')

    assert link1 == link1_dup

    def test(sender, **kwargs):
        return sender

    link1.connect(test)
    _, result = link1.send('hello')
    assert result == 'hello'
