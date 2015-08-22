import unittest
from csv_conversor import add_timezone

class TestCSVConversor(unittest.TestCase):

  def test_pacific_auckland_timezone(self):
      input_rows = [['2013-07-10 02:52:49', '-44.490947', '171.220966']]
      rows_with_timezone = add_timezone(input_rows)
      self.assertEqual(
        ('2013-07-10 02:52:49','-44.490947','171.220966',
        'Pacific/Auckland','2013-07-10 14:52:49'), rows_with_timezone[0])

  def test_america_saopaulo_timezone(self):
      input_rows = [['2015-3-8 12:00:34', '-27.6402821', '-48.72778460000001']]
      rows_with_timezone = add_timezone(input_rows)
      self.assertEqual(
        ('2015-3-8 12:00:34', '-27.6402821', '-48.72778460000001',
        'America/Sao_Paulo','2015-03-08 09:00:34'), rows_with_timezone[0])

  def test_pacific_losangeles_timezone(self):
      input_rows = [['2015-3-8 12:00:34', '37.4224764', '-122.0842499']]
      rows_with_timezone = add_timezone(input_rows)
      self.assertEqual(
        ('2015-3-8 12:00:34', '37.4224764', '-122.0842499',
        'America/Los_Angeles','2015-03-08 05:00:34'), rows_with_timezone[0])

  def test_two_rows_timezone(self):
      input_rows = [['2015-3-8 12:00:34', '37.4224764', '-122.0842499'],
      ['2013-07-10 02:52:49', '-44.490947', '171.220966']]
      rows_with_timezone = add_timezone(input_rows)
      self.assertEqual(
        ('2015-3-8 12:00:34', '37.4224764', '-122.0842499',
        'America/Los_Angeles','2015-03-08 05:00:34'), rows_with_timezone[0])
      self.assertEqual(
        ('2013-07-10 02:52:49','-44.490947','171.220966',
        'Pacific/Auckland','2013-07-10 14:52:49'), rows_with_timezone[1])
        
if __name__ == '__main__':
    unittest.main()
