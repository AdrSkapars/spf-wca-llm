(declare-const in2 Int)
(declare-const in1 Int)
(declare-const in3 Int)

(assert (and (and  ( >=  in1 100)  ( >=  in2 100))  ( >=  in3 100)))

(check-sat)
(get-model)