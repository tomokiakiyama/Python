# Python

~GitHub�̔F��~

ssh-keygen -t rsa -C "�o�^�������[���A�h���X"
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\Owner/.ssh/id_rsa):   ��Enter
Created directory '/c/Usres/  /.ssh'.
Enter passsghrase(empty for no passphrase)  ���p�X���[�h����
Enter same passphrase again�@ ���p�X���[�h����


�u���͌�.ssh�t�@�C����id_rsa.pub���쐬�����B���g���R�s�[����B
�@GitHub��Setting��SSH and GPS keys��New SSH key
�@Key���ɃR�s�[�����\��t����v

~����~


~�m�F~

ssh -T git@github.com
Enter passphrase for key 'C:\Users\Owner/.ssh/id_rsa':�@���p�X���[�h����
Hi tomokiakiyama! You've successfully authenticated, but GitHub does not provide shell access.
���F�؊����̊m�F


GitHub�ɂă��|�W�g���̍쐬


~���|�W�g���̓��e�ύX�`commit�`push~


C:\Users\Owner>git clone "���|�W�g���̃A�h���X"
Cloning into 'sample'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), done.


�u�t�@�C�����쐬����Ă���̂ł����ɕύX���e��ۑ��v


cd "�ύX�������t�@�C���̃A�h���X"

git add "�ύX����t�@�C����"
git commit -m "�R�����g"
*1

git push
*2

~push����~
