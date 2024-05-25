#!/usr/bin/env python3
'''
Detects the amount of RISC-V Vector (RVV) commands in a RISC-V binary (including library)

$ ./rvv_detector.py  /home/sander/risc-binaries/sabctools.cpython-312-riscv64-linux-gnu.so
number of RVV commands 416 (and 7648 non-RVV commands)

'''

# objdump -d --no-addresses --no-show-raw-insn /home/sander/risc-binaries/sabctools.cpython-312-riscv64-linux-gnu.so
objdump_output = """
        ld      a3,0(a5)
        ld      a5,8(a5)
        vsetivli        zero,16,e8,m1,ta,ma
        sd      a3,40(sp)
        sd      a5,48(sp)
        addi    a5,sp,40
        vle8.v  v9,(a5)
        vsetvli zero,a2,e16,mf2,ta,ma
        vmv.v.i v8,4
        bgez    a4,<_Z14do_encode_simdIL_ZN9RapidYenc13do_encode_rvvEiPiPKhRrPhRmEEmiS1_S3_S4_mi+0x1a6>
        lui     a5,0x1
        addi    a5,a5,-1523 # <_PROCEDURE_LINKAGE_TABLE_-0x3683>
        sd      s7,104(sp)

"""

import sys
import magic
import os

debug = False

def check_if_riscv_binary(file):
    # ELF 64-bit LSB executable, UCB RISC-V
    # ELF 64-bit LSB shared object, UCB RISC-V
    try:
        magic_output = magic.from_file(file)
        return "ELF 64-bit" in magic_output and "RISC-V" in magic_output
    except:
        return False

try:
    file = sys.argv[1]
except:
    print("Specify file")
    sys.exit(1)

if not os.path.isfile(file):
    print(f"{file} is not a file")
    sys.exit(1)

if not check_if_riscv_binary(file):
    print(f"{file} is not a risc-v binary")
    sys.exit(1)

# run objdump
rvv_counter = non_rvv_counter = 0
cmd = f"objdump -d --no-addresses --no-show-raw-insn {file}"
for line in os.popen(cmd).readlines():
    try:
        if line.split()[0].startswith("v"):
            if debug:
                print(line.strip())
            rvv_counter += 1
        else:
            non_rvv_counter += 1
    except:
        pass

print(f"number of RVV commands {rvv_counter} (and {non_rvv_counter} non-RVV commands)")
