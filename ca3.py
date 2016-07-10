
#######           Mary Hennessy        10345121    CA 3      ########

################  Program to examine the detail in 5000 line report on 'Commits' made during a Project  ######################


class Commit(object):

    def __init__(self, ref = None, author = None, date = None, time = None, hour = None, weekday = None, month = None, comment_line_count = None):
        self.reference = ref
        self.author = author
        self.date = date
        self.time = time
        self.hour = hour
        self.weekday = weekday
        self.month = month
        
        self.comment_line_count =comment_line_count

    def prepare_data(self):
    
        index = 0                           #NameError: name 'index' is not defined if this omitted
        #print index
        new_fact = 72*'-'                   #each new_fact a commit description
        count = 0
        self.num_commits =0

        self.additions =[]
        self.modifications =[]
        self.deletions =[]
        self.dates =[]
        self.hours =[]
        self.hours_d ={}
        self.weekdays =[]
        self.weekday_d ={}
        self.authors =[]
        self.authors_d ={}
        self.comments =[]
        self.comments_date =[]
        self.no_comments =[]
    
    
        while True:
            try:                                #IndexError: list index out of range if don't go for try/except guard as per example
                                            # check is this also handy anyway or not a good thing to do?
           
                self.num_commits = self.num_commits+1     # count number of commits
                
            
                print '_____________________________________________________'
                details = data[index+1].split('|')  
                commit.ref = details[0]
                commit.author = details[1].strip()
                commit.date = details[2].strip().split(' ')[0]
                commit.time = details[2].strip().split(' ')[1]
                commit.hour = details[2].strip().split(' ')[1].strip().split(':')[0]  #int required for further down
                commit.weekday = details[2].strip().split(' ')[3].strip().strip('(').strip(',').strip(')')
                commit.month =  details[2].strip().split(' ')[5].strip()#.strip('(').strip(',').strip(')')
        
                commit.comment_line_count = int(details[3].strip().split(' ')[0])
                print commit.comment_line_count
        
                #sorting comments
                commit_comment = data[index-commit.comment_line_count:index]
                comment_date = commit.date
                print commit_comment
            
                if not commit_comment == '' or not commit_comment ==' ':    #don't append blank comments
                    self.comments.append((comment_date,commit_comment))
                
                else:
                    self.no_comments.append(comment_date)                        #list of uncommented commits
    
                #print details
                print 'AUTHOR:',commit.author
                print 'REFERENCE:', commit.ref
                print 'COMMIT DATE:', commit.date
                print 'COMMIT TIME:', commit.time
                print 'COMMIT HOUR:', commit.hour
                print 'This Commit happened on a',commit.weekday
                print 'This Commit happened in', commit.month
        
                #sorting dates#
                self.dates.append(commit.date)
                #ref: http://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
                self.distinct_dates = [e for i, e in enumerate(self.dates) if self.dates.index(e) == i] #ref: http://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
                self.distinct_dates.sort()

                #sorting time-hours
                self.hours.append(commit.hour)
                self.hours_d[commit.hour] = self.hours_d.get(commit.hour,0)+1                 # counts and divides 'commit_hour's by number per hour
   
                #sorting weekday
                self.weekdays.append(commit.weekday)
                self.weekday_d[commit.weekday] = self.weekday_d.get(commit.weekday,0)+1       # counts and divides 'commit_weekday's by number commits by day of week
           
                #sorting people
                self.authors.append(commit.author)
                self.authors_d[commit.author] = self.authors_d.get(commit.author,0)+1
                
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
        
                self.modifications.append(m_items)       # master list with count of number per day of all modifications
                self.deletions.append(d_items)           # master list with count of number per day of all deletions
                self.additions.append(a_items)           # master list with count of number per day of all additions
        
        
                print 'Number of Modifications',commit.ref, ' =' ,m_items,  '\nNumber of Deletions    ' ,commit.ref,' =', d_items, '\nNumber of Additions    ',commit.ref,' =', a_items
            
            
                index = data.index(new_fact, index+1)       #without index+1 index does not move to next block => essential to include

            except IndexError:
                break  
        self.total_commits = self.num_commits
        
        self.sort_print_data()
            
    def sort_print_data(self):
        print  '______________________________________________________\n'
        print  '            PROJECT COMMENTs by DATE'
        print  '______________________________________________________'

        self.comments.sort(reverse=True)                 # print most recent comments first
   
        for i in self.comments :                         # list each comment separately
            print i
 
        print self.no_comments
        print  '______________________________________________________\n'
        print  '            PROJECT STATISTICS'
        print  '______________________________________________________'

        self.total_commits = float(self.total_commits-1) # adjust for extra 'new_fact' line at finish, need float for percent division
       
    
        distinct_date_count =0                  # returns days commits made without duplication   
        for i in self.distinct_dates:
            distinct_date_count = float(distinct_date_count +1)
 
        print '     COMMITS by HOUR of DAY\n'
        self.num_by_hour_l =[]                  # returns commits by hour of day 
        self.hour_l =[]
        for key,value in self.hours_d.items():
            self.hour_l.append((key,value))
        self.hour_l.sort()
        for key,value in self.hour_l:
            print '      Hour of Day:',key, ':commits:' ,value,'(',round((value/self.total_commits)*100,2),'%)'

        for key,value in self.hours_d.items():
            self.num_by_hour_l.append((value,key))
        self.num_by_hour_l.sort(reverse=True)
    
        busiest_hour = self.num_by_hour_l[0]            # Mode 

        print '          busiest time of day: hour commencing',busiest_hour[1]+':00'

        print '_______________________________________________________\n'
    
        print '      COMMITS by DAY of WEEK\n'
        self.num_by_weekday_l=[]                # returns number of commits by weekday
        self.weekday_l =[]
        for key,value in self.weekday_d.items():
            self.weekday_l.append((value,key))
    
        self.weekday_l.sort(reverse = True)
        busiest_day = self.weekday_l[0]
    
        for value,key in self.weekday_l:
            print '     ',key,value, '(',round((value/self.total_commits)*100,2),'%)'
            
        print '      busiest day of the week was:', busiest_day [1] ,': in total', busiest_day [0],'commits happened on',busiest_day [1]+"rsday's"
        print '_______________________________________________________\n'
    
        print '      COMMITS per PERSON \n'
        
        authors =[]
        for key,value in self.authors_d.items():
            authors.append((value,key))
        authors.sort(reverse = True)           #busiest commit person on this project at the top
        for value, key in authors:
            print '     ',key, value
        busiest_committer =authors[0]
        print '     Person with most commits on this project is',busiest_committer[1], 'with a total of', busiest_committer[0],'commits'
    

        print '______________________________________________________\n'
   
        print '      Total number of commits:',self.num_commits  
        print '      Total no. of project days =',distinct_date_count
        print '      Average number of commits per day =', round(self.num_commits/distinct_date_count,2)

        print '______________________________________________________\n'
        print '      JOBS by proportion/type carried out in COMMITs\n'
        #print '     additions = ',additions\n
        print '     Total additions(A) for this project     =', sum(self.additions) ,'('+str(round((float(sum(self.additions)))/((sum(self.additions))+(sum(self.deletions))+(sum(self.modifications))),2)*100) ,'%)'
        #print '     deletions = ',deletions,
        print '     Total deletions(D) for this project     = ', sum(self.deletions),'('+str(round((float(sum(self.deletions)))/((sum(self.additions))+(sum(self.deletions))+(sum(self.modifications))),2)*100) ,'%)'
        #print '     modifications =',modifications,
        print '     Total modifications(M) for this project =', sum(self.modifications),'('+str(round((float(sum(self.modifications)))/((sum(self.additions))+(sum(self.deletions))+(sum(self.modifications))),2)*100) ,'%)'
 
        print '\n______________________________________________________\n'
        print '     Total number of lines in this document:',len(data)
        print
        #print dates 
        #print '     Project working dates:',distinct_dates 
        print '________________________________________________________'

   





if __name__ =='__main__':
    
    commit = Commit()
    
    changes_file = 'mini.txt'
    data =[line.strip() for line in open(changes_file)]
    #print data
    #print len(data)

    
    commit.prepare_data()

    
        #for i in changes:
        #   count =count+1
        #print 'count ='  ,  count





        
