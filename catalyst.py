import time
import sys
import pyautogui
import keyboard
from requests_html import HTMLSession
import asyncio
import pyppeteer
from promise import Promise
from bs4 import BeautifulSoup

# 主要是重写HTMLSession类
# HTMLSession类是用来包装pyppeteer的,添加参数的也是在pyppeteer里面
import asyncio
from playwright.async_api import async_playwright

import asyncio
from playwright.async_api import async_playwright

count = 0;

while(True):
	count += 1;
	print(count);
	pyautogui.click(201, 537)
	async def run(playwright):
		chromium = playwright.chromium
		browser = await chromium.launch()
		page = await browser.new_page()
		for current_url in ["https://dubioustunic.github.io/spinning-sword/philosophers_stone"]:
			await page.goto(current_url, wait_until="domcontentloaded")
			element = await page.wait_for_selector("#spellbook")
			keyboard.write(await element.inner_text())
		await browser.close()

	async def main():
		async with async_playwright() as playwright:
			await run(playwright)
	asyncio.run(main())
	#session = HTMLSession2()
	#session.browser
	#response = session.get(url=url)	
	#response.html.render(sleep = 66)#OPTIMUS PRIME
	#soup = BeautifulSoup(response.content, 'html.parser')
	#ss = soup.find("div", {"id": "spellbook"})
	#print(ss.contents);
	
	time_start = time.time()
	seconds = 0
	minutes = 0
	while True:
		time.sleep(1)
		seconds = int(time.time() - time_start) - minutes * 60#YHVH
		if seconds==1:			
			pyautogui.click(900,340);
			break;
			#sys.exit();	
	time.sleep(37);	
