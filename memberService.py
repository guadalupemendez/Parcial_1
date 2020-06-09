from repository import Repository


class MemberService():
    def add_member(self, member):
        lastKey = -1
        for key in Repository.membersList:
            lastKey = key
        lastKey += 1
        Repository.membersList[lastKey] = member._dict_
        return lastKey

    def update_member(self, legajo, member):
        itsIn = False
        for members in Repository.membersList:
            if members == legajo:
                itsIn = True
                break
        if itsIn:
            Repository.membersList[legajo] = member._dict_
        else:
            raise ValueError

    def delete_member(self, legajo):
        itsIn = False
        for members in Repository.membersList:
            if members == legajo:
                itsIn = True
                break
        if itsIn:
            del Repository.membersList[legajo]
        else:
            raise ValueError
