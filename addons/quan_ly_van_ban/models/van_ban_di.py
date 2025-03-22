from odoo import models, fields

class VanBanDi(models.Model):
    _name = "van_ban_di"
    _description = "Quản lý Văn Bản Đi"
    _rec_name = "ten_vb"

    so_hieu_vb = fields.Char(string="Số Hiệu Văn Bản", required=True)
    ten_vb = fields.Char(string="Tên Văn Bản", required=True)
    noi_dung = fields.Char(string="Điền nội dung", required=True)
    so_luong_vb = fields.Integer(string="Số Lượng Văn Bản", default=1)
    noi_nhan = fields.Char(string="Nơi Nhận", required=True)
    ngay_gui = fields.Date(string="Ngày Gửi", default=fields.Date.today)

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

    # Quan hệ với Văn Bản Đến (Many2one)
    van_ban_den_id = fields.Many2one("van_ban_den", string="Văn Bản Đến")
