import pkg_resources
import subprocess

def install():
    #TODO: add --version when we support more than 1.3
    push_script = pkg_resources.resource_filename(__name__, "push_bundles.sh")
    pkg_path = pkg_resources.resource_filename(__name__, "bundles")
    proc = subprocess.Popen(["%s 1.3 %s" % (push_script, pkg_path)],
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
    install()
