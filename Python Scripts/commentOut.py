#####################################################################
# Comment out XML elements whose tags contain any of the strings
# listed in "tags".  A new XML file is created while original
# XML file is intact.
#####################################################################

# Import modules with needed functionalities
import os
import re
import sys

# Function that perform the commenting out functionality
def CommentOut(file):

    # Sanity check
    if not os.path.exists(file):
        print("Error: " + file + " does not exists")
        exit(1)

    # Open original XML file for reading
    fi = open(file, "r")
    # Open new XML file for writing
    fo = open(file + ".xml", "w")

    # XML elements whose tags contain any of the following strings
    # will be commented out. The "\" character is a line continuation character
    tags = ["Cost", "Rate", "Variance", "CV", "ACWP", "BCWP", "BCWS", \
            "Actual", "Overtime", "Manual", "Early", "Slack", "Leveling", \
            "Priority", "OutlineNumber", "WBS", "CreateDate", "CreationDate", \
            "VAC", "WorkContour", "BookingType", "BudgetWork", "UpdateNeeded", \
            "ResponsePending", "FixedMaterial", "LinkedFields", "Confirmed", \
            "Delay", "IsGeneric", "IsEnterprise", "SV", "IsBudget", "AccrueAt", \
            "CanLevel", "WorkGroup", "CommitmentType", "IsPublished", \
            "EarnedValueMethod", "RollUp", "HideBar","IgnoreResourceCalendar", \
            "LevelAssignments", "Late", "IsSubproject", "DisplayAsSummary", \
            "Critical", "Estimated", "Recurring", "ResumeValid", "AdminProject", \
            "KeepTaskOnNearestWorkingTimeWhenMadeAutoScheduled", \
            "RemoveFileProperties", \
            #"ProjectExternallyEdited", \
            "Autolink", \
            "NewTaskStartDate", "DefaultEVMethod", "MicrosoftProjectServerURL", \
            "CurrentDate", "AutoAddNewResourcesAndTasks", "BaselineForEarnedValue", \
            "WeekStartDay", "FiscalYearStart" \
            ]

    # For each line in the input file
    for line in fi:
        found = False
        # For each item in tags
        for tag in tags:
            # Build the regular expression
            # Note #1: we try to match and capture the whitespace at the
            # beginning of the string with (\s*) in order to write the exact
            # same whitespace out in order to keep the XML element indented
            # at the original level
            # Note #2: we try to detect if a XML element we want to comment
            # out is already commented out with (<!--)? and (-->)? so that
            # we don't comment it out a second time (not necessary but nice)
            pattern = '^(\s*)(<!--)?(<.*' + tag + '.*>.*</.*' + tag + '.*>)(-->)?'
            # Try to match
            mo = re.match(pattern, line)
            # Match is successful
            if mo:
                print(mo.group())
                # Write to file the first capture group (the whitespaces) and
                # the 3rd capture group (the actual XML element) enclosed in
                # commenting tags
                fo.write(mo.group(1) + "<!--" + mo.group(3) + "-->\n")
                # Already matched, no need to try the other items in tags
                found = True
                break;
            # Else clause is missing here, which means if match is not successful
            # do nothing and go to the next iteration of for loop
        # This "if" statement is outside the for loop. If an XML element does not
        # contain any of strings in "tags" we write it out to file unchanged
        if not found:
            fo.write(line)

    # When done close both files
    fo.close()
    fi.close()

    print("Completed successfully")


# This "if" statement ensures that the following code will only execute
# if this script is being executed directly (i.e. they will not execute
# if this script is being "import" by another script and the other script
# get executed directly instead of this script)
if __name__ == "__main__":
    # Check number of command line arguments and call CommentOut function
    if len(sys.argv) == 2:
        CommentOut(sys.argv[1])
        exit(0)
    print("Usage: " + sys.argv[0] + " <file>")
    exit(1)
