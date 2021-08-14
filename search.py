
### 検索ツールサンプル
### これをベースに課題の内容を追記してください
### source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

import os

CSV_FILE = 'source.csv'
CARACTOR_NAME = ["ねずこ","たんじろう","きょうじゅろう"]


def csv_reading(csv_path:str):
    if not os.path.exists(csv_path):
        print('ファイルが有りません。作成します。')
        csv_writing(csv_path,CARACTOR_NAME)
    with open(csv_path, 'r') as f:
        return f.read().splitlines()

def csv_writing(csv_path:str, source:list):
    with open(csv_path, 'w') as f:
        f.write('\n'.join(source))



### 検索ツール
def search():

    source = csv_reading(CSV_FILE)

    while True:

        word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
        ### ここに検索ロジックを書く
        if word in source:
            print("{}が見つかりました".format(word))
        else:
            print("{}が見つかりませんでした".format(word))

            is_add = input("追加しますか？(n:しない y:する)")
            if is_add == "y":
                source.append(word)

        csv_writing(CSV_FILE, source=source)

if __name__ == "__main__":
    search()