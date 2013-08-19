import sys

def url_scrub(arg):
        if '://' in arg:
                arg = arg.split('//')[1]
                if '/' in arg:
                        arg = arg.split('/')[0]
        return arg

print
print '<eccu>'
for i in sys.argv[1:]:
        print     '''<match:request-header operation="name-value-cmp" argument1="Host" argument2="%s">
    <revalidate>now</revalidate>
</match:request-header>''' % (url_scrub(i))
print '</eccu>'
print
