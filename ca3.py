
#######           Mary Hennessy        10345121    CA 3      ########




class Commit(object):

    def __init__(self, ref = None, author = None, date = None, time = None, hour = None, weekday = None, month = None, ):
        self.reference = ref
        self.author = author
        self.date = date
        self.time = time
        self.hour = hour
        self.weekday = weekday
        self.month = month
    
   # def count_num_commits():            # count number of commits
       # count = count+1
        #return num_commits+1



if __name__ =='__main__':
    
    commit = Commit()
    
    changes_file = 'mini.txt'
    data =[line.strip() for line in open(changes_file)]
    #print data
    #print len(data)
    index = 0                           #NameError: name 'index' is not defined if this omitted
        #print index
    new_fact = 72*'-'                   #each new_fact a commit description
    count = 0
    num_commits =0

    additions =[]
    modifications =[]
    deletions=[]
    dates=[]
    hours =[]
    hours_d ={}
    weekday =[]
    weekday_d ={}
    comments =[]
    comments_date =[]
    no_comments =[]
    
    while True:
        try:                                #IndexError: list index out of range if don't go for try/except guard as per example
                                            # check is this also handy anyway or not a good thing to do?
            
            num_commits = num_commits+1     # count number of commits
            print '_____________________________________________________'
            details = data[index+1].split('|')  
            commit_ref = details[0]
            commit_author = details[1].strip()
            commit_date = details[2].strip().split(' ')[0]
            commit_time = details[2].strip().split(' ')[1]
            commit_hour = details[2].strip().split(' ')[1].strip().split(':')[0]  #int required for further down
            commit_weekday = details[2].strip().split(' ')[3].strip().strip('(').strip(',').strip(')')
            commit_month =  details[2].strip().split(' ')[5].strip()#.strip('(').strip(',').strip(')')
        
            commit_comment_line_count = int(details[3].strip().split(' ')[0])
            print commit_comment_line_count
        
            #sorting comments
            commit_comment = data[index-commit_comment_line_count:index]
            comment_date = commit_date
            print commit_comment
            
            if not commit_comment == '' or not commit_comment ==' ':    #don't append blank comments
                comments.append((comment_date,commit_comment))
                
            else:
                no_comments.append(comment_date)                        #list of uncommented commits
    
            #print details
            print 'AUTHOR:',commit_author
            print 'REFERENCE:', commit_ref
            print 'COMMIT DATE:', commit_date
            print 'COMMIT TIME:', commit_time
            print 'COMMIT HOUR:', commit_hour
            print 'This Commit happened on a',commit_weekday
            print 'This Commit happened in', commit_month
        
            #sorting dates#
            dates.append(commit_date)
            #ref: http://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
            distinct_dates = [e for i, e in enumerate(dates) if dates.index(e) == i] #ref: http://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
            distinct_dates.sort()

            #sorting time-hours
            hours.append(commit_hour)
            hours_d[commit_hour] = hours_d.get(commit_hour,0)+1                 # counts and divides 'commit_hour's by number per hour
   
            #sorting weekday
            weekday.append(commit_weekday)
            weekday_d[commit_weekday] = weekday_d.get(commit_weekday,0)+1       # counts and divides 'commit_weekday's by number commits by day of week
           
        
        
            
            
            commit_changes = data[index+2:data.index('',index+1)]# still to figure this ' index+1' out but changing the +n makes a difference
            #print commit_changes
            
            # count total number of _Additions_Deletions_Modifications made per commit and add to master lists
            m_items =0
            d_items =0
            a_items =0
            
            for item in commit_changes:
                if item.startswith('M'):
                    m_items = m_items+1
                    #print item                  # printing 'M's
                elif item.startswith('D'):
                    d_items = d_items+1
                    #print item                  # printing 'D's
                elif item.startswith('A'):
                    a_items = a_items+1
                    #print item                  # printing 'A's
        
            modifications.append(m_items)       # master list with count of number per day of all modifications
            deletions.append(d_items)           # master list with count of number per day of all deletions
            additions.append(a_items)           # master list with count of number per day of all additions
        
        
            print 'Number of Modifications',commit_ref, ' =' ,m_items,  '\nNumber of Deletions    ' ,commit_ref,' =', d_items, '\nNumber of Additions    ',commit_ref,' =', a_items
            
            
            index = data.index(new_fact, index+1)       #without index+1 index does not move to next block => essential to include

        except IndexError:
            break  
    print  '______________________________________________________\n'
    print  '            PROJECT COMMENTs by DATE'
    print  '______________________________________________________'

    comments.sort(reverse=True)                 # print most recent comments first
   
    for i in comments :                         # list each comment separately
        print i
 
    print no_comments
    print  '______________________________________________________\n'
    print  '            PROJECT STATISTICS'
    print  '______________________________________________________'

    num_commits = float(num_commits-1) # adjust for extra 'new_fact' line at finish, need float for percent division
    
    
    distinct_date_count =0     # returns days commits made without duplication   
    for i in distinct_dates:
        distinct_date_count = float(distinct_date_count +1)
 
    print '     COMMITS by HOUR of DAY\n'
    num_by_hour_l =[]          # returns commits by hour of day 
    hour_l =[]
    for key,value in hours_d.items():
        hour_l.append((key,value))
    hour_l.sort()
    for key,value in hour_l:
        print '     Hour of Day:',key, ':commits:' ,value,'(',round((value/num_commits)*100,2),'%)'

    for key,value in hours_d.items():
        num_by_hour_l.append((value,key))
    num_by_hour_l.sort(reverse=True)
    
    busiest_hour = num_by_hour_l[0]

    print '          busiest time of day: hour commencing',busiest_hour[1]+':00'

    print  '_______________________________________________________\n'
    
    print '      COMMITS by DAY of WEEK\n'
    num_by_weekday_l=[]
    weekday_l =[]
    for key,value in weekday_d.items():
        weekday_l.append((value,key))
    
    weekday_l.sort(reverse = True)
    busiest_day = weekday_l[0]
    
    for value,key in weekday_l:
        print '     ',key,value, '(',round((value/num_commits)*100,2),'%)'
    
    
    print '      busiest day of the week was:', busiest_day [1] ,': in total', busiest_day [0],'commits happened on',busiest_day [1]+"rsday's"
    print  '______________________________________________________\n'
   
    print '     Total number of commits:',num_commits  
    print '     Total no. of project days =',distinct_date_count
    print '     Average number of commits per day =', round(num_commits/distinct_date_count,2)

    print  '______________________________________________________'
    #print '     additions = ',additions\n
    print '     Total additions(A) for this project     =', sum(additions) ,'('+str(round((float(sum(additions)))/((sum(additions))+(sum(deletions))+(sum(modifications))),2)*100) ,'%)'
    #print '     deletions = ',deletions,
    print '     Total deletions(D) for this project     = ', sum(deletions),'('+str(round((float(sum(deletions)))/((sum(additions))+(sum(deletions))+(sum(modifications))),2)*100) ,'%)'
    #print '     modifications =',modifications,
    print '     Total modifications(M) for this project =', sum(modifications),'('+str(round((float(sum(modifications)))/((sum(additions))+(sum(deletions))+(sum(modifications))),2)*100) ,'%)'
 
    print
    print '     Total number of lines in this document:',len(data)
    print
    #print dates 
    #print '     Project working dates:',distinct_dates 
    print'__________________________________________________________'

   
        #for i in changes:
        #   count =count+1
        #print 'count ='  ,  count





        
