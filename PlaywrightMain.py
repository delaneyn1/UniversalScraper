import asyncio
from playwright.async_api import async_playwright

async def run_automation():
    # Ask the user for the URL in the terminal
    target_url = input("https://www.boonecountyky.org/government_administration/county_government/jailer/inmates.php")
    
    # Ensure URL has a protocol
    if not target_url.startswith("http"):
        target_url = f"https://www.boonecountyky.org/government_administration/county_government/jailer/inmates.php"

    print(f"\n🚀 Launching Chromium to visit: {target_url}...")

    async with async_playwright() as p:
        # Launch browser. headless=False is key for seeing it on your VM.
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        
        # Create a new page
        page = await browser.new_page()

        try:
            # Navigate to the URL
            await page.goto(target_url, wait_until="domcontentloaded")
            
            # Get the page title
            title = await page.title()
            print(f"✅ Page Loaded! Title: '{title}'")
            
            # Take a screenshot
            await page.screenshot(path="last_run.png")
            print("📸 Screenshot saved as 'last_run.png'")

            # Keep the browser open for a few seconds to inspect
            print("Waiting 5 seconds before closing...")
            await asyncio.sleep(5)

        except Exception as e:
            print(f"❌ Navigation failed: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(run_automation())