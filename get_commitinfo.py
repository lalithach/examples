import glob,re

files = []
components = ['u-boot-xlnx', 'linux-xlnx', 'arm-trusted-firmware']
for file in glob.glob('./allure-results/*.txt'):
    with open(file) as f:
        contents = f.read()
    for comp in components:
        if comp in contents:
            files.append(file)
final_set = set(files)

start_pattern = "*"*27
end_pattern = "*"*27

def is_marker_line(line, start="*"*54, end=""):
    return line.startswith(start) and line.endswith(end)

def advance_past_next_marker(lines):
    '''
    Advances the given iterator through the first encountered marker
    line, if any.
    '''
    for line in lines:
        if is_marker_line(line):
            break

def lines_before_next_marker(lines):
    '''
    Yields all lines up to but not including the next marker line.  If
    no marker line is found, yields no lines.
    '''
    valid_lines = []
    for line in lines:
        if is_marker_line(line):
            break
        valid_lines.append(line)
    else:
        # `for` loop did not break, meaning there was no marker line.
        valid_lines = []
    for content_line in valid_lines:
        if not re.match(r'^\s*$', line):
            yield content_line
        
def lines_between_markers(lines):
    '''
    Yields the lines between the first two marker lines.
    '''
    # Must use the iterator --- if it's merely an iterable (like a list
    # of strings), the call to lines_before_next_marker will restart
    # from the beginning.
    it = iter(lines)
    advance_past_next_marker(it)
    for line in lines_before_next_marker(it):
        if not re.match(r'^\s*$', line):
            yield line
        
lines = []
with open("new.txt",'w') as fd:
    for file in files:
        with open(file) as f:
            for line in lines_between_markers(f):
                fd.write(line)

with open("new.txt") as f:
    for line in f:
        if "REPO URL" in line:
            i = line.rfind("/")
            j = line.rfind(".")
            print(line[i+1:j]+ " :", end=" ")
        if "BRANCH" in line:
            i = line.rfind("* ")
            print(line[i+2:-1] + " :", end=" ")
        if "ORIGIN_COMMIT" in line:
            i = line.find(":")
            j = line.find("-")
            print(line[i+2:j])
        if "COMMIT DIFF" in line:
            secondline = next(f)
            commit_index = secondline.find("-")
            print("patched commit:"+secondline[:commit_index].strip())
        
        

            
