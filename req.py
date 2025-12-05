import subprocess
import shutil
import sys
import os

def run_command(command, tool_name, use_sudo=False):
    """
    تشغيل أوامر Shell مع معالجة الأخطاء.
    """
    print(f"\n🔵 [جاري التثبيت] {tool_name}...")
    
    try:
        # بعض الأوامر تحتاج sudo وبعضها (مثل سكربتات bash) قد تطلبه داخلياً
        # هنا ننفذ الأمر مباشرة كما هو في التيرمينال
        subprocess.run(command, shell=True, check=True, executable='/bin/bash')
        print(f"✅ تم تثبيت {tool_name} بنجاح.")
    except subprocess.CalledProcessError as e:
        print(f"❌ فشل تثبيت {tool_name}.")
        print(f"   الخطأ: {e}")

def check_requirements():
    """
    التحقق من وجود Node.js و Curl.
    """
    missing = []
    if shutil.which("curl") is None:
        missing.append("curl")
    if shutil.which("npm") is None:
        missing.append("npm (Node.js)")
    
    if missing:
        print("⚠️  تنبيه: الأدوات التالية مفقودة ويجب تثبيتها أولاً:")
        print(f"   {', '.join(missing)}")
        print("   للتثبيت على Ubuntu/Debian: sudo apt install curl nodejs npm")
        return False
    return True

def main():
    print("=== مثبت أدوات التطوير بالذكاء الاصطناعي (AI CLI Tools) ===")
    
    if not check_requirements():
        sys.exit(1)

    # -------------------------------------------
    # 1. Amp Code CLI
    # بناءً على طلبك: https://ampcode.com/install.sh
    # -------------------------------------------
    amp_cmd = "curl -fsSL https://ampcode.com/install.sh | bash"
    run_command(amp_cmd, "Amp Code CLI")

    # -------------------------------------------
    # 2. Atlassian CLI (Rovo Dev)
    # Rovo Dev هو جزء من ACLI. التثبيت يتم عبر سكربت Atlassian الرسمي.
    # -------------------------------------------
    # ملاحظة: قد يطلب منك السكربت كلمة مرور sudo أثناء التنفيذ
    acli_cmd = "curl -fsSL https://atlassian.com/acli/install.sh | sudo sh"
    run_command(acli_cmd, "Atlassian CLI (Rovo Dev)")

    # -------------------------------------------
    # 3. Gemini CLI
    # المصدر الرسمي: @google/gemini-cli
    # -------------------------------------------
    gemini_cmd = "sudo npm install -g @google/gemini-cli"
    run_command(gemini_cmd, "Google Gemini CLI")

    # -------------------------------------------
    # 4. Qwen Code CLI
    # المصدر: @qwen-code/qwen-code (مبني على Gemini CLI)
    # -------------------------------------------
    qwen_cmd = "sudo npm install -g @qwen-code/qwen-code"
    run_command(qwen_cmd, "Qwen Code CLI")

    print("\n" + "="*40)
    print("🎉 انتهت عملية التثبيت!")
    print("="*40)
    print("📌 أوامر التشغيل:")
    print("   1. Amp Code    -> اكتب: amp")
    print("   2. Rovo Dev    -> اكتب: acli rovodev")
    print("   3. Gemini CLI  -> اكتب: gemini")
    print("   4. Qwen Code   -> اكتب: qwen")
    print("\nملاحظة: إذا لم تعمل الأوامر، أغلق التيرمينال وافتحه مجدداً.")

if __name__ == "__main__":
    main()
