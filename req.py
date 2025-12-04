import subprocess
import shutil
import sys
import os

def run_command(command, tool_name):
    """
    يقوم بتشغيل أمر Shell وطباعة النتيجة.
    """
    print(f"\n[+] جاري تثبيت {tool_name}...")
    try:
        # تشغيل الأمر في التيرمينال
        subprocess.run(command, shell=True, check=True, executable='/bin/bash')
        print(f"✅ تم تثبيت {tool_name} بنجاح.")
    except subprocess.CalledProcessError as e:
        print(f"❌ حدث خطأ أثناء تثبيت {tool_name}.")
        print(f"Error Details: {e}")

def check_npm():
    """
    التحقق من وجود NPM لأن معظم الأدوات تعتمد عليه.
    """
    if shutil.which("npm") is None:
        print("⚠️ تحذير: NPM غير مثبت. يرجى تثبيت Node.js أولاً (يفضل الإصدار 20+).")
        print("Command: sudo apt install nodejs npm")
        return False
    return True

def main():
    print("=== أدوات التثبيت الآلي (Linux) ===")
    
    # 1. التحقق من المتطلبات
    if not check_npm():
        sys.exit(1)

    # -------------------------------------------
    # 2. تثبيت Gemini CLI
    # المصدر: Google Gemini CLI (Official/Open Source)
    # -------------------------------------------
    gemini_cmd = "sudo npm install -g @google/gemini-cli"
    run_command(gemini_cmd, "Gemini CLI")

    # -------------------------------------------
    # 3. تثبيت Qwen Code CLI
    # المصدر: Qwen Code (Based on Gemini CLI)
    # -------------------------------------------
    qwen_cmd = "sudo npm install -g @qwen-code/qwen-code"
    run_command(qwen_cmd, "Qwen Code CLI")

    # -------------------------------------------
    # 4. تثبيت Atlassian CLI (Rovodev)
    # المصدر: Atlassian Official Script
    # ملاحظة: Rovodev هو إضافة داخل ACLI
    # -------------------------------------------
    # نقوم بتحميل وتثبيت ACLI الرسمي
    acli_cmd = "curl -fsSL https://atlassian.com/acli/install.sh | sudo sh"
    run_command(acli_cmd, "Atlassian CLI (with Rovodev)")

    # -------------------------------------------
    # 5. تثبيت AMP CLI
    # المصدر: Amphitheatre CLI (الأكثر شيوعاً للاسم amp)
    # -------------------------------------------
    # ملاحظة: إذا كنت تقصد AWS Amplify فالأمر هو: npm install -g @aws-amplify/cli
    # هنا سنثبت 'amp' tool (Amphitheatre)
    amp_cmd = "curl -L https://github.com/amphitheatre-app/cli/raw/master/install.sh | sudo sh"
    run_command(amp_cmd, "AMP CLI (Amphitheatre)")

    print("\n=== اكتملت العملية ===")
    print("ملاحظة: قد تحتاج إلى فتح تيرمينال جديد لتعمل الأوامر.")

if __name__ == "__main__":
    main()
