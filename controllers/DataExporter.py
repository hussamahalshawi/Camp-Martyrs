
from tkinter import filedialog, messagebox

class DataExporterC:
    def __init__(self, data):
        self.data = data  # البيانات التي سيتم تصديرها كـ DataFrame

    def export_to_excel(self, file_path):
        """تصدير البيانات إلى Excel"""
        self.data.to_excel(file_path, index=False)
        messagebox.showinfo("نجاح", "تم حفظ البيانات كملف Excel.")

    def save_file(self, format_type):
        """حفظ البيانات بالتنسيق المطلوب"""
        file_types = {
            "excel": ("Excel Files", "*.xlsx"),
            "json": ("JSON Files", "*.json"),
            "pdf": ("PDF Files", "*.pdf"),
        }
        file_extension = {
            "excel": ".xlsx",
            "json": ".json",
            "pdf": ".pdf",
        }

        file_path = filedialog.asksaveasfilename(
            defaultextension=file_extension[format_type],
            filetypes=[file_types[format_type]],
        )

        if not file_path:
            return  # المستخدم أغلق نافذة الحفظ

        if format_type == "excel":
            self.export_to_excel(file_path)