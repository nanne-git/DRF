from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .serializers import StudentSerializer, TeacherSerializer, StudentListSerializer, TeacherListSerializer
from .models import Student, Teacher
from rest_framework.views import APIView
from django.template import loader


def on_input_student(request):
    query = Student.objects.all()
    serializer = StudentListSerializer(query, many=True)
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)


def on_input_teacher(request):
    query = Teacher.objects.all()
    serializer = TeacherListSerializer(query, many=True)
    return JsonResponse(serializer.data, safe=False)


class StudentSearch(APIView):
    def get(self, request, name):
        queryset = Student.objects.filter(name=name)
        serializer_class = StudentSerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)


class SearchByMarks(APIView):
    def get(self, request, marks):
        queryset = Student.objects.filter(marks__gte=marks)
        serializer_class = StudentSerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)


class TeacherSearch(APIView):
    def get(self, request, name):
        queryset = Teacher.objects.filter(name=name)
        serializer_class = TeacherSerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)


class TeacherList(APIView):
    def get(self, request):
        queryset = Teacher.objects.all()
        serializer_class = TeacherSerializer(queryset, many=True)
        return Response(serializer_class.data)


def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))



# def without_select_ex(request):
#     stundets = Student.objects.all()
#     for student in stundets:
#         print(student.name, student.teacher.name)
#
#
# def with_select_ex(request):
#     stundets = Student.objects.all().select_related("teacher")
#     for student in stundets:
#         print(student.name, student.teacher.name)

# class OninputStundet(APIView):
#     def get(self, request, name):
#         queryset = Student.objects.filter(name__startswith=name)
#         serializer_class = StudentSerializer(queryset, many=True)
#         return JsonResponse(serializer_class.data, safe=False)
#
#
# class OninputTeacher(APIView):
#     def get(self, request, name):
#         queryset = Teacher.objects.filter(name__startswith=name)
#         serializer_class = TeacherSerializer(queryset, many=True)
#         return JsonResponse(serializer_class.data, safe=False)


# def with_prefetch(request):
#     teachers = Teacher.objects.all().prefetch_related("students")
#     for teacher in teachers:
#         print(teacher)


#
# @api_view(['GET'])
# def searchstudent(request, name):
#     query = Student.objects.filter(name__startswith=name)
#     serializer = StudentSerializer(query, many=True)
#     return Response(serializer.data)


########################################################
################### Generic Views ######################
########################################################

#
# class ListStudentGenerics(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class RDStudentGenerics(generics.RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


#####################################################################
######################## MIXINS #####################################
#####################################################################
# class StudentsMixin(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
# class StudentsCRUDMixin(mixins.CreateModelMixin, mixins.RetrieveModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


################################################################
######################## Class Based Views #####################
################################################################

# class ListStudents(APIView):
#     def get(self, request):
#         query = Student.objects.all()
#         serializer_class = StudentSerializer(query, many=True)
#         return Response(serializer_class.data)
#
# class DetailedStudent(APIView):
#     def get(self, request, idnum):
#         query = Student.objects.filter(id=idnum)
#         serializer = StudentSerializer(query, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, idnum):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"sucess":"the data is saved"})
#         return serializer.errors()
#
#     def delete(self, request, idnum):
#         query = Student.objects.filter(id=idnum)
#         query.delete()
#
#     def put(self,request,idnum):
#         query = Student.objects.get(id=idnum)
#         serializer = StudentSerializer(query, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"success": "saved"})
#
#
# def index(request):
#     template = loader.get_template("index.html")
#     context = {}
#     return HttpResponse(template.render(context, request))
#
#
# def search(request):
#     search_term = request.POST["search"]
#     search_by = request.POST["filter"]
#     if search_by == 'st':
#         query = Student.objects.get(name=search_term)
#         thead = ["Name", "Age", "Course", "Section", "Marks", "Teacher"]
#         tbody = [query.name, query.age, query.course.course_name, query.class_room.section, query.marks, query.teacher.name]
#     elif search_by == 'te':
#         query = Teacher.objects.get(name=search_term)
#         thead = ["Name", "Age"]
#         tbody = [query.name,query.age]
#     return JsonResponse({"thead":thead, "tbody": tbody})
#
#
# def oninputvalue(request):
#     search_term = request.POST["search_term"]
#     search_by = request.POST["search_by"]
#     data = []
#     if search_by == 'st':
#         query = Student.objects.filter(name__startswith=search_term).values()
#         for q in query:
#             data.append(q['name'])
#     elif search_by == 'te':
#         query = Teacher.objects.filter(name__startswith=search_term).values()
#         for q in query:
#             data.append(q['name'])
#     return JsonResponse({"data": data}, safe=False)
