docker run --name tmpfs_container \
--mount type=tmpfs,destination=/my_folder1 \
-v /tmp:/my_folder2 -itd nginx:1.23
