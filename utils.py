class utils:
  def reversed(self, num):
    return int(str(int(num))[::-1])

  def formatter(self, num):
    octal = 0
    count = 1
    deci = int(num)
    while(deci != 0):
      remainder = deci % 8
      octal += remainder * count
      count = count * 10
      deci = deci // 8

    return bin(int(num)), octal
