N = Int('N')
ss = Function('ss', IntSort(), IntSort())
x = Int('x')

prediction = If(N >= 3, 
                ForAll([x], 
                       Implies(And(0 <= x, x < N), 
                               And(ss(x) == 37, ss(x) != 36, ss(x) != 35, ss(x) != 64)
                              )
                      ),
                True
               )
