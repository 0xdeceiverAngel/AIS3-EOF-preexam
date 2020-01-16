# baby RMI
這題要把他的那個zip下載下來 然後解壓縮
題目裡面那個Click me一點用都沒有 點進去LMGTFY是Let Me Google That For You的縮寫
啊點下去就是介紹RMI是什麼東西
這題我解的出來是因為我本來就會一點JAVA 加上他程式碼又不多
所以我就直接看
雖然我一開始以為他的這些程式碼是那個網站的程式碼
不過點進去看就知道不是了

一進去可以直接跑看看 跑完之後會有response: Hello, RMI!
RMI就是 Java遠端方法呼叫 所以會有ip位址跟port
接著往下看會看到registry 就只是和那個位址做連線
先看那個response 因為最後的output是output response
我們可以看到他有用到另一個程式碼也就是下面那個程式裡面的函式
這邊我們可以把stub.sayHello()改成stub.getSecret()
改完之後跑程式output會變response: Hint: FLAG is ..... object
因為Java裡面的東西都是物件(我不確定ㄛ) 加上能改的東西也沒多少了
我就把             
RMIInterface stub = (RMIInterface) registry.lookup("Hello");
改成
RMIInterface stub = (RMIInterface) registry.lookup("FLAG");
就跳出FLAGㄌ
然後現在我跑不出來我8知道為啥
ㄏ
說8定是我連太多次
因為他跳ㄉ錯誤訊息不是沒這個東西
是connection  refused