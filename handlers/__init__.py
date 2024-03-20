from .chat import chat_labeler
from .admin import admin_labeler
from .global_handlers import labeler
from .keyboard import kb_labeler

__all__ = ("admin_labeler", "chat_labeler", "labeler", "kb_labeler")