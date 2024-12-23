from data.repository.UserRepository import UserRepository


class UserService:
    @staticmethod
    def validate_fields(data, required_fields):
        """Перевірка наявності обов'язкових полів."""
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

    @staticmethod
    def add_user(data):
        """Бізнес-логіка для додавання користувача"""
        required_fields = [
            'user_ip', 'campain_client_id', 'pixel', 'fbclid', 'bundle',
            'sub1', 'sub2', 'sub3', 'sub4', 'sub5', 'sub6', 'sub7', 'sub8'
        ]
        UserService.validate_fields(data, required_fields)
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
        required_fields = ['user_ip', 'bundle']
        UserService.validate_fields(data, required_fields)

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

        return
