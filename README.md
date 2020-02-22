# Python-Line_Notify_Stock
## 透過line發送個股即時股價

專題重點：
1. 用twstock模組取得股票資料(pip install twstock)
2. 利用IFTTT服務發送訊息

以英業達(股票代號2356為例)

1. 透過twstock模組取得股票即時或歷史資訊
    stock方法查詢*歷史*資訊
    | 方法  | 傳回資料 |
    | ----- | -------- |
    | price |傳回最近31筆收盤價資料|
    | high |傳回最近31筆最高價資料|
    | low  |傳回最近31筆最低價資料|
    | date  |傳回最近31筆日期資料|
    | fetch(西元年,月) |傳回參數指定月份的資料|
    | fetch_from(西元年,月|傳回參數指定月份到現在的資料|

    realtime方法查詢*即時*資訊
    ```
    real = twstock.realtime.get('2356')
    pr int(real)
    ```
    回傳回來的結果為：
    ```
    {'timestamp': 1582266600.0, 'info': {'code': '2356', 'channel': '2356.tw', 'name': '英業達', 'fullname': '英業達股份有限公司', 'time': '2020-02-21 14:30:00'}, 'realtime': {'latest_trade_price': '23.35', 'trade_volume': '710', 'accumulate_trade_volume': '8684', 'best_bid_price': ['23.35', '23.30', '23.25', '23.20', '23.15'], 'best_bid_volume': ['893', '1915', '238', '411', '118'], 'best_ask_price': ['23.40', '23.45', '23.50', '23.55', '23.60'], 'best_ask_volume': ['52', '665', '876', '284', '434'], 'open': '23.30', 'high': '23.45', 'low': '23.15'}, 'success': True}      
    ```
    可知所有股價資訊皆在realtime裡，且可透過'success':'True'做判斷是否成功取得資料

2. 透過IFTTT(IF This Then That)服務來達到傳送通知到Line上面
https://ifttt.com/

```
url_ifttt = "http://maker.ifttt.com/trigger/stock_price_through_line/with/key/c1eoMLuXYEX0LVL-fGMqL8?value1=英業達&value2=" + realprice
```

3. 設定發送條件，我設定為在早上九點到下午三點，每小時發送一次通知。亦可設定股價條件，當股價高於或低於條件時才發送通知。

4. realtime中若傳回訊息發生錯誤，會將錯誤訊息傳送到'rtmessage'中，可將錯誤訊息print出來，方便維護。