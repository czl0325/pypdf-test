from PyPDF2 import PdfReader, PdfWriter

def remove_pdf_password(input_path: str, output_path: str, password: str):
    """
    移除PDF密码，生成无密码新文件
    :param input_path: 加密pdf路径
    :param output_path: 输出解密后的pdf路径
    :param password: pdf密码（字符串）
    """
    reader = PdfReader(input_path)
    # 解密
    if reader.is_encrypted:
        ok = reader.decrypt(password)
        if not ok:
            raise ValueError("密码错误，解密失败")
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    with open(output_path, "wb") as f_out:
        writer.write(f_out)
    print(f"解密完成，输出文件：{output_path}")


if __name__ == "__main__":
    IN_FILE = "1.pdf"
    OUT_FILE = "decrypted.pdf"
    PWD = "20260912"
    remove_pdf_password(IN_FILE, OUT_FILE, PWD)
