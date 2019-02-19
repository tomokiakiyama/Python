# Python

~GitHubの認証~

ssh-keygen -t rsa -C "登録したメールアドレス"
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\Owner/.ssh/id_rsa):   ←Enter
Created directory '/c/Usres/  /.ssh'.
Enter passsghrase(empty for no passphrase)  ←パスワード入力
Enter same passphrase again　 ←パスワード入力


「入力後.sshファイルにid_rsa.pubが作成される。中身をコピーする。
　GitHub→Setting→SSH and GPS keys→New SSH key
　Key欄にコピーした貼り付ける」

~完了~


~確認~

ssh -T git@github.com
Enter passphrase for key 'C:\Users\Owner/.ssh/id_rsa':　←パスワード入力
Hi tomokiakiyama! You've successfully authenticated, but GitHub does not provide shell access.
←認証完了の確認


GitHubにてリポジトリの作成


~リポジトリの内容変更～commit～push~


C:\Users\Owner>git clone "リポジトリのアドレス"
Cloning into 'sample'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), done.


「ファイルが作成されているのでそこに変更内容を保存」


cd "変更したいファイルのアドレス"

git add "変更するファイル名"
git commit -m "コメント"
*1

git push
*2

~push完了~
