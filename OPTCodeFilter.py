import os
import shutil
import subprocess


path = "/home/"
destination = "/home/optcode/"
destinationImg = "/home/destinationImg/"


filter_words = {'aaa', "aad", "aam", "amx", "aas", "aci", "add", "adc", "adx", "adi", "adsize", "ana", "and", "arpl",
                "andps", "andpd", "andnps", "andnpd", "addps", "addss", "addpd", "addsd", "addsubpd", "addsubps",
                "bound", "blendvps", "blendvpd", "blendps", "blendpd", "blendpw", "bt", "bts", "btr", "btc", "bsf",
                "brs", "bswap",
                "call", "callq", "callf", "cmp", "cmpl", "cmps", "cmpsb", "cmpsw", "cmpw", "clc", "cld", "cli", "cs",
                "cbw", "cwd", "cdq", "cwde", "cmove", "cmc", "clts", "comiss", "comisd", "cmovs", "cmovne", "cmovo",
                "cmovno", "cmovb", "cmovnae", "cmovc", "cmovnb", "cmovae", "cmovnc", "cmovz", "cmove", "cmovnz",
                "cmovne", "cmovbe", "cmovna", "cmovnbe", "cmova", "cmovns", "cmovp", "cmovpe", "cmovpp", "cmovpo",
                "cmovl", "cmovnge", "cmovnl", "cmovge", "cmovle", "cmovg", "cmovnle", "cmovg", "cmpxchg", "cupid",
                "clflush", "cmpps", "cmppd", "cmpsd", "ctrl",
                "das", "dec", "ds", "daa", "div", "dpps", "dppd", "divps", "divss", "divpd", "divsd",
                "es", "enter", "esc", "extractps", "emms",
                "fs", "fwait", "fadd", "fmul", "focm", "fcomp", "fsub", "fsubr", "fdiv", "fdivr", "fld", "fxch", "fst",
                "fnop", "fstp", "fstp1", "flednv", "fchs", "fabs", "ftst", "fxam", "fldcw", "fld1", "fldl2t", "fldl2e",
                "fldpi", "fldlg2", "fldz", "fnstenv", "f2xm1", "fyl2x", "fptan", "fpatan", "fxtract", "fprem1",
                "fdecstp", "fxsave", "fxrstor", "fninit",
                "fincstp", "fnstcw", "fstcw", "frem", "fyl2xp1", "fsqrt", "fsincos", "frdint", "fscale", "fsin", "fcos",
                "fiadd", "fcmove", "fimul", "ficom", "fcmovbe", "ficomp", "fcmovu", "fisub", "fisubr", "fucompp",
                "fidiv",
                "fidivr", "fild", "fcmovnb", "fist", "fistp", "fisttp", "fcmovnb", "fisttp", "fcmovnbe", "fcmovne",
                "fcmovnbe", "fcmovnu", "fneni", "fndisi", "fnclex", "fnint", "finit", "fnsetpm", "fucomi", "fcomi",
                "fucom", "fucomp", "fnsave", "fsave", "fnstsw", "fstsw", "fiadd", "faddp", "fimul", "fmulp",
                "gs", "getsec",
                "hlt", "hint_nop", "haddpd", "haddps", "hsubpd", "hsubps",
                "imul", "int", "int1", "int3", "into", "iret", "iretd", "in", "inc", "ins", "insb", "insw", "insd",
                "incl", "insertps",
                "icebg", "imul", "idiv", "invlpg", "invd", "invetp", "invept", "invvpid",
                "jo", "jno", "jb", "jnb", "jmp", "jz", "jnz", "ja", "js", "jns", "jcz", "jne", "je", "jbe",
                "jp", "jnp", "jl", "jnl", "jle", "jnle", "jnae", "jc", "jae", "jnc", "jna", "jnbe", "jmpq", "jmpf",
                "jpe", "jop", "jnge", "jge", "jng", "jmdp", "jile", "jg", "jcxz", "jecxz", "jpo",
                "lahf", "lea", "leave", "lodsb", "loopnz", "loopz", "lock", "loop", "les", "lds", "lods", "lodsw",
                "lodsd", "ldmxcsr", "lfence", "lss", "lfs", "lgs", "lddqu",
                "loopne", "lldt", "ltr", "lgdt", "lidt", "lmsw", "lar", "lsl",
                "mov", "movd", "movl", "movsb", "movsw", "movslq", "movs", "movsd", "movzbl", "movzwl", "movabs",
                "movq", "movapd", "mpsadbw", "movmskps", "movmskpd", "multps", "mulss", "mulpd", "mulsd", "maxss",
                "movaps", "mul", "monitor", "mwait", "mobups", "movss", "movupd", "movsd", "movhlps", "movlps", "maxps",
                "movdupp", "movsldup", "movlpd", "movlhps", "movhps", "movhpd", "movhsdup", "movntps", "movntpd",
                "maxpd", "maxsd", "movdqa", "movdqu", "mfence", "movzx", "movsx", "movnti", "movntq", "movntdq",
                "movbe", "movups", "movddup", "movshdup", "movntdqa", "minps", "minss", "minpd", "minss", "minsd",
                "maskmovq", "maskmovdqu", "movzble",
                "nopl", "nopw", "nop", "neg", "not",
                "opsize", "or", "outsb", "outsw", "outs", "out", "orps", "orpd",
                "pop", "popa", "popad", "popf", "popfd", "push", "pusha", "pushf", "pushfd", "pushad", "pause", "psubb",
                "pmaxsw", "palignr", "pextrb", "pextrw", "pextrd", "pinsrb", "pinsrd", "pinsrq", "pcmpestrm", "pavgw",
                "pcmpestri", "pshufw", "pshuflw", "pshufhw", "pshufd", "psrlw", "psraw", "psllw", "psrld", "psrad",
                "pslld", "psllq", "psrlq", "psrldq", "pcmpeqb", "pcmpeqw", "pcmpeqd", "pinsrw", "paddq", "pmullw",
                "prefetchnta", "prefetchnt0", "prefetchnt1", "prefetchnt2", "pshufb", "pcmpgtq", "pminsb", "pminuw",
                "phaddw", "phaddd", "phaddsw", "pmaddubsw", " pmaddun2", "pushbw", "phusubd", "phusubsw", "psignb",
                "psignw", "pblendvb", "packusdw", "pmovzxbw", "pmovzxbd", "pmovzxbq", "pminud", "pmaxsb", "pmaxsb",
                "pmulhrsw", "plendvb", "ptest", "pabsb", "pabsw", "pansd", "pmovsxbd", "pmovsxbq", "pmovsxwq", "pmaxsd",
                "pmovsxdq", "pmovsxbw", "pmovsxqw", "pmovsxbd", "pmovsxwd", "pmovsxwq", "pmovsxdq", "pmuldq", "pcmpeqq",
                "punpcklbw", "punpckldw", "punpckldq", "packsswd", "pcmpgtb", "pcmgtw", "pcmpgtd", "packuswb", "psubw",
                "psubsb", "psubsw", "pminsw", "por", "paddsb", "paddsw", "pxor", "pmuludq", "pmaddwd", "psadbw",
                "punpckhbw", "punpckhwd", "punpckhdq", "packssdw", "punpcklqdq", "popcnt", "pmovmskb", "psubusb",
                "psubusw", "pminub", "pand", "paddusb", "paddusw", "pmaxub", "pandn", "pavgb", "pmulhuw", "pmulhw",
                "psubd", "psubq", "paddb", "paddw", "paddd",
                "retq", "retf", "retn", "repne", "rep", "rol", "ror", "rcl", "rcr", "rex.W",
                "repnz", "repe", "rdtscp", "rdtsc", "rundps", "roundpd", "roundss", "roundsd", "roundps",
                "roundpd", "roundss", "roundsd", "repz", "rsqrtps", "rsqrtss", "rcpps", "rsm",
                "sbb", "sub", "sahf", "salc", "scasb", "scasw", "ss", "sti", "stosb", "stos", "stosd", "scas", "seta",
                "sete", "sqrtps", "sqrtss", "sqrtpd", "sqrtsd", "subps", "subss", "subpd", "subsd", "seto", "setno",
                "setb", "setnae", "setc", "setnb", "setae", "setnc", "setz", "setnz", "setnp", "setpo", "setl", "setg",
                "setnge", "setnl", "setge", "setle", "setng", "setnle", "stmxcsr", "sfence", "shufps", "shufpd",
                "stosw", "stc", "std", "str", "shl", "sal", "shr", "setalc", "sldt", "sgdt", "sidt", "smsw", "sysenter",
                "sysexit", "setne", "setbe", "setna", "setnbe", "sets", "setns", "setp", "setpe", "shld", "shrd",
                "test", "twobyte", "testb",
                "verr", "verw", "vmcall", "vmlaunch", "vmresume", "vmxoff", "vmread", "vmwrite", "vmptrld", "vmclear",
                "vmxon", "vmptrst",
                "xchg", "xlat", "xor", "xlatb", "xgetbv", "xsetbv", "xorps", "xorpd", "xsave", "xrstor", "xadd",
                "ud2", "unpcklps", "unpcklpd", "ucomiss", "ucomisd", "unpckhps", "unpckhpd",
                "wait", "wbinvd", "wrmsr"}

os.chdir(path)

os.mkdir(destinationImg)


dictionary = {}


for filename in os.listdir():
    if filename.endswith(""):
        subprocess.run(f'objdump -b binary -D -m i386 {filename}  > {filename}.txt ',
                       shell=True)
        print("OPT code extraction")

os.mkdir(destination)

with open('/home/legend/' + 'legend.txt', "r") as f:
    for line in f:
        s = line.strip().split(" ")
        dictionary[s[0]] = s[1]


def filter_text_file(file_path):
    newLines = []

    with open(file_path, 'r') as f:

        for line in f:
            words = line.split()
            for word in words:
                if word in filter_words:
                    newLines.append(word)

    theFile = open(file_path, 'w')
    for line in newLines:
        theFile.write(line)
        theFile.write(" ")
    theFile.close()


def filter_grb_value(file_path):
    data = []

    with open(file_path, 'r') as f1:
        for line1 in f1:
            words = line1.split()

        for data_item in words:
            for key, values in dictionary.items():
                if key == str(data_item):
                    data.append(values)

        file = open(file_path, "w")
        for values in data:
            file.write(values)
            file.write("\n")
        file.close()


for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
        filter_text_file(file_path)
        filter_grb_value(file_path)
        print("RGB filtered")



for filenames in os.listdir():
    if filenames.endswith(".txt"):
        shutil.move(pathcp + filenames, destination + filenames)



