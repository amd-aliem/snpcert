
![Build Status](https://github.com/AMDEPYC/sev-certify/actions/workflows/build-images.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# Welcome to SEV-SNP OS Certification


The purpose of this repository is to build a view of operating systems and the AMD-SEV features that they support. Self-service tools are provided to run a series of certification tests using an AMD EPYC server, allowing for any user/organization to test an OS for AMD-SEV support. Note that [`mkosi`](https://github.com/systemd/mkosi) support for the operating system is required.

## Certification Matrix

This table contains operating systems that have undergone certification testing for AMD features through this repository. 


_Table to be inserted or linked to here._

## Self-Service Certification Tools


Users/Organizations may target their own SEV-enabled EPYC server for self-service certification runs. Follow our guide on running an automated certification test [here](https://github.com/AMDEPYC/sev-certify/blob/update-readme/docs/how-to-generate-certs.md).


## Project Organization

The repository is organized as follows:

- `docs/`: Documentation, guides, and images for using and understanding the project.
- `images/`: Host and guest OS image build configurations for various distributions.
- `modules/`: Modular components, scripts, and systemd service definitions for building and running certification workflows. Key submodules include:
	- `beacon/`: Contains build scripts and extra files for the beacon utility.
	- `build/`: General build configuration for the modular system.
	- `common/`: Shared configuration and systemd extras used by multiple modules.
	- `embed-guest-image/`: Scripts and configs for embedding guest images into host images.
	- `guest/`: Guest OS configuration for certification.
	- `guest-measurement/`: Tools and scripts for measuring guest state and integrity.
	- `guest-notices/`: Systemd extras for guest notification handling.
	- `host/`: Host OS configuration for certification.
	- `launch-snp-guest/`: Scripts and extras for launching SEV-SNP guests.
	- `load-kernel-modules/`: Build scripts for loading required kernel modules.
	- `logging/`: Logging utilities, including:
		- `capture-guest-logs-in-host/`: Capture guest logs from the host.
		- `display-guest-environment/`: Display guest environment details.
		- `display-guest-logs/`: Display guest logs.
		- `sev-certificate-generator/`: Tools for generating SEV certificates.
		- `upload-guest-logs/`: Utilities for uploading guest logs.
	- `reboot/`: Scripts and extras for reboot operations during workflows.
	- `snpguest/`: SEV-SNP guest configuration and extras.
	- `snpguest-build/`: Build scripts for SEV-SNP guest images.
	- `snphost/`: Build scripts and configuration for SEV-SNP host images.

### Certification Run Results

Each certification run will open a GitHub Issue in this repository.

_Issue tags and details to be added here._

### Images


Host and Guest images are constructed in GitHub Workflows via [`mkosi`](https://github.com/systemd/mkosi). Host images are designed to be booted on a SEV-enabled EPYC server, and are configured with a series of custom systemd services that will run tests on an embedded guest image. The resulting host and guest images are available in GitHub releases in this repository.

