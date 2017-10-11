from django.db import models
# from DjangoUeditor.models import UEditorField

# Create your models here.
class Article(models.Model) :
    title = models.CharField(u"标题",max_length = 100)  #博客题目
    category = models.CharField(u"标签",max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(u"更新时间",auto_now_add = True)  #博客日期
    content = models.TextField(u"内容",blank = True, null = True)  #博客文章正文
    # content = UEditorField(u"内容",width=600, height=300, toolbars="full", imagePath="", filePath="", upload_settings={"imageMaxSize":1204000},settings={},command=None,event_handler=myEventHander(),blank=True)

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']
        verbose_name = "文章"
        verbose_name_plural = "文章"


	