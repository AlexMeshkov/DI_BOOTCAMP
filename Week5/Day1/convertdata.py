import json

notebook_data = {
    "cells": [
        {
            "cell_type": "markdown",
            "id": "45fdec3b-e0c6-470a-ac0a-8ab3ffe3723f",
            "metadata": {},
            "source": ["Exercise1"],
        },
        {
            "cell_type": "code",
            "execution_count": 30,
            "id": "8ac5f39a-19d3-4320-abe5-3a5cf09163e1",
            "metadata": {},
            "outputs": [],
            "source": ["import numpy as np"],
        },
        {
            "cell_type": "markdown",
            "id": "379d65b6-9403-4a5b-9574-7894ec649105",
            "metadata": {},
            "source": ["Exercise 2"],
        },
        {
            "cell_type": "code",
            "execution_count": 31,
            "id": "8c5dd6c7-4355-4002-8ac6-93a87680c9e6",
            "metadata": {},
            "outputs": [],
            "source": ["zero_array = np.zeros(10)"],
        },
        {
            "cell_type": "code",
            "execution_count": 32,
            "id": "8a26086e-bc85-40b1-bc91-6d5ab8c8dc08",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])"
                        ]
                    },
                    "execution_count": 32,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["zero_array"],
        },
        {
            "cell_type": "markdown",
            "id": "d7266b2f-9ad8-4679-85dd-8022493bf914",
            "metadata": {},
            "source": ["Exercise 3"],
        },
        {
            "cell_type": "code",
            "execution_count": 33,
            "id": "923728f0-bcd6-4230-8872-bf391a3beceb",
            "metadata": {},
            "outputs": [],
            "source": ["array = np.arange(1,11)"],
        },
        {
            "cell_type": "code",
            "execution_count": 34,
            "id": "bf05e804-15e6-4ff2-be76-d4ac8c980e4c",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])"
                        ]
                    },
                    "execution_count": 34,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["array"],
        },
        {
            "cell_type": "code",
            "execution_count": 35,
            "id": "fb69aa62-6694-4e75-a886-4de258e0d560",
            "metadata": {},
            "outputs": [],
            "source": ["array_size = array.itemsize"],
        },
        {
            "cell_type": "code",
            "execution_count": 36,
            "id": "5b5ebaba-23f8-45e1-aace-a23516b0feb5",
            "metadata": {},
            "outputs": [
                {
                    "data": {"text/plain": ["8"]},
                    "execution_count": 36,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["array_size"],
        },
        {
            "cell_type": "code",
            "execution_count": 37,
            "id": "942590d2-d861-47d1-808f-38130a278da8",
            "metadata": {},
            "outputs": [],
            "source": ["array_len = len(array)"],
        },
        {
            "cell_type": "code",
            "execution_count": 38,
            "id": "a9f01d8f-8507-48bf-a468-e7f7a2a1e6aa",
            "metadata": {},
            "outputs": [
                {
                    "data": {"text/plain": ["10"]},
                    "execution_count": 38,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["array_len"],
        },
        {
            "cell_type": "code",
            "execution_count": 39,
            "id": "9f12c4b5-c1fd-4e42-92bf-84cd67fa0216",
            "metadata": {},
            "outputs": [],
            "source": ["output = array_len * array_size"],
        },
        {
            "cell_type": "code",
            "execution_count": 40,
            "id": "023b2521-6fae-4f50-990e-614353908f37",
            "metadata": {},
            "outputs": [
                {
                    "data": {"text/plain": ["80"]},
                    "execution_count": 40,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["output"],
        },
        {
            "cell_type": "markdown",
            "id": "2f9f2b7b-2cf2-446f-95f9-97559905c606",
            "metadata": {},
            "source": ["Exercise 4"],
        },
        {
            "cell_type": "code",
            "execution_count": 41,
            "id": "6fad357a-1962-47f0-87df-55601c137540",
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": [
                        "add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n",
                        "\n",
                        "Add arguments element-wise.\n",
                        "\n",
                        "Parameters\n",
                        "----------\n",
                        "x1, x2 : array_like\n",
                        "    The arrays to be added.\n",
                        "    If ``x1.shape != x2.shape``, they must be broadcastable to a common\n",
                        "    shape (which becomes the shape of the output).\n",
                        "out : ndarray, None, or tuple of ndarray and None, optional\n",
                        "    A location into which the result is stored. If provided, it must have\n",
                        "    a shape that the inputs broadcast to. If not provided or None,\n",
                        "    a freshly-allocated array is returned. A tuple (possible only as a\n",
                        "    keyword argument) must have length equal to the number of outputs.\n",
                        "where : array_like, optional\n",
                        "    This condition is broadcast over the input. At locations where the\n",
                        "    condition is True, the `out` array will be set to the ufunc result.\n",
                        "    Elsewhere, the `out` array will retain its original value.\n",
                        "    Note that if an uninitialized `out` array is created via the default\n",
                        "    ``out=None``, locations within it where the condition is False will\n",
                        "    remain uninitialized.\n",
                        "**kwargs\n",
                        "    For other keyword-only arguments, see the\n",
                        "    :ref:`ufunc docs <ufuncs.kwargs>`.\n",
                        "\n",
                        "Returns\n",
                        "-------\n",
                        "add : ndarray or scalar\n",
                        "    The sum of `x1` and `x2`, element-wise.\n",
                        "    This is a scalar if both `x1` and `x2` are scalars.\n",
                        "\n",
                        "Notes\n",
                        "-----\n",
                        "Equivalent to `x1` + `x2` in terms of array broadcasting.\n",
                        "\n",
                        "Examples\n",
                        "--------\n",
                        ">>> np.add(1.0, 4.0)\n",
                        "5.0\n",
                        ">>> x1 = np.arange(9.0).reshape((3, 3))\n",
                        ">>> x2 = np.arange(3.0)\n",
                        ">>> np.add(x1, x2)\n",
                        "array([[  0.,   2.,   4.],\n",
                        "       [  3.,   5.,   7.],\n",
                        "       [  6.,   8.,  10.]])\n",
                        "\n",
                        "The ``+`` operator can be used as a shorthand for ``np.add`` on ndarrays.\n",
                        "\n",
                        ">>> x1 = np.arange(9.0).reshape((3, 3))\n",
                        ">>> x2 = np.arange(3.0)\n",
                        ">>> x1 + x2\n",
                        "array([[ 0.,  2.,  4.],\n",
                        "       [ 3.,  5.,  7.],\n",
                        "       [ 6.,  8., 10.]])\n",
                        "None\n",
                    ],
                }
            ],
            "source": ["print(np.info(np.add))"],
        },
        {
            "cell_type": "markdown",
            "id": "ff7e2384-3564-4490-873d-92c79a1779d4",
            "metadata": {},
            "source": ["Exercise 5"],
        },
        {
            "cell_type": "code",
            "execution_count": 42,
            "id": "3c998b23-aeb1-422b-9ea6-c8ee2e896717",
            "metadata": {},
            "outputs": [],
            "source": ["my_vector = np.arange(10, 50)"],
        },
        {
            "cell_type": "code",
            "execution_count": 43,
            "id": "904ab17f-153d-4576-a60a-84d9dcc66d9d",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,\n",
                            "       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,\n",
                            "       44, 45, 46, 47, 48, 49])",
                        ]
                    },
                    "execution_count": 43,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["my_vector"],
        },
        {
            "cell_type": "markdown",
            "id": "8d66fd59-c163-41d4-ac82-d8aa3fc1ba4d",
            "metadata": {},
            "source": ["Exercise 6"],
        },
        {
            "cell_type": "markdown",
            "id": "6dfafd60-bddf-4d1b-b035-323d2be2d6f8",
            "metadata": {},
            "source": ["my_vector[::-1]"],
        },
        {
            "cell_type": "markdown",
            "id": "a7bc6608-7115-41cc-ac16-eeb1849e4326",
            "metadata": {},
            "source": ["Exercise 7"],
        },
        {
            "cell_type": "code",
            "execution_count": 45,
            "id": "e85df41c-7523-4f1c-a8a0-908639990852",
            "metadata": {},
            "outputs": [],
            "source": ["array = np.array([0,1,2,3,4,5,6,7,8])"],
        },
        {
            "cell_type": "code",
            "execution_count": 50,
            "id": "b1e71ced-511d-43c8-b1fb-57b7b0b9ce0a",
            "metadata": {},
            "outputs": [],
            "source": ["matrix = array.reshape(3,3)"],
        },
        {
            "cell_type": "code",
            "execution_count": 52,
            "id": "4f596f2e-f983-4971-9597-ecfca16f8756",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([[0, 1, 2],\n",
                            "       [3, 4, 5],\n",
                            "       [6, 7, 8]])",
                        ]
                    },
                    "execution_count": 52,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["matrix"],
        },
        {
            "cell_type": "markdown",
            "id": "d35e5d07-fcc0-470b-95e1-df7630dd9f15",
            "metadata": {},
            "source": ["Exercise 8"],
        },
        {
            "cell_type": "code",
            "execution_count": 53,
            "id": "37bbf031-8f65-470d-a042-1454683cde42",
            "metadata": {},
            "outputs": [],
            "source": ["some_array = ([1,2,0,0,4,0])"],
        },
        {
            "cell_type": "code",
            "execution_count": 54,
            "id": "d0923380-3249-43fb-989c-b90aca2f1806",
            "metadata": {},
            "outputs": [],
            "source": ["output = np.nonzero(some_array)"],
        },
        {
            "cell_type": "code",
            "execution_count": 55,
            "id": "0ce74d40-a439-443a-ab42-e219cfde79f6",
            "metadata": {},
            "outputs": [
                {
                    "data": {"text/plain": ["(array([0, 1, 4]),)"]},
                    "execution_count": 55,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["output"],
        },
        {
            "cell_type": "markdown",
            "id": "9c6652b2-805f-40cc-96ea-a4eae214fd9e",
            "metadata": {},
            "source": ["Exercise 9"],
        },
        {
            "cell_type": "code",
            "execution_count": 65,
            "id": "1a4900cd-3930-4310-80ac-20ffa77f0923",
            "metadata": {},
            "outputs": [],
            "source": ["three_dimensional_matrix = np.eye(3)"],
        },
        {
            "cell_type": "code",
            "execution_count": 66,
            "id": "1a15cd85-ee61-41b9-9897-0c7a38141658",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([[1., 0., 0.],\n",
                            "       [0., 1., 0.],\n",
                            "       [0., 0., 1.]])",
                        ]
                    },
                    "execution_count": 66,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["three_dimensional_matrix"],
        },
        {
            "cell_type": "markdown",
            "id": "8166a166-0d7d-4244-8d63-a9ce577f75a9",
            "metadata": {},
            "source": ["Exercise 10"],
        },
        {
            "cell_type": "code",
            "execution_count": 80,
            "id": "41c2d2f7-94db-419e-b31e-3ac21cbb4fd6",
            "metadata": {},
            "outputs": [],
            "source": ["matrix_five = np.full((5,5),[0, 1, 2, 3, 4])"],
        },
        {
            "cell_type": "code",
            "execution_count": 81,
            "id": "ab4571f2-fae0-4fdf-9656-ac2cc02beb2e",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([[0, 1, 2, 3, 4],\n",
                            "       [0, 1, 2, 3, 4],\n",
                            "       [0, 1, 2, 3, 4],\n",
                            "       [0, 1, 2, 3, 4],\n",
                            "       [0, 1, 2, 3, 4]])",
                        ]
                    },
                    "execution_count": 81,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["matrix_five"],
        },
        {
            "cell_type": "markdown",
            "id": "712c3f55-17a7-40e5-adc0-7783ea93c38c",
            "metadata": {},
            "source": ["Exercise 11"],
        },
        {
            "cell_type": "code",
            "execution_count": 84,
            "id": "b39c4843-ef2a-49ae-b99b-96d65bda51ee",
            "metadata": {},
            "outputs": [],
            "source": ["my_vector2 = np.linspace(0,1,10)"],
        },
        {
            "cell_type": "code",
            "execution_count": 85,
            "id": "edb7be7b-8a71-4950-a9f2-d7680f2ab427",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([0.        , 0.11111111, 0.22222222, 0.33333333, 0.44444444,\n",
                            "       0.55555556, 0.66666667, 0.77777778, 0.88888889, 1.        ])",
                        ]
                    },
                    "execution_count": 85,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["my_vector2"],
        },
        {
            "cell_type": "markdown",
            "id": "d70675e7-db94-49a6-8c49-1afd577d785b",
            "metadata": {},
            "source": ["Exercise 12"],
        },
        {
            "cell_type": "code",
            "execution_count": 88,
            "id": "0733f093-fa5b-4713-bb98-03d0b5d45c5b",
            "metadata": {},
            "outputs": [],
            "source": ["rand_vector = np.random.rand(10)"],
        },
        {
            "cell_type": "code",
            "execution_count": 89,
            "id": "9d049cea-91c4-4b1b-918b-5ad79661380e",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([0.02768959, 0.79116458, 0.33400323, 0.09103213, 0.15067725,\n",
                            "       0.3528438 , 0.85050972, 0.09443845, 0.01511782, 0.83372111])",
                        ]
                    },
                    "execution_count": 89,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["rand_vector"],
        },
        {
            "cell_type": "markdown",
            "id": "aad9de7b-fcde-458e-984f-8d6ce20275e2",
            "metadata": {},
            "source": ["Exercise 13"],
        },
        {
            "cell_type": "code",
            "execution_count": 96,
            "id": "1c469e27-4509-4785-8541-d323bc2a6fe2",
            "metadata": {},
            "outputs": [
                {
                    "data": {"text/plain": ["iinfo(min=-128, max=127, dtype=int8)"]},
                    "execution_count": 96,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["np.iinfo('int8')"],
        },
        {
            "cell_type": "code",
            "execution_count": 97,
            "id": "deb9ae91-928e-4b94-9e87-b3d74569c279",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "iinfo(min=-2147483648, max=2147483647, dtype=int32)"
                        ]
                    },
                    "execution_count": 97,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["np.iinfo('int32')"],
        },
        {
            "cell_type": "code",
            "execution_count": 98,
            "id": "58e04135-53bc-4a77-a123-3088cfe2741d",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "iinfo(min=-9223372036854775808, max=9223372036854775807, dtype=int64)"
                        ]
                    },
                    "execution_count": 98,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["np.iinfo('int64')"],
        },
        {
            "cell_type": "code",
            "execution_count": 99,
            "id": "f158a3f7-8825-4d0a-9de5-d49cd0f31761",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "finfo(resolution=1e-06, min=-3.4028235e+38, max=3.4028235e+38, dtype=float32)"
                        ]
                    },
                    "execution_count": 99,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["np.finfo('float32')"],
        },
        {
            "cell_type": "code",
            "execution_count": 100,
            "id": "9e22be4a-e023-4d92-96ef-42588d7565ea",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "finfo(resolution=1e-15, min=-1.7976931348623157e+308, max=1.7976931348623157e+308, dtype=float64)"
                        ]
                    },
                    "execution_count": 100,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["np.finfo('float64')"],
        },
        {
            "cell_type": "markdown",
            "id": "b470649c-8caa-475c-8a27-b6a56dd6484e",
            "metadata": {},
            "source": ["Exercise 14"],
        },
        {
            "cell_type": "code",
            "execution_count": 101,
            "id": "d8ef2de7-da18-422c-a134-dcc2249bda82",
            "metadata": {},
            "outputs": [],
            "source": ["array = np.arange(10, dtype = 'float32')"],
        },
        {
            "cell_type": "code",
            "execution_count": 102,
            "id": "6563aaa1-a2de-4164-99e3-d3e0d815c11b",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.], dtype=float32)"
                        ]
                    },
                    "execution_count": 102,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["array"],
        },
        {
            "cell_type": "code",
            "execution_count": 103,
            "id": "5030cb88-8d3f-426c-9d50-e73195fe9ddc",
            "metadata": {},
            "outputs": [],
            "source": ["int_array = array.astype('int32')"],
        },
        {
            "cell_type": "code",
            "execution_count": 104,
            "id": "3450b2ff-032a-4b82-990f-85fc215087dc",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int32)"
                        ]
                    },
                    "execution_count": 104,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["int_array"],
        },
        {
            "cell_type": "markdown",
            "id": "a546d807-4633-4ec0-a314-96fc681fafef",
            "metadata": {},
            "source": ["Exercise 15"],
        },
        {
            "cell_type": "code",
            "execution_count": 106,
            "id": "367250d5-aaf3-44fe-b771-6eb4b03d4f7b",
            "metadata": {},
            "outputs": [],
            "source": ["two_dim_array = np.arange(0,25)"],
        },
        {
            "cell_type": "code",
            "execution_count": 114,
            "id": "39e07e3d-e72f-4941-9845-d758a7ac3a42",
            "metadata": {},
            "outputs": [],
            "source": ["two_dim_array = two_dim_array.reshape(5,5)\n"],
        },
        {
            "cell_type": "code",
            "execution_count": 118,
            "id": "cc490e29-d4a7-428b-8d62-71eb4e04e89b",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([[ 0,  1,  2,  3,  4],\n",
                            "       [ 5,  6,  7,  8,  9],\n",
                            "       [10, 11, 12, 13, 14],\n",
                            "       [15, 16, 17, 18, 19],\n",
                            "       [20, 21, 22, 23, 24]])",
                        ]
                    },
                    "execution_count": 118,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["two_dim_array\n"],
        },
        {
            "cell_type": "code",
            "execution_count": 119,
            "id": "d5d56158-d9bb-4411-a412-24b06867cf5a",
            "metadata": {},
            "outputs": [
                {
                    "data": {"text/plain": ["array([ 2.,  7., 12., 17., 22.])"]},
                    "execution_count": 119,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["two_dim_array.mean(axis = 1)"],
        },
        {
            "cell_type": "markdown",
            "id": "94aefa4e-a1c5-43cb-b893-39922b5a91a7",
            "metadata": {},
            "source": ["Exercise 16"],
        },
        {
            "cell_type": "code",
            "execution_count": 151,
            "id": "971e4f56-057c-4324-8da1-0d4861043fc8",
            "metadata": {},
            "outputs": [],
            "source": ["twodim_array = np.random.randint(0,15, (3,3))"],
        },
        {
            "cell_type": "code",
            "execution_count": 152,
            "id": "62d4832b-8401-46c6-9da9-2bf7fb7862f0",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([[11,  0,  6],\n",
                            "       [ 5,  3,  1],\n",
                            "       [11, 14,  7]])",
                        ]
                    },
                    "execution_count": 152,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["twodim_array"],
        },
        {
            "cell_type": "code",
            "execution_count": 153,
            "id": "098338d0-48d7-45a4-8b02-3613566b3cb6",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([[ 5,  3,  1],\n",
                            "       [11,  0,  6],\n",
                            "       [11, 14,  7]])",
                        ]
                    },
                    "execution_count": 153,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["twodim_array[twodim_array[:,2].argsort()]"],
        },
        {
            "cell_type": "markdown",
            "id": "0926b406-2a36-41d2-a4ff-0f73f35cd70b",
            "metadata": {},
            "source": ["Exercise 17"],
        },
        {
            "cell_type": "code",
            "execution_count": 166,
            "id": "d3b5ad78-6d71-418c-a8b2-0fc4667bcc9c",
            "metadata": {},
            "outputs": [],
            "source": ["an_array = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]] )"],
        },
        {
            "cell_type": "code",
            "execution_count": 167,
            "id": "144be9e1-a7d9-41ea-a14c-f6957e8361d4",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([[0, 1, 2],\n",
                            "       [3, 4, 5],\n",
                            "       [6, 7, 8]])",
                        ]
                    },
                    "execution_count": 167,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["an_array\n"],
        },
        {
            "cell_type": "code",
            "execution_count": 168,
            "id": "abca9042-9d1a-468a-b6b1-a184957cf53c",
            "metadata": {},
            "outputs": [],
            "source": ["an_array[[0, 2]] = an_array[[2, 0]]"],
        },
        {
            "cell_type": "code",
            "execution_count": 169,
            "id": "4fa117ef-06d0-4827-b4ed-8826cb4635e1",
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "array([[6, 7, 8],\n",
                            "       [3, 4, 5],\n",
                            "       [0, 1, 2]])",
                        ]
                    },
                    "execution_count": 169,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["an_array"],
        },
        {
            "cell_type": "markdown",
            "id": "f1df7624-726c-4c72-a65b-079e514348dc",
            "metadata": {},
            "source": ["Exercise 18"],
        },
        {
            "cell_type": "code",
            "execution_count": 177,
            "id": "c9464828-c223-4c49-9189-6ad516957f9c",
            "metadata": {},
            "outputs": [
                {
                    "data": {"text/plain": ["array([0, 0, 1, 1, 1, 2])"]},
                    "execution_count": 177,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
            "source": ["np.repeat ([0,1,2], [2,3,1])"],
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "id": "127f7f8f-318f-4350-83a8-8ffdd775106c",
            "metadata": {},
            "outputs": [],
            "source": [],
        },
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3",
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.11.4",
        },
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}


with open("your_notebook_name.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook_data, f, ensure_ascii=False, indent=4)
