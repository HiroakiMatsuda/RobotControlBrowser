RobotControlBrowser
======================
SQLデータベースを利用して，RTCとWebブラウザを接続するRTCです．  
RTCとWebブラウザの連携方法を提案しています．  


動作環境
------
**OS:**  
Windows 7 32bit/64bit  
Windows 8 32bit/64bit  
Ubuntu12.04 LTS 32bit  

**RT-Middleware:**  
[OpenRTM-aist Python 1.1.0-RC1][py]  
[py]:http://openrtm.org/openrtm/ja/node/4526

ファイル構成
------

ファイル構成について，一部抜粋で説明します．  

RobotControlBrowser  
│―RobotService\_Windows  
│　　　　│―WebServer  
│　　　　│　　　　│―cgi-bin  
│　　　　│　　　　│　　　│―form2sql.py  
│　　　　│　　　　│  
│　　　　│　　　　│―form_select.html  
│　　　　│　　　　│―form.html  
│　　　　│　　　　│―dbmaker.py  
│　　　　│　　　　│―data.db  
│　　　　│　　　　│―cgiserver.py  
│　　　　│  
│　　　　│―src    
│　　　　│―include  
│　　　　│―idl  
│　　　　│―doc  
│　　　　│―cpack_resources  
│　　　　│―cmake_modules  
│　　　　│―cmake  
│　　　　│―RTC.xml20130930125324     
│　　　　│―RTC.xml      
│　　　　│―rtc.conf    
│　　　　│―RobotService.py  
│　　　　│―RobotService.conf    
│　　　　│―README.RobotService  
│　　　　│―COPYING.LESSER  
│　　　　│―COPYING  
│　　　　│―CMakeLists.txt  
│　　　　│―.project  
│  
│―RobotService\_Linux  
│  
│―README.md  
│  
│―TestRTC  
　　　　　│― PyStringConsoleOut  
  

* RobotService\_Windows  
Windows OS用のファイルです．  
Windows OSをお使いの方はこのフォルダ内のファイルを使用してください．    

* RobotService\_Linux  
Linux OS用のファイルです．ファイル構成はWindows OS用と同様です．    
Linux OSをお使いの方はこのディレクトリ内のファイルを使用してください．  

* form2sql.py  
フォームから送信された値を読み，レスポンスとデータベースへの書き込みを行います．  
フォームの構成を変えた場合はここを変更してください．   

以下，ファイルの説明はWindows/Linux共に同じです．  

* form_select.html     
セレクトされた値を送信するサンプルです．

* form.html  
入力されたテキストを送信するサンプルです．   
  
* dbmaker.py    
データベースを作成するPythonスクリプトです．  
データベースを変更する場合や，削除した場合はこのスクリプトを実行して下さい．       

* cgiserver.py  
CGIサーバーを起動します．  
まずはじめにこのスクリプトを実行し，サーバーを起動する必要があります．  

* RobotService.py  
データベースからテキストデータを取得するRTCです．  
このRTCを通して，WebブラウザとRT-Middlewareを接続します．   

* TestRTC   
本RTCの動作確認をするためのTest用RTCが収められています．

システムの構成
------  
システムの構成を説明します．  

<img src="http://farm4.staticflickr.com/3714/11292663015_2607a581f5_o.png" width="600px" />  

* Human Interface    
複数のWebブラウザからロボットへユーザの指令を送信します．  
また，送信結果を表示します．  

* CGI Server  
Webブラウザに表示するGUI（フォーム）を通して，テキストデータのやりとりを行います．  
入力されたテキストデータをSQLデータベースに書き込みます．  
また，書き込みを行った値をレスポンスとしてユーザに返し，表示します．   

* SQL Database  
Webブラウザから入力されたテキストデータを保存します．    

* RTC  
SQLデータベースにアクセし，テキストデータをOutポートから出力します．  

以上のような仕組みを用いて，Webブラウザ(サーバー)とRTCを接続します．  
このような構成を用いることで，Webブラウザを通じて多数の人間がロボットに指令を送ることが可能となります．  


RTCの構成
------  
<img src="http://farm6.staticflickr.com/5516/11292329243_2f3d9e6866_o.png" width="400px" />    
データポートは以下のようになっています  

* string port :OutPort  
データ型; TimedString  
 ・String : Webブラウザから入力されたテキストデータを出力します．
  
使い方
------
###1.CGIサーバーの起動###
CGIサーバーを起動します． 　

Windows:  
cgiserver.pyをダブルクリックで起動します．  
Linux:  
以下のコマンドで起動します．  
$ python cgiserver.py  
次に，cgi-binディレクトリに移動しform2sql.pyに実行権限を以下のコマンドで与えます．  
$ chmod 755 form2sql.py  

###2. ネームサーバーの起動###
ネームサーバーを起動します．  

Windows:  
Start Naming Serviceで起動します．  
Linux:  
以下のコマンドで起動します．2809はポート番号で任意で選んで構いません．  
$ rtm-naming 2809

###3. RTCの起動###
1. RobotServiceRTCを起動します．  
Windows:  
RobotService.pyをダブルクリックで起動します．  
Linux:  
以下のコマンドで起動します．  
$ python RobotService.py  
 
2. PyStringConsoleOut.pyを起動します．  
Windows:  
PyStringConsoleOut.pyをダブルクリックで起動します．  
Linux:  
以下のコマンドで起動します．  
$ python PyStringConsoleOut.py  

3. RTCの接続
RT System Editorを使用して，RobotServiceとPyStringConsoleOutを接続します．  

###4. Webフォームへ入力　テキストサンプル 
Webブラウザを起動し，アドレス欄に以下のアドレスを入力してください．  
http://127.0.0.1:8000/form.html  
フォームに外部からアクセスする場合は127.0.0.1をIPアドレスに置き換えてください．  

<img src="http://farm4.staticflickr.com/3806/11292318486_c8b49d6e9a_o.png" width="400px" />    

テキストフォームに「TEST」と入力し，送信ボタンを押すと以下の様なレスポンスが得られます．  
<img src="http://farm4.staticflickr.com/3747/11292409053_7a40c5032c_o.png" width="400px" />    

PyStringConsoleOutのコンソール上に「TEST」と表示されていることを確認してください．  
Webブラウザから入力した値をRTCに連携できたことを確認できました．    

<img src="http://farm8.staticflickr.com/7323/11292287175_2865ee5c49_o.png" width="400px" />    

###5. Webフォームへ入力　セレクトサンプル
Webブラウザを起動し，アドレス欄に以下のアドレスを入力してください．  
http://127.0.0.1:8000/form_select.html  
フォームに外部からアクセスする場合は127.0.0.1をIPアドレスに置き換えてください．  

<img src="http://farm6.staticflickr.com/5473/11292323136_be1627d522_o.png" width="400px" />    

セレクト要素から「E」を選択し，送信ボタンを押すと以下の様なレスポンスが得られます．   

<img src="http://farm4.staticflickr.com/3744/11292326126_56259dc70d_o.png" width="400px" />    

PyStringConsoleOutのコンソール上に「E」と表示されていることを確認してください．  
Webブラウザから選択した値をRTCに連携できたことを確認できました．    

<img src="http://farm8.staticflickr.com/7423/11292412413_b9810fe297_o.png" width="400px" />    

以上が本RTCの使い方となります  

LICENSE
----------
Copyright © 2013 Hiroaki Matsuda
Licensed under the [Apache License, Version 2.0][Apache].  
Distributed under the [MIT License][MIT].  
Dual licensed under the [MIT License][MIT] and [Apache License, Version 2.0][Apache].   
 
[Apache]: http://www.apache.org/licenses/LICENSE-2.0
[MIT]: http://www.opensource.org/licenses/mit-license.php