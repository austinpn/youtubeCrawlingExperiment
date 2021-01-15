from bs4 import BeautifulSoup
import requests


def clean_link(url):
    url = url.replace('\\' , '')
    url = url.replace('u0026' , '&')
    # url = url.replace('%26' , '&')
    # url = url.replace('%2F' , '/')
    # url = url.replace('%3A' , ':')
    # url = url.replace('%3F' , '?')
    # url = url.replace('%3D' , '=')

    
    #url = url.replace('%25' , '%')
    
    return(url)

def fetch_link_list(y_url):
    page = requests.get('https://www.youtube.com/watch?v=5UNXnqNpzKw').text
    soup = BeautifulSoup(page , 'html.parser')

    link_soup = soup.find('div' , id = 'player').find_all('script')[1].text
    link_split = link_soup.split('url')
    # with open('blank.txt' , 'w') as f:
    #     f.write(link_soup)

    #link_split = [x for x in link_split if x[32:38]=='google' and x[0]=='=']

    with open('split.txt' , 'w') as f:
        for link in link_split:
            f.write(link+'\n')

    link_dict = {}

    for line in link_split:
        

        #search for quality label location
        lab_loc = line.find('qualityLabel')
        if(lab_loc ==-1):
            lab_loc = line.find('AUDIO_Q')
        check_populated = 0
        
        if "audio" in line:
            vid_type = 'audio'
        elif 'mp4' in line:
            vid_type = 'mp4'
        else:
            vid_type = 'webm'
        if lab_loc!=-1:
            #print(line)
            while True:
                key ='{}_{}{}'.format(vid_type , (line[lab_loc+17:line.find('\\' , lab_loc+18)]) , check_populated)
                if key not in link_dict:
                    link_dict[key] = clean_link(line[1:line.find('"' , 5)-1])
                    break
                else:
                    check_populated+=1


    with open('dict.txt' , 'w') as f:
        for link in sorted(link_dict):
            f.write(f'{link}: {link_dict[link]}'+'\n')
    # with open('split.txt' , 'w') as f:
    #     for link in link_split:
    #         f.write(link+'\n')

if __name__ == "__main__":
    fetch_link_list('https://www.youtube.com/watch?v=9NjKgV65fpo')