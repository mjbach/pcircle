class T:
    WORK_REQUEST    = 1
    WORK_REPLY      = 2
    REDUCE          = 3
    BARRIER         = 4
    TOKEN           = 7

class G:

    ZERO            = 0
    ABORT           = -1
    WHITE           = 50
    BLACK           = 51
    NONE            = -99
    TERMINATE       = -100
    MSG             = 99

    detail_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    simple_fmt = '%(name)s - %(levelname)s - %(rank)s - %(message)s'
    bare_fmt   = '%(message)s'

    str = {WHITE: "white", BLACK: "black", NONE: "not set", TERMINATE: "terminate",
           ABORT: "abort", MSG: "message"}

