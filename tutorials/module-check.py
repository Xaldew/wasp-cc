import sys
import imp

print(sys.executable, sys.version_info)
for package in sys.argv[1:]:
    try:
        print(imp.find_module(package))
    except ImportError:
        print("'%s' not found." % package)
