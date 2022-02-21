# Imports
import requests
import json
from bs4 import BeautifulSoup
import sys
import time
import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from removeGoogle import removeGoogle
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from PIL import Image
from io import BytesIO
from alive_progress import alive_bar
import imagehash


# print("starting program")

# print(Path.cwd())

if len(sys.argv) <= 2:
    searchTerm = (input("Search term: ")).strip()
    targetQuantity = int((input("Quantity of images: ")).strip())

else:
    targetQuantity = int(sys.argv[1])
    searchTerm = " ".join(list(sys.argv[2:]))

if searchTerm == None or targetQuantity == None or searchTerm == "" or targetQuantity == "":
    sys.exit()

# targetQuantity = int(sys.argv[1])
# searchTerm = " ".join(list(sys.argv[2:]))


# Options
options = Options()
options.headless = True
searchQuery = f"https://www.google.co.in/search?q={searchTerm}&source=lnms&tbm=isch"
waitTime = 2
knownImageTypes = ['jpeg', 'png', 'jpg']
displayCounterPadding = "0"
folderNameOfOutput = "output"
blurSize = 16
paddingAdjustment = 30

# print("finished setting options")


# Quit if target is impossible
if targetQuantity > 400:
    # print("somehow, the target quantity specified is more than 400, so we're exiting")
    sys.exit()


# print("starting the driver")

# Starting Driver
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
driver.get(searchQuery)

# print("finished setting up the driver")



historyOfLengthOfLinks = []




while True:


    # print("starting to go down")

    # Scrolling to bottom
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    time.sleep(waitTime)

    # print("finished waiting")


    # print("getting the page")
    # Getting the page
    soup = BeautifulSoup(driver.page_source, features='lxml')
    daSoup = BeautifulSoup(soup.prettify(), 'html.parser')
    soup = daSoup


    # print("gotten the page")


    # Getting every link starting with http
    listOfA = soup.find_all('a')

    # print("getting all the a tags")

    listOfLinks = []
    


    for line in listOfA:

        theHref = line.get('href')

        if type(theHref) == str:
            if theHref.startswith('http'):
                listOfLinks.append(theHref)
                # print("adding this http tag to the list of links")


    # Removing google-related links
    filteredLinks = removeGoogle(listOfLinks)

    # print("removed google-related links")

    # print(f"current length of fitered links is {len(filteredLinks)}")

    historyOfLengthOfLinks.append(len(filteredLinks))

    # Only ending if it reaches 400 links

    if len(historyOfLengthOfLinks) >= 2:
        if historyOfLengthOfLinks[-1] == historyOfLengthOfLinks[-2]:
            # print("last two records of the length of links recorded were the same, so we'll stop this scrolling")
            break

    # if len(filteredLinks) >= 400:
        
    #     break



# After getting all 400 links, we start on the main loop
os.system('cls')



if targetQuantity > historyOfLengthOfLinks[-1]:
    targetQuantity = historyOfLengthOfLinks[-1]



# print(f"Length of filtered links without google: {len(filteredLinks)}")

# print(f"Setting up directory for '{searchTerm}'")
dirToOutput = Path(folderNameOfOutput)
dirToProjOutput = dirToOutput / searchTerm


# print(f"Directory to project output: {str(dirToProjOutput)}")

dirToProjOutput.mkdir(parents=True, exist_ok=True)
currentDir = Path.cwd()






# lengthOfImageLinks = len(linkOfImages)
lengthOfImageLinks = int(targetQuantity)
charsOfImageLinks = len(str(lengthOfImageLinks))


# print(f"the total number of image links i found: {lengthOfImageLinks}")


# Announcement as to which image we're trying to do
# print(f"Grepping images for: '{searchTerm}'")
print(f"Downloading images for: '{searchTerm}'")



imageHashes = {}
imageDuplicates = []



linkOfImages = []
finishedLoop = False

indexOfCurrentImage = -1
simpleIndex = 1

# for link in filteredLinks:
# for total in [lengthOfImageLinks]:
for total in [targetQuantity]:
    with alive_bar(total) as bar:
        while True:
            # print(finishedLoop)
            # print("1")

            if finishedLoop == True:

                # print("breaking out of this loop")
                # break
                # print("exiting")
                sys.exit()
            
            # print("2")

            indexOfCurrentImage += 1
            actualIndex = indexOfCurrentImage

            # print(f"index of the current image: (out of all search results) {actualIndex}")
            # print(f"index of the numbered attempt of downloading. basically, the successful downloads, this is for labelling: {simpleIndex}")

            # print("sleeping 2 seconds........////////////................")
            time.sleep(2)

            # print("3")

            try:
                # print("getting the request")
                r = requests.get(filteredLinks[actualIndex])
                soup = BeautifulSoup(r.text, 'html.parser')
                listOfMeta = soup.find_all("meta")
                # print(f"found all the metas, {len(listOfMeta)}")

                # print("4")

                for theMeta in listOfMeta:
                    theProperty = theMeta.get('property')


                    # print("5")

                    if str(theProperty) == "og:image":

                        
                        imageLink = theMeta.get('content')

                        # print(f"the og:image is apparently {imageLink}")

                        imageLinkResponse = requests.head(imageLink)
                        theContentType = imageLinkResponse.headers['content-type']

                        
                        theFileExtension = (theContentType.partition("/"))[2]

                        # print("6")

                        # print(f"and the file extension is {theFileExtension}")

                        if theFileExtension in knownImageTypes:

                            # print(f"which is recognised in our known image types")
                            # linkOfImages.append([imageLink, theFileExtension])
                            # currentLengthOfImages = len(linkOfImages)
                            displayCounter = (str(simpleIndex)).rjust(charsOfImageLinks, displayCounterPadding)
                            fullPathToImg = dirToProjOutput / (displayCounter + "." + theFileExtension)

                            # print(f"full path to image: {str(fullPathToImg)}")

                            # print(f"attempting to get the requested image now")


                            requestImage = requests.get(imageLink)
                            myImage = Image.open(BytesIO(requestImage.content))
                            myImage.save(fullPathToImg)

                            # print("7")

                            

                            # print(f"it got saved, and the simple index (completed images) got upped by 1")



                            # now, check whether the image is a duplicate
                            # if it's a duplicate, treat it like an except. up the indexOfCurrentImage and go next
                            # otherwise, THEN check whether the 
                            # 
                            # 
                            # simpleindex exceeded the target quantity
                            # then deal with finishedLoop


                            # imageIsDuplicate = False

                            



                            with Image.open(fullPathToImg) as investigateImage:




                                width, height = investigateImage.size

                                theSmallerDimension = ""
                                if width > height:
                                    theSmallerDimension = "height"
                                    paddingMargin = int(int(paddingAdjustment / 100) * height)
                                elif height > width:
                                    theSmallerDimension = "width"
                                    paddingMargin = int(int(paddingAdjustment / 100) * width)
                                elif width == height:
                                    theSmallerDimension = "equal"
                                    paddingMargin = int(int(paddingAdjustment / 100) * height)
                                else:
                                    pass

                                if theSmallerDimension == "equal":

                                    point1 = (0 + paddingMargin, 0 + paddingMargin)
                                    point2 = (width - paddingMargin, height - paddingMargin)

                                    value1, value2 = point1
                                    value3, value4 = point2

                                    investigateImageInput = investigateImage.crop((value1, value2, value3, value4))
                                    
                                
                                else:
                                    if theSmallerDimension == "height":
                                        theDifference = width - height
                                        theMargin = int(theDifference / 2)

                                        point1 = (theMargin + paddingMargin, 0 + paddingMargin)
                                        point2 = (theMargin + height - paddingMargin, height - paddingMargin)

                                    elif theSmallerDimension == "width":
                                        theDifference = height - width
                                        theMargin = int(theDifference / 2)

                                        point1 = (0 + paddingMargin, theMargin + paddingMargin)
                                        point2 = (width - paddingMargin, theMargin + width - paddingMargin)
                                    
                                    value1, value2 = point1
                                    value3, value4 = point2
                                    investigateImageInput = investigateImage.crop((value1, value2, value3, value4))

                                    # imageCropped.save(pathToCroppedThumbnail)
                                







                                # investigateImageSmall = investigateImage.resize((blurSize, blurSize), resample=Image.BILINEAR)

                                investigateImageSmall = investigateImageInput.resize((blurSize, blurSize), resample=Image.BILINEAR)


                                investigateImageBlurred = investigateImageSmall.resize(investigateImage.size, Image.NEAREST)

                                # temp_hash = imagehash.average_hash(investigateImage)
                                temp_hash = imagehash.average_hash(investigateImageBlurred)

                                # print("8")


                                # if temp_hash in imageHashes:
                                #     print(f"Duplicate image for {simpleIndex} found")
                                #     imageDuplicates.append(simpleIndex)
                                #     imageIsDuplicate = True
                                # else:
                                #     imageHashes[temp_hash] = simpleIndex
                                #     imageIsDuplicate = False


                                if temp_hash not in imageHashes:

                                    # print("9")

                                    imageHashes[temp_hash] = simpleIndex


                                    if simpleIndex >= targetQuantity:
                                        # print("it's considered done, so we'll tell it to consider finishedLoop to be true")

                                        # print("10: simpleindex over targetquantity")
                                        finishedLoop = True
                                    
                                    else: 
                                        # print("it's NOT finished, we're adding 1 to the simple index for it to continue next round")
                                        # print(f"{simpleIndex} -> {simpleIndex + 1}")
                                        simpleIndex += 1


                                        # print("10: simpleindex NOT over targetquantity")

                                    # print(f"bumped up the bar by one")

                                    # print("11")
                                    bar()

                                else:
                                    # print("!!!!!!!!!!!!!!!! welp, it's a duplicate LOL !!!!!!!!!!!!!!!!!!!")
                                    # print("DELETE THAT SHIT")
                                    os.unlink(fullPathToImg)
                                    indexOfCurrentImage += 1
                                    # print("DUPLICATE!!")
                                    # print(f"WE'RE STARTING FROM {simpleIndex} AGAIN")


            except:
                # print(f"for some reason, we're failling this {indexOfCurrentImage} so we're upping it by 1 and hoping for the next to work")

                # print("WRONG?")
                indexOfCurrentImage += 1


sys.exit()

# counter = 0
# for total in [lengthOfImageLinks]:
#     with alive_bar(total) as bar:
#         for i in range(lengthOfImageLinks):
#             theImageBundle = linkOfImages[i]
#             theImageLink = theImageBundle[0]
#             counter += 1
#             displayCounter = (str(counter)).rjust(charsOfImageLinks, displayCounterPadding)
#             theFileExtension = theImageBundle[1]

#             fullPathToImg = dirToProjOutput / (displayCounter + "." + theFileExtension)

#             requestImage = requests.get(theImageLink)
#             myImage = Image.open(BytesIO(requestImage.content))
#             myImage.save(fullPathToImg)

#             bar()



#             for i in range(lengthOfImageLinks):

#                 if finishedLoop == True:
#                     break

#                 try:
#                     r = requests.get(link)
#                     soup = BeautifulSoup(r.text, 'html.parser')

#                     listOfMeta = soup.find_all("meta")

#                     for theMeta in listOfMeta:
#                         theProperty = theMeta.get('property')

#                         if str(theProperty) == "og:image":
#                             imageLink = theMeta.get('content')

#                             imageLinkResponse = requests.head(imageLink)
#                             theContentType = imageLinkResponse.headers['content-type']
#                             theFileExtension = (theContentType.partition("/"))[2]

#                             if theFileExtension in knownImageTypes:
#                                 # linkOfImages.append([imageLink, theFileExtension])

#                                 # currentLengthOfImages = len(linkOfImages)
#                                 currentLengthOfImages = len(linkOfImages)

#                                 print(f"Matched images: [{currentLengthOfImages}/{targetQuantity}]")

#                                 # if len(linkOfImages) >= targetQuantity:
#                                 #     finishedLoop = True
#                 except:
#                     pass



# counter = 0
# for total in [lengthOfImageLinks]:
#     with alive_bar(total) as bar:
#         for i in range(lengthOfImageLinks):
#             theImageBundle = linkOfImages[i]
#             theImageLink = theImageBundle[0]
#             counter += 1
#             displayCounter = (str(counter)).rjust(charsOfImageLinks, displayCounterPadding)
#             theFileExtension = theImageBundle[1]

#             fullPathToImg = dirToProjOutput / (displayCounter + "." + theFileExtension)

#             requestImage = requests.get(theImageLink)
#             myImage = Image.open(BytesIO(requestImage.content))
#             myImage.save(fullPathToImg)

#             bar()

# sys.exit()