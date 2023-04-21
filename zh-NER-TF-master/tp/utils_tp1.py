import logging, sys, argparse


def str2bool(v):
    # copy from StackOverflow
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_entity(tag_seq, char_seq):
    PER = get_per(tag_seq, char_seq)
    # TP = get_tp(tag_seq, char_seq)
    # O = get_O(tag_seq, char_seq)
    return PER


def get_per(tag_seq, char_seq):
    # length = len(char_seq)
    PER = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        # if tag == 'B-CH':
        #     if 'per' in locals().keys():
        #         PER.append(per)
        #         del per
        #     per = char
        #     if i + 1 == length:
        #         PER.append(per)
        # if tag == 'I-CH':
        #     try:
        #         per += char
        #     except UnboundLocalError:
        #         per = char
        #     if i + 1 == length:
        #         PER.append(per)
        #
        # if tag == 'B-SP':
        #     if 'per' in locals().keys():
        #         PER.append(per)
        #         del per
        #     per = char
        #     if i + 1 == length:
        #         PER.append(per)
        # if tag == 'I-SP':
        #     try:
        #         per += char
        #     except UnboundLocalError:
        #         per = char
        #     if i + 1 == length:
        #         PER.append(per)
        #
        # if tag == 'O':
        #     if 'per' in locals().keys():
        #         PER.append(per)
        #         del per
        #     per = char
        #     if i + 1 == length:
        #         PER.append(per)
        #
        # if tag not in ['I-CH', 'B-CH', "B-SP", "I-SP", "O"]:
        #     if "per" in locals().keys():
        #         PER.append(per)
        #         PER.append(char)
        #         del per
        #         continue
        if tag == "B-CH":
            PER.append("\\")
            PER.append(char)
        elif tag == "I-CH":
            PER.append(char)
        elif tag == "B-SP":
            PER.append("\\")
            PER.append(char)
        elif tag == "I-SP":
            PER.append(char)
        elif tag == "O":
            PER.append("\\")
            PER.append(char)
        else:
            PER.append("\\")
            PER.append(char)
    return PER


# def get_tp(tag_seq, char_seq):
#     length = len(char_seq)
#     PER = []
#     for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
#         if tag == 'Bsp':
#             if 'per' in locals().keys():
#                 PER.append(per)
#                 del per
#             per = char
#             if i + 1 == length:
#                 PER.append(per)
#         if tag == 'Isp':
#             try:
#                 per += char
#             except UnboundLocalError:
#                 per = char
#             if i + 1 == length:
#                 PER.append(per)
#         if tag not in ['Isp', 'Bsp']:
#             PER.append(per)
#             del per
#             continue
#     return PER
#
# def get_O(tag_seq, char_seq):
#     length = len(char_seq)
#     PER = []
#     for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
#         if tag == 'O':
#             if 'per' in locals().keys():
#                 PER.append(per)
#                 del per
#             per = char
#             if i + 1 == length:
#                 PER.append(per)
#         if tag not in ['O']:
#             PER.append(per)
#             del per
#             continue
#     return PER
# #


def get_logger(filename):
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logging.getLogger().addHandler(handler)
    return logger
