# Audible Web Scraping

![Project Image](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Audible_logo.svg/768px-Audible_logo.svg.png)

---
## Notes

- This script was developed for educational and learning purposes.
- Make sure to comply with Audible's terms of use when using this script to collect data from the site.
- It is recommended to periodically check for updates to Audible to ensure the accuracy of collected data.
---
## Description

- The script accesses the [Data Science pages](https://www.audible.com.br/search?node=41939682011&ref_pageloadid=O2wAvvyEoz3fDgU6&ref=a_cat_Compu_c0&pf_rd_p=dc1344c1-8d8e-4f1d-a788-ceb52686bd73&pf_rd_r=KB4NDK2FWR4G4CP0357Z&pageLoadId=NZKf8UFA0nMOR8Y3&creativeId=55f26bd3-b057-4923-8e9f-4199dafc0395%22) and extracts information such as movie title, playtime and author.
- Data is collected in an automated manner, ensuring accuracy and efficiency.
- After collection, the data is organized into a Pandas DataFrame and saved to a CSV file named "Books.csv".

---

## Technologies

- Python
  - Selenium
  - Pandas
  - time 

---

#### Dependencies

```html
    pip install pandas selenium
```
- Make sure to have ChromeDriver installed on your system. You can download it from [ChromeDriver](https://chromedriver.chromium.org/downloads)

---

## Author Info

- [Linkedin](https://www.linkedin.com/in/gustavo-vinhola-dos-santos-269a01215/)
