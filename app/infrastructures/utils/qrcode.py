import segno
from io import BytesIO

def generate_qr(data: str):
    """
        Genarate a qr code.
    """
    qr = segno.make(data)
    buf = BytesIO()
    qr.save(buf, kind="png")
    buf.seek(0)
    return buf