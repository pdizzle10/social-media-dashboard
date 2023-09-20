<h1> Social Media Dashboard </h1>

This was a small personal project to create an example dashboard that might be used by a Marketing team to track their social media performance. I used a few different tools to complete this. I imagined this might be used by Channel 4 and so I used their logo, colours, and fonts to design the dashboard.

<h3>1. Creating a dummy dataset</h3>
I wanted to create a fake dataset to use because I couldn't find one on Kaggle/online that I thought would work well for what I wanted. I created a file in Google Sheets making use of some of its inbuilt functions to randomise some of the data. I got chatGPT to write me some random post names. I created an ER diagram which you can see [here](https://github.com/pdizzle10/social-media-dashboard/blob/main/materials/dummy_data_erd.pdf).

<h3>2. Creating random data points</h3>
I found the inbuilt Google Sheets functions to be limiting and I wanted to create a more realistic random set of data points. I used Python, specifically the Pandas and Numpy packages, to do this. First, I needed to populate the "post_performance" sheet so that I could have an individual row for every date between the date of the post and the end date (25th August). I then created a random number for the performance metrics that was higher when closer to its publishing date that decreased as time went on. I then applied a random number to the spend column. Finally, I randomly assigned countries into a top 20 in terms of number of users for each day. However, I subsequently changed how I managed the country performance so that it was a more accurate and better addition to the dashboard which made this final section of code redundant.

<h3>3. Building the dashboard</h3>
I used Tableau to create the dashboards. I decided to make two: one that showed more general information about social media performance and one that allowed a bit more of a deepdive into separate platforms or post types. I used 3 separate data sources and used joins and blends to create relationships between them. I used Dynamic Parameters to allow people using the dashboard to select the date and platform. I then created the dashboards and made sure all the parameters were working correctly with the individual charts.


<h3>Global Dashboard screenshot</h3>
<img src ="https://github.com/pdizzle10/social-media-dashboard/blob/main/finished_product/global_dashboard.png">

<h3>Platform Dashboard screenshot</h3>
<img src = "https://github.com/pdizzle10/social-media-dashboard/blob/main/finished_product/platform_dashboard.png">

<h3>Platform walkthrough</h3>

https://github.com/pdizzle10/social-media-dashboard/assets/134708540/6dab7ebe-f653-4e01-ac53-19f9598d6926




I tried to upload this to Tableau Public but unfortunately it deleted all of my formatting when I uploaded, so the easiest way to view this project yourself is to download this repo and run the Tableau file directly.
