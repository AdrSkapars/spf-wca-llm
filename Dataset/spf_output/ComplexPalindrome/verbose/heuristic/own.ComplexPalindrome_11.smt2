(declare-const in6 Int)
(declare-const in8 Int)
(declare-const in7 Int)
(declare-const in9 Int)
(declare-const in10 Int)
(declare-const in0 Int)
(declare-const in2 Int)
(declare-const in1 Int)
(declare-const in4 Int)
(declare-const in3 Int)

(assert (and (and (and (and  ( <  in0 in10)  ( <  in1 in9))  ( <  in2 in8))  ( <  in3 in7))  ( <  in4 in6)))

(check-sat)
(get-model)