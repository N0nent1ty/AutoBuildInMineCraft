#!python3
#main.py
'''
SettingUp:
	(1)please read readme.md.


Description:
	Something shoud be imporve:
		(1)I will add GUI  to let it more easy to use.
		(2)Maybe I can add somehow machine learning procceing to let it build real 3D constucture by give it a 2D picture.
		(3)Use GUI to let user can change option of picture esily.
		(4)Use Classes to let the code maintainable.
'''





'''
#不同於平方差計算 O(N)，KDTree 是 O(logN)

#Differnd from computational complexity of using root_squerd,
KD_tree is O(logN) rather than O(N).
'''
from sklearn.neighbors import KDTree
from PIL import Image,ImageDraw
import os
import mcpi.block as block
from mcpi.minecraft import Minecraft



'''
Datastructure :
	name:
		array2_RGBDataofBlock
	Format:
		{[int,int,int]}
	Description:
		(1)RGB data of evey color block.
		(2)Use indeces as forign key, so that canget id, 
'''
array2_RGBDataOfBlock = (
[209,95,220], 		#品紅羊毛	1
[203,116,225],  	#品紅玻璃	2
[187,129,156],		#品紅粘土	3
[184,75,85],		#紅羊毛		4
[184,88,97],		#紅玻璃		5
[180,95,93],		#紅粘土		6
[217,159,185],		#粉紅羊毛	7
[231,169,199],		#粉紅玻璃	8
[195,117,120],		#粉紅粘土	9
[167,84,216],		#紫羊毛		10
[164,103,204],		#紫玻璃		11
[156,108,133],		#紫粘土		12
[62,84,188],		#藍羊毛		13
[81,116,204],		#藍玻璃		14
[110,98,139],		#藍粘土		15
[127,169,222],		#淡藍羊毛	16
[139,186,222],		#淡藍玻璃	17
[154,151,180],		#淡藍粘土	18
[63,153,184],		#青羊毛		19
[111,166,188],		#青玻璃		20
[127,133,140],		#青粘土		21
[77,107,72],		#綠羊毛		22
[140,166,96],		#綠玻璃		23
[113,124,69],		#綠粘土		24
[100,218,97],		#黃綠羊毛	25
[163,215,74],		#黃綠玻璃	26
[143,160,97],		#黃綠粘土	27
[203,196,73],		#黃羊毛		28
[225,226,96],		#黃玻璃		29
[209,175,84],		#黃粘土		30
[227,170,108],		#橙羊毛		31
[219,166,96],		#橙玻璃		32
[191,127,81],		#橙粘土		33
[128,89,76],		#棕羊毛		34
[140,116,96],		#棕玻璃		35
[114,85,82],		#棕粘土		36
[47,54,71],			#黑羊毛		37
[50,60,74],			#黑玻璃		38
[63,55,68],			#黑粘土		39
[103,107,116],		#灰羊毛		40
[112,117,122],		#灰玻璃		41
[90,77,82],			#灰粘土		42
[189,197,199],		#淡灰羊毛	43
[184,186,188],		#淡灰玻璃	44
[174,153,148],		#淡灰粘土	45
[225,226,229],		#白羊毛		46
[234,235,236],		#白玻璃		47
[220,206,200]		#白粘土		48
)

'''
Datastructure :
	name
{[rgb_data]}
'''

array1tuple_IDColorDataOfBlock = [
(35,2), 				#品紅羊毛	1
(95,2),  				#品紅玻璃	2
(251,2),				#品紅粘土	3
(35,14),				#紅羊毛		4
(95,14),				#紅玻璃		5
(251,14),				#紅粘土		6
(35,6),					#粉紅羊毛	7
(95,6),					#粉紅玻璃	8
(251,6),				#粉紅粘土	9
(35,10),				#紫羊毛		10
(95,10),				#紫玻璃		11
(251,10),				#紫粘土		12
(35,11),				#藍羊毛		13
(95,11),				#藍玻璃		14
(251,11),				#藍粘土		15
(35,3),					#淡藍羊毛	16
(95,3),					#淡藍玻璃	17
(251,3),				#淡藍粘土	18
(35,9),					#青羊毛		19
(95,9),					#青玻璃		20
(251,9),				#青粘土		21
(35,13),				#綠羊毛		22
(95,13),				#綠玻璃		23
(251,13),				#綠粘土		24
(35,5),					#黃綠羊毛	25
(95,5),					#黃綠玻璃	26
(251,5),				#黃綠粘土	27
(35,4),					#黃羊毛		28
(95,4),					#黃玻璃		29
(251,4),				#黃粘土		30
(35,1),					#橙羊毛		31
(95,1),					#橙玻璃		32
(251,1),				#橙粘土		33
(35,12),				#棕羊毛		34
(95,12),				#棕玻璃		35
(251,12),				#棕粘土		36
(35,15),				#黑羊毛		37
(95,15),				#黑玻璃		38
(251,15),				#黑粘土		39
(35,7),					#灰羊毛		40
(95,7),					#灰玻璃		41
(251,7),				#灰粘土		42
(35,8),					#淡灰羊毛	43
(95,8),					#淡灰玻璃	44
(251,8),				#淡灰粘土	45
(35,0),					#白羊毛		46
(95,0),					#白玻璃		47
(251,0)					#白粘土		48
]


#建構kd_tree


#函數:計算最相近該圖元顏色的方塊id值
def getMostSim(InputRGBArray):
	indexOfNearestColor=tree.query(InputRGBArray, k=1)#k參數是指最接近的前幾個
	scalarIndex=int(indexOfNearestColor[1][0])
	return array1tuple_IDColorDataOfBlock[scalarIndex]
	
	
	
	
	
#main function	
if __name__== "__main__" :
	#Create kd_tree 
	tree = KDTree(array2_RGBDataOfBlock,leaf_size=2)
	#Hard code like this should be modify.
	im = Image.open("C:/Users/sheng/Desktop/tt.jpg")
	pix = im.load()
	#shrink the image.
	im.thumbnail((150,150))#目標圖元
	mc = Minecraft.create()
	pos = mc.player.getTilePos()
	
	
	print(im.size[0])
	print(im.size[1])
	height=im.size[0]
	for x in range(im.size[0]):
		for y in range(im.size[1]):
			id,color = getMostSim([im.getpixel((x,y))])
			print(id,color)
			mc.setBlock(pos.x+x,pos.y+(height-y),pos.z,id,color)

	input("pause")

