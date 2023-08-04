from io import BytesIO
from PIL import Image
import requests
import pandas as pd



def create_disneydf():
    #I would likelt change this to be more dynamic of a url to get count in the future
    #or set the number to 1000000 since it auto changes it to the max count of characters. 
    #but that also depends on performance.
    url = 'https://api.disneyapi.dev/character?page=1&pageSize=8000'
    response= requests.get(url)
    #creating a counting variable
    max_cnt=response.json()['info']['count']
    #create a variable to shorthand the data we will be indexing through
    my_data = response.json()['data']


    #columns list for PANDA PANDA PANDA PANDA
    c=['disney_id','name','allies','ally_count','enemies','enemy_count','films','film_count','tv_shows','show_count','park_attractions','ride_count','image_blob']
    df = pd.DataFrame(columns=c)

    for cnt in range(max_cnt):
    #begin to loop through the data and grab our info
        
        row=[]
        str1=''
        #initialize variables needed to create rows
        

        #disney_id (there are dupe names that are sep chars)
        row.append(my_data[cnt]['_id'])
        #name of character
        row.append(my_data[cnt]['name'])
        #allies
        str1='|'.join(i for i in my_data[cnt]['allies'] )
        row.append(str1)
        row.append(len(my_data[cnt]['allies']))
        #enemies
        str1='|'.join(i for i in my_data[cnt]['enemies'])
        row.append(str1)
        row.append(len(my_data[cnt]['enemies']))
        #films
        str1='|'.join(i for i in my_data[cnt]['films'])
        row.append(str1)
        row.append(len(my_data[cnt]['films']))
        #tvshows
        str1='|'.join(i for i in my_data[cnt]['tvShows'])
        row.append(str1)
        row.append(len(my_data[cnt]['tvShows']))
        #attractions
        str1='|'.join(i for i in my_data[cnt]['parkAttractions'])
        row.append(str1)
        row.append(len(my_data[cnt]['parkAttractions']))
        #image (had to try here because field is optional)
        try:
            row.append(my_data[cnt]['imageUrl'])
        except:
            row.append('')
        #record

        df.loc[len(df)] = row
    #
    #------------end of for loop-------------------------------------
    return df

def removal_criteria(df):
    #remove any characters that don't exist in shows, movies, or as a ride
    mask = (df['show_count']==0)&(df['film_count']==0)&(df['ride_count']==0)
    df.drop(df[mask].index, inplace=True)
    return df

def update_data_sql(df):
    #this is MY URL and password for my server.
    sql_url = 'postgresql://nikgyzol:Ds1C2-7ZejdawQEDjuWA71oCvOl4zMFZ@drona.db.elephantsql.com/nikgyzol'
    df.to_sql('disney_chars',con=sql_url, if_exists='replace')
    #I wanted preserve the commas in movie titles so I utilized the semicolon
    df.to_csv('disney_chars_info',index=False,sep=';')

    return print('SQL DB Updated! and file created')

def get_image(n,df):
    ndf = df[(df['name']== n.title() )]
    if len(ndf)>0:
        for char in ndf['image_blob']:

            try:   
                #block for image
                img_str = char
                response = requests.get(img_str)
                img= Image.open(BytesIO(response.content))
                img =img.convert('RGB')
                output_image_path = 'output_image.jpg'
                img.save(output_image_path)
                #display image
                img.show()
            except:
                print('Image not found')
        return print(f'Here is {n}, they belong to {len(ndf)} characters(s)')
    else:
        return print('Character not found check your spelling!')


#Function testing block

d = create_disneydf()
d = removal_criteria(d)
update_data_sql(d)

#Bonus block

get_image('achhilles',d)
get_image('achilles',d)
get_image('ariel',d)