Pygments lexer for VDMについて
=================================

VDMLexerの概要
------------------
VDMLexerは、 [Sphinx](http://sphinx-users.jp/) や [Trac](http://trac.edgewall.org/) で使われている、
シンタックスハイライトライブラリー「 [Pygments](http://pygments.org/) 」のVDM用プラグインです。
このプラグインを使うと、SphinxでVDMコードを貼りつけた時に、予約語がハイライトして出力することができます。


VDMLexerのインストール
---------------------------
VDMLexerのインストールは以下のようにします。

* 前提条件

  * Pythonがインストールされていること
  * Pythonのパッケージ管理ツールであるeasy_installがインストールされていること

* インストール
    
  * コマンドラインで、以下のコマンドを入力
  
     * `easy_install pygments_plugin_vdm_lexer-0.1-py2.6.egg`


VDMLexerの使い方（Sphinxで使う場合）
-----------------------------------------
VDMLexerを用いて、Sphinxでシンタックスハイライトをするには、以下のようにします。

    .. literalinclude:: vdm/hoge.vpp
       :language: vdm

literalincludeを使わない場合は、以下のようにします。

    .. code-block:: vdm
    
      class Hoge
      （中略）
      end Hoge

