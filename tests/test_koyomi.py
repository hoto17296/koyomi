from unittest import TestCase
import koyomi


class TestKoyomi(TestCase):

    def test_name(self):
        """各節気の名前が正しいかどうか"""
        self.assertEqual('小寒', koyomi.from_date(2018,  1,  5).name)
        self.assertEqual('大寒', koyomi.from_date(2018,  1, 20).name)
        self.assertEqual('立春', koyomi.from_date(2018,  2,  4).name)
        self.assertEqual('雨水', koyomi.from_date(2018,  2, 19).name)
        self.assertEqual('啓蟄', koyomi.from_date(2018,  3,  6).name)
        self.assertEqual('春分', koyomi.from_date(2018,  3, 21).name)
        self.assertEqual('清明', koyomi.from_date(2018,  4,  5).name)
        self.assertEqual('穀雨', koyomi.from_date(2018,  4, 20).name)
        self.assertEqual('立夏', koyomi.from_date(2018,  5,  5).name)
        self.assertEqual('小満', koyomi.from_date(2018,  5, 21).name)
        self.assertEqual('芒種', koyomi.from_date(2018,  6,  6).name)
        self.assertEqual('夏至', koyomi.from_date(2018,  6, 21).name)
        self.assertEqual('小暑', koyomi.from_date(2018,  7,  7).name)
        self.assertEqual('大暑', koyomi.from_date(2018,  7, 23).name)
        self.assertEqual('立秋', koyomi.from_date(2018,  8,  7).name)
        self.assertEqual('処暑', koyomi.from_date(2018,  8, 23).name)
        self.assertEqual('白露', koyomi.from_date(2018,  9,  8).name)
        self.assertEqual('秋分', koyomi.from_date(2018,  9, 23).name)
        self.assertEqual('寒露', koyomi.from_date(2018, 10,  8).name)
        self.assertEqual('霜降', koyomi.from_date(2018, 10, 23).name)
        self.assertEqual('立冬', koyomi.from_date(2018, 11,  7).name)
        self.assertEqual('小雪', koyomi.from_date(2018, 11, 22).name)
        self.assertEqual('大雪', koyomi.from_date(2018, 12,  7).name)
        self.assertEqual('冬至', koyomi.from_date(2018, 12, 22).name)

    def test_timezone(self):
        """UT と JST で日付が違う場合は JST の日付で計算できているかどうか"""
        # 2019年の春分点は 03/20 21:58 UT だが、JST だと翌日になる
        self.assertIsNone(koyomi.from_date(2019, 3, 20))
        self.assertIsNotNone(koyomi.from_date(2019, 3, 21))
        self.assertIsNone(koyomi.from_date(2019, 3, 22))

    def test_accuracy(self):
        """2000±50年くらいなら精度に問題がないかどうか"""
        self.assertIsNotNone(koyomi.from_date(1950, 3, 21))
        self.assertIsNotNone(koyomi.from_date(2050, 3, 20))
