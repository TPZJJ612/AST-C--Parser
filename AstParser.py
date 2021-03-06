#!/usr/bin/env python
#coding=utf-8
import sys
import clang.cindex
from clang.cindex import Config
from clang.cindex import _CXString
Config.set_compatibility_check(False)
Config.set_library_path("C:/Program Files (x86)/LLVM/bin")
# Config.set_library_path(sys.path[0])


def dumpnode(node, indent):
    '递归打印 C++ 语法树'
    # ...
    # do something with the current node here, i.e
    # check the kind, spelling, displayname and act baseed on those
    # kind     : 所查看的 AST 节点的类型, 该节点是类定义 是函数定义 还是参数声明
    # spelling : 标记的文本定义. 比如游标指向 void foo(int x); 这样一个函数声明，该游标
    #            的 spelling 则是 foo.
    # ...
    text = node.spelling or node.displayname
    kind = str(node.kind)[str(node.kind).index('.')+1:]
    print ' ' * indent,'{} {}'.format(kind, text)
    for i in node.get_children():
        dumpnode(i, indent + 2)

# def check_argv():
#     if len(sys.argv) != 2:
#         print("Usage: clang_3.py [header file name]")
#         sys.exit()

def main():
    # check_argv()
    # clang.cindex.Config.set_library_path('/usr/local/Cellar/llvm/3.5.0/lib')
    index = clang.cindex.Index.create()
    # print sys.argv[1]
    a = "global.cpp"
    tu = index.parse(a, ['-x', 'c++', '-std=c++11', '-D__CODE_GENERATOR__'])
    # index = clang.cindex.Index.create()
    # tu = index.parse(a, ['-x', 'c++', '-std=c++11', '-D__CODE_GENERATOR__'])
    b = dumpnode(tu.cursor, 0)
    print b


if __name__ == '__main__':
    main()