import asyncio
from pyppeteer import launch

async def main():
    browser = await launch({'headless': True})
    page = await browser.newPage()
    await page.goto('https://en.wikipedia.org/wiki/Computer')
    await page.waitForSelector('#mw-content-text')
    content = await page.querySelector('#mw-content-text')
    allP = await content.querySelectorAll('p')
    print(allP)
    p = await page.evaluate('(element) => element.innerText', allP)
    print(p)
    await page.screenshot({'path': 'example.png'})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())