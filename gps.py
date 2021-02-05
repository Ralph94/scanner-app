from time import sleep
from PIL import Image
import sound
import time


	
image = Image.open('dhl.PNG')
image2 = Image.open("box.JPG")
image3 = Image.open("des.JPG")
image4 = Image.open("dhls.jpg")
#image5 = Image.open("dhlV.JPG")
image.show()
size = image3.resize((150,150))
time.sleep(1)
image4.show()



Courier = input("Courier I.D ")
sound.play_effect('arcade:Coin_1')

Service = input("Service: ")
sound.play_effect('arcade:Coin_1')

Facility = input("Facility: ")
sound.play_effect('arcade:Coin_1')

MyRoute = input("Please input route I.D ")
sound.play_effect('arcade:Coin_1')

Cyclecode = input("Cycle code: ")
sound.play_effect('arcade:Coin_1')

Load = input("Scan your boxs: ")
sound.play_effect('digital:PowerUp2')
image2.show()
	


Address = ["1095 Nevada ST", "375 Harbor Cove Dr", "700 Putnam Court", "5798 Bozic Lane", "2136 San Remo Drive", "3171 Sky Country Dr", "4130 Riverhaven Drive"]
sound.play_effect(' ')

if Courier == ("RNOSP01"):
	print(Courier)
	
	
if Service == ("RNO"):
	print(Service)
	
	
if Facility == ("RNO"):
	print(Facility)
	

if MyRoute == ("RN1R"):
	print("This is how many boxes we have for today " + Load)
	
if Cyclecode == ("A"):
	print("OK were all loaded up lets roll out!\n")
	
	while True:
		directions = input("input location: ")
		
		
		if directions == ("1"):		 
			sound.play_effect('547350__legnalegna55__truck-drive-by-and-drive-away.mp3')
			size.show()
			print("This is your first stop: " + str(Address[0]) + " \nName: Roger Blaine"
		 + " \nItem: Package" + " \nWeight: 2lbs "+ " \ncheck for your next stop!\n")
		 
		 
		 
		 
		elif directions == ("2"):
			sound.play_effect('547350__legnalegna55__truck-drive-by-and-drive-away.mp3')
			size.show()
			print("This is your second stop: " + str(Address[1]) + " \nName: Blake White"
		 + " \nItem: Box" + " \nWeight: 12lbs "+ " \ncheck for your next stop!\n")
		 
		 
		 
		elif directions == ("3"):
			sound.play_effect('547350__legnalegna55__truck-drive-by-and-drive-away.mp3')
			size.show()
			print("This is your third stop: " + str(Address[2]) + " \nName: Lily Reys"
		 + " \nItem: Box" + " \nWeight: 8lbs "+ " \ncheck for your next stop!\n")
		 
		 
		elif directions == ("4"):
			sound.play_effect('547350__legnalegna55__truck-drive-by-and-drive-away.mp3')
			size.show()
			print("This is your fourth stop: " + str(Address[3]) + " \nName: Juan Dykes"
		 + " \nItem: Package" + " \nWeight: 5lbs "+ " \ncheck for your next stop!\n")
		 
		 
		 
		elif directions == ("5"):
			sound.play_effect('547350__legnalegna55__truck-drive-by-and-drive-away.mp3')
			size.show()
			print("This is your fifth stop: " + str(Address[4]) + " \nName: Tim Mclean"
		 + " \nItem: Package" + " \nWeight: 22lbs "+ " \ncheck for your next stop!\n")
		 
		 
		elif directions == ("6"):
			sound.play_effect('547350__legnalegna55__truck-drive-by-and-drive-away.mp3')
			size.show()
			print("This is your sixth stop: " + str(Address[5]) + " \nName: Antonio Garza"
		 + " \nItem: Package" + " \nWeight: 4lbs "+ " \ncheck for your next stop!\n")
			
			
			
		elif directions == ("7"):
			sound.play_effect('547350__legnalegna55__truck-drive-by-and-drive-away.mp3')
			size.show()
			print("This is your seventh and final stop: " + str(Address[6]) + " Your route has been completed good job!" + "\U0001f31f")
			break
			
		
			
done_route = input(": ")	
			
def Done():
	if done_route == ("done"):
		print("Okay route is done time to go back to the hub and park the van!" + " \U0001F69A ")
		#image5.show()
		sound.play_effect('digital:ZapTwoTone2')
		sound.play_effect('truck.wav')
		
    	
Done()		
			
			




	
		 
		 
		
	
		 
	


	
		 
		 
		
