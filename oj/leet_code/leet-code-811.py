class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        if cpdomains:

            dic = {}

            for item in cpdomains:
                if item:

                    visit_count, domain = item.split()
                    sub_domains = domain.split(".")

                    for i, x in enumerate(sub_domains):
                        full_name = ".".join([x] + sub_domains[i + 1:])
                        if not dic.get(full_name):
                            dic[full_name] = visit_count
                        else:
                            dic[full_name] = str(
                                int(dic[full_name]) + int(visit_count))

            if dic:
                return [" ".join([v, k]) for k, v in dic.items()]


s = Solution()
print(s.subdomainVisits(["9001 discuss.leetcode.com"]))
print(s.subdomainVisits(["900 google.mail.com", "50 yahoo.com",
                         "1 intel.mail.com", "5 wiki.org"]))
print(s.subdomainVisits([]))
print(s.subdomainVisits([None]))
print(s.subdomainVisits(None))
