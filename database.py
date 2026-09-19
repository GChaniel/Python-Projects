
#import sqlite3 module
import sqlite3

# Created a fileList variable that stores all file names.
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


# Connect to the filelist database
conn = sqlite3.connect('filelist.db')

with conn:
    cur = conn.cursor()
    
    # Create a table with an automatic ID and a text field for filenames
    cur.execute("CREATE TABLE IF NOT EXISTS tb1_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT UNIQUE \
        )")

    # Use a for loop to filter .txt filenames, insert them into the database,
    # Used UNIQUE constraint and INSERT OR IGNORE statement,
    # to prevent duplicate entries when the program runs again.
    for item in fileList:
        if item.endswith('.txt'):
            cur.execute("INSERT OR IGNORE INTO tb1_files(col_fileName) VALUES (?)",
                    (item,))
            print(item)
        
    
    conn.commit()
conn.close()
