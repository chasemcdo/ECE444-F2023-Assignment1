from utils import utils

try:
  obj = utils()
  assert (obj.reversed(1234) == 4321)
  assert (obj.reversed("1234") == 4321)
  assert (obj.reversed(1234.0) == 4321)

  assert (obj.formatter(41) == ('0b101001', 51))
  assert (obj.formatter("41") == ('0b101001', 51))
  assert (obj.formatter(41.0) == ('0b101001', 51))
  print("Tests Passed!")
except:
  print("Tests Failed!")
