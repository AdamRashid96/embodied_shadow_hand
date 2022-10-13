import numpy as np

from . import generic
from . import selectors
from . import limiters


class Uniform(generic.Generic):

  def __init__(
      self, length, capacity=None, directory=None, online=False,
      chunks=1024, seed=0):
    super().__init__(
        length=length,
        capacity=capacity,
        remover=selectors.Fifo(),
        sampler=selectors.Uniform(seed),
        limiter=limiters.MinSize(1),
        directory=directory,
        online=online,
        chunks=chunks,
    )


class Queue(generic.Generic):

  def __init__(
      self, length, capacity=None, directory=None, overlap=0, chunks=1024):
    # TODO: Work in progress, not thread-safe yet.
    super().__init__(
        length=length,
        overlap=overlap,
        capacity=capacity,
        remover=selectors.Fifo(),
        sampler=selectors.Fifo(),
        limiter=limiters.Queue(capacity),
        directory=directory,
        chunks=chunks,
        max_times_sampled=1,
    )


class Prioritized(generic.Generic):

  def __init__(
      self, length, capacity=None, directory=None, chunks=1024, **kwargs):
    # TODO: Work in progress, is too slow.
    super().__init__(
        length=length,
        overlap=length - 1,
        capacity=capacity,
        remover=selectors.Fifo(),
        sampler=selectors.Prioritized(**kwargs),
        limiter=limiters.MinSize(1),
        directory=directory,
        chunks=chunks,
    )
