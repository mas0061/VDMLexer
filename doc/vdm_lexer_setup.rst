=================================
Pygments lexer for VDMについて
=================================

VDMLexerの概要
------------------

VDMLexerは、 `Sphinx <http://sphinx-users.jp/>`_ や `Trac <http://trac.edgewall.org/>`_ で使われている、
シンタックスハイライトライブラリー「 `Pygments <http://pygments.org/>`_ 」のVDM用プラグインです。
このプラグインを使うと、SphinxでVDMコードを貼りつけた時に、予約語がハイライトして出力することができます。


VDMLexerのインストール
---------------------------

VDMLexerのインストールは以下のようにします。

* 前提条件

  * Pythonがインストールされていること
  * Pythonのパッケージ管理ツールであるeasy_installがインストールされていること

* インストール
    
  #. コマンドラインで、以下のコマンドを入力
  
     #. easy_install pygments_plugin_vdm_lexer-0.1-py2.6.egg

.. note::
   これらのインストール方法については、 `ここ <http://sphinx-users.jp/gettingstarted/index.html>`_ を参照のこと


VDMLexerの使い方（Sphinxで使う場合）
-----------------------------------------

.. highlight:: rest

VDMLexerを用いて、Sphinxでシンタックスハイライトをするには、以下のようにします。 ::

  .. literalinclude:: vdm/hoge.vpp
     :language: vdm

literalincludeを使わない場合は、以下のようにします。 ::

  .. code-block:: vdm
  
  class Hoge
  （中略）
  end Hoge

