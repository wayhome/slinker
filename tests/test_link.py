#!/usr/bin/env python
# -*- coding: utf-8 -*-
from slinker import Link, receiver
started = Link()
middle = Link()
end = Link()


@receiver(started, sender=None)
@receiver(middle, sender=None)
def each(sender, **kwargs):
    print sender
    return 'hello'


@receiver(end, sender=None)
def every(sender, **kwargs):
    print "every", kwargs
    return 'world'

print started.send('started', request=1)
print end.send(None, request=2)
print 20 * "*"
print middle.send_robust(None, request=3)

a_link = Link()
print a_link.send(None, request=4)

started.disconnect(each)
print started.send(None, request=1)
started.connect(every)
print started.send(None, request=1)
