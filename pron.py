#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


class de_other:
    """German word declination in other languages"""


    def __init__(self, arg_words):
        super(de_other, self).__init__()
        # print(arg_words[1])
        
        if (len(arg_words) < 1) | (len(arg_words) > 2):
            print("Too many or too little arguments \nNo. of args:\t",
                  len(arg_words))
            exit()

        self.w_1 = arg_words[0]
        try:
            self.w_2 = arg_words[1]
            if "զիխ" in (self.w_1, self.w_2):
                self.refl = True
                print("զիխ գտա")
            else:
                print("Not a right verb!")
                exit()
            pass
        except IndexError:
            self.refl = False
            print("Non-reflexive verb")
        self.vrb = ""
        self.dec = []  # declination list


# reflexive doesn't work
    def dec_list(self, in_verb):
        """ making the word list """
        print(self.refl)
        if self.refl:
            if self.w_1 == "զիխ":
                self.vrb = self.w_2[:-2]
            else:
                self.vrb = self.w_1[:-2]
            # print(self.w_1, self.w_2)
        else:
            self.vrb = self.w_1[:-2]
            print(self.w_1)

    def armdec_dict(self):
        """ making a dictionary for declination """
        decs_arm = {("ես ", "ում եմ"): "",
                    ("դու ", "ում ես"): "",
                    ("նա ", "ում է"): "",
                    ("մենք ", "ում ենք"): "",
                    ("դուք/Դուք ", "ում եք"): "",
                    ("նրանք ", "ում են"): ""}

        [print(x[0] + self.vrb + x[1]) for x in decs_arm]

        print(self.vrb)


def hy_de(in_verb):
    """ Armenian declination with german verbs """
    # print(in_verb)
    x = de_other(in_verb)
    x.dec_list(in_verb)
    x.armdec_dict()
    print(x.dec)
    # if in_verb[-4:-2] == "են":
    #     print("\n\n\n\n")
    #     root = in_verb[2:-4]
    #     print("ես " + root+"ում եմ\t", "մենք " + root + "ում ենք")
    #     print("դու " + root+"ում ես\t", "դուք " + root + "ում եք")
    #     print("նա " + root+"ում է\t", "նրանք " + root + "ում են\n\n\n\n")

    # else:
    #     print("Not a german verb\nTry again!")

    # print(in_verb[-4:-2])


def main(in_verb):
    ''' main function for all crazy stuff '''
    # print(type(in_verb))
    # in_verb = argv
    hy_de(in_verb)


if __name__ == '__main__':
    main(sys.argv[1:])
