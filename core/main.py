#coding: utf-8
from __future__ import division
import sys
from sympy import *

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols("a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z")
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = symbols("A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z")

data = input()
try:
	f = data["f"]
	eval(f)
except:
	print "函数输入错误！"
	sys.exit(1)
#print latex(f)

try:
	variables = data["variables"].replace("\n", ",")
except:
	print "变量参数错误！"
	sys.exit(1)
#print variables

command = 'Integral(%s, %s)' % (f, variables)
try:
	d = eval(command)
except:
	print "输入数据错误！"
	sys.exit(2)

print "$$%s = %s$$" % (latex(d), latex(d.doit()))
sys.exit(0)

