(declare-const in6 Int)
(declare-const in5 Int)
(declare-const in8 Int)
(declare-const in7 Int)
(declare-const in0 Int)
(declare-const in2 Int)
(declare-const in1 Int)
(declare-const in4 Int)
(declare-const in3 Int)

(assert (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (not ( = in0 95))  ( ==  in0 45)) (not ( = in1 95)))  ( ==  in1 45)) (not ( = in2 95)))  ( ==  in2 45)) (not ( = in3 95)))  ( ==  in3 45)) (not ( = in4 95)))  ( ==  in4 45)) (not ( = in5 95)))  ( ==  in5 45)) (not ( = in6 95)))  ( ==  in6 45)) (not ( = in7 95)))  ( ==  in7 45)) (not ( = in8 95)))  ( ==  in8 45)))

(check-sat)
(get-model)