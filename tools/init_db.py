from apps.community.models import CommunityGroup, CommunityGroupMember, Post, PostComment, CommentLike
from apps.question.models import *

from MacroTornado.settings import database


def init():
    database.create_tables([User])
    database.create_tables([CommunityGroup,CommunityGroupMember])
    database.create_tables([Post, PostComment, CommentLike])
    database.create_tables([Question, Answer])


if __name__ == "__main__":
    init()