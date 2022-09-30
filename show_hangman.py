# 1 - print 'Stand'
# 2 - additionaly print 'Bar'
# 3 - additionaly print 'Rope'
# 4 - additionaly print 'Head'
# 5 - additionaly print 'Body'
# 6 - additionaly print 'Right hand'
# 7 - additionaly print 'Left hand'
# 8 - additionaly print 'Right leg'
# 9 - additionaly print 'Left leg'


def txt_to_show(n):

    """
    Picture of hangman.
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

