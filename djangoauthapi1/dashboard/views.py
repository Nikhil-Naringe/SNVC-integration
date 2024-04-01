from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import TestSuite, TestSuiteName
from .serializers import TestSuiteSerializer, TestSuiteNameSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import TestSuiteDetailSerializer
from .models import TestSuiteName
from .models import TestSuite
from rest_framework.views import APIView
from SNVC_Machine_Connector import connect_remote_vm



class TestSuitePagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 10000


class TestSuiteCreateView(generics.CreateAPIView):
    queryset = TestSuite.objects.all()
    serializer_class = TestSuiteSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        test_suite_id = serializer.instance.id

        headers = self.get_success_headers(serializer.data)
        return Response({'status': 'success', 'code': status.HTTP_201_CREATED, 'msg': 'TestSuite created successfully', 'data': {'id': test_suite_id}}, headers=headers)



class TestSuiteListView(generics.ListAPIView):
    queryset = TestSuite.objects.all().order_by('id')
    serializer_class = TestSuiteSerializer
    pagination_class = TestSuitePagination
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuites retrieved successfully', 'data': serializer.data})

        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuites retrieved successfully', 'data': serializer.data})



class TestSuiteDeleteView(generics.DestroyAPIView):
    queryset = TestSuite.objects.all()
    serializer_class = TestSuiteSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuite deleted successfully'})
    
# class TestSuiteDeleteView(generics.DestroyAPIView):
#     queryset = TestSuite.objects.all()
#     serializer_class = TestSuiteSerializer
#     permission_classes = [IsAuthenticated]

#     def delete(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#         except Http404:
#             return Response({'status': 'error', 'code': status.HTTP_404_NOT_FOUND, 'msg': 'TestSuite not found'}, status=status.HTTP_404_NOT_FOUND)

#         self.perform_destroy(instance)
#         return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuite deleted successfully'})






    
    
    
    
    
    
class TestSuiteNamePagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 1000


class TestSuiteNameCreateView(generics.CreateAPIView):
    queryset = TestSuiteName.objects.all()
    serializer_class = TestSuiteNameSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        test_suite_name_id = serializer.instance.id

        headers = self.get_success_headers(serializer.data)
        return Response({'status': 'success', 'code': status.HTTP_201_CREATED, 'msg': 'TestSuiteName created successfully', 'data': {'id': test_suite_name_id}}, headers=headers)



class TestSuiteNameListView(generics.ListAPIView):
    queryset = TestSuiteName.objects.all().order_by('id')
    serializer_class = TestSuiteNameSerializer
    pagination_class = TestSuiteNamePagination
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuiteNames retrieved successfully', 'data': serializer.data})

        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuiteNames retrieved successfully', 'data': serializer.data})




class TestSuiteNameRetrieveView(generics.RetrieveAPIView):
    queryset = TestSuiteName.objects.all()
    serializer_class = TestSuiteNameSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuiteName retrieved successfully', 'data': serializer.data})

# class TestSuiteNameRetrieveView(generics.RetrieveAPIView):
#     queryset = TestSuiteName.objects.all()
#     serializer_class = TestSuiteNameSerializer
#     permission_classes = [IsAuthenticated]

#     def retrieve(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#         except Http404:
#             return Response({'status': 'error', 'code': status.HTTP_404_NOT_FOUND, 'msg': 'TestSuiteName not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = self.get_serializer(instance)
#         if serializer.data:
#             return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuiteName retrieved successfully', 'data': serializer.data})
#         else:
#             return Response({'status': 'error', 'code': status.HTTP_404_NOT_FOUND, 'msg': 'No data available'}, status=status.HTTP_404_NOT_FOUND)








class TestSuiteNameDeleteView(generics.DestroyAPIView):
    queryset = TestSuiteName.objects.all()
    serializer_class = TestSuiteNameSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuiteName deleted successfully'})


# class TestSuiteNameDeleteView(generics.DestroyAPIView):
#     queryset = TestSuiteName.objects.all()
#     serializer_class = TestSuiteNameSerializer
#     permission_classes = [IsAuthenticated]

#     def delete(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#         except Http404:
#             return Response({'status': 'error', 'code': status.HTTP_404_NOT_FOUND, 'msg': 'TestSuiteName not found'}, status=status.HTTP_404_NOT_FOUND)

#         self.perform_destroy(instance)
#         return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuiteName deleted successfully'})








class TestSuiteDetailView(generics.RetrieveAPIView):
    queryset = TestSuite.objects.all()
    serializer_class = TestSuiteDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuite detail retrieved successfully', 'data': serializer.data})

# class TestSuiteDetailView(generics.RetrieveAPIView):
#     queryset = TestSuite.objects.all()
#     serializer_class = TestSuiteDetailSerializer
#     permission_classes = [IsAuthenticated]

#     def retrieve(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#         except Http404:
#             return Response({'status': 'error', 'code': status.HTTP_404_NOT_FOUND, 'msg': 'TestSuite not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = self.get_serializer(instance)
#         if serializer.data:
#             return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuite detail retrieved successfully', 'data': serializer.data})
#         else:
#             return Response({'status': 'error', 'code': status.HTTP_404_NOT_FOUND, 'msg': 'No data available'}, status=status.HTTP_404_NOT_FOUND)







class TestSuiteNameUpdateView(generics.UpdateAPIView):
    queryset = TestSuiteName.objects.all()
    serializer_class = TestSuiteNameSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        if serializer.data:
            return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuiteName updated successfully', 'data': serializer.data})
        else:
            return Response({'status': 'error', 'code': status.HTTP_400_BAD_REQUEST, 'msg': 'Serializer data is not available'}, status=status.HTTP_400_BAD_REQUEST)


# class TestSuiteNameUpdateView(generics.UpdateAPIView):
#     queryset = TestSuiteName.objects.all()
#     serializer_class = TestSuiteNameSerializer
#     permission_classes = [IsAuthenticated]

#     def put(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#         except Http404:
#             return Response({'status': 'error', 'code': status.HTTP_404_NOT_FOUND, 'msg': 'No TestSuiteName found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = self.get_serializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
        
#         if serializer.data:
#             return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuiteName updated successfully', 'data': serializer.data})
#         else:
#             return Response({'status': 'error', 'code': status.HTTP_404_NOT_FOUND, 'msg': 'No TestSuiteName found'}, status=status.HTTP_404_NOT_FOUND)





class TestSuiteNameListViewBySuite(generics.ListAPIView):
    serializer_class = TestSuiteNameSerializer
    pagination_class = TestSuiteNamePagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        test_suite_id = self.kwargs.get('pk')
        return TestSuiteName.objects.filter(test_suite_id=test_suite_id).order_by('id')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            if serializer.data: 
                return self.get_paginated_response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuiteNames retrieved successfully', 'data': serializer.data})
            else:
                return Response({'status': 'error', 'code': status.HTTP_404_NOT_FOUND, 'msg': 'No TestSuiteNames found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        if serializer.data:
            return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuiteNames retrieved successfully', 'data': serializer.data})
        else:
            return Response({'status': 'error', 'code': status.HTTP_404_NOT_FOUND, 'msg': 'No TestSuiteNames found'}, status=status.HTTP_404_NOT_FOUND)



class SuiteNameView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        suite_names = TestSuiteName.objects.values_list('suite_name', flat=True).distinct()
        return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'Suite Names retrieved successfully', 'data': list(suite_names)})




from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import TestSuiteName
from .serializers import TestSuiteNameDetailSerializer 

class TestSuiteNameDetailView(RetrieveAPIView):
    queryset = TestSuiteName.objects.all()
    serializer_class = TestSuiteNameDetailSerializer 
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    



from django.http import HttpResponse
from django.views import View

# class TestSuiteRun(View):
def start_suite(requests):
    server_data = TestSuite.objects.latest('id')
    client_data = TestSuiteName.objects.latest('id')
    host_ip_address = server_data.host_ip_address
    share = server_data.share
    server_user_name = server_data.user_name
    server_password = server_data.password
    log_level = server_data.log_level
    suite_name = client_data.suite_name
    client_ip_address = client_data.ip_address
    client_user_name = client_data.user_name
    client_password = client_data.password
        

    print("Host IP Address:", host_ip_address)
    print("Share:", share)
    print("Server User Name:", server_user_name)
    print("Server Password:", server_password)
    print("Log Level:", log_level)
    print("Suite Name:", suite_name)
    print("Client IP Address:", client_ip_address)
    print("Client User Name:", client_user_name)
    print("Client Password:", client_password)
    
    connectionResponse = connect_remote_vm.connect_to_vm(server_ip=host_ip_address,
                                        server_username=server_user_name,
                                        server_password=server_password,
                                        pike_log_level=log_level,
                                        pike_share=share,
                                        client_ip=client_ip_address,
                                        client_username=client_user_name,
                                        client_password=client_password,
                                        suite_name=suite_name
                                        )
        
        # Uncomment below to print further steps
        # time.sleep(5)
        # log_file_path = fr"../SNVC_Machine_Connector/LogReport/{self.suite_name}.log"
        # with open(log_file_path, 'r') as log_file:
        #     log_content = log_file.read()
        #
        # # Create an HTTP response with the log file content
        # response = HttpResponse(log_content, content_type='text/plain')
        # response['Content-Disposition'] = f'attachment; filename="{self.suite_name}"'
        #
        # return response
    return HttpResponse(f"Test Suite started successfully{connectionResponse}")

# test_suite_run = TestSuiteRun()
# test_suite_run.start_suite(None)


# class TestSuiteRun:
#     server_data = TestSuite.objects.latest('id')
#     client_data = TestSuiteName.objects.latest('id')
#     host_ip_address = server_data.host_ip_address
#     share = server_data.share
#     server_user_name = server_data.user_name
#     server_password = server_data.password
#     log_level = server_data.log_level
#     suite_name = client_data.suite_name
#     client_ip_address = client_data.ip_address
#     client_user_name = client_data.user_name
#     client_password = client_data.password

#     def run_suite(self, requests):
#         connect_remote_vm.connect_to_vm(server_ip=self.host_ip_address,
#                                         server_username=self.server_user_name,
#                                         server_password=self.server_password,
#                                         pike_log_level=self.log_level,
#                                         pike_share=self.share,
#                                         client_ip=self.client_ip_address,
#                                         client_username=self.client_user_name,
#                                         client_password=self.client_password,
#                                         suite_name=self.suite_name,
#                                         )
#         # time.sleep(5)
#         # log_file_path = fr"../SNVC_Machine_Connector/LogReport/{self.suite_name}.log"
#         # with open(log_file_path, 'r') as log_file:
#         #     log_content = log_file.read()
#         #
#         # # Create an HTTP response with the log file content
#         # response = HttpResponse(log_content, content_type='text/plain')
#         # response['Content-Disposition'] = f'attachment; filename="{self.suite_name}"'
#         #
#         # return response
