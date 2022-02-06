"""
https://www.hackerrank.com/challenges/attribute-parser/problem

Problem Statement :

This challenge works with a custom-designed markup language HRML. In HRML, each element consists of a starting and ending tag, and there are attributes associated with each tag. Only starting tags can have attributes. We can call an attribute by referencing the tag, followed by a tilde, '~' and the name of the attribute. The tags may also be nested.

The opening tags follow the format:

<tag-name attribute1-name = "value1" attribute2-name = "value2" ...>

The closing tags follow the format:

</tag-name>

The attributes are referenced as:

tag1~value
tag1.tag2~name

Given the source code in HRML format consisting of N lines, answer Q queries. For each query, print the value of the attribute specified. Print "Not Found!" if the attribute does not exist.

Example

HRML listing
<tag1 value = "value">
<tag2 name = "name">
<tag3 another="another" final="final">
</tag3>
</tag2>
</tag1>

Queries
tag1~value
tag1.tag2.tag3~name
tag1.tag2~value

Here, tag2 is nested within tag1, so attributes of tag2 are accessed as tag1.tag2~<attribute>. Results of the queries are:

Query                 Value
tag1~value            "value"
tag1.tag2.tag3~name   "Not Found!"
tag1.tag2.tag3~final  "final"

Input Format

The first line consists of two space separated integers, N and Q.  N specifies the number of lines in the HRML source program.
Q specifies the number of queries.

The following N lines consist of either an opening tag with zero or more attributes or a closing tag. There is a space after the tag-name, attribute-name, '=' and value.There is no space after the last value. If there are no attributes there is no space after tag name.

Constraints
 1 <= N <= 20
 1 <= Q <= 20
 Each line in the source program contains, at most, 200 characters.
Every reference to the attributes in the Q queries contains at most 200 characters.
All tag names are unique and the HRML source program is logically correct, i.e. valid nesting.
A tag can may have no attributes.

Output Format

Print the value of the attribute for each query. Print "Not Found!" without quotes if the attribute does not exist.




"""


import re

def retrace(tag_path, root):
    tag_copy = tag_path[::]
    while True:
        temp = tag_copy.pop()
        if not tag_copy:
            return root[temp] == temp
        if root[temp] != tag_copy[-1]:
            return False
    return True

def main():
    arr = []
    n, q = [int(x) for x in input().split()]
    for _ in range(n):
        arr.append(input())
    mystack = []
    tags = {}
    root = {}
    for item in arr:

        tag_name, *atrs = re.findall(r'(?<=[ "<\/])([^"\s=\/]+?)(?=[ ">])', item)

        if mystack and tag_name in mystack[-1]:
            mystack.pop()
            continue
        tag_attrib = {attr_name : attr_val for attr_name, attr_val in zip(atrs[::2], atrs[1::2])}

        tags[tag_name] = tag_attrib
        if not mystack:
            root[tag_name] = tag_name
        else:
            root[tag_name] = mystack[-1]
        mystack.append(tag_name)
    res = []
    for _ in range(q):
        s = input()

        tag_path, *tag_attr = s.split('~')
        if tag_attr:
            tag_attr = tag_attr[0]
        tag_path = tag_path.split('.')
        if tag_path[-1] in tags.keys() and tag_attr in tags[tag_path[-1]] and retrace(tag_path, root):
            res.append(tags[tag_path[-1]][tag_attr])
        else:
            res.append('Not Found!')

    for item in res:
        print(item)

main()