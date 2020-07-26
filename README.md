# HDU-Curriculum-Spider
关于杭电全部课程开课情况的爬虫

简单粗暴的selenium爬虫

爬取网站：http://jxgl.hdu.edu.cn/jxrwcx.aspx?tdsourcetag=s_pcqq_aiomsg

推荐在正式接到选课通知后爬取，因为课程信息可能会随时变动

+ 爬取原因：

  1.服务器晚上十点后维护，不便查询

  2.无robots协议限制

  3.爬取下来的Excel提供了更多查询和筛选条件(例如按课程性质查询公选课等等，可以让你有更多的选择


+ 由于某些原因，爬虫需要知道爬取的页数，最后多余的几页可能需要手动复制，所以需要先遍历一遍得到页数，再进行爬取
已有修改思路：判断`<a href="javascript:__doPostBack('DBGrid$ctl18$ctl01','')">`的数量，枚举情况爬取

 环境：python 3.7.4 ; selenium ; xlwt ; Chrome
