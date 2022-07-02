from operator import index
import requests, openpyxl
excel=openpyxl.Workbook()
print(excel.sheetnames)
sheet=excel.active
sheet.title='league 2013'
sheet.append(['Team name','Team points'])



from bs4 import BeautifulSoup
url = 'https://www.skysports.com/premier-league-table/2013'
page = requests.get(url)
print(page.status_code)
print(page)
print(page.text)
soup = BeautifulSoup(page.text,'html.parser')
#print(soup.prettify)
print(soup.find('a'))
print(soup.find_all('a'))
soup.find_all('a')[1]
league=soup.find('table',class_ = 'standing-table__table')
#print(league)
league_table= league.find_all('tbody')
#print(league_table)
for league_teams in league_table:
    rows=league_teams.find_all ('tr')
    for row in rows:
        team_names=row.find('td',class_='standing-table__cell standing-table__cell--name').text.strip() 
        #print(team_names)
        team_points = row.find_all('td', class_='standing-table__cell')[9].text.strip()
        print(team_names,team_points)
        league_2013=[]
        for league_teams in league_table:
            rows=league_teams.find_all ('tr')
            for row in rows:
                team_names=row.find('td',class_='standing-table__cell standing-table__cell--name').text.strip() 
            #print(team_names)
            team_points = row.find_all('td', class_='standing-table__cell')[9].text.strip()
            #print(team_points)
            sheet.append([team_names,team_points])

        excel.save('league score.xlsx')
           
        

