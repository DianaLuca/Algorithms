"""
Given a list of directory info including directory path, and all the files with contents in this directory, 
you need to find out all the groups of duplicate files in the file system in terms of their paths.
A group of duplicate files consists of at least two files that have exactly the same content.
A single directory info string in the input list has the following format:
"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content, respectively) 
in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.
The output is a list of group of duplicate file paths. 
For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:
"directory_path/file_name.txt"
Example 1:
Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output:  
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

time complexity: O(N * k)
space complexity: O(N * k)
"""


from collections import defaultdict


class Solution(object):
    def findDuplicate(self, paths):
        """
        INPUT
        :type paths: List[str]
        ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]

        OUTPUT
        :rtype: List[List[str]]
        [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
        """
        # directory name, file name and file content
        d = defaultdict(list)
        for p in paths:
            psplit = p.split(' ')
            for j, file in enumerate(psplit):
                if j == 0:
                    path = file
                else:
                    file_name = file.split('(')[0]
                    content = file.split('(')[1][:-1]
                    d[content] = d[content] + [path + '/' + file_name]
        duplicates = []
        #print(d)
        for key, value in d.items():
            if len(value) > 1:
                duplicates.append(value)
        return duplicates


def main():
    s = Solution()
    inp = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    print(s.findDuplicate(inp))


if __name__ == '__main__':
    main()