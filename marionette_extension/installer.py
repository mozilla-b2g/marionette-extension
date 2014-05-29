import pkg_resources
import subprocess
from optparse import OptionParser

SUPPORTED_VERSIONS=['1.3', '1.4']

def cli():
    parser = OptionParser(usage="usage: %prog [options] version",
                                 description="Installs Marionette as an extension " \
                                "on the device, given the device's build version. " \
                                "Accepted versions are: 1.3 or 1.4")
    parser.add_option("--adb-path", dest="adb_path", default="adb",
                        help="path to adb executable. If not passed, we assume"\
                        " that 'adb' is on the path")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        raise Exception("please enter a version number, one of: %s" % SUPPORTED_VERSIONS)
    version = args[0]
    install(version, options.adb_path)

def install(version, adb="adb"):
    if version not in SUPPORTED_VERSIONS:
        raise Exception("%s not in supported versions: %s" % (version, SUPPORTED_VERSIONS))
    push_script = pkg_resources.resource_filename(__name__, "push_bundles.sh")
    pkg_path = pkg_resources.resource_filename(__name__, "bundles")
    proc = subprocess.Popen(["bash %s %s %s %s" % (push_script, version, adb, pkg_path)],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            shell=True)
    last_line = None
    while proc.poll() is None:
        output = proc.stdout.readline()
        if output:
            last_line = output
        print output
    ret = proc.wait()
    if ret:
        out = proc.stdout.read() or last_line
        raise Exception("Failed to install extension: %s" % out)

if __name__ == "__main__":
    cli()
