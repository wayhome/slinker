Slinker
=======

Slinker provide a single one to one event, we call it a ``link``.

A ``link`` can only have a single sender and a single reciver.


Signal receivers can subscribe to specific senders or receive signals
sent by any sender.

  >>> from slinker import link
  >>> started = link('round-started')
  >>> def each(round):
  ...     print "Round %s!" % round
  ...
  >>> started.connect(each)

  >>> for round in range(1, 4):
  ...     started.send(round)
  ...
  Round 1!
  Round 2!
  Round 3!
