# malware_detector_folder.py
import os
import re
from time import sleep
from load import start
import colorama


print(colorama.Fore.BLUE)
print("**************************************************************************************")
print("**************************************************************************************")
print("**                                                                                  **")
print("**                                                                                  **")
print("**     **********  **********  **********  **********  ***    ***      *********    **")
print("**     ***    ***  **********  **********  **********  ***    ***      *********    **")
print("**     ***    ***  ***    ***     ****     ***         ***    ***            ***    **")
print("**     **********  ***    ***     ****     ***         **********  ****      ***    **")
print("**     **********  **********     ****     ***         **********  ****      ***    **")
print("**     ***    ***  **********     ****     ***         ***    ***            ***    **")
print("**     ***    ***  ***    ***     ****     **********  ***    ***            ***    **")
print("**     **********  ***    ***     ****     **********  ***    ***            ***    **")
print("**                                                                                  **")
print("**             KANNAN   B                                                           **")
print("**                             KRISHNA KUMAR    E                                   **")
print("**                                                      MADHAVAN  M                 **")
print("**                                                                                  **")
print("**         Disclaimer: The code shared is for educational purposes only             **")
print("**         Use it responsibly, and we are not liable for any consequences           **")
print("**         resulting from its application in real-world scenarios.                  **")
print("**                                                                                  **")
print("**************************************************************************************")
print("**************************************************************************************")
print(colorama.Fore.RESET)

sleep(3)




def load_signatures():
    # Example signatures (modify or expand based on actual signatures)
    signatures = {
        b'\x90\x90\x90\x90': 'NOP Sled',
        b'\xD9\xEE\xD9\x74\x24\xF4\x59': 'Metasploit Payload',
        b'\x55\x8B\xEC\x83\xEC\x08': 'Stack Frame Setup',
        b'\xE8\x00\x00\x00\x00': 'Call Instruction',
        b'\xEB\xFE': 'Jump Backward',
        b'\x33\xC0\xC3': 'XOR and RET',
        b'\xB8\xFF\xFF\xFF\x7F': 'Infinite Loop',
        b'\xCC': 'Int3 Breakpoint',
        b'\xE9\x68\x32\xC7': 'JMP Instruction',
        b'\xE8\x4B\x3D\xE0\xFF': 'CALL Instruction',
        b'\xC3': 'RET Instruction',
        b'\x0F\x01\xD0': 'VMCALL Instruction'
        '''
        b'\x55\x8B\xEC\x83\xEC\x08': 'Stack Frame Setup',
        b'\xE8\x00\x00\x00\x00': 'Call Instruction',
        b'\xEB\xFE': 'Jump Backward',
        b'\x33\xC0\xC3': 'XOR and RET',
        b'\xB8\xFF\xFF\xFF\x7F': 'Infinite Loop',
        b'\x8B\x45\x08\x89\x45\xF8': 'Stack Variable Manipulation',
        b'\x8D\x7D\xF4\x8B\x4D\xF8': 'Register Indirect Loading',
        b'\xBA\xAD\xDE\xEF\xFE': 'Magic Value',
        b'\xCC': 'Int3 Breakpoint',
        b'\x0F\x0B': 'UD2 Instruction',
        b'\x2E\x2E\x2E': 'Ellipsis',
        b'\x55\x55\x55\x55': 'Repeating Values',
        b'\x41\x41\x41\x41': 'Repeating ASCII Values',
        b'\xDE\xAD\xBE\xEF': 'Dead Beef',
        b'\xCA\xFE\xBA\xBE': 'Cafebabe',
        b'\xAA\xAA\xAA\xAA': 'Repeating AAAA',
        b'\xBB\xBB\xBB\xBB': 'Repeating BBBB',
        b'\xCC\xCC\xCC\xCC': 'Repeating CCCC',
        b'\xDD\xDD\xDD\xDD': 'Repeating DDDD',
        b'\xEE\xEE\xEE\xEE': 'Repeating EEEE',
        b'\xFF\xFF\xFF\xFF': 'Repeating FFFF',
        b'\x41\x42\x43\x44': 'ABCD',
        b'\x31\x32\x33\x34': '1234',
        b'\x78\x56\x34\x12': 'Little-endian Byte Order',
        b'\x12\x34\x56\x78': 'Big-endian Byte Order',
        b'\x4D\x5A': 'MZ Header (Executable)',
        b'\x50\x45\x00\x00': 'PE Signature',
        b'\x7F\x45\x4C\x46': 'ELF Header',
        b'\x25\x50\x44\x46': 'PDF Header',
        b'\x4F\x67\x67\x53': 'OGG Header',
        b'\x1F\x8B\x08': 'Gzip Header',
        b'\x42\x5A\x68': 'Bzip2 Header',
        b'\x37\x7A\xBC\xAF': '7z Header',
        b'\xFD\x37\x7A\x58\x5A\x00\x00': 'xz Header',
        b'\x30\x39\x0A': 'INI File Signature',
        b'\x2F\x2A': 'C Style Comment',
        b'\x3B': 'Semicolon (;) Comment',
        b'\x23': 'Hash (#) Comment',
        b'\x2F\x2F': 'Double Slash (//) Comment',
        b'\x2D\x2D': 'Double Dash (--) Comment',
        b'\x2D\x2D\x3E': 'Arrow (->) Sequence',
        b'\x2F\x2A\x20': 'C Style Comment with Space',
        b'\x21\x2F\x42\x49': 'Shebang (#!) Script Header',
        b'\xE9\x68\x32\xC7': 'JMP Instruction',
        b'\xE8\x4B\x3D\xE0\xFF': 'CALL Instruction',
        b'\xC3': 'RET Instruction',
        b'\xC2\x10\x00': 'RET Instruction with Pop',
        b'\xC9\xC3': 'LEAVE and RET Instructions',
        b'\xC9\xC2\x10\x00': 'LEAVE and RET Instructions with Pop',
        b'\xC9': 'LEAVE Instruction',
        b'\xF3\x0F\x1E\xFB': 'NOP Instruction',
        b'\xF4': 'HLT Instruction',
        b'\xCD\x20': 'INT 20h',
        b'\xCD\x21': 'INT 21h',
        b'\x0E': 'PUSH CS',
        b'\x1F': 'PUSH DS',
        b'\x07': 'POP ES',
        b'\x17': 'POP SS',
        b'\x9C': 'PUSHF',
        b'\x9D': 'POPF',
        b'\xFC': 'CLD',
        b'\xFD': 'STD',
        b'\xFA': 'CLI',
        b'\xFB': 'STI',
        b'\x66\x0F\x3A\x0F\xD5': 'AES-NI Instruction',
        b'\x0F\x01\xD0': 'VMCALL Instruction',
        b'\x0F\x01\xD1': 'VMLAUNCH Instruction',
        b'\x0F\x01\xD2': 'VMRESUME Instruction',
        b'\x0F\x01\xD4': 'VMXOFF Instruction',
        b'\x0F\x01\xD5': 'VMXON Instruction',
        b'\x0F\x3F\x0F': 'RDTSCP Instruction',
        b'\x0F\x05': 'SYSCALL Instruction',
        b'\x0F\x34': 'SYSENTER Instruction',
        b'\x0F\x35': 'SYSEXIT Instruction',
        b'\x0F\x22\xC0': 'PAUSE Instruction',
        b'\xC4\xE2\x79\x7D': 'VMP0 Algorithm',
        b'\xC4\xE2\x7A\x7D': 'VMP1 Algorithm',
        b'\xC4\xE2\x7B\x7D': 'VMP2 Algorithm',
        b'\xC4\xE2\x7C\x7D': 'VMP3 Algorithm',
        b'\xC4\xE2\x7D\x7D': 'VMP4 Algorithm',
        b'\xC4\xE2\x7E\x7D': 'VMP5 Algorithm',
        b'\xC4\xE2\x7F\x7D': 'VMP6 Algorithm',
        b'\xC4\xE2\x80\x7D': 'VMP7 Algorithm',
        b'\xC4\xE2\x81\x7D': 'VMP8 Algorithm',
        b'\xC4\xE2\x82\x7D': 'VMP9 Algorithm',
        '''
    }
    return signatures

def analyze_file(file_path, signatures):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()

            for signature, signature_type in signatures.items():
                match = re.search(re.escape(signature), content)
                if match:
                    start_offset = match.start()
                    end_offset = match.end()
                    located_signature = content[start_offset:end_offset].hex()
                    print(f"\nMalware Signature Detected in {file_path}: {signature_type}")
                    print(f"Signature Type: {signature_type}")
                    print(f"Start Offset: {start_offset}, End Offset: {end_offset}")
                    print(f"Located Signature: {located_signature}\n")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def detect_malware_in_folder(folder_path):
    signatures = load_signatures()

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            analyze_file(file_path, signatures)

if __name__ == "__main__":
    print("\n\n")
    folder_path = input("Enter the folder path: ")
    print("\n")
    start("DETECTING")
    sleep(2)
    detect_malware_in_folder(folder_path)
print(f"\n\n{colorama.Fore.RED}THESE ARE THE MALWARE FIND IN YOUR FOLDER PATH{colorama.Fore.RESET}")
