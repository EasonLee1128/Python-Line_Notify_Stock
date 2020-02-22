import twstock
import requests
import time

#計算發送次數
counterLine = 0
#計算錯誤次數
counterError = 0

print('Get ready!')
#True for what?
while True:
    #取得即時股價
    realdata = twstock.realtime.get('2356')
    if realdata['success']:
        realprice = realdata['realtime']['latest_trade_price']
        print('英業達目前股價:' + realprice)
        counterLine+=1
        url_ifttt = "http://maker.ifttt.com/trigger/stock_price_through_line/with/key/c1eoMLuXYEX0LVL-fGMqL8?value1=英業達&value2=" + realprice

        #取得時間/[0:2]只抓小時的部分
        hour = int(time.strftime('%H:%M:%S')[0:2])
        
        if 9 <= hour < 15:
            res1 = requests.get(url_ifttt)
            print('第' + str(counterLine) + '次發送LINE回傳訊息：' + res1.text)
            #打瞌睡一小時(60sec*60min = 3600s)
            time.sleep(3600)
        else:
            print('have a nice day')
            break 
        
        
        
        
        if counterLine >= 7:
            print('Have a nice day')
            break
        #? 每五分鐘讀一次
        # for i in range(300):
        #     time.sleep(300)

    #列出錯誤訊息，且錯誤超過三次則中斷
    else:
        print('something wrong:' + realdata['rtmessage'])
        counterError+=1
        if counterError >=3:
            print('維護中，請稍等')
            break
        #?每五分鐘讀一次
        # for i in range(300):
        #     time.sleep(300)

        