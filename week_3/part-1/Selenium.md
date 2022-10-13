# Week 3 Part 1 (Deadline: 2022/11/03 00:00)

## Assignment 1:  Non-element Interaction (Selenium)

Write a script to automate the below scenario in using Chrome browser.
 
### Scenario:
1. Open the Chrome browser.
2. Maximize the browser window.
3. Navigate to Appworks School Website (https://school.appworks.tw).
4. Print “PASS” if the title of the page matches with “Code Your Future” else “FAIL”.
5. Click the link “AppWorks” in top right corner
6. Switch to new tabs to AppWorks website
7. Print “PASS” if there is text “By Founders, For Founders” else “FAIL”.
8. Navigate to https://appworks.tw/investments/
9. Print “PASS” if there is text “We know you have a choice. We want you to choose us.” else “FAIL”.
10. Navigate back to the Appworks School Website
11. Print the URL of the current page.
12. Navigate forward.
13. Close the current window
14. Switch back to the original window and reload the page.
15. Finally, Close the Browser.

## Assignment 2: Interacting with Web Elements (Selenium)
Write a script to automate the below scenario in using Chrome browser.

In this Assignment, you should use a **Python Assert Statement** to verify the conditions.
 
### Scenario:
1. Open the Chrome browser
2. Go to Demo Store (http://demostore.supersqa.com)
3. Add “Album” to cart
4. Change the quantity to 2 and update cart in Cart Page
5. Verify that Subtotal is $30.00
6. Click “Checkout” and Fill in the form as below:
   * First Name: “First”
   * Last Name: “Last” 
   * Company: ABC Company 
   * Country / Region: Taiwan 
   * Street address:
     * Address Line 1 
     * Address Line 2
   * Town / City: Taipei
   * State / County: Taipei 
   * Postcode / ZIP: 101 
   * Phone: 0123456789 
   * Email: abc@abc.com
7. Create an account with password “1234QWERasdf!@#$” in Checkout Page
8. Fill in Additional Information with “Thank you!” in Checkout Page
9. Click Place Order
10. Verify that “Invalid payment method” is displayed.
11. Finally, Close the Browser
