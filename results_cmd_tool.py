# Command line tool using Python to fetch the results of students from "http://exam.msrit.edu/"
# Refer the readme file for instructions on how to use the tool
# Made by Manish.M

import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import optparse


branches = ['CS', 'EC', 'IS', 'ME', 'ML', 'CH', 'CV', 'EE', 'TI', 'EI', 'IM', 'AT', 'BT']

url = 'http://exam.msrit.edu/index.php'


def fetch_results(usn):

    final_res = "<tr>"
    values = {'usn': usn,  
              'option': 'com_examresult',
              'task': 'getResult'}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result_page = response.read().decode("utf-8")

    soup = BeautifulSoup(result_page, 'html.parser')
    try:
        name = soup.find("div", {"class": "uk-card uk-card-body stu-data stu-data1"}).find('h3').get_text(strip=True)
        sem = soup.find("div", {"class": "uk-card uk-card-body stu-data stu-data2"}).find('p').get_text(strip=True)[-1:]
        credits_registered = soup.find("div", {"class": "uk-card uk-card-default uk-card-body credits-sec1"}).find(
            'p').get_text(strip=True)
        credits_earned = soup.find("div", {"class": "uk-card uk-card-default uk-card-body credits-sec2"}).find(
            'p').get_text(strip=True)
        sgpa = soup.find("div", {"class": "uk-card uk-card-default uk-card-body credits-sec3"}).find('p').get_text(
            strip=True)
        cgpa = soup.find("div", {"class": "uk-card uk-card-default uk-card-body credits-sec4"}).find('p').get_text(
            strip=True)

        final_res += "<td>" + usn + "</td>" + "<td>" + name + "</td>" + "<td>" + sem + "</td>" + "<td>" + credits_registered + "</td>"
        final_res += "<td>" + credits_earned + "</td>" + "<td>" + sgpa + "</td>" + "<td>" + cgpa + "</td>"
        final_res += "<td><table><tr><th>Code</th><th>Subject</th><th>Creds registered</th><th>Creds earned</th><th>Grade</th></tr>"

        res = soup.find("table", {"class", "uk-table uk-table-striped res-table"}).find_all("tr")[1:]
        results = []
        for item in res:
            r = []
            data = item.find_all('td')
            final_res += "<tr>"
            for x in data:
                r.append(x.get_text(strip=True))
                final_res += "<td>" + x.get_text(strip=True) + "</td>"
            final_res += "</tr>"
            results.append(r)

        final_res += "</table></td></tr>"

    except:
        print(usn + " not found "+ " or website is down " + " or check your internet connection")
        return None

    return final_res


def is_int(y):
    try:
        int(y)
        return True
    except:
        return False


def validate_parameters(year, branch, max_range, parser):
    if not year or not branch or not max_range:
        print(parser.usage)
        exit(0)
    
    else:
        # Validating the year entered by the user
        if is_int(year):
            if len(year) == 2:
                pass
            else:
                print("Enter only the last 2 digits for year (yy)")
                exit(1)
        else:
            print("The year should be an integer")
            exit(2)
        
        # Validating the branch entered by the user
        if branch in branches:
            pass
        else:
            print("Enter a valid branch extension such as: ")
            for b in branches:
                print(b, end=' ')
            print("\n")
            exit(3)
        # Validating the Max range of USNs
        if is_int(max_range):
            pass
        else:
            print("Enter a valid integer for max range of USNs")
            exit(4)


def make_usn(y, b, n):
    usn = '1MS' + y + b 
    num = str(n)

    if len(num) < 2:
        usn = usn + '00' + num
    elif len(num) < 3:
        usn = usn + '0' + num
    else:
        usn = usn + num

    return usn


def main():
    parser = optparse.OptionParser('Usage: ' + '-y <year(yy)> -b <branch extension(XX)> -m <max range of USN>')
    parser.add_option('-y', '--year', dest='year', action="store", type='string', help='specify the last two digits of the year')
    parser.add_option('-b', '--branch', dest='branch', action="store", type='string', help='specify the branch extension')
    parser.add_option('-m','--max', dest='max', action="store", type='string', help='specify the max limit of USNs')
    (options, args) = parser.parse_args()

    year = options.year
    branch = options.branch
    max_range = options.max

    branch = branch.upper()

    validate_parameters(year, branch, max_range, parser)

    text = """<html>
            <head>
                <title>Results</title>
                <style>
                    td, th {
                         border: 1px solid #dddddd;
                         text-align: left;
                         padding: 8px;
                    }
                </style>
            </head>
            <body>
                <table>
                    <tr><th>USN</th><th>Name</th><th>Sem</th><th>Creds registered</th><th>Creds earned</th><th>SGPA</th><th>CGPA</th><th>Subject-wise results</th></tr>"""

    f = open('results.html', 'w')

    for i in range(1, int(max_range)+1):
        usn = make_usn(year, branch, i)
        r = fetch_results(usn)
        if r:
            # check if the usn exists or not before writing to the file
            text += r
        print('Writing results of ' + usn + ' to results.html')

    text += """          </table>
                    </body>
                </html>
    """

    f.write(text)
    f.close()

    print("Results successfully fetched and stored in results.html")


if __name__ == '__main__':
    main()
