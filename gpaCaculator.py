import pandas as pd
import numpy as np
import matplotlib as plt

class gpaCaculator:
    
    
    def __init__(self,data):
        self.data = data
        self.originCopy = data
        self.originRemain = data
        self.standerlize()
        self.withWaterStdlize()
        self.remainStdlize()
        assert(data,pd)
    
    def remainStdlize(self):
        def changeHead(df):
            head = []
            for i in df.loc[0]:
                head.append(i)
            df.columns = head
            df = df.iloc[1:,:]
            return df
        self.originRemain = changeHead(self.originRemain)
        self.originRemain = self.originRemain.set_index('序号')
        self.originRemain = self.originRemain.head(61)
        self.originRemain['课程名称'] = self.originRemain['课程名称'].str.replace('（', '(')
        self.originRemain['课程名称'] = self.originRemain['课程名称'].str.replace('）', ')')
        self.originRemain['课程名称'] = self.originRemain['课程名称'].str.replace(' ', '')
        self.originRemain['课程名称'] = self.originRemain['课程名称'].str.replace('II','Ⅱ')
        self.originRemain['总成绩'] = self.originRemain['总成绩'].astype(float)    
        self.originRemain['学分'] = self.originRemain['学分'].astype(float)  
        self.originCopy = self.originCopy.where(self.originCopy['总成绩']!= 0).dropna(how = 'all')
    
    def withWaterStdlize(self):
        def changeHead(df):
            head = []
            for i in df.loc[0]:
                head.append(i)
            df.columns = head
            df = df.iloc[1:,:]
            return df
        self.originCopy = changeHead(self.originCopy)
        self.originCopy = self.originCopy.set_index('序号')
        self.originCopy = self.originCopy.head(61)
        self.originCopy['课程名称'] = self.originCopy['课程名称'].str.replace('（', '(')
        self.originCopy['课程名称'] = self.originCopy['课程名称'].str.replace('）', ')')
        self.originCopy['课程名称'] = self.originCopy['课程名称'].str.replace(' ', '')
        self.originCopy['课程名称'] = self.originCopy['课程名称'].str.replace('II','Ⅱ')
        self.originCopy['总成绩'] = self.originCopy['总成绩'].astype(float)    
        self.originCopy['学分'] = self.originCopy['学分'].astype(float)  
        self.originCopy = self.originCopy.where(self.originCopy['总成绩']!= 0).dropna(how = 'all')
    
    def standerlize(self):
        def changeHead(df):
            head = []
            for i in df.loc[0]:
                head.append(i)
            df.columns = head
            df = df.iloc[1:,:]
            return df
        self.data = changeHead(self.data)
        self.data = self.data.set_index('序号')
        self.data = self.data.head(61)
        self.data['课程名称'] = self.data['课程名称'].str.replace('（', '(')
        self.data['课程名称'] = self.data['课程名称'].str.replace('）', ')')
        self.data['课程名称'] = self.data['课程名称'].str.replace(' ', '')
        self.data['课程名称'] = self.data['课程名称'].str.replace('II','Ⅱ')
        self.data['总成绩'] = self.data['总成绩'].astype(float)    
        self.data['学分'] = self.data['学分'].astype(float)  
        self.data = self.data.where(self.data['总成绩']!= 0).dropna(how = 'all')
        waterCourse = ['军事训练','国家安全教育与军事理论','马克思主义中国化进程与青年学生使命担当','思想道德修养和法律基础(含廉洁修身)','中国近现代史纲要',
               '社会主义发展史','形势与政策Ⅰ','形势与政策Ⅱ','毛泽东思想和中国特色社会主义理论体系概论','习近平新时代中国特色社会主义思想概论','马克思主义基本原理']
        self.data = self.data.where(~self.data['课程名称'].isin(waterCourse)).dropna(how = 'all')
        
        
       

    def caculateCreditAvg(self):
        msg = '\nAnnoucement:因水课定义繁多，本计算器只剔除意识形态相关课程\n以下成绩为学分加权均分:\n'
        def mul(row):
            return row['学分'] * row['总成绩']
        def caculate(data):
            data['mulCreditGrade'] = data.apply(mul,axis = 1)
            sumPoints = data['mulCreditGrade'].sum()
            sumCredit = data['学分'].sum()
            return sumPoints / sumCredit
        originRel = caculate(self.originCopy)
        rel = caculate(self.data)
        if originRel > rel:
            msg += f"你的含水课均分为:{originRel}\n不含水课均分为:{rel}\n你的爱国指数为:{originRel // rel},\n恭喜！\n"
        else:
            msg += f"你的含水课均分为:{originRel}\n不含水课均分为:{rel}\n你的爱国指数为:{originRel / rel}\n呃呃!鉴定为罕见\n"
        print(msg)    
        return 

    
    def CheckDelay(self):
        checkDelay = self.originRemain[['成绩标志','课程名称']].dropna()
        delay = []
        print(f"你有{len(checkDelay)}科缓考: \n")
        for i in checkDelay['课程名称']:
            print(f"{i}\n")
            delay.append(i)
        dfDelay = self.originRemain.loc[self.originRemain['课程名称'].isin(delay), ['课程名称','总成绩']]
        dfDelay = dfDelay.where(dfDelay['总成绩']!= 0)
        dfDelay = dfDelay.dropna()
        for k in delay:
            if k in dfDelay['课程名称'].values:
                point = dfDelay.where(dfDelay['课程名称'] == k).dropna()['总成绩']
                for p in point:
                    print(f"其中{k}已补考,分数为{p}")
        print("\n")
        
