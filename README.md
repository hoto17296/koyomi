# Koyomi
Python で二十四節気を扱うためのモジュール。

## Installation
``` console
$ pip install koyomi
```

## Usage

### `koyomi.from_date`
日付を数値または `datetime` オブジェクトとして指定すると、指定した日が二十四節気だった場合に `Koyomi` オブジェクトを返す。
二十四節気でなかった場合は `None` を返す。

``` python
import koyomi

koyomi.from_date(2019, 3, 21)  #=> <Koyomi name=春分>
```

``` python
from datetime import datetime, timezone, timedelta
import koyomi

JST = timezone(timedelta(hours=+9), 'JST')
koyomi.from_date(datetime(2019, 3, 21, tzinfo=JST))  #=> <Koyomi name=春分>
```

### `koyomi.today`
日本時間での現在の日付が二十四節気だった場合に `Koyomi` オブジェクトを返す。

``` python
koyomi.today()  #=> <Koyomi name=春分>
```

### `Koyomi` object
`name` と `description` プロパティが利用可能。

``` python
equinox = koyomi.from_date(2019, 3, 21)

print(equinox.name)  #=> "春分"
print(equinox.description)  #=> "日天の中を行て昼夜等分の時也"
```

## Note
- 太陽の視黄経から二十四節気の日付を計算している
    - 2000年前後では特に問題ないが、遠い過去や未来については精度が悪くなる
- 日本の祝日の振替休日は考慮されていない
