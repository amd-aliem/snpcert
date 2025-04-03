# Welcome to SEV-SNP OS Certification

This contains images constructed using `mkosi`. The specific images all
inherit from the `common` image data. This means that we can put things
like `snpguest` tests and other workloads in `common` to be shared by
all of the OS images.

Individual guest tests should be written as systemd services.

# How to Run

1. Download the build artifacts for your relevant guest distro.

2. Unzip the artifacts.

3. Run them:

```sh
$ qemu-kvm -m 2G \
    -bios /usr/share/edk2/ovmf/OVMF_CODE.fd \
    -kernel guest-fedora-41/image.efi \
    -hda guest-fedora-41/image.qcow2
```
