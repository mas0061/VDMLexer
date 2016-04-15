# Pygments lexer for VDMについて

## VDMLexerの概要
VDMLexerは、 [Sphinx](http://sphinx-users.jp/) や [Trac](http://trac.edgewall.org/) で使われている、
シンタックスハイライトライブラリー **[Pygments](http://pygments.org/)** のVDM用プラグインです。
このプラグインを使うと、SphinxでVDMコードを貼りつけた時に、予約語がハイライトして出力することができます。


## VDMLexerのインストール
VDMLexerのインストールは以下のようにします。

* 前提条件
    * Pythonがインストールされていること
    * Pythonのパッケージ管理ツールであるpipかeasy_installがインストールされていること

* インストール
    * [pygments_plugin_vdm_lexer-1.0-py2.7.egg](https://github.com/mas0061/VDMLexer/releases/download/v1.0.0/pygments_plugin_vdm_lexer-1.0-py2.7.egg) をダウンロード
    * コマンドラインで、以下のコマンドを入力

         * `easy_install pygments_plugin_vdm_lexer-1.0-py2.7.egg`

## VDMLexerのビルド
```bash
% cd LexerDev
```

### easy_install向けのeggを作成する場合
```bash
% python setup.py bdist_egg
```

これで、 *pygments_plugin_vdm_lexer-1.0-py\*.\*.egg* がdistディレクトリ下にできます。

### pip向けのwheelを作成する場合
```bash
% python setup.py bdist_wheel
```

これで、 *pygments_plugin_vdm_lexer-1.0-py\*-none-any.whl* がdistディレクトリ下にできます。

## VDMLexerの使い方（Sphinxで使う場合）
VDMLexerを用いて、Sphinxでシンタックスハイライトをするには、以下のようにします。

```rst
.. literalinclude:: vdm/hoge.vpp
   :language: vdm
```

literalincludeを使わない場合は、以下のようにします。

```rst
.. code-block:: vdm

  class Hoge
  （中略）
  end Hoge
```
