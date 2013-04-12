# encoding: utf-8
# VDM lexerを試すサンプルだが、日本語が交じるとダメ
# ただし、日本語がダメなのは、lexerの問題ではなく、呼び出す時の問題だと思う

from pygments import highlight
from pygments_plugin.lexers.vdm import VDMLexer
from pygments.formatters import HtmlFormatter


if __name__ == '__main__':
    code = ''
    for line in file('FizzBuzz.vpp', 'r').readlines():
        code += line.decode('utf-8')

    highlight(code, VDMLexer(), HtmlFormatter(full=True), file('vdm.html', 'w'))

