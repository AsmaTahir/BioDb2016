
# coding: utf-8

# # DNA

# In[25]:

string="AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
def dna(s):
    counta=0
    countc=0
    countg=0
    countt=0
    for i in range(len(s)):
        if s[i]=='A':
            counta=counta+1
        elif s[i]=='C':
            countc=countc+1
        elif s[i]=='G':
            countg=countg+1
        elif s[i]=='T':
            countt=countt+1
    list1=[counta,countc,countg,countt]
    return (list1)


print(*dna(string))
    


# # RNA

# In[26]:

string="GATGGAACTTGACTACGTAAATT"
def rna(s):
    return(s.replace("T","U"))

rna(string)


# 
# # COMPLEMENTARY STRAND 

# In[24]:

def complementary(s):
    list1=list(s)
    for i in range(len(list1)):
        if i==0 or i==(len(list1)-1):
            continue
        elif list1[i]=='A':
            list1[i]='T'
        elif list1[i]=='C':
            list1[i]='G'
        elif list1[i]=='T':
            list1[i]='A'
        elif list1[i]=='G':
            list1[i]='C'
    str1 = ''.join(list1)
    return str1

string="AAAACCCGGT"
complementary(string)


# # RECURRENCE

# In[23]:

def recurrence(month,rabbit):
    if month==1:
        return 1
    elif month==2:
        return rabbit
    i=recurrence(month-1,rabbit)
    j=recurrence(month-1,rabbit)
    
    if month<=4 or month>=40:
        return i+j
    
    else:
        return (i+(j+rabbit))
    
recurrence(5,3)


# # GC PERCENTAGE 

# In[13]:

def percentage(s):
    counta=0
    countc=0
    countg=0
    countt=0
    header=s[1:14]
    for i in range(len(s)):
        if s[i]=='A':
            counta=counta+1
        elif s[i]=='C':
            countc=countc+1
        elif s[i]=='G':
            countg=countg+1
        elif s[i]=='T':
            countt=countt+1
    sum1=(countc+countg)/(counta+countc+countg+countt)
    percent=sum1*100
    return header,percent

seq='''>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT'''
print(*percentage(seq), sep="\n")


# In[ ]:



