# Welcome to SEV-SNP OS Certification

The purpose of this repository is to build a view of operating systems and the AMD-SEV features that they support. Self-service tools are provided to run a series of certification tests using an AMD EPYC server, allowing for any user/organization to test an OS for AMD-SEV support. Note that [mkosi](https://github.com/systemd/mkosi) support for the operating system is required.

## Certification Matrix

This table contains operating systems that have undergone certification testing for AMD features through this repository. 

-- table to be inserted or linked to here --

## Self-Service Certification Tools

Users/Organizations may target their own SEV-enabled EPYC server for self-service certification runs. Follow our guide on running an automated certification test here: https://github.com/amd-aliem/sev-certify/blob/update-readme/docs/how-to-generate-certs.md

## Project Organization

### Certification Run Results

Each certification run will open a Github Issue in this repository.

-- issue tag information to be added here --

### Images

Host and Guest images are constructed in Github Workflows via `mkosi`. Host images are designed to be booted on a SEV-enabled EPYC server, and are configured with a series of custom systemd services that will run tests on an embedded guest image. The resulting host and guest images are available in Github releases in this repository.

