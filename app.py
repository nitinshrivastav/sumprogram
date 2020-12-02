#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def dhjdfhjfe():
    return render_template("water.html")
@app.route("/inputdata",methods=['GET','POST'])
def hjdshjdsjhsd():
    if(request.method=='POST'):
        x=int(request.form['a'])
        y=int(request.form['b'])
        z=int(request.form['c'])
        res=x+y+z
        return render_template('water.html',answer=res)
if "__main__"==__name__:
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




