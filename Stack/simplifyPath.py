"""

Given an absolute path for a Unix-style file system, which begins with a slash '/', transform this path
into its simplified canonical path.

In Unix-style file system context, a single period '.' signifies the current directory, a double period
".." denotes moving up one directory level, and multiple slashes such as "//" are interpreted as a single
slash. In this problem, treat sequences of periods not covered by the previous rules (like "...") as
valid names for files or directories.

The simplified canonical path should adhere to the following rules:

It must start with a single slash '/'.
Directories within the path should be separated by only one slash '/'.
It should not end with a slash '/', unless it's the root directory.
It should exclude any single or double periods used to denote current or parent directories.
Return the new path.

"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = path.split('/')
        stack = []

        for item in path_list:
            if item == '.' or item == '':
                continue
            if item == '..':
                if stack:
                    stack.pop()
                continue
            stack.append(item)

        return '/' + '/'.join(stack)


if __name__ == "__main__":
    solution = Solution()
    # assert solution.simplifyPath('/home/user/Documents/../Pictures') == '/home/user/Pictures'
    # assert solution.simplifyPath('/home/') == '/home'
    # assert solution.simplifyPath('/home//foo/') == '/home/foo'
    assert solution.simplifyPath('/../') == '/'
    assert solution.simplifyPath('/.../a/../b/c/../d/./') == '/.../b/d'