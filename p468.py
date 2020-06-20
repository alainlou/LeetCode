class Solution:
    def validIPAddress(self, IP: str) -> str:
        def IPv4(IP):
            nums = IP.split('.')
            if len(nums) != 4:
                return False

            for n in nums:
                if not n.isnumeric() or int(n) < 0 or int(n) > 255 or (n[0] == '0' and len(n) > 1):
                    return False

            return True

        def IPv6(IP):
            valid = set({'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F'})

            nums = IP.split(':')
            if len(nums) != 8:
                return False

            for n in nums:
                if len(n) > 4 or len(n) < 1:
                    return False
                for c in n:
                    if c not in valid:
                        return False
            return True

        return "IPv4" if IPv4(IP) else "IPv6" if IPv6(IP) else "Neither"
