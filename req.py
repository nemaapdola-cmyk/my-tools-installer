#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AI Development Tools Installer
--------------------------------------------------
A robust script to install AI CLI tools on Linux.
Tools included: Amp Code, Atlassian CLI (Rovo Dev), Google Gemini, Qwen Code.

Author: [Macro/Handle]
License: MIT
"""

import subprocess
import shutil
import sys
import os
import platform
import time

# --- Terminal Colors ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_step(message):
    print(f"\n{Colors.BLUE}🔵 {message}{Colors.ENDC}")

def print_success(message):
    print(f"{Colors.GREEN}✅ {message}{Colors.ENDC}")

def print_error(message):
    print(f"{Colors.FAIL}❌ {message}{Colors.ENDC}")

def print_warning(message):
    print(f"{Colors.WARNING}⚠️  {message}{Colors.ENDC}")

def run_command(command, tool_name, shell=True, check=True):
    """
    Execute a shell command with error handling.
    """
    try:
        subprocess.run(command, shell=shell, check=check, executable='/bin/bash')
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"فشل تثبيت {tool_name} (Failed to install {tool_name}).")
        print(f"   Error Details: {e}")
        return False

def check_requirements():
    """
    Ensure basic requirements (curl, npm, sudo) exist.
    """
    missing = []
    required_tools = ["curl", "npm", "sudo"]
    
    for tool in required_tools:
        if shutil.which(tool) is None:
            missing.append(tool)
    
    if missing:
        print_warning("الأدوات التالية مفقودة ويجب تثبيتها أولاً:")
        print(f"   Missing: {', '.join(missing)}")
        print(f"   {Colors.CYAN}Try: sudo apt update && sudo apt install -y curl nodejs npm{Colors.ENDC}")
        return False
    return True

def install_atlassian_cli():
    """
    Install Atlassian CLI (ACLI) properly based on system architecture.
    Ref: https://developer.atlassian.com/cloud/acli/guides/install-linux/
    """
    tool_name = "Atlassian CLI (Rovo Dev)"
    print_step(f"جاري تثبيت {tool_name}...")

    # 1. Detect Architecture
    arch = platform.machine().lower()
    if arch in ['x86_64', 'amd64']:
        download_url = "https://acli.atlassian.com/linux/latest/acli_linux_amd64/acli"
    elif arch in ['aarch64', 'arm64']:
        download_url = "https://acli.atlassian.com/linux/latest/acli_linux_arm64/acli"
    else:
        print_error(f"المعمارية غير مدعومة حالياً: {arch}")
        return

    # 2. Download and Install
    try:
        # Download
        print(f"   ⬇️  Downloading binary for {arch}...")
        subprocess.run(f"curl -L -o acli_temp '{download_url}'", shell=True, check=True)
        
        # Make executable
        os.chmod("acli_temp", 0o755)
        
        # Move to /usr/local/bin (Requires sudo)
        print("   📦 Moving to /usr/local/bin/acli...")
        subprocess.run("sudo mv acli_temp /usr/local/bin/acli", shell=True, check=True)
        
        # Verify
        result = subprocess.run("acli version", shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print_success(f"تم تثبيت {tool_name} بنجاح.")
        else:
            print_error(f"تم التثبيت ولكن لم نتمكن من التحقق من الإصدار.")
            
    except subprocess.CalledProcessError as e:
        print_error(f"حدث خطأ أثناء تثبيت ACLI: {e}")
        if os.path.exists("acli_temp"):
            os.remove("acli_temp")

def install_amp_code():
    tool_name = "Amp Code CLI"
    print_step(f"جاري تثبيت {tool_name}...")
    cmd = "curl -fsSL https://ampcode.com/install.sh | bash"
    if run_command(cmd, tool_name):
        print_success(f"تم تثبيت {tool_name} بنجاح.")

def install_npm_package(package_name, display_name):
    print_step(f"جاري تثبيت {display_name}...")
    # Using 'sudo npm install -g'
    cmd = f"sudo npm install -g {package_name}"
    if run_command(cmd, display_name):
        print_success(f"تم تثبيت {display_name} بنجاح.")

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{Colors.HEADER}{'='*50}")
    print(f"   🚀 AI Developer Tools Installer (Linux)")
    print(f"{'='*50}{Colors.ENDC}")
    print("سيتم تثبيت الأدوات التالية:")
    print(" 1. Amp Code CLI")
    print(" 2. Atlassian CLI (Supports Rovo Dev)")
    print(" 3. Google Gemini CLI")
    print(" 4. Qwen Code CLI")
    print("-" * 50)

    if not check_requirements():
        sys.exit(1)

    # Give user a moment to cancel
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()

    # --- Start Installations ---
    
    # 1. Amp Code
    install_amp_code()

    # 2. Atlassian CLI (Specific Logic)
    install_atlassian_cli()

    # 3. Gemini CLI
    install_npm_package("@google/gemini-cli", "Google Gemini CLI")

    # 4. Qwen Code CLI
    install_npm_package("@qwen-code/qwen-code", "Qwen Code CLI")

    # --- Summary ---
    print(f"\n{Colors.HEADER}{'='*50}")
    print("🎉 انتهت عملية التثبيت! (Installation Complete)")
    print(f"{'='*50}{Colors.ENDC}")
    
    print(f"{Colors.BOLD}📌 أوامر التشغيل (How to use):{Colors.ENDC}")
    print(f"   1. Amp Code    -> {Colors.CYAN}amp{Colors.ENDC}")
    print(f"   2. Rovo Dev    -> {Colors.CYAN}acli rovodev{Colors.ENDC} (Requires login: acli login)")
    print(f"   3. Gemini CLI  -> {Colors.CYAN}gemini{Colors.ENDC}")
    print(f"   4. Qwen Code   -> {Colors.CYAN}qwen{Colors.ENDC}")
    
    print(f"\n{Colors.WARNING}ملاحظة: إذا لم تعمل الأوامر، يرجى إعادة تشغيل التيرمينال.{Colors.ENDC}")
    print(f"{Colors.WARNING}Note: Please restart your terminal if commands are not found.{Colors.ENDC}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ تم إلغاء العملية بواسطة المستخدم.")
        sys.exit(0)
