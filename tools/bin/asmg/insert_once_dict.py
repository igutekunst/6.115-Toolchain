class DuplicateKeyError(Exception):
  def __init__(self, key, insert_once_dict = None):
    self.key = key
    self.insert_once_dict = insert_once_dict
  def __str__(self):
      return "Attempt to overwrite existing key %s" % repr(self.key)
  def __repr__(self):
    return str(self)
class InsertOnceDict(object):

  def __init__(self,data=None):
    if data is None:
      self.data = {}
    if isinstance(data, dict):
      self.data = data
  def __getitem__(self, i):
    return self.data[i]
  def __setitem__(self, key, item):
    if key in self.data:
      raise DuplicateKeyError(key)
    self.data[key] = item
  def __contains__(self, key):
    return key in self.data
  def __str__(self):
    return "InsetOnceDict: %s" % str(self.data)
  def __repr__(self):
    return str(self)






if __name__ == '__main__':
  print "Testing InsertOnceDict"
  a = InsertOnceDict()
