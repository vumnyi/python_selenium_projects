import sys

def is_issue_line(line):
    issues_type = ('ERROR', 'ISSUE', 'WARN')
    return True in [issue in line for issue in issues_type]

def main():
    try:
        text = open('email.txt', 'r')
    except IOError:
        print('There was some issue during reading file')
        sys.exit(1)

    issues_lines = filter(is_issue_line, text)

    for (issue, some, num, desc) in [line.split() for line in issues_lines]:
        num, issue = int(num[:-1]), issue[1:-1]
        if num == 56 and issue == 'ERROR':
            desc += ' (JIRA-1234)'
        elif issue == 'WARN':
            desc += ' (You can ignore it)'
        elif issue == 'ISSUE':
            desc += ' (Need to retest issue)'
        print ('\n\t%s\tin line %d: \t%s' % (issue, num, desc))


if __name__ == "__main__":
    main()