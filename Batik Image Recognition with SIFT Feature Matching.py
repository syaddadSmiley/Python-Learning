sk_path = 'batik-sekar/5.jpg'
sk_img = cv2.imread(sk_path)

path_celup = ["batik-celup/*.jpg"]
path_ciamis = ["batik-ciamis/*.jpg"]
path_kawung = ["batik-kawung/*.jpg"]
path_priangan = ["batik-priangan/*.jpg"]

# Random Images======================================
glob_celup = glob.glob(random.choice(path_celup))
glob_ciamis = glob.glob(random.choice(path_ciamis))
glob_kawung = glob.glob(random.choice(path_kawung))
glob_priangan = glob.glob(random.choice(path_priangan))

takeRandom_celup = random.choice(glob_celup)
takeRandom_ciamis = random.choice(glob_ciamis)
takeRandom_kawung = random.choice(glob_kawung)
takeRandom_priangan = random.choice(glob_priangan)

img_celup = cv2.imread(takeRandom_celup)
img_ciamis = cv2.imread(takeRandom_ciamis)
img_kawung = cv2.imread(takeRandom_kawung)
img_priangan = cv2.imread(takeRandom_priangan)

# image in list=======================================
list_image = []

list_image.append(img_celup)
list_image.append(img_ciamis)
list_image.append(img_kawung)
list_image.append(img_priangan)

#SIFT=================================================
sift = cv2.xfeatures2d.SIFT_create()

imgGray2 = cv2.cvtColor(sk_img, cv2.COLOR_BGR2GRAY)
keypoints2, _2 = sift.detectAndCompute(sk_img, None)

#accu in list
accu = []

for i in range(len(list_image)):

  # gray scale
  imgSGray = cv2.cvtColor(list_image[i], cv2.COLOR_BGR2GRAY)

  keypoints1, des1= sift.detectAndCompute(list_image[i], None)

  # initialize Brute force matching
  bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
  matches = bf.match(desQ,des1)

  #sort the matches 
  matches = sorted(matches, key= lambda match : match.distance)
  matched_imge = cv2.drawMatches(sk_img, keypoints2, list_image[i], keypoints1, matches[:30], None)

  #percentage
  pointQ = len(matches)
  pointi = len(keypoints1)
  percentage = (len(matches) / len(keypoints1)) * 100
  percen = '{:.2f}'.format(percentage)
  accu.append(percen)

# Setting Values to Rows, Column Variables, and Size
rows = 2
columns = 4
fig = plt.figure(figsize=(18, 14))

# Adds a Subplot at the 1st Position
fig.add_subplot(rows, columns, 2)

# Showing Image
plt.imshow(sk_img)
plt.axis('on')
plt.title("Query Image \n" + que)

# Adds a Subplot at the 1st Position
fig.add_subplot(rows, columns, 5)

# Showing Image
plt.imshow(img_celup)
plt.axis('on')
plt.title(accu[0] + takeRandom_celup)

# Adds a Subplot at the 1st Position
fig.add_subplot(rows, columns, 6)

# Showing Image
plt.imshow(img_ciamis)
plt.axis('on')
plt.title(accu[1] + takeRandom_ciamis)

# Adds a Subplot at the 1st Position
fig.add_subplot(rows, columns, 7)

# Showing Image
plt.imshow(img_kawung)
plt.axis('on')
plt.title(accu[2] + takeRandom_kawung)

# Adds a Subplot at the 1st Position
fig.add_subplot(rows, columns, 8)

# Showing Image
plt.imshow(img_priangan)
plt.axis('on')
plt.title(accu[3] + takeRandom_priangan)