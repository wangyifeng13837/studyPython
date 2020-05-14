# 这是笔记
# md的使用
# 面向对象
-类和对象的概念

    -类：抽象名词，代表一个集合，共性的事物
    -对象，具象的事物，单个个体
    -类和对象的关系
        -一个具象，代表一类事物的某一个个体
        -一个抽象，代表的是一大类事物

-类中的内容，应该具有两个类容
    
    - 表明事物的特性，叫做属性（变量）
    - 表明事物功能或动作，成为成员方法（函数）
   
#1.类的基本实践

-1.类的命名

    -遵守变量命名的规范
    -大驼峰（由一个或者多个单词构成，每个单词首字母大写，单词跟单词直接相连）
    -尽量避开跟系统命名相似的命名

-2.如何声明一个类

    -必须用class关键字
    -类由属性和方法构成，其他不允许出现
    -成员属性定义可以直接使用变量赋值如果没有，使用None
    -案列01.py
 -3.实例化类
 
        变量 = 类名（） #实例化了一个对象
 -4.访问对象成员
 
    - 使用点操作符
        obj.成员属性名称
        obj.成员方法
 -5.可以通过默认内置变量检查类和对象所有成员
 
    -对象所有成员检查
        # dict前后各有两个下划线
        obj.__dict__
    -类所有的成员
        class_name.__dict__
 # anaconda基本使用

    -annconda主要是一个虚拟环境管理器
    -还是一个安装包管理器
    
 # git 几条常用命名

    -git commit -m：将暂存区文件提交到仓库（单引号内为注释） -am将文件提交到暂存区，并将暂存区文件提交到仓库
    -git remote add origin <远程仓库项目地址> ： 将本地仓库与远程仓库链接
    -git pull --rebase origin master 拉取远程仓库分支代码并合并到本地仓库
    -git push origin master 将合并好的代码上传到远程仓库 第一次推送时 push后加上-u
    
# 2.类和对象的成员分析
    
    -案列02.py
    -类和对象都可以储存成员，成员可以归类所有，也可以归对象所有
    -类存储成员时使用的是类关联的一个对象
    -独享存储成员是存储在当前对象中
    -对象访问一个成员时，如果对象中没有该成员，尝试访问同类中的同名成员
        如果对象中有此成员，一定使用对象中的成员
    -创建对象的时候，类中的成员不会放入对象当中，而是得到一个空的对象，没有成员
    -通过对象对类中成员重新赋值或者通过对象添加成员时，对应成员会保存在对象中，而不会修改类成员

# 3.关于self
    -案例03
    -self在对象的方法中表示当前对象本身，如果通过对象调用方法，那么该对象会自动传入到当前
        的第一个参数
    -self 并不是关键字，只是一个用于接受对象的普通参数，理论上可以用任何一个普通变量名代替
    -案例04
    -方法中有self形参的方法称为非绑定类的方法，可以通过对象访问，没有self的时绑定类的方法，
        只能通过类访问
    -使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员，可以通过__class__成员名访问
    
#4.面向对象

    -封装
    -继承
    -多态
##4.1封装
    -封装就是对对象的成员进行访问限制
    -封装的三个级别
        -公开，public
        -受保护的，protected
        -私有的，private
        - public,pratected,private都不是关键字
    -判别对象的位置
        -对象内部
        -对象外部
        -子类中
    -私有
        -私有成员是最高级的封装，只能在当前类或对象中访问
        -在成员前面添加两个下划线即可
        -案例05.py
        -Python的私有不是真私有，是一种成为name mangling的改名策略
            可以使用对象._classname_attributename访问

