from src.repository.mem_repo import MemoryRepository
from src.repository.txt_repo import TextFileRepository
from src.repository.bin_repo import BinaryFileRepository
from src.service.service import Service
from src.ui.ui import Ui

# repository = MemoryRepository()
repository = TextFileRepository("books.txt")
# repository = BinaryFileRepository("books.pkl")
service = Service(repository)
ui = Ui(service)
ui.start()
