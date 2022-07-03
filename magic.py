from PIL import Image

# import OS module
import os

# Delete Old Images
path = "/home/silvey/Documents/GitHub/YOLACT/test_images/"
os.system("rm -rf "+path.replace("test","output")+"/*")
 
# Get the list of all files and directories

os.system("cd "+path)
dir_list = os.listdir(path)

for file in dir_list:
    try:
        if("padded" in file):
            print("Already Padded")
        else:
            print("Analyzing "+str(file))
            image = Image.open(path+"/"+file)
            padding_data = 50
            right = padding_data
            left = padding_data
            top = padding_data
            bottom = padding_data
            width, height = image.size
            new_width = width + right + left
            new_height = height + top + bottom
            image = image.convert('RGB')
            # print(image.mode)
            result = Image.new(image.mode, (new_width, new_height), (255, 255, 255))
            result.paste(image, (left, top))
            os.system("rm -rf \""+path+"/"+file+"\"")
            result.save(path+"/"+file.replace("(","").replace(")","").replace(".","_padded."))
    except Exception as e: print(e)
        # print("Error Opening file "+str(file)+". Skipping.")

os.system("python ./eval.py --trained_model=/home/silvey/Documents/GitHub/YOLACT/weights/leaves_detection_8333_800000.pth --config=yolact_darknet53_leaves_custom_config --score_threshold=0.15 --top_k=15 --images=test_images:output_images")
os.system("xdg-open "+path.replace("test","output"))
