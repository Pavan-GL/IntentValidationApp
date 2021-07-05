from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase, APIClient
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += "/JSONfiles"


# Create your tests here.

class POSTServiceTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_finite_one_valid(self):
        fp_in = open(dir_path + "/" + "input1.json")
        fp_out = open(dir_path + "/" + "output1.json")

        jsonin = json.load(fp_in)
        jsonout = json.load(fp_out)

        response = self.client.post('/validateFiniteEntity', jsonin, format='json')
        self.assertEqual(json.loads(response.content), jsonout)
        fp_in.close()
        fp_out.close()

    def test_finite_invalid_only(self):
        fp_in = open(dir_path + "/" + "input2.json")
        fp_out = open(dir_path + "/" + "output2.json")

        jsonin = json.load(fp_in)
        jsonout = json.load(fp_out)

        response = self.client.post('/validateFiniteEntity', jsonin, format='json')
        self.assertEqual(json.loads(response.content), jsonout)
        fp_in.close()
        fp_out.close()

    def test_finite_empty(self):
        fp_in = open(dir_path + "/" + "input3.json")
        fp_out = open(dir_path + "/" + "output3.json")

        jsonin = json.load(fp_in)
        jsonout = json.load(fp_out)

        response = self.client.post('/validateFiniteEntity', jsonin, format='json')
        self.assertEqual(json.loads(response.content), jsonout)
        fp_in.close()
        fp_out.close()

    def test_finite_valid_invalid(self):
        fp_in = open(dir_path + "/" + "input4.json")
        fp_out = open(dir_path + "/" + "output4.json")

        jsonin = json.load(fp_in)
        jsonout = json.load(fp_out)

        response = self.client.post('/validateFiniteEntity', jsonin, format='json')
        self.assertEqual(json.loads(response.content), jsonout)
        fp_in.close()
        fp_out.close()

    def test_finite_all_valid(self):
        fp_in = open(dir_path + "/" + "input5.json")
        fp_out = open(dir_path + "/" + "output5.json")

        jsonin = json.load(fp_in)
        jsonout = json.load(fp_out)

        response = self.client.post('/validateFiniteEntity', jsonin, format='json')
        self.assertEqual(json.loads(response.content), jsonout)
        fp_in.close()
        fp_out.close()

    def test_numeric_one_valid(self):
        fp_in = open(dir_path + "/" + "input6.json")
        fp_out = open(dir_path + "/" + "output6.json")

        jsonin = json.load(fp_in)
        jsonout = json.load(fp_out)

        response = self.client.post('/validateNumEntity', jsonin, format='json')
        self.assertEqual(json.loads(response.content), jsonout)
        fp_in.close()
        fp_out.close()

    def test_numeric_invalid_only(self):
        fp_in = open(dir_path + "/" + "input7.json")
        fp_out = open(dir_path + "/" + "output7.json")

        jsonin = json.load(fp_in)
        jsonout = json.load(fp_out)

        response = self.client.post('/validateNumEntity', jsonin, format='json')
        self.assertEqual(json.loads(response.content), jsonout)
        fp_in.close()
        fp_out.close()

    def test_numeric_empty(self):
        fp_in = open(dir_path + "/" + "input8.json")
        fp_out = open(dir_path + "/" + "output8.json")

        jsonin = json.load(fp_in)
        jsonout = json.load(fp_out)

        response = self.client.post('/validateNumEntity', jsonin, format='json')
        self.assertEqual(json.loads(response.content), jsonout)
        fp_in.close()
        fp_out.close()

    def test_numeric_valid_invalid(self):
        fp_in = open(dir_path + "/" + "input9.json")
        fp_out = open(dir_path + "/" + "output9.json")

        jsonin = json.load(fp_in)
        jsonout = json.load(fp_out)

        response = self.client.post('/validateNumEntity', jsonin, format='json')
        self.assertEqual(json.loads(response.content), jsonout)
        fp_in.close()
        fp_out.close()

    def test_numeric_all_valid(self):
        fp_in = open(dir_path + "/" + "input10.json")
        fp_out = open(dir_path + "/" + "output10.json")

        jsonin = json.load(fp_in)
        jsonout = json.load(fp_out)

        response = self.client.post('/validateNumEntity', jsonin, format='json')
        self.assertEqual(json.loads(response.content), jsonout)
        fp_in.close()
        fp_out.close()
