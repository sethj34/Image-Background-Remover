#Import Libraries
from rembg import remove
import easygui
from PIL import Image
import time

#UX
print("When using the Image Converter v2.1.2, you may choose any file format (ex. .png, .jpg, .jpeg), but when saving the image, please only use the file format .png. Thanks!")
print("Now opening the Image Converter, please be patient...")
time.sleep(3)

#Image upload and download
inputPath = easygui.fileopenbox(title='Select image file')
outputPath = easygui.filesavebox(title='Save file to: ')

#Optional image resizing
while True:
    try:
        resize_choice = input("Would you like to resize the new image? (Y or N): ")

        #Y FOR RESIZE

        #User input

        if resize_choice.upper() == "Y":
            resizeyn = 1

            #WHILE STATEMENT FOR WIDTH

            while True:
                try:
                    width = int(input("What would you like the width to be? (Integer values only!): "))
                    if width < 1:
                        print("Width cannot be less than 1.")    
                        continue
                    elif width >= 1:
                        print("Chosen width is %s" % (width))
                        time.sleep(1)
                    
                except ValueError or NameError:
                    print("Please choose an integer value.")
                    continue
            
            #WHILE STATEMENT FOR HEIGHT
                

                while True:
                    try:
                        height = int(input("What would you like the height to be? (Integer values only!): "))
                        if height < 1:
                            print("Height cannot be less than 1.")    
                            continue
                        elif height >= 1:
                            print("Chosen height is %s" % (height))
                            time.sleep(1)
                            break

                    except ValueError or NameError:
                        print("Please do not include letters or special characters.")
                        continue
                break
            break

        #N FOR RESIZE

        elif resize_choice.upper() == "N":
            resizeyn = 0
            break
        
    except ValueError:
        print("Please make a valid choice.")

#If user chose to resize

if resizeyn == 1:
    input = Image.open(inputPath)
    resizedimage = input.resize((width, height))
    output= remove(resizedimage)
    output.save(outputPath)
    print("Your file has been saved in the chosen directory! This program will automatically close.")
    time.sleep(3)

#If user chose not to resize

elif resizeyn == 0:
    input = Image.open(inputPath)
    output= remove(input)
    output.save(outputPath)
    print("Your file has been saved in the chosen directory! This program will automatically close.")
    time.sleep(3)