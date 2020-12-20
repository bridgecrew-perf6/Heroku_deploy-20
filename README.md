# Heroku_deploy
目的
デプロイという単語を覚えたので、勉強のついでにpythonアプリケーションをHerokuにデプロイします。

（2020/12/19）まず、チュートリアルに沿ってHerokuのサンプルコード（node.js）をデプロイしてみます。　　

ついでに、gitの使用も必要そうだったので入れました。 

さらにSSHも通した方が良い気がしたので、gitHubと連携しておきました。(参考：「GitHub に SSH で接続する」https://docs.github.com/ja/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh) 

node.jsのサンプルコードをforkしてとりあえず、Herokuにデプロイできました。 
 
 (2020/12/20）pycharmを導入した。「venv」（仮想環境を作成するためのモジュール）や「pip」（パッケージ管理ツール）、インタプリタの管理がめっちゃ楽。使い勝手よさそう。インタプリタとは、Pythonのコードを解釈して実行してくれるソフトウェアのことです。
 biopythonを入れて本格的にfastaが読めるような実装を目指す。
 
→pip install biopythonでbiopython入れた。なぜか上手くいかない。
→numpyの最新版バージョンのせいだったらしい。ダウングレードしたら治った。(参考：https://qiita.com/bear_montblanc/items/b4b75dfd77da98076da5)

pycharmとgithubをアクセストークン使って連携。
biopytonの使い方(https://biomedicalhacks.com/2020-05-12/biopython-basic-1/)
Genbank(.gb)のファイルは読めるようになった。
