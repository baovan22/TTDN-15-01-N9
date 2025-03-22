from odoo import models, fields

class CongViec(models.Model):
    _name = "cong_viec"
    _description = "Quản lý Công Việc"
    _rec_name = "ten_cv"

    ma_cv = fields.Char(string="Mã Công Việc", required=True)
    ten_cv = fields.Char(string="Tên Công Việc", required=True)
    so_luong_cv = fields.Integer(string="Số Lượng Công Việc", default=1)
    noi_thuc_hien = fields.Char(string="Nơi Thực Hiện", required=True)
    ngay_bat_dau = fields.Date(string="Ngày Bắt Đầu", default=fields.Date.today)
    ngay_hoan_thanh = fields.Date(string="Ngày Hoàn Thành")

    muc_do_uu_tien = fields.Selection([
        ('thap', 'Thấp'),
        ('trung_binh', 'Trung Bình'),
        ('cao', 'Cao')
    ], string="Mức Độ Ưu Tiên", default='trung_binh')

    trang_thai = fields.Selection([
        ('draft', 'Nháp'),
        ('in_progress', 'Đang Thực Hiện'),
        ('completed', 'Hoàn Thành'),
        ('cancelled', 'Hủy Bỏ')
    ], string="Trạng Thái", default='draft')

    loai_cong_viec = fields.Selection([('nho', 'Nhỏ'), ('lon', 'Lớn')], string="Loại Công Việc")

    ghi_chu = fields.Text(string="Ghi Chú")

    nhan_su_ids = fields.Many2many("nhan_vien", string="Người được phân công")
    du_tru_kinh_phi_ids = fields.Many2many("du_tru_kinh_phi", string="Dự Trù Kinh Phí")


