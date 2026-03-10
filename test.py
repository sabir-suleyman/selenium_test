from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import matplotlib.pyplot as plt

URL = "https://www.saucedemo.com/"

steps = [
    "Login",
    "Add to Cart",
    "Go to Cart",
    "Checkout",
    "Finish"
]

def run_test(username, password):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)

    times = []

    # LOGIN
    start = time.time()

    driver.find_element(By.ID,"user-name").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()

    time.sleep(2)
    times.append(time.time() - start)

    # ADD TO CART
    start = time.time()

    driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
    time.sleep(1)
    times.append(time.time() - start)

    # GO TO CART
    start = time.time()

    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
    time.sleep(2)
    times.append(time.time() - start)

    # CHECKOUT
    start = time.time()
    driver.find_element(By.ID,"checkout").click()
    time.sleep(2)

    driver.find_element(By.ID,"first-name").send_keys("Sabir")
    driver.find_element(By.ID,"last-name").send_keys("Test")
    driver.find_element(By.ID,"postal-code").send_keys("12345")
    driver.find_element(By.ID,"continue").click()

    time.sleep(2)
    times.append(time.time() - start)

    # FINISH
    start = time.time()

    driver.find_element(By.ID,"finish").click()
    time.sleep(1)
    times.append(time.time() - start)

    driver.quit()

    return times


print("\nRunning standard_user test...")
standard = run_test("standard_user","secret_sauce")

print("Running performance_glitch_user test...")
glitch = run_test("performance_glitch_user","secret_sauce")


print("\n--- PERFORMANCE CHECK (5 seconds rule) ---")

for i in range(len(steps)):
    if glitch[i] < 5:
        print(f"{steps[i]} : PASS ({glitch[i]:.2f}s)")
    else:
        print(f"{steps[i]} : FAIL ({glitch[i]:.2f}s)")


plt.figure(figsize=(8,5))

plt.plot(steps,standard,marker="o",label="standard_user")
plt.plot(steps,glitch,marker="o",label="performance_glitch_user")

plt.xlabel("Steps")
plt.ylabel("Time (seconds)")
plt.title("SauceDemo Performance Comparison")

plt.legend()
plt.grid(True)

plt.show()