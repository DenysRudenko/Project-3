"""
Description about hangman.

1 - print 'Stand',2 - additionaly print 'Bar',3 - additionaly print 'Rope',4 - additionaly print 'Head',5 - additionaly print 'Body'
6 - additionaly print 'Right hand',7 - additionaly print 'Left hand',8 - additionaly print 'Right leg',9 - additionaly print 'Left leg'
"""


def txt_to_show(n):
    """
    About function.

    Picture of hangman and properties that represents for showing the correct part of the body to user,

    depends how much incorrect letters user gets.
    """
    t1 = "-------------    "  # bar
    t21 = "|| "               # stand
    t22 = "         |    "    # rope
    t31 = "|| "               # stand
    t32 = "         o    "    # head
    t41 = "|| "               # stand
    t42 = "      ---"         # right hand
    t43 = "|"                 # body
    t44 = "--- "              # left hand
    t51 = "|| "               # stand
    t52 = "         |    "    # body
    t61 = "|| "               # stand
    t62 = "        /"         # right leg
    t63 = " \\  "             # left leg
    t71 = "|| "               # stand
    t72 = "      _/ "         # right leg
    t73 = "  \\_"             # left leg
    t8 = "||              "   # stand
    t9 = "===              "  # stand
    pad = "    "

    s1 = t1 if n >= 2 else ""
    s2 = (t21 if n >= 1 else "") + (t22 if n >= 3 else "")
    s3 = (t31 if n >= 1 else "") + (t32 if n >= 4 else "")
    s4 = (t41 if n >= 1 else "") + (t42 if n >= 6 else "         ") + \
        (t43 if n >= 5 else "") + (t44 if n >= 7 else "")
    s5 = (t51 if n >= 1 else "") + (t52 if n >= 5 else "")
    s6 = (t61 if n >= 1 else "") + (t62 if n >=
                                    8 else "") + (t63 if n >= 9 else "")
    s7 = (t71 if n >= 1 else "") + (t72 if n >=
                                    8 else "") + (t73 if n >= 9 else "")
    s8 = t8 if n >= 1 else ""
    s9 = t9 if n >= 1 else ""
    return "\n".join([pad + s1, pad + s2, pad + s3, pad + s4, pad + s5, pad + s6, pad + s7, pad + s8, pad + s9])
