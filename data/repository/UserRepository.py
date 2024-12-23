from data.DataBaseHelp import DataBaseHelp


class UserRepository(DataBaseHelp):

    def insert_user(self, user_ip, campaign_client_id, pixel, fbclid, bundle, sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8):
        query = ("INSERT INTO `users` ("
                 "`user_ip`, `campaign_client_id`, `pixel`, `fbclid`, `bundle`, "
                 "`sub1`, `sub2`, `sub3`, `sub4`, `sub5`, `sub6`, `sub7`, `sub8`) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")
        return self._insert(
            query, (user_ip, campaign_client_id, pixel, fbclid, bundle, sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8)
        )

    def select_ip(self, user_ip, bundle):
        query = "SELECT * FROM `users` WHERE `user_ip` = %s AND `bundle` = %s;"
        return self._select_one(query, (user_ip, bundle))

    def select_last5m_ips(self, bundle):
        query = "SELECT * FROM `users` WHERE `bundle` = %s AND `date` >= NOW() - INTERVAL 5 MINUTE;"
        return self._select(query, (bundle,))
