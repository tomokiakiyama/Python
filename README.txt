# Python

~GitHub�̔F��~

\ssh-keygen -t rsa -C "�o�^�������[���A�h���X"
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\Owner/.ssh/id_rsa):   ��Enter
Created directory '/c/Usres/  /.ssh'.
Enter passsghrase(empty for no passphrase)  ���p�X���[�h����
Enter same passphrase again�@ ���p�X���[�h����


�u���͌�.ssh�t�@�C����id_rsa.pub���쐬�����B���g���R�s�[����B
�@GitHub��Setting��SSH and GPS keys��New SSH key
�@Key���ɃR�s�[�������̂�\��t����v

~����~


~�m�F~

\ssh -T git@github.com
Enter passphrase for key 'C:\Users\Owner/.ssh/id_rsa':�@���p�X���[�h����
Hi name! You've successfully authenticated, but GitHub does not provide shell access.
���F�؊����̊m�F


GitHub�ɂă��|�W�g���̍쐬


~���|�W�g���̓��e�ύX�`commit�`push~


\git clone "���|�W�g���̃A�h���X"
Cloning into '�t�@�C����'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), done.


�u�t�@�C�����쐬����Ă���̂ł����ɕύX���e��ۑ��v


\cd "�ύX�������t�@�C���̃A�h���X"

\git add "�ύX����t�@�C����"
\git commit -m "�R�����g"
*1

\git push
*2

~push����~



*1�uYour push would publish a private email address.�v���ł��Ƃ��̑Ώ���
private�ݒ肳��Ă���̃��[���A�h���X�����J����Ă��܂����߂ɂ�����G���[�B
setting��Emails��Keep my email address private�̃`�F�b�N���O���B


*2�uPlease tell me who you are.�v���łĂ������̑Ώ��@
git�Ɏ������N�����킩�点��΂悢

\git config --global user.email "�����Ɏ����̃A�h���X"
\git config --global user.name "�����Ɏ����̖��O"

