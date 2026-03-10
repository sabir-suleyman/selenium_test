# Selenium Performance Test Automation

This project demonstrates an automated performance testing scenario using Selenium WebDriver and Python.  
The test script simulates a typical e-commerce workflow on the SauceDemo testing platform and measures the execution time of each step.

The goal of the project is to compare the performance of two different user accounts and visualize the response times using a graph.

---

## Test Scenario

The automated test performs the following steps:

1. User login
2. Add product to cart
3. Navigate to cart
4. Enter checkout information
5. Complete the order

Two test accounts are used:

- `standard_user`
- `performance_glitch_user`

The `performance_glitch_user` account is intentionally designed to simulate slower performance conditions.

---

## Technologies Used

- Python
- Selenium WebDriver
- Chrome Browser
- Matplotlib
- WebDriver Manager

Test platform:

- https://www.saucedemo.com/

---

## Installation

### Clone the repository:

```bash
git clone https://github.com/yourusername/selenium-performance-test.git
cd selenium-performance-test
```

### Install required dependencies:

```
pip install selenium
pip install matplotlib
pip install webdriver-manager
```

## Running the Test

Run the test script:
```
python test.py
```
### During execution the script will:

1. Open Chrome browser

2. Perform the automated test scenario

3. Measure execution time of each step

4. Print PASS / FAIL results in the terminal

5. Generate a performance comparison graph

## Example output:

```
PERFORMANCE CHECK (5 seconds rule)

Login : FAIL (7.62s)
Add to Cart : PASS (1.09s)
Go to Cart : PASS (2.13s)
Checkout : PASS (4.68s)
Finish : PASS (1.12s)
```

## Performance Rule

A simple threshold rule is used:

Execution time < 5 seconds → _PASS_

Execution time ≥ 5 seconds → *FAIL*

This allows quick identification of potential performance issues.


## Output

The script produces:

Terminal performance results

A Matplotlib graph comparing execution times

Example visualization:
```
Performance comparison between standard_user and performance_glitch_user
```

### Project Structure
```
selenium-performance-test
│
├── test.py
├── performance_graph.png
└── README.md
```

### Author

Sabir Süleymanlı <br />
Computer Engineering Master's Degree Student <br />
Bursa Uludağ University <br />

---

/*![Performance Graph](performance_graph.png)*/
