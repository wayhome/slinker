#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slinker import Link, receiver
from nose.tools import raises


def test_receiver():

    started = Link()
    middle = Link()
    end = Link()

    @receiver(started)
    @receiver(middle)
    def each(sender, **kwargs):
        print sender
        return 'hello'

    @receiver(end)
    def every(sender, **kwargs):
        assert sender == 'end'
        return 'world'

    func, result = started.send('started', request=1)
    assert func == each
    assert result == 'hello'

    _, result = end.send('end', request=2)
    assert result == 'world'

    func, result = middle.send_robust(None, request=3)
    assert result == 'hello'


def test_connect():
    a_link = Link()
    func, result = a_link.send(None, request=4)
    assert result is None

    def a_func(sender, **kwargs):
        return 'a_func'

    a_link.connect(a_func)

    func, result = a_link.send(None, request=4)
    assert result == 'a_func'

    a_link.disconnect(a_func)

    def b_func(sender, **kwargs):
        return 'b_func'

    a_link.connect(b_func)
    func, result = a_link.send(None, request=4)
    assert result == 'b_func'


@raises(Exception)
def test_dupconnect():
    some_link = Link()

    def a_func(sender, **kwargs):
        return 'a_func'

    def b_func(sender, **kwargs):
        return 'b_func'

    some_link.connect(a_func)
    some_link.connect(b_func)
