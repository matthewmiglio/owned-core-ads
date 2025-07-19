import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
from creds import CredsManager

# --- User credentials ---
creds_manager = CredsManager()
usernames_passwords = creds_manager.get_creds()
usernames = [cred["username"] for cred in usernames_passwords]
print(f"Loaded these usernames:")
for username in usernames:
    print(f"\t{username}")


# --- Thread URLs ---
threads = [
    "https://www.ownedcore.com/forums/world-of-warcraft/world-of-warcraft-bots-programs/",
    "https://www.ownedcore.com/forums/world-of-warcraft/world-of-warcraft-bots-programs/wow-bots-questions-requests/",
    "https://www.ownedcore.com/forums/world-of-warcraft/world-of-warcraft-exploits/",
    "https://www.ownedcore.com/forums/world-of-warcraft/world-of-warcraft-guides/",
    "https://www.ownedcore.com/forums/world-of-warcraft/world-of-warcraft-general/",
    "https://www.ownedcore.com/forums/wow-classic/wow-classic-exploits/",
    "https://www.ownedcore.com/forums/wow-classic/wow-classic-guides/",
    "https://www.ownedcore.com/forums/wow-classic/wow-classic-general/",
    "https://www.ownedcore.com/forums/mmo-trading-market/wow-classic-buy-sell-trade/",
    "https://www.ownedcore.com/forums/mmo-trading-market/world-of-warcraft-buy-sell-trade/",
]

# --- Random user agents ---
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/112.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/110.0",
]

gif_urls = [
    f"https://fishbot.org/_next/image?url=%2F2025-03-10%2017-38-42_subclip_612_624_cropped_5_1_1911_951_sped_up_15.gif&w=1920&q=75",
    f"https://fishbot.org/_next/image?url=%2F2025-03-10%2017-38-42_subclip_612_624_cropped_5_1_1911_951_sped_up_15.gif&w=1920&q=75",
]


# --- Generate random ad message ---
def make_ad_message():
    time_emojis = ["⏳", "⏰", "🕒", "⌛", "🕞", "🕓", "⏲️", "🕙", "🕥", "🕧"]

    title_emojis = ["🐟", "🎣", "🔥", "🚀", "💥", "🏆", "⭐", "🌊", "⚡", "🎉"]

    fishing_emojis = ["🐟", "🎣", "🐠", "🦈", "🐡", "🐬", "🌊"]

    colors = ["lime", "royalblue", "orangered", "cyan", "gold"]

    exiting_emojis = ["🚀", "🔥", "⚡", "💥", "🎆", "🎇", "🏎️", "💨", "🌪️"]

    valid_emojis = ["✅", "✔️", "👍", "💯", "🙌", "🎉", "🥳", "👏"]

    accuracy_emojis = ["🎯", "🏹", "🧭", "🔭", "📍", "📌", "🎯"]

    computer_emojis = ["💻", "🖥️", "🖱️", "⌨️", "📱", "🕹️", "🤖", "🛠️"]

    messages_emojis = ["💬", "💭", "🗨️", "🗣️", "📢", "📣", "✉️", "📩"]

    update_emojis = ["🔄", "🔃", "🔁", "♻️", "➡️", "⬆️", "⬇️", "🔂"]

    return f"""[CENTER]
[SIZE=7]{random.choice(title_emojis)} WoW FishBot - The Ultimate AI Fishing Assistant! {random.choice(fishing_emojis)}[/SIZE]
[SIZE=4][/SIZE]
[SIZE=5]{random.choice(time_emojis)} Save time & let AI handle fishing for you effortlessly![/SIZE]
[SIZE=4][/SIZE]
[SIZE=4]WoW FishBot is [B][COLOR="{random.choice(colors)}"]100% undetectable[/COLOR][/B], [B][COLOR="{random.choice(colors)}"]completely automated[/COLOR][/B], and functions on [B][COLOR="{random.choice(colors)}"]all WoW versions[/COLOR][/B]! 🚀[/SIZE]
[/CENTER]

[HR][/HR]

[CENTER][B][SIZE=5]{random.choice(exiting_emojis)} Why Choose WoW FishBot? {random.choice(exiting_emojis)}[/SIZE][/B]
[LIST]
{random.choice(valid_emojis)} Works on ALL WoW Versions - Classic, Retail & Private Servers
{random.choice(accuracy_emojis)} Advanced AI Image Recognition - Fast, precise, and stealthy
{random.choice(fishing_emojis)} Smart Fishing Logic - Target only what you need
{random.choice(computer_emojis)} Multi-Bot Capability - Run several instances at once
{random.choice(update_emojis)} Frequent Updates & Ongoing Development - Always improving!
{random.choice(messages_emojis)} 24/7 Discord Support - Help is always available!
[/LIST]
[HR][/HR]

[CENTER]
[B][SIZE=5]🎥 Watch WoW FishBot in Action![/SIZE][/B]

[IMG]{random.choice(gif_urls)}[/IMG]
[/CENTER]

[HR][/HR]

[B][SIZE=6]⚡ Download for FREE - No Risk, Just Rewards! ⚡[/SIZE][/B]
[B]🎣 Get Started Now:[/B] [URL="http://fishbot.org"][COLOR="cyan"]FishBot.org[/COLOR][/URL]  
[B]💬 Join Our Community:[/B] [URL="https://discord.gg/PyTD4xBhme"][COLOR="gold"]Click Here![/COLOR][/URL]  
🚀 Make Fishing in WoW Effortless Today! 🚀
[/CENTER]"""


def make_ad_title():
    titles = [
        "WoW FishBot - The Ultimate AI Fishing Assistant!",
        "Effortless WoW Fishing with FishBot AI",
        "WoW FishBot - Catch More, Grind Less!",
        "Dominate WoW Fishing with FishBot AI!",
        "WoW FishBot - 100% Undetectable, All Versions",
        "Maximize WoW Fishing - Try FishBot Free!",
        "Fish Smarter, Not Harder - WoW FishBot FTW!",
        "WoW FishBot - Your Secret Fishing Weapon!",
        "WoW FishBot - Boost Your Fishing Gains!",
        "AI-Powered Fishing in WoW - Get FishBot Now!",
        "WoW FishBot - For Classic, Retail & Private Servers!",
        "Advanced WoW Fishing Bot - Free Download",
        "Ultimate WoW Fishing Bot - Join the Revolution!",
        "WoW FishBot - AI Fishing Mastered!",
        "Top-Rated WoW Fishing Bot - Why Wait?",
        "WoW FishBot - Grind Less, Win More!",
        "Fastest Fishing Bot for WoW - FishBot AI!",
        "Undetectable WoW Fishing Bot - Get It Free!",
        "Boost Your WoW Fishing - FishBot in Action!",
        "WoW FishBot - Elite Fishing Made Easy!",
        "WoW FishBot Pro - Join Thousands of Users!",
        "Ready to Fish Smarter? Meet WoW FishBot!",
        "WoW FishBot - Advanced AI at Your Service!",
        "24/7 Fishing Power - Only with WoW FishBot!",
        "Level Up Fishing in WoW - FishBot Awaits!",
        "WoW FishBot - Simple, Smart, Effective!",
        "Join the WoW FishBot Community Today!",
        "Turn Hours into Minutes - WoW FishBot",
        "Master WoW Fishing with FishBot AI",
        "WoW FishBot - Tested. Trusted. Loved.",
        "Smash Fishing Goals in WoW - FishBot Time!",
        "Get WoW FishBot - Fish Like a Pro!",
        "Fishing Evolved - WoW FishBot Edition!",
        "Skip the Grind - Use WoW FishBot Now!",
        "WoW FishBot - Your Fishing Companion!",
        "Big Gains, Zero Effort - WoW FishBot!",
        "Fish Smarter with WoW FishBot's AI Magic!",
        "AI Fishing Perfection - WoW FishBot Here!",
        "Undetectable, Reliable, Powerful - WoW FishBot!",
        "Fish Like Never Before - Try WoW FishBot!",
        "WoW FishBot - Revolutionizing Fishing!",
        "Ready to Rule WoW Fishing? Get FishBot!",
        "WoW FishBot - Because Time Matters.",
        "100% Automated Fishing - Thanks, FishBot!",
        "WoW FishBot - Upgrade Your Fishing Game!",
        "No Risk, Just Rewards - WoW FishBot Free!",
        "Join the FishBot Revolution - WoW Awaits!",
        "WoW FishBot - Make Fishing Fun Again!",
        "Fishing Bots Reimagined - WoW FishBot Style!",
    ]

    return random.choice(titles)


def post_1_ad():
    # --- Setup driver ---
    options = uc.ChromeOptions()
    options.add_argument(f"user-agent={random.choice(user_agents)}")
    driver = uc.Chrome(options=options)

    try:
        account = random.choice(usernames_passwords)
        username = account["username"]
        password = account["password"]

        thread_url = random.choice(threads)
        driver.get(thread_url)
        time.sleep(3)

        username_input = driver.find_element(By.ID, "navbar_username")
        username_input.clear()
        username_input.send_keys(username)

        password_hint = driver.find_element(By.ID, "navbar_password_hint")
        password_hint.click()
        time.sleep(0.5)  # small wait to allow JS swap

        password_input = driver.find_element(By.ID, "navbar_password")
        password_input.clear()
        password_input.send_keys(password)

        login_button = driver.find_element(
            By.CSS_SELECTOR, "li.submitPad.loginbuttonfx input[type='submit']"
        )
        login_button.click()
        # --- Smart wait for page load ---
        max_wait = 10

        try:
            WebDriverWait(driver, max_wait).until(
                EC.presence_of_element_located((By.LINK_TEXT, "ADVERTISE"))
            )
            print("✅ Page loaded, ADVERTISE tab found.")
        except TimeoutException:
            print(f"⚠ Timed out after {max_wait} seconds waiting for ADVERTISE tab.")

        post_button = driver.find_element(By.ID, "newthreadlink_top")
        post_button.click()
        time.sleep(3)

        try:
            WebDriverWait(driver, max_wait).until(
                EC.presence_of_element_located((By.LINK_TEXT, "ADVERTISE"))
            )
            print("✅ Page loaded, ADVERTISE tab found.")
        except TimeoutException:
            print(f"⚠ Timed out after {max_wait} seconds waiting for ADVERTISE tab.")

        # --- Fill title ---
        title_input = driver.find_element(By.ID, "subject")
        title_input.clear()
        title_input.send_keys(make_ad_title())

        message = make_ad_message()
        driver.execute_script(
            f"CKEDITOR.instances['vB_Editor_001_editor'].setData(`{message}`);"
        )

        time.sleep(1)

        try:
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "input[type='submit'][value='Submit New Thread']")
                )
            )
            print("✅ Submit button is present and clickable.")
        except TimeoutException:
            print("⚠ Could not find a clickable Submit New Thread button.")
            driver.quit()
            exit()

        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            submit_button,
        )
        time.sleep(1)  # Give time for scroll

        submit_button.click()
        print("✅ Clicked Submit button.")

        time.sleep(5)
        print("✅ Post submission process should be complete.")

    except Exception as e:
        print(f"Tried to post to this thread: {thread_url}")
        print(f"This error occurred: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    post_1_ad()
