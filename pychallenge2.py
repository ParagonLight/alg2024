from email import iterators


input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
input = 'map'
out_words = ""

print(len(input))

for w in input:
    ascii_w = ord(w)
    if ascii_w >= ord('a') and ascii_w <= ord('z'):
        n_w = ascii_w + 2
        if n_w > ord('z'):
            n_w -= 26
        n_w_chr = chr(n_w)
    else:
        n_w_chr = w
    out_words += n_w_chr
    print(w, ord(w), n_w_chr)
print(out_words)