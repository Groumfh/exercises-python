#!/usr/bin/env python

import ex2_version as version

if __name__ == '__main__':
    print("Hello my number version is {major}.{minor}.{patch}-{hash}".format(
        major= version.major,
        minor=version.minor,
        patch=version.patch,
        hash=version.hash))