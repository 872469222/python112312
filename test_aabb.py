# -*- coding: utf-8 -*-
# Auther : SHL
# Date : 2023-05-17 21:52
# File : test_demo.py
import pytest


def doubule(a):
    return a * 2


# 测试数据：整型
@pytest.mark.int
def test_doubule_int():
    print("test double int")
    assert 2 == doubule(1)


# 测试数据：负数
@pytest.mark.minus
def test_doubule1_minus():
    print("test double minus")
    assert -2 == doubule(-1)


# 测试数据：浮点型
@pytest.mark.float
def test_doubule_float():
    assert 0.2 == doubule(0.1)


@pytest.mark.float
def test_doubule2_minus():
    assert -0.2 == doubule(-0.1)


@pytest.mark.zero
def test_doublle_0():
    assert 10 == doubule(0)


@pytest.mark.bignum
def test_double_bignum():
    assert 200 == doubule(100)


@pytest.mark.str
def test_double_str():
    assert 'aa' == doubule('a')


@pytest.mark.str
def test_double_str1():
    assert 'a$a$' == doubule('a$')


if __name__ == '__main__':
    #1.运行当前目录下所有的用例
    pytest.main()
    #2.运行./目录下所有（test_*py  和 *_test.py）
    #pytest.main(['/','-vs'])
    #3.运行test_mark1.py::test_dkej模块中的某一条用例
   # pytest.main(['test_command_param.py','-vs','-m','str'])
    #4.运行某个标签
    #   pytest.main(['test_mark1.py','-vs','-m','dkej'])