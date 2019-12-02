from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Application
from .serializers import ApplicationSerializer


class ApplicationsListView(APIView):
    '''Предоставляет весть список приложений'''

    def get(self, request):
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response({"application": serializer.data})

class ApiMixin(object):
    def execute(self, request, set_access_Token=False, *args, **kwargs):
        '''Метод возвращает либо результат генерации нового API ключа
           либо информацию об объекте приложении.
           Доступ предоставляется после верификации предоставленого в 
        '''
        if set_access_Token and 'api_key' not in request.POST:
            return 404, 'api key not in post request'
        elif not set_access_Token and 'api_key' not in kwargs:
            return 404, 'api key not in post request'
        try:
            api_key = request.POST['api_key'] if set_access_Token else kwargs['api_key']
            application = Application.objects.get(access_token=api_key)
            print(application)
        except Application.DoesNotExist:
            status, result = 404, 'Access denied'
        else:
            if set_access_Token:
                status, result = application.set_access_Token()
            else:
                status, result = 200, application
        return status, result


class AppApiView(ApiMixin, APIView):
    def post(self, request, *args, **kwargs):
        '''Метод создания нового ключа API
           Доступ к методу производится только после проверки старого ключа API
        '''
        status, result = self.execute(request, True, *args, **kwargs)
        return Response({"result": result}, status=status)


class AppApiTestView(ApiMixin, APIView):
    def get(self, request, *args, **kwargs):
        '''Метод возращает JSON, содержащий всю информацию о приложении,
           Доступ к методу производится только после проверки ключа API
        '''
        status, result = self.execute(request, *args, **kwargs)
        if not isinstance(result, str):
            serializer = ApplicationSerializer(result)
            result = serializer.data
        return Response({"result": result}, status=status)
