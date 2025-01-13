# gooddays

日程調整のため，指定された範囲で候補日一覧をテキストで出力するツールです．土日祝日は自動的に候補日から外します．

日程調整ツール[「調整さん」](https://chouseisan.com)の日程候補欄などにコピーしてお使いください．

## 事前準備

以下のようにPython実行環境をご準備ください．

```sh
$ git clone https://github.com/kanaya/gooddays.git
$ cd gooddays
$ python3 -m venv env
$ . env/bin/activate
$ pip3 install paredatetime jpholiday
```

## 使い方

Pythonで次のように走らせます．

```sh
$ python3 gooddays.py --start tomorrow --end  "next friday" --slots "09, 10, 11" --suffix "時台"
```
次のオプションが使えます．

### --start

開始日．

例：tomorrow, "1 January 2025"

### --end

終了日．

例："next Friday", "30 January 2025"

### --slots

各候補日の時間スロット．カンマ区切りで記載します．

例："1, 2, 3, 4, 5"

### --suffix

各候補日の時間スロットにつける文字列．

例："時間目", "時台"

## 使用例

入力：

```sh
$ python3 gooddays.py --start "1 feb. 2025" --end "4 feb. 2025" --slots "09, 10, 11" --suffix "時台"
```

出力：
```
02/03 (月) 09時台
02/03 (月) 10時台
02/03 (月) 11時台
02/04 (火) 09時台
02/04 (火) 10時台
02/04 (火) 11時台
```

（2025年2月1日，2日は土日となるために候補日から除かれています．）


