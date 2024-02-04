from utils import pdf_path, txt_path, xls_path, xlsx_path
from zipfile import ZipFile
import os.path





def test_main_zip(tmp_directory):
    pdf_size = os.path.getsize(pdf_path)
    pdf_name = os.path.basename(pdf_path)
    text_size = os.path.getsize(txt_path)
    text_name = os.path.basename(txt_path)
    xls_size = os.path.getsize(xls_path)
    xls_name = os.path.basename(xls_path)
    xlsx_size = os.path.getsize(xlsx_path)
    xlsx_name = os.path.basename(xlsx_path)

    with ZipFile(file="tmp/my_archive.zip", mode="a") as myzip:
        myzip.write(filename=pdf_path, arcname='file1.pdf', compress_type=None,
                    compresslevel=None)
        myzip.write(filename=txt_path, arcname='file4.txt', compress_type=None,
                    compresslevel=None)
        myzip.write(filename=xls_path, arcname='file3.xls', compress_type=None,
                    compresslevel=None)
        myzip.write(filename=xlsx_path, arcname='file2.xlsx', compress_type=None,
                    compresslevel=None)

    with ZipFile(file="tmp/my_archive.zip", mode="r") as myzip:
        pdf_archive_file = myzip.getinfo("file1.pdf")
        pdf_archive_file_name = pdf_archive_file.filename
        pdf_archive_file_size = pdf_archive_file.file_size

        txt_archive_file = myzip.getinfo("file4.txt")
        txt_archive_file_name = txt_archive_file.filename
        txt_archive_file_size = txt_archive_file.file_size

        xls_archive_file = myzip.getinfo("file3.xls")
        xls_archive_file_name = xls_archive_file.filename
        xls_archive_file_size = xls_archive_file.file_size

        xlsx_archive_file = myzip.getinfo("file2.xlsx")
        xlsx_archive_file_name = xlsx_archive_file.filename
        xlsx_archive_file_size = xlsx_archive_file.file_size

    assert pdf_name == pdf_archive_file_name
    assert pdf_size == pdf_archive_file_size
    assert text_name == txt_archive_file_name
    assert text_size == txt_archive_file_size
    assert xls_name == xls_archive_file_name
    assert xls_size == xls_archive_file_size
    assert xlsx_name == xlsx_archive_file_name
    assert xlsx_size == xlsx_archive_file_size