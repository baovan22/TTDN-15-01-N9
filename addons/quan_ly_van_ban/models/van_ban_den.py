from odoo import models, fields

class VanBanDen(models.Model):
    _name = "van_ban_den"
    _description = "Quản lý Văn Bản Đến"
    _rec_name = "ten_vb"

    so_vb_den = fields.Char(string="Số Văn Bản Đến", required=True)
    ten_vb = fields.Char(string="Tên Văn Bản", required=True)
    so_luong_vb_den = fields.Integer(string="Số Lượng Văn Bản Đến", default=1)
    noi_den = fields.Char(string="Nơi Đến", required=True)
    ngay_nhan = fields.Date(string="Ngày Nhận", default=fields.Date.today)

    muc_do = fields.Selection([
        ('thap', 'Thấp'),
        ('trung_binh', 'Trung Bình'),
        ('cao', 'Cao')
    ], string="Mức Độ", default='trung_binh')

    trang_thai = fields.Selection([
        ('draft', 'Nháp'),
        ('sent', 'Đã Gửi'),
        ('received', 'Đã Nhận'),
        ('processed', 'Đã Xử Lý')
    ], string="Trạng Thái", default='draft')

    ghi_chu = fields.Text(string="Ghi Chú")

    # Quan hệ với Văn Bản Đi (One2many)
    van_ban_di_ids = fields.One2many('van_ban_di', 'van_ban_den_id', string="Danh Sách Văn Bản Đi")
