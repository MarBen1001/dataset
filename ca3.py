





class Commit:
    def __init__(self):
    
#######  CA 3  #########










changes_file = 'mini.txt'
data =[line.strip() for line in open(changes_file)]
#print data
print len(data)
index = 0                           #NameError: name 'index' is not defined if this omitted
print index
new_fact = 72*'-'                   #each new_fact a commit description
count = 0
num_commits =0
while True:
    try:                                #IndexError: list index out of range if don't go for try/except guard as per example
                                        # check is this also handy anyway or not a good thing to do?
        
        num_commits = num_commits+1
        print '_____________________________________________________'
        details = data[index+1].split('|')  
        commit_ref = details[0]
        commit_author = details[1]
        commit_date = details[2].strip().split(' ')[0]
        commit_time = details[2].strip().split(' ')[1]
        commit_weekday = details[2].strip().split(' ')[3].strip().strip('(').strip(',').strip(')')
        commit_month =  details[2].strip().split(' ')[5].strip()#.strip('(').strip(',').strip(')')

        #print details
        print 'AUTHOR:',commit_author
        print 'REFERENCE:', commit_ref
        print 'COMMIT DATE:', commit_date
        print 'COMMIT TIME:', commit_time
        print 'This Commit happened on a',commit_weekday
        print 'This Commit happened in', commit_month
        
        changes = data[index+2:data.index('',index+1)]# still to figure this ' index+1' out but changing the +n makes a difference
        #print changes 
        m_items =0
        d_items =0
        a_items =0
        for item in changes:
            if item.startswith('M'):
                m_items = m_items+1
                print item                  # printing M
            elif item.startswith('D'):
                d_items = d_items+1
                print item                  # printing D
            elif item.startswith('A'):
                a_items = a_items+1
                print item                  # printing A
        print 'Number of Modifications',commit_ref, ' =' ,m_items,  '\nNumber of Deletions    ' ,commit_ref,' =', d_items, '\nNumber of Additions    ',commit_ref,' =', a_items
        index = data.index(new_fact, index+1)#without index+1 index does not move to next block => essential to include

    except IndexError:
        break   
        
for i in range (index):
     count = count +1

print 'total number of commits:',num_commits  
print 'total number of lines:',count
print'_______________________________________________________'

       
        #for i in changes:
        #   count =count+1
        #print 'count ='  ,  count





        
