from constants.errors import ERROR_CODE
class Error(Exception):
  def __int__(self,message='Internal error!',code=ERROR_CODE.get('INTERNAL_ERROR')):
    self._message = message
    self._code = code
    self.exception = Exception(message)

class ValidationError(Error):
  def __init__(self,message='Validation Error!',code=ERROR_CODE.get('VALIDATION_ERROR')):
    super().__init__(message,code)

