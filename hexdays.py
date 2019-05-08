# -*- coding: UTF-8 -*-
from collections import Counter


class HexDays:

  DAYS = 'sun', 'mon', 'tue', 'wed', 'thu','fri','sat','all'

  def  hex_to_days(self, dia):
    """Retorna un listado con los dias utilizado marcados con el número 1.

    Arguments:
      dia {str} -- Número hexadecimal

    Returns:
      [list] -- listado con los dias de la semana


    >>> HexDays().hex_to_days("F5")
    [0, 2, 4, 5, 6, 7]

    >>> HexDays().hex_to_days(None)
    None

    >>> HexDays().hex_to_days('')
    None
    """
    if dia:
      hex_to_bin  = bin(int(dia,16))[2:]
      bit_to_list = [str(i) for i in hex_to_bin.zfill(8)]

      bit_to_list.reverse()
      return [i for i in range(len(bit_to_list)) if bit_to_list[i] == '1']
      # return bit_to_list
      # return {DAYS[i] : int(bit_to_list[i])   for i in range(8)}
    return None


  def days_to_hex(self, dias):
    """A partir de un listado de dias en formato numérico. Teniendo en 
    cuenta el día domingo comienza en 0'

    >>> HexDays().days_to_hex([0, 2, 4, 5, 6, 7])
    'F5'

    >>> HexDays().days_to_hex(['0', '2', '4', '5', '6', '7'])
    'F5'

    >>> HexDays().days_to_hex([])
    '00'

    >>> HexDays().days_to_hex(None)
    None
    """
    try:
      if len(dias) > 0:
        days_to_int = [int(i) for i in dias]
        days_list = ['1' if i in days_to_int else '0' for i in range(8)]
        days_list.reverse()

        n = hex(int("".join(days_list),2))
        return "{:X}".format(int(n, 16)).zfill(2)
      return '00'
    except TypeError:
      return None


if __name__ == "__main__":

  import doctest

  doctest.testmod(verbose=True)

