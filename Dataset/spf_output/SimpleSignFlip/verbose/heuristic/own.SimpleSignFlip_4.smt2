(declare-const in0 Int)
(declare-const in2 Int)
(declare-const in1 Int)
(declare-const in3 Int)

(assert (and (and  ( ==  in0 in1)  ( <  in1 in2))  ( ==  in2 in3)))

(check-sat)
(get-model)