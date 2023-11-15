(declare-const in1 Int)

(assert  ( >=  in1 100))

(check-sat)
(get-model)