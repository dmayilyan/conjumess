#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import OrderedDict


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
        self.bold = True


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
            # print(self.w_1)

    def colorize(func):
        def make_red(*args):
            res = func(*args)
            return "\033[1;31m{0}\033[0;0m".format(res)
        return make_red

    @colorize
    def armdec_dict(self):
        """ making a dictionary for declination \033[1m  \033[0m"""
        return "Barev"
        # decs_arm_addons = OrderedDict([(("ես ", "ում եմ"), ""),
        #                                (("դու ", "ում ես"), ""),
        #                                (("նա ", "ում է"), ""),
        #                                (("մենք ", "ում ենք"), ""),
        #                                (("դուք/Դուք ", "ում եք"), ""),
        #                                (("նրանք ", "ում են"), "")])

        # # building the sentence
        # decs_arm_raw = [x[0] + self.vrb + x[1] for x in decs_arm_addons]

        # #  getting the space locations
        # bold_list = []
        # for elm in decs_arm_raw:
        #     space_pos = []
        #     for i, c in enumerate(elm):
        #         if " " == c:
        #             space_pos.append(i)

        #     # making it bold
        #     bold_list.append(elm[:space_pos[0]] +
        #                      "\033[1;31m" +
        #                      elm[space_pos[0]:space_pos[1]] +
        #                      "\033[0;0m" + elm[space_pos[1]:])
        #     # print(bold_line)
        # return bold_list


def hy_de(in_verb):
    """ Armenian declination with german verbs """
    # print(in_verb)
    x = de_other(in_verb)
    x.dec_list(in_verb)
    # armdec_list = x.armdec_dict()
    print(x.armdec_dict())
    # print(x.refl)

    # for i in range(3):
    #     print(armdec_list[i], armdec_list[i+3], sep="\t")

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
