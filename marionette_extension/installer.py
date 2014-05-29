import pkg_resources
import subprocess
from optparse import OptionParser
from mozdevice import DeviceManagerADB
import socket

SUPPORTED_VERSIONS=['1.3', '1.4']


class MarionetteInstallationException(Exception):
    pass

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
    if not check_marionette_exists():
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
            raise MarionetteInstallationException("Failed to install extension: %s" % out)
    else:
        raise MarionetteInstallationException("Marionette is already installed")


def check_marionette_exists(adb="adb"):
    dm = DeviceManagerADB(adbPath=adb)
    if dm.dirExists("/system/b2g/distribution/bundles/marionette@mozilla.org"):
        return True
    else:
        if dm.forward("tcp:2828", "tcp:2828") != 0:
            # This is not a marionette installation exception, this is more general
            raise Exception("Can't use localhost:2828 for checking if marionette exists." \
                            "Is something else using port 2828?")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', 2828))
            data = sock.recv(16)
            sock.close()
            if 'root' in data:
                return True
        except socket.error:
            return False
    return False


if __name__ == "__main__":
    cli()
