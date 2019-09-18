from django.db import models

class contract_details(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=100)
    message =models.CharField(max_length=100)
    contruct_informations = models.CharField(max_length=50,default='Contruct Info')
    Address = models.CharField(max_length=50,default='Address')
    Address_details = models.CharField(max_length=100,default='203 Fake St. Mountain View, San Francisco, California')
    phone = models.CharField(max_length=10,default='Phone')    
    phone_num = models.CharField(max_length=15,default='01794895700')
    email_adress = models.CharField(max_length=50,default='programmerjahid162@gmail.com')
    our_agents = models.CharField(max_length=50,default='')
    our_angets_details = models.CharField(max_length=200,default='')
    

    def __str__(self):
        return self.fullname


class agent_details(models.Model):
    our_angent_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    our_agent_name = models.CharField(max_length=50,default='')
    our_agnet_type = models.CharField(max_length=50,default='') 
    our_agent_details = models.CharField(max_length=500,default='')
    fb_link = models.CharField(max_length=50,default='')
    twitter_link = models.CharField(max_length=50,default='')
    linkend_link = models.CharField(max_length=50,default='')
   
   
    def __str__(self):
        return self.our_agent_name


class defualt_detials(models.Model):
    about_homeland =models.CharField(max_length=50,default='')
    about_homeland_details =models.CharField(max_length=150,default='')
    company_name = models.CharField(max_length=30,default='')
    company_fb_link = models.CharField(max_length=50,default='')
    company_twitter_link = models.CharField(max_length=50,default='')
    company_instagrame_link = models.CharField(max_length=30)
    company_linkend_link = models.CharField(max_length=50,default='')
    our_company_details  = models.CharField(max_length=300)
    def __str__(self):
        return self.about_homeland

class index_house_details(models.Model):
    house_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    house_name = models.CharField(max_length=50)
    house_location =models.CharField(max_length=50)
    rent_price = models.CharField(max_length=50)
    beds =  models.IntegerField(max_length=2)
    baths = models.IntegerField(default=0)
    spaces =  models.IntegerField(default=0)
    offer_type = models.CharField(max_length=50,default='')


    def __str__(self):
        return self.house_name

class index_defoult_change(models.Model):
    why_choose =models.CharField(max_length=50,default='')
    chose_details = models.CharField(max_length=200,default='')
    recent_blog_hedings = models.CharField(max_length=50,default='')
    recent_blog_details = models.CharField(max_length=200,default='')
    


    def __str__(self):
        return self.recent_blog_hedings   

class top_house_details(models.Model):

    house_name = models.CharField(max_length=100)
    doing_quality = models.CharField(max_length=50)
    ammount = models.CharField(max_length=50)

    def __str__(self):
        return self.house_name


class why_we_choose_details(models.Model):
    chose_topic_title = models.CharField(max_length=100)
    topic_details = models.CharField(max_length=100)

    def __str__(self):
        return self.chose_topic_title


class about_page_defaut(models.Model):
    ledership_details = models.CharField(max_length=100)
    ask_question_titlle = models.CharField(max_length=100)
    as_question_details =  models.CharField(max_length=300)
    company_contract =  models.CharField(max_length=100)
    company_contract_details = models.CharField(max_length=300)


class ledership_details(models.Model):
    leader_ship_agent_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    leader_ship_agent_name = models.CharField(max_length=100)
    leader_ship_agent_type = models.CharField(max_length=30)
    leader_ship_agent_details = models.CharField(max_length=300)



class blog_post_create(models.Model):
    blog_post_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date_of_blog_post = models.CharField(max_length=100)
    blog_post_title = models.CharField(max_length=100)
    blog_post_details = models.CharField(max_length=400)

    def __str__(self):
        return self.blog_post_title



