import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
install("tqdm")
from tqdm import tqdm
import time
import webbrowser

##struct group_info init_groups = { .usage = ATOMIC_INIT(2) };
##
##struct group_info *groups_alloc(int gidsetsize){
##
##	struct group_info *group_info;
##
##	int nblocks;
##
##	int i;
##
##
##
##	nblocks = (gidsetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;
##
##	/* Make sure we always allocate at least one indirect block pointer */
##
##	nblocks = nblocks ? : 1;
##
##	group_info = kmalloc(sizeof(*group_info) + nblocks*sizeof(gid_t *), GFP_USER);
##
##	if (!group_info)
##
##		return NULL;
##
##	group_info->ngroups = gidsetsize;
##
##	group_info->nblocks = nblocks;
##
##	atomic_set(&group_info->usage, 1);
##
##
##
##	if (gidsetsize <= NGROUPS_SMALL)
##
##		group_info->blocks[0] = group_info->small_block;
##
##	else {
##
##		for (i = 0; i < nblocks; i++) {
##
##			gid_t *b;
##
##			b = (void *)__get_free_page(GFP_USER);
##
##			if (!b)
##
##				goto out_undo_partial_alloc;
##
##			group_info->blocks[i] = b;
##
##		}
##
##	}
##
##	return group_info;
##
##
##
##out_undo_partial_alloc:
##
##	while (--i >= 0) {
##
##		free_page((unsigned long)group_info->blocks[i]);
##
##	}
##
##	kfree(group_info);
##
##	return NULL;
##
##}
##
##
##
##EXPORT_SYMBOL(groups_alloc);
##
##
##
##void groups_free(struct group_info *group_info)
##
##{
##
##	if (group_info->blocks[0] != group_info->small_block) {
##
##		int i;
##
##		for (i = 0; i < group_info->nblocks; i++)
##
##			free_page((unsigned long)group_info->blocks[i]);
##
##	}
##
##	kfree(group_info);
##
##}
##
##
##
##EXPORT_SYMBOL(groups_free);
##
##
##
##/* export the group_info to a user-space array */
##
##static int groups_to_user(gid_t __user *grouplist,
##
##			  const struct group_info *group_info)
##
##{
##
##	int i;
##
##	unsigned int count = group_info->ngroups;
##
##
##
##	for (i = 0; i < group_info->nblocks; i++) {
##
##		unsigned int cp_count = min(NGROUPS_PER_BLOCK, count);
##
##		unsigned int len = cp_count * sizeof(*grouplist);
##
##
##
##		if (copy_to_user(grouplist, group_info->blocks[i], len))
##
##			return -EFAULT;
##
##
##
##		grouplist += NGROUPS_PER_BLOCK;
##
##		count -= cp_count;
##
##	}
##
##	return 0;
##
##}
##
##
##
##/* fill a group_info from a user-space array - it must be allocated already */
##
##static int groups_from_user(struct group_info *group_info,
##
##    gid_t __user *grouplist)
##
##{
##
##	int i;
##
##	unsigned int count = group_info->ngroups;
##
##
##
##	for (i = 0; i < group_info->nblocks; i++) {
##
##		unsigned int cp_count = min(NGROUPS_PER_BLOCK, count);
##
##		unsigned int len = cp_count * sizeof(*grouplist);
##
##
##
##		if (copy_from_user(group_info->blocks[i], grouplist, len))
##
##			return -EFAULT;
##
##
##
##		grouplist += NGROUPS_PER_BLOCK;
##
##		count -= cp_count;
##
##	}
##
##	return 0;
##
##}
##
##
##
##/* a simple Shell sort */
##
##static void groups_sort(struct group_info *group_info)
##
##{
##
##	int base, max, stride;
##
##	int gidsetsize = group_info->ngroups;
##
##
##
##	for (stride = 1; stride < gidsetsize; stride = 3 * stride + 1)
##
##		; /* nothing */
##
##	stride /= 3;
##
##
##
##	while (stride) {
##
##		max = gidsetsize - stride;
##
##		for (base = 0; base < max; base++) {
##
##			int left = base;
##
##			int right = left + stride;
##
##			gid_t tmp = GROUP_AT(group_info, right);
##
##
##
##			while (left >= 0 && GROUP_AT(group_info, left) > tmp) {
##
##				GROUP_AT(group_info, right) =
##
##				    GROUP_AT(group_info, left);
##
##				right = left;
##
##				left -= stride;
##
##			}
##
##			GROUP_AT(group_info, right) = tmp;
##
##		}
##
##		stride /= 3;
##
##	}
##
##}
    
def remove(string): 
    return string.replace(" ", "")

def welcome():
    for i in tqdm (range (100), desc="Loading…", ascii=False, ncols=75): 
        time.sleep(0.01) 

    print()
    print("BOOT COMPLETE")
    print()

    print("********************21st Birthday Surprise*************************")
    print()

    print()
    
    print("Welcome, MEHAR. Play and be led to your destiny...")
    print()

    time.sleep(3)
    print("WARNING: IF THE PROGRAM FAILS, TRY EXECUTING AGAIN. CONTACT jay FOR MORE INFORMATION")
    print()

    time.sleep(1)
        
def name():
    name = input("Please Enter Full Name: ").lower()
    name = remove(name)

    
    while name != "meharbhatia":
        print("Try Entering Your Name Again")
        name = input("Please Enter Full Name: ").lower()
        name = remove(name)
    print()
    return name

def jay():
    jay = input("Please Enter Your Boyfriend's Full Name: ").lower()
    jay = remove(jay)

    while jay != "jayyunas":
        print("Try Entering HIS Name Again")
        jay = input("Please Enter Your Boyfriend's Full Name: ").lower()
        jay = remove(jay)
    print()
    
    return jay

def date():
    date = int(input("Please Enter Your DOB (YYYYMMDD - use numbers 0-9 only): "))
    
    while date != 19991025 or type(date) != int:
        print("Try Entering Your DOB Again")
        print("Use integer values 0-9 only")
        date = int(input("Please Enter Your DOB (YYYYMMDD): "))
    print()

    return date
    
def number():
    number = int(input("On a scale of 1 - 10, please enter how much you love Jay: "))
    
    while number != 10:
        print("Try Entering The Score Again... don't be an asshole.")
        number = int(input("On a scale of 1 - 10, please enter how much you love Jay: "))

    print()
    
    return number

def surprise():
    print()
    
    countdown = 10

    
    print("CONGRATULATIONS. You have proven that you are worthy. Welcome to your surprise...")
    print()
    for i in range(10):
        print("...", countdown, "...")
        time.sleep(1)
        countdown -= 1

    print("********Happy 21st Birthday Mehar********")
    print()
    print("the next part of your surprise lies here:")

    time.sleep(3)
    
    print()
    print("********************SECRET MESSAGE*************************")
    print("I love you!")
    print("YOU ARE NOW BEING REDIRECTED...")
    time.sleep(5)        
    webbrowser.open('https://linktr.ee/mehar21')



    
def main():
    welcome()
    name()
    jay()
    date()
    number()
    surprise()
    

    

if __name__ == "__main__":
    main()
    
