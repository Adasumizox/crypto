from hashing.src.Hash import HashHelper
from hashing.src.Transfer import Transfer

if __name__ == '__main__':
    HashHelper.hashing_time_for_all_algorithms(text='password', loops=10000)
    name = Transfer.download_file("https://releases.ubuntu.com/20.04.2.0/ubuntu-20.04.2.0-desktop-amd64.iso")
    HashHelper.compare_file_with_checksum("./{}".format(name), "93bdab204067321ff131f560879db46bee3b994bf24836bb78538640f689e58f", "sha256")
    HashHelper.display_plot(
        HashHelper.generate_hash_size_times(length=1000000, algorithm="sha1", step=100000, loops=1000))
