import asyncio
import csv
import random
from openpyxl import Workbook
from config import delay
from utils import update_wallet
from loguru import logger
from sys import stderr

logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <3}</level> | <level>{message}</level>")

async def main():
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(['key', 'result'])
    sheet.column_dimensions['A'].width = 65
    sheet.column_dimensions['B'].width = 12
    with open("keys.txt", "r") as f:
        keys = [row.strip() for row in f]
    for key in keys:
        res = await update_wallet(key)
        if res != 'already updated' and res != 'updated':
            sheet.append([key, res])
    workbook.save("result.xlsx")

if __name__ == '__main__':
    asyncio.run(main())
    logger.success(f'muнетинг закончен...')
