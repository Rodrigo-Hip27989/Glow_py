import glob
import subprocess

def stashFilesToGlow(): 
    md_file_list = glob.glob("**/*.md", recursive=True)
    #txt_file_list = glob.glob("**/*.txt", recursive=True)

    stash_file_list = md_file_list
    #stash_file_list = md_file_list+txt_file_list
    print("")

    for file in stash_file_list:
        status = subprocess.run(["glow", "stash", "-m", file, file], capture_output=True, text=True)
        print(f"{file}  ==>  {status.stdout}")


def main():
    stashFilesToGlow()

main()

