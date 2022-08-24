from PIL import Image
import urllib.request, json, os.path
from urllib.request import Request, urlopen
import json

smol_size = 350
LAST_MALE = 6710
LAST_FEMALE = 13421
nft = ['smol', 'pet', 'swol' 'legion', 'gl']

phone_dic = {'i12':(1170, 2532),'i12mini':[1125,2436],'i12pro':[1170, 2532],'i12max':[1284,2778], 'i13':[1170,2532], 'i13mini':[1080,2340], 'i13pro':[1170,2532],'i13max':[1284,2778], 'gflip3':[2520, 2520], 'gflip3_cover':[2260, 2260]}

nft_url = {'smol_male': "https://ipfs.io/ipfs/QmY71ban6QoWg9nbNwikk6wVWknj8NFBG8nMGHEuzwfAwf/", 'smol_female': "https://gateway.pinata.cloud/ipfs/QmR87K1oY8dXL4op91A9zcz4hPmCd8JbMVDTTuUnpXyQcr/", 'brain_pet': "https://ipfs.io/ipfs/QmdRyjjv6suTcS9E1aNnKRhvL2McYynrzLbg5VwXH8cCQB/"}

nft_url_local = {'smol_male': "http://bafybeiercznqjdejbvccbp4byylolmlgybsivp433qx77fkqzyt3s67ccy.ipfs.localhost:8080/", 'smol_female': "https://gateway.pinata.cloud/ipfs/QmR87K1oY8dXL4op91A9zcz4hPmCd8JbMVDTTuUnpXyQcr/", 'brain_pet': "https://ipfs.io/ipfs/QmdRyjjv6suTcS9E1aNnKRhvL2McYynrzLbg5VwXH8cCQB/"}

def create_smol_wp(file_name, device, nft_loc, nft_size):
	w = phone_dic[device][0]
	h = phone_dic[device][1]
	img = Image.open(file_name)
	img = img.convert("RGBA")

	datas = img.load()
	print(img.size)
	newData = []

	bg_color = datas[0,0]

	img_bg = Image.new("RGBA", (w,h), bg_color)
	bg_datas = img_bg.load()

	smol_size_tmp = smol_size

	if nft_size == "XL":
		smol_size_tmp = smol_size_tmp*3
		img_resize = img.resize((smol_size_tmp, smol_size_tmp));
	elif nft_size == "L":
		smol_size_tmp = smol_size_tmp*2
		img_resize = img.resize((smol_size_tmp, smol_size_tmp));

	datas = img_resize.load()
	half_size = smol_size_tmp/2

	if nft_loc == "high":
		x = int(w/2 - half_size)
		y = 0
	elif nft_loc == "medium":
		x = int(w/2 - half_size)
		y = int(h/2 - half_size)
	elif nft_loc == "low":
		x = int(w/2 - half_size)
		y = int(h - smol_size_tmp)

	#concat images between wallpaper and a nft
	for i in range(0, smol_size_tmp):
		for j in range(0, smol_size_tmp):
			bg_datas[x+i, y+j] = datas[i,j]

	img_bg.save("./out/wp_" + device + "_" + file_name, "PNG")

def get_nft_url(nft_name, id, head_size):
	if nft_name == "smol":
		if id <= LAST_MALE:
			# url = nft_url["smol_male"] + str(id) + "/" + str(head_size) + ".png"
			url = nft_url_local["smol_male"] + str(id) + "/" + str(head_size) + ".png"
		elif id <= LAST_FEMALE:
			id = id - LAST_MALE - 1 #Female starts 0 index
			url = nft_url["smol_female"] + str(id) + "/" + str(head_size) + ".png"
	elif nft_name == "brain_pet":
		url = nft_url[nft_name] + str(id) + ".gif"
	print(url)
	return url;

def save_nft_image(nft_name, id, head_size):
	url = get_nft_url(nft_name, id, head_size)
	#first check saved image
	if nft_name == "smol":
		file_name = nft_name + "_" + str(id) + "_" + str(head_size) + ".png"
		if os.path.exists(file_name):
			print(file_name + " is already exist")
		else:
			urllib.request.urlretrieve(url, file_name)
			img.save("./images/smol/" + file_name,'png', optimize=True, quality=100)

	elif nft_name == "brain_pet":
		file_name = nft_name + "_" + str(id) + ".png"
		file_gif = nft_name + "_" + str(id) + ".gif"
		if os.path.exists(file_name):
			print(file_name + " is already exist")
		else:
			urllib.request.urlretrieve(url, file_gif)
			img = Image.open(file_gif)
			img.save("./images/brain_pets/" + file_name,'png', optimize=True, quality=100)
	return file_name

def wp(device, nft_name, id, head_size):
	file_name = save_nft_image(nft_name, id, head_size)
	create_smol_wp(file_name, device, "low", "L")

# wp("i12pro","smol",710,5)
wp("i12pro","smol",6710,5)
# wp("i12pro","smol",6711,5)
# wp("i12pro","smol",6752,5)


# wp("gflip3_cover","pet",770,5)
# get_ipfs_url("smol",3553,5)
# wp("i12pro","tool",384,5)
