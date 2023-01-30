import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_course_one(client, course_factory):
    course = course_factory()
    response = client.get(f'/api/v1/courses/{course.id}/')
    assert 200 == response.status_code
    assert course.id == response.json()['id']


@pytest.mark.django_db
def test_course_list(client, course_factory):
    course = course_factory(_quantity=5)

    response = client.get('/api/v1/courses/')
    assert 200 == response.status_code
    assert len(response.json()) == 5
    assert len(response.json()) == len(course)\


@pytest.mark.django_db
def test_course_filter_id(client, course_factory):
    course = course_factory(_quantity=5)

    response = client.get(f'/api/v1/courses/?id={course[2].id}')
    assert 200 == response.status_code
    assert response.json()[0]['id'] == course[2].id


@pytest.mark.django_db
def test_course_filter_name(client, course_factory):
    course = course_factory(_quantity=5)
    response = client.get(f'/api/v1/courses/?name={course[2].name}')
    assert 200 == response.status_code
    assert response.json()[0]['name'] == course[2].name


@pytest.mark.django_db
def test_course_post(client, course_factory):
    counter = Course.objects.count()
    data = {
        "name": "test"
            }
    response = client.post('/api/v1/courses/', data=data)
    assert 201 == response.status_code
    assert Course.objects.count() == counter + 1


@pytest.mark.django_db
def test_course_patch(client, course_factory):
    course = course_factory()
    data = {
        "name": "test"
            }
    response = client.patch(f'/api/v1/courses/{course.id}/', data=data)
    checker = client.get(f'/api/v1/courses/{course.id}/')
    assert 200 == response.status_code
    assert checker.json()['id'] == course.id


@pytest.mark.django_db
def test_course_delete(client, course_factory):
    counter = Course.objects.count()
    course = course_factory()

    assert counter + 1 == Course.objects.count()
    response = client.delete(f'/api/v1/courses/{course.id}/')
    assert 204 == response.status_code
    assert counter == Course.objects.count()
