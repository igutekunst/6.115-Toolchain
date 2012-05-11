class DuplicateKeyError(Exception):
  pass
class InsertOnceDict(object):

  def __init__(self,data=None):
    if data is None:
      self.data = {}
    if isinstance(data, dict):
      self.data = data
  def add(self, item, key):
    if key in self.data:
      raise DuplicateKeyError()
    self.data[key] = item




if __name__ == '__main__':
  print "Testing InsertOnceDict"
  a = InsertOnceDict({'a':4})
