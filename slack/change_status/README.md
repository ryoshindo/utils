# 概要
## 何をするものか
change_status.pyはBSSIDの値によってslackのステータスを変更してくれるスクリプトです。具体的には、
1. 研究室にいるときはステータスを「研究室」にする
2. 研究室意外にいるときはステータスを「自宅」にする

といった感じです。

## 注意点
### 以下の設定は必ずMacBookで行ってください。
change_status.pyはこのスクリプトが動いているパソコンが接続されているWi-Fiが研究室のものかそうでないものかによって研究室にいる・いないを判定しています。iMacは基本的に研究室以外のWi-Fiに接続されることはないため、iMacで以下の設定を行ってしまった場合はその人は本当は家にいても常に研究室にいることになってしまい正しく動作しません。

### change_status.pyは必ずgit cloneしてください。
change_status.pyは随時機能拡充、そしてバグ取り等を行う予定です。git cloneであれば常に最新のバージョンでchange_status.pyを実行することができます。

## 動作環境
Python 3.7.4
<br>OS Mojave

# セットアップの手順
具体的なセットアップの手順としては、
1. macの環境設定
2. pythonの環境設定
3. スクリプトの実行
4. 定期実行の設定（cron）

です。

## macの環境設定
1. まず研究室のBSSIDの値を取得します。ターミナルを開いて以下のコマンドを実行してください。このコマンドは必ず研究室で実行してください。
<br>```$ /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | grep BSSID | awk '{print $2}'```

2. ターミナルに表示された結果を環境変数として設定します。
<br>```$ export CMT_BSSID="1.のコマンドの結果"```

3. SlackのユーザーIDを環境変数として設定します。
<br>```$ export CMT_SLACK_USER_ID="SlackのユーザーID"```

4. 以下のコマンドを実行して正しく環境変数が設定されたか確認してください。
<br>```$ echo $CMT_BSSID```
<br>```$ echo $CMT_SLACK_USER_ID```

## pythonの環境設定
1. まずpythonをインストールしてください。
2. 以下のコマンドを実行してください。
<br>```$ which python```

3. 2.のコマンドの中のどこかに'anaconda'と書かれていた場合と'pyenv'と書かれている場合でコマンドが異なります。
<br>'anacondaのとき'
  <br>```$ conda install requests```
  <br>```$ conda install subprocess```
<br><br>'pyenvのとき'
  <br>```$ pip install requests```
  <br>```$ pip install subprocess```

## スクリプトの実行
1. CMT-MUのpythonレポジトリをgit cloneしてください。
2. GitHubのレポジトリまでディレクトリを移動し、以下のコマンドを実行してください。
<br>```$ python change_status.py```

3. Slackの自分のステータスが変更されていたら問題ありません。

## 定期実行の設定
1. OSがCatalinaの人は[このURL](https://mac-ra.com/catalina-crontab/)を参考にして```crontab```を設定してください。OSがMojaveの人はこの手順を行う必要はありません。
2. 以下のコマンドを実行してください。
<br>```crontab -e```

3. 2.のコマンドを実行するとvimが立ち上がります（vimの使用法は検索してください）。INSERTモードにして以下の文字列を入力してください。
<br>```*/5 * * * * (which pythonの結果) (change_status.pyのフルパス)```
<br>例：```*/5 * * * * /usr/local/var/pyenv/shims/python ~/Documents/GitHub/python/slack/change_status/change_status.py```

4. 以下のコマンドを実行し、3.の設定が正しく入力できているかを確認してください。
<br>```$ crontab -l```

5. 以上の設定を行うことで5分毎にchange_status.pyが動作すると思います。
