from django.db import models

class UserDetails(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.username


    

#   CREATE TABLE IF NOT EXISTS `user_details` (
#   `user_id` int(11) NOT NULL AUTO_INCREMENT,
#   `username` varchar(255) DEFAULT NULL,
#   `first_name` varchar(50) DEFAULT NULL,
#   `last_name` varchar(50) DEFAULT NULL,
#   `gender` varchar(10) DEFAULT NULL,
#   `password` varchar(50) DEFAULT NULL,
#   `status` tinyint(10) DEFAULT NULL,
#   PRIMARY KEY (`user_id`)
# ) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1000001 ;  