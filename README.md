# MSRIT-Results-scraper

![Sample Result of a student](https://github.com/Manish-M2018/MSRIT-Results-scraper/blob/master/images/sample_result.png)
<br>
<b>Sample result of a student</b>
<br>

# Results scraper cli tool (results_cmd_tool.py)

A command line interface that is designed for automating the task of fetching the results of students from http://exam.msrit.edu/ and displaying it in a tabular format on the browser<br>

# Usage

<b>Clone the repository to the local machine</b> <br>
<pre>
git clone https://github.com/Manish-M2018/MSRIT-Results-scraper.git
</pre>

<b> Change directory </b> <br>
<pre>
cd MSRIT-Results-scraper
</pre>

<b> Using the tool </b> <br>
<pre>
python3 results_cmd_tool.py -y &lt;year(yy)&gt; -b &lt;branch extension(XX)&gt; -m &lt;max range of USN&gt; 
</pre>

<b> Arguments </b> <br>
<pre> 
-y &lt;year(yy)&gt; -b &lt;branch extension(XX)&gt; -m &lt;max range of USN&gt; 
</pre>  
 
<b> Options </b> <br>
<pre>
  -h, --help            show this help message and exit  <br>
  -y YEAR, --year=YEAR  specify the last two digits of the year <br>
  -b BRANCH, --branch=BRANCH
                        specify the branch extension  <br>
  -m MAX, --max=MAX     specify the max limit of USNs <br>
</pre>

<b> Allowed branches for option -b or --branch</b> <br>
<pre>
CS, EC, IS, ME, ML, CH, CV, EE, TI, EI, IM, AT, BT
</pre>

<b> Example usage </b> <br>
Let us take the example where we want to retrieve the results of the students from USN 1 to 10 in Computer Science (CS) branch who joined the college in the year 2018<br>
<pre>
python results_cmd_tool.py -y 18 -b CS -m 10
</pre>
<b>(OR)</b> <br>
<pre>
python results_cmd_tool.py --year 18 --branch CS --max 10
</pre>

# Where can I view the results that were fetched?
- The results that were fetched from the website is stored in a file called <b>results.html</b> in the same directory
- Open the file <b>results.html</b> in order to view the results in a tabular format on the browser

# Points to note
- Make sure that the website is not down for maintenance before using the tool
- Do not use the tool for disrupting the normal functioning of the website
- The tool does not store the results anywhere online (results are fetched on the spot)
- Make sure you have an active internet connection while using the tool 
- Some USNs in the range may not be available due to various reasons

<br><br>
# Normal code for scraping the results of a single student (scraper.py)
This is a piece of code in Python to scrape the results of a single student of MSRIT.<br>
Take a look at this new results feature in action on [MSRIT Connect](https://play.google.com/store/apps/details?id=msrit.msritconnect.com.msritconnect&hl=en)!<br>
<br>
Replace <i>"USN Goes Here"</i> with your <i>USN</i> to fetch the result :) <br>
All the best!
