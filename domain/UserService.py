from data.repository.UserRepository import UserRepository


class UserService:
    @staticmethod
    def add_user(data):
        """Бізнес-логіка для додавання користувача"""
        return UserRepository().insert_user(
            data['user_ip'],
            data['campain_client_id'],
            data['pixel'],
            data['fbclid'],
            data['bundle'],
            data['sub1'],
            data['sub2'],
            data['sub3'],
            data['sub4'],
            data['sub5'],
            data['sub6'],
            data['sub7'],
            data['sub8'],
        )

    @staticmethod
    def check_user(data):
        """Бізнес-логіка для перевірки користувача"""
        search_by_ip_result = UserRepository().select_ip(data['user_ip'], data['bundle'])
        if search_by_ip_result:
            print(f"Default search by IP: {search_by_ip_result}")
            return {**search_by_ip_result}

        ip = data['user_ip']
        ip_parts = ip.split(".")
        ip_without_last = ".".join(ip_parts[:-1])

        search_last5m_result = UserRepository().select_last5m_ips(data['bundle'])

        for result in search_last5m_result:
            ip_parts_db = result['user_ip'].split(".")
            ip_without_last_db = ".".join(ip_parts_db[:-1])
            if ip_without_last == ip_without_last_db:
                print(f"Secondary search by IP last 5 minutes: {result}")
                return {**result}

        return None