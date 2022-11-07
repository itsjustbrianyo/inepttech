# import modules
import os
import sys
import time
import qrcode
from PIL import Image

# Set the logo directory
logo_dir = os.getcwd() + "/logos/"
save_dir = os.getcwd() + "/qr codes/"

# Set save directory
#user_profile = os.environ['USERPROFILE']
#save_dir = user_profile + "/Desktop/"

# Show Banner
banner = """
╭━━━┳━━━╮  ╭━━━╮╱╱╱╱╭╮
┃╭━╮┃╭━╮┃  ┃╭━╮┃╱╱╱╱┃┃
┃┃╱┃┃╰━╯┃  ┃┃╱╰╋━━┳━╯┣━━┳━━╮
┃┃╱┃┃╭╮╭╯  ┃┃╱╭┫╭╮┃╭╮┃┃━┫━━┫
┃╰━╯┃┃┃╰╮  ┃╰━╯┃╰╯┃╰╯┃┃━╋━━┃
╰━━╮┣╯╰━╯  ╰━━━┻━━┻━━┻━━┻━━╯
╱╱╱╰╯By Inepttech.com 2022.10
-----------------------------"""
print(banner + "\n\n")

try:
    repeat = True
    while repeat:
        time.sleep(1.5)

        # User Selection
        user_selection = True
        while user_selection:
            user_option = input("Select one of the following: \
            \n 1 - Option 1 \
            \n 2 - Option 2 \
            \n 3 - Option 3 \
            \nOr press Q to quit \
            \n\nYour Selection: ")

            # Logo selection based on charter
            if user_option == "1":
                option_logo = logo_dir + "logo1.png"
                break
            elif user_option == "2":
                option_logo = logo_dir + "logo2.png"
                break
            elif user_option == "3":
                option_logo = logo_dir + "logo3.png"
                break
            elif user_option == ("q" or "Q"):
                print("Quitting")
                sys.exit()
            else:
                print("Not a valid selection. Please try again")

        # Get serial number and concatenate the inventory URL
        serial_number=input("Enter the serial number: ")
        inventory_url=("" + serial_number)

        logo = Image.open(option_logo)

        # base width of logo
        basewidth = 200

        # adjust image size
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        QRcode = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )

        # adding URL or text to QRcode
        QRcode.add_data(inventory_url)

        # generating QR code
        QRcode.make()

        # taking color name from user
        QRcolor = "black"

        # adding color to QR code
        QRimg = QRcode.make_image(
            fill_color=QRcolor, back_color="white").convert("RGB")

        # set size of QR code
        pos = ((QRimg.size[0] - logo.size[0]) // 2,
            (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)

        # save the QR code generated
        QRimg.save(save_dir + serial_number + ".png")

        print("\n\n==========\
        QR code generated!\
        ==========\n\n")
        time.sleep(.5)

        # start again?
        restart_selection = True
        while restart_selection:
            restart = input("Would you like to generate another QR code? Enter Y to generate another QR Code or Q to exit: ")
            if restart == ("q" or "Q"):
                print("Quitting")
                sys.exit()
            elif restart == ("y" or "Y"):
                print("\n")
                break
            else:
                print("That is not a valid selection, please try again!")
except Exception as e:
    print("\n\nUnexpected error:" + str(e))
    time.sleep(10)