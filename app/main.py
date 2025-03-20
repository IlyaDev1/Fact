from asyncio import run

from app.core.service.main_service import loop

if __name__ == "__main__":
    run(loop())
