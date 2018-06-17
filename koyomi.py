import os
import csv
from datetime import datetime, timezone, timedelta
import numpy as np


sl = np.array([
    [36000.7695,280.4659,1.9147,0.0200,-0.0048,0.0020,0.0018,0.0018,0.0015,0.0013,0.0007,0.0007,0.0007,0.0006,0.0005,0.0005,0.0004,0.0004],
    [0,0,35999.05,71998.1,35999,32964,19,445267,45038,22519,65929,3035,9038,33718,155,2281,29930,31557],
    [0,0,267.52,265.1,268,158,159,208,254,352,45,110,64,316,118,221,48,161],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
])


def sun_lng(d):
    """ある時点での太陽の視黄経を返す"""
    assert type(d) == datetime
    delta = (58 + 0.44 * (d.year - 1990)) / 86400
    jd = d.timestamp() / 86400 + 2440587.5
    t = (jd - 2451545 + delta) / 36525
    m_lng = (sl[0] * np.cos(np.deg2rad(sl[1] * t + sl[2])) * ((t - 1) * sl[3] + 1)).sum()
    lng = m_lng + np.cos(np.deg2rad(1934 * t + 145)) * 0.0048 - 0.0057
    return lng % 360


koyomi_list = [
    ('春分', '日天の中を行て昼夜等分の時也'),
    ('清明', '万物発して清浄明潔なれば、此芽は何の草としれる也'),
    ('穀雨', '春雨降りて百穀を生化すれば也'),
    ('立夏', '夏の立つがゆへ也'),
    ('小満', '万物盈満すれば草木枝葉繁る'),
    ('芒種', '芒ある穀類、稼種する時也'),
    ('夏至', '陽熱至極しまた、日の長きのいたりなるを以て也'),
    ('小暑', '大暑来れる前なれば也'),
    ('大暑', '暑気いたりつまりたるゆえんなれば也'),
    ('立秋', '初めて秋の気立つがゆへなれば也'),
    ('処暑', '陽気とどまりて、初めて退きやまんとすれば也'),
    ('白露', '陰気ようやく重なりて露こごりて白色となれば也'),
    ('秋分', '陰陽の中分となれば也'),
    ('寒露', '陰寒の気に合って、露むすび凝らんとすれば也'),
    ('霜降', 'つゆが陰気に結ばれて、霜となりて降るゆへ也'),
    ('立冬', '冬の気立ち初めていよいよ冷ゆれば也'),
    ('小雪', '冷ゆるが故に雨も雪となりてくだるがゆへ也'),
    ('大雪', '雪いよいよ降り重ねる折からなれば也'),
    ('冬至', '日南の限りを行て日の短きの至りなれば也'),
    ('小寒', '冬至より一陽起るが故に陰気に逆らう故益々冷る也'),
    ('大寒', '冷ゆることの至りて甚だしきときなれば也'),
    ('立春', '春の気たつを以て也'),
    ('雨水', '陽気地上に発し、雪氷とけて雨水となれば也'),
    ('啓蟄', '陽気地中にうごき、ちぢまる虫、穴をひらき出れば也'),
]


class Koyomi:

    def __init__(self, index):
        self.index = None
        if type(index) == int:
            self.index = index
        else:
            for i, (name, desc) in enumerate(koyomi_list):
                if name == index:
                    self.index = i
                    break
        if self.index is None:
            raise KeyError('Unknown koyomi "{}".'.format(index))

    def __repr__(self):
        return '<{} name={}>'.format(type(self).__name__, self.name)

    @property
    def name(self):
        return koyomi_list[self.index][0]

    @property
    def description(self):
        return koyomi_list[self.index][1]


JST = timezone(timedelta(hours=+9), 'JST')


def from_date(y, m=None, d=None, tz=JST):
    """指定した日付が二十四節気であれば Koyomi オブジェクトを返す"""
    if type(y) == datetime:
        assert m is None and d is None
        date = y
    else:
        date = datetime(y, m, d, tzinfo=tz)
    index = int(sun_lng(date + timedelta(days=1)) / 15)
    if index != int(sun_lng(date) / 15):
        return Koyomi(index)
    return None


def today():
    """現在の日付が二十四節気であれば Koyomi オブジェクトを返す"""
    return from_date(datetime.now(tz=timezone.utc))


__all__ = [Koyomi, from_date, today]
