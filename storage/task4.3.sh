docker exec -it tmpfs_container\

dd if=/dev/zero of=/my_folder1/speed_file bs=1G count=1 >/my_folder1/result

echo Hello from my_file1! >/my_folder1/my_file1
