class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def __init__(self):
        self.head = None

    def mergeTwoLists(self, list1, list2):
        my_merged_list = ListNode()
        tail = my_merged_list

        while list1 and list2:
            if list1 and list1.val <= list2.val:
                tail.next = ListNode(list1.val)
                list1 = list1.next
            elif list2:
                tail.next = ListNode(list2.val)
                list2 = list2.next
            tail = tail.next

        return my_merged_list.next

    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        num1 = ""
        num2 = ""

        if l1 == 0 and l2 == 0:
            return ListNode()
        elif l1 == 0:
            return ListNode(l2.val)
        elif l2 == 0:
            return ListNode(l1.val)

        while l1 or l2:
            if l1:
                stack1.append(str(l1.val))
                l1 = l1.next
            if l2:
                stack2.append(str(l2.val))
                l2 = l2.next

        while stack1 or stack2:
            if stack1:
                num1 += stack1.pop()
            if stack2:
                num2 += stack2.pop()

        result = int(num1) + int(num2)
        result = str(result)
        for char in result:
            new_node = ListNode(int(char))
            new_node.next = self.head
            self.head = new_node
        return self.head

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")


def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    merged = ''
    # merged += word1[0]
    # print(merged)
    # print(len(merged))
    # print(len(word1) + len(word2))
    i = 0
    while len(merged) < len(word1) + len(word2):
        if len(word1) > i:
            merged += word1[i]

        if len(word2) > i:
            merged += word2[i]
        i += 1
    print(merged)


def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""

    t = ""
    len_str2 = len(str2)
    for i in range(len_str2):
        if t and str2[i] == t[0]:
            break
        t += str2[i]

    rehearsals_of_t_in_str2 = len_str2 // len(t)
    rehearsals_of_t_in_str1 = len(str1) // len(t)

    i = 0
    while (True):
        if rehearsals_of_t_in_str1 % (rehearsals_of_t_in_str1 - i) == 0:
            if rehearsals_of_t_in_str2 % (rehearsals_of_t_in_str1 - i) == 0:
                result = t * (rehearsals_of_t_in_str1 - i)
                return result
        i += 1


def gcd_1(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""

    lenStr1 = len(str1)
    lenStr2 = len(str2)
    t = lenStr2
    while (t):
        if lenStr1 % t == 0:
            if lenStr2 % t == 0:
                break
        t -= 1

    result = ''
    for i in range(t):
        result += str2[i]

    return result


def number_to_linked_list(number):
    linked_list = Solution()
    digits = []

    # פירוק המספר ושמירת הספרות ברשימה זמנית
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number = number // 10

    # הוספת הספרות לרשימה המקושרת בסדר הנכון
    for digit in reversed(digits):
        linked_list.append(digit)

    return linked_list.head


def longestPalindrome(s):
    s_dummy = ""

    for char in reversed(s):
        s_dummy += char

    cnt = 0
    j = 0
    i = 0
    manly_palindrome = ""
    palindrome = ''
    # for i in range(len(s_dummy)):
    while True:
        if s[i] == s_dummy[j]:
            while s[i] == s_dummy[j] and s[i] is not None and s_dummy[j] is not None:
                manly_palindrome += s[i]
            # if s_dummy[j] is None:
            #     break
            # i += 1
            # j += 1
            # if s[i] is None:
            #     i = 0
        else:
            i += 1
            if s[i] is None:
                i = 0
                j += 0
            # i = 0
            # cnt += 1
            # j = cnt
            # if len(palindrome) < len(manly_palindrome):
            #     palindrome = manly_palindrome
            #     manly_palindrome = ""
            #     if s[i+1] is not None:

        # if s[i] == s_dummy[j]:
        #     manly_palindrome += s[i]
        # if s[i + 1] is not None:
        #     i += 1
        #     j += 1
        # elif len(palindrome) < len(manly_palindrome):
        #     palindrome = manly_palindrome
        # else:
        #     manly_palindrome = ''
        #     if cnt == len(s_dummy):
        #         break
        #     i = 0
        #     cnt += 1
        #     j = cnt
        # else:
        #     if s[i + 1] is not None:
        #         i += 1
        #         j += 1
        #     elif len(palindrome) < len(manly_palindrome):
        #         palindrome = manly_palindrome
        #     manly_palindrome = ''
        #     if cnt == len(s_dummy):
        #         break
        #     i = 0
        #     cnt += 1
        #     j = cnt

    # return palindrome




if __name__ == '__main__':
    # mergeAlternately("abc", "pqrdd")
    # print(gcd_1("OBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNO", "OBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNOOBCNO"))

    # number = 21
    # l1 = number_to_linked_list(number)
    #
    # number2 = 81
    # l2 = number_to_linked_list(number2)

    # list_1 = ListNode(9)
    # list_1.next = ListNode(9)
    # list_1.next.next.next = ListNode(9)
    #
    # list_2 = ListNode(9)
    # list_2.next = ListNode(9)
    # list_2.next.next = ListNode(9)

    # solution = Solution()
    # merged_list = solution.mergeTwoLists(list_1, list_2)
    #
    # current = merged_list
    # while current:
    #     print(current.val, end=" -> ")
    #     current = current.next
    # print("None")

    # l1 = ListNode()
    # l2 = ListNode()

    # solution = Solution()
    # added_numbers = solution.addTwoNumbers(l1, l2)
    #
    # current = added_numbers
    # while current:
    #     print(current.val, end=" -> ")
    #     current = current.next
    # print("None")

    s = 'ccac'
    print(longestPalindrome(s))
