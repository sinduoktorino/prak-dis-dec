from sqlmodel import Field, Session, SQLModel, create_engine


class Produk(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    kode_produk: str
    nama_produk: str
    stok: int
    tersedia: bool
    harga: float


engine = create_engine("sqlite:///inventaris.db")


def isi_data():
    daftar_produk = [
        Produk(kode_produk="PRD01", nama_produk="Keyboard Mekanikal", stok=15, tersedia=True, harga=450000.50),
        Produk(kode_produk="PRD02", nama_produk="Mouse Wireless", stok=30, tersedia=True, harga=175000.00),
        Produk(kode_produk="PRD03", nama_produk="Monitor IPS 24 Inch", stok=0, tersedia=False, harga=1850000.75),
        Produk(kode_produk="PRD04", nama_produk="USB-C Hub 7-in-1", stok=22, tersedia=True, harga=230000.25),
        Produk(kode_produk="PRD05", nama_produk="Webcam Full HD", stok=8, tersedia=True, harga=320000.00),
    ]

    with Session(engine) as session:
        session.add_all(daftar_produk)
        session.commit()
        print("Berhasil menambahkan 5 data produk ke inventaris.db!")


if __name__ == "__main__":
    isi_data()
