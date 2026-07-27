import copy
from PyPDF2 import PdfReader, PdfWriter

def split_horizontal_double_page(input_path: str, output_path: str):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        box = page.mediabox
        width = float(box.width)
        height = float(box.height)

        # 判断：横向页面才拆分（宽>高）；如果有竖页不改动
        half = width / 2
        # ========== 左半边页面 ==========
        left_page = copy.deepcopy(page)
        left_page.mediabox.lower_left = (box.left, box.bottom)
        left_page.mediabox.upper_right = (box.left + half, box.top)
        writer.add_page(left_page)

        # ========== 右半边页面 ==========
        right_page = copy.deepcopy(page)
        right_page.mediabox.lower_left = (box.left + half, box.bottom)
        right_page.mediabox.upper_right = (box.right, box.top)
        writer.add_page(right_page)
    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"处理完成！输出文件：{output_path}")

# ==================== 修改这里的文件路径 ====================
if __name__ == "__main__":
    INPUT_FILE = "2025年一建-机电-圈题AB卷.pdf"
    OUTPUT_FILE = "拆分后_单竖页.pdf"
    split_horizontal_double_page(INPUT_FILE, OUTPUT_FILE)