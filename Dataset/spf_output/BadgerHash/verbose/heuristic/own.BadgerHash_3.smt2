(declare-const put2_1 Int)
(declare-const put2_0 Int)
(declare-const put1_1 Int)
(declare-const put1_0 Int)
(declare-const put0_0 Int)
(declare-const put0_1 Int)
(declare-const get0 Int)
(declare-const get1 Int)

(assert (and (and (and (and (and (and  ( ==  0 ( %  ( +  put0_1 put0_0) 3))  ( ==  0 ( %  ( +  put1_1 put1_0) 3)))  ( ==  0 ( %  ( +  put2_1 put2_0) 3)))  ( ==  0 ( %  ( +  get1 get0) 3))) (not ( = put0_0 get0))) (not ( = put1_0 get0))) (not ( = put2_0 get0))))

(check-sat)
(get-model)