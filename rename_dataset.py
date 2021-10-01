import os

root_dir = "dataset/train"
target_dir = "ants_image"
img_path = os.listdir(os.path.join(root_dir, target_dir))
label = target_dir.split('_')[0]  # 是str.split的用法，即将字符串"ants_image"以_分开，并取其中的"ants"作为label
out_dir = "ants_label"
for i in img_path:
    file_name = i.split('.jpg')[0]  # 这也是str.split的用法，即将"dataset/train/ants_image"里的图片以.jpg的方式隔开，并取其中的前一部分名称
    # 下一行的操作是:将file_name连接上.txt将其变成名为file_name的txt文件;
    # w 表示可写的，使用w来写入文件时，如果文件不存在会创建文件，如果文件存在则会截断文件;截断文件指删除文件中的所有内容
    with open(os.path.join(root_dir, out_dir, "{}.txt".format(file_name)), 'w') as f:
        f.write(label)
