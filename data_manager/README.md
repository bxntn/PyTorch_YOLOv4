#For Rename_file.py
your data folder structure should be like this
<pre>
data
  |- [type of class]
  |  |- [class]
  |  |  |- [images]
  |  |  |- [labels]
  |  |
  |
</pre>
EX.
<pre>
data
  |- [drink]
  |  |- [Sodadrink]
  |  |  |- [images]
  |  |  |- [labels]
  |  |- [Coffee]
  |  |  |- [images]
  |  |  |- [labels]
  |  |-
  |
</pre>
If you don't want to use this structure. you have to change the code.<br>
Each loop is to go inside a folder.

#For move.py
You must have outdir that have folder structure like this
<pre>
[outdir]
  |- [train]
  |  |- [images]
  |  |- [labels]
  |- [test]
  |  |- [images]
  |  |- [labels]
  |- [valid]
     |- [images]
     |- [labels]
</pre>
