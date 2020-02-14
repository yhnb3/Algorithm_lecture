INDENT = "         "
# INDENT = "#  "
def func_r(indent, k) :
    indent = indent + INDENT
    if k==5 :
        print(indent, "returned] TERMINAL");
        return

    for i in range(1,k+1) :
        print(indent, "k=%d, i=%d"%(k,i))
        func_r(indent, k+1)
        # func_r(indent, k)

    print(indent, "returned] func_r() <---------------")

##메인
func_r(INDENT,1)